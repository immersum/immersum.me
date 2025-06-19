+++
title = """
Egysorosok, amelyek segítségével a synben használt egyes típusokból kinyerhetjük a kifejezéseket
"""
date = "2025-06-12"

[taxonomies]
blog-tags = ["Rust"]

[extra]
comments.host = "noc.social"
comments.username = "immersum"
comments.id = "114669335434162042"
+++

### Az elképzelésemről röviden

A legutóbbi projektemben, amely az [mplusfonts](/hu/projects/mplusfonts/) nevet viseli, és amely
az azonos nevű TrueType-betűtípusnak egy `no_std` grafikus könyvtárcsomaghoz készült adaptációja,
volt egy olyan elképzelésem, hogy a *#[strings::emit]* segédattribútumot ne egy adott kifejezésre
kelljen alkalmazni, hanem lehessen arra az utasításra is, amelyben a kifejezésnek az eredményét
értékül adjuk egy változónak. Az volt az célom, hogy ezt általánosítva bármilyen kifejezésnek a
szülője hordozhassa az attribútumot, mint ez az alábbi példában látható.

```rust
// Előtte
let bitmap_font =
    #[strings::emit]
    mplus!(2, 500, 25, false, 1, 4);

// Utána
#[strings::emit]
let bitmap_font = mplus!(2, 500, 25, false, 1, 4);
```

Ebben a példában a kifejezés szerepét az *mplus!* függvényszerű makrónak a hívása tölti be, és ez
az a kifejezés, amelyen a *#[strings]* makrónak a feldolgozása során valamilyen műveletet végzünk
majd.

### A megvalósítás mikéntje

A [syn] crate (kódcsomag) egy olyan interfészhármast kínál, amellyel a szintaxisfát járhatjuk be és
manipulálhatjuk:

* A [fold](https://docs.rs/syn/latest/syn/fold/index.html) modulban található függvények megszerzik
  a csomópont tulajdonjogát, és ezeknek ugyanilyen típusú értékkel is kell visszatérniük.
* A [visit](https://docs.rs/syn/latest/syn/visit/index.html) modulban található függvények
  kölcsönbe kapják meg a csomópontot, így ezek megvizsgálhatják annak értékét, de nem módosíthatják
  azt.
* A [visit_mut](https://docs.rs/syn/latest/syn/visit_mut/index.html) modulban található függvények
  kölcsönbe kapják meg a csomópontot, de megkapják hozzá a lehetőségét annak is, hogy módosítsák a
  csomópont adatmezőit.

Ebben a harmadik modulban található az a trait (jellemvonás), amelyet a *MacroVisitor* implementál.

{{ icon(type="github") }}
<https://github.com/immersum/mplusfonts/blob/v0.2.0/macros/src/strings/visitor/mac.rs>

Bár használhattam volna a modulból származó függvényeket is, amelyeket alapértelmezett esetben a
traitnek a tagfüggvényei meghívnak, az elképzeléseimnek megfelelően típusonként egy-egy híváslánc
gyűjti össze a segédattribútummal jelölt csomópontból indulva azokat a kifejezéseket, amelyek a
részfát tekintve közvetlen leszármazottai a csomópontnak.

Miközben a kinyert kifejezések iterálása történik, amelynek a módját ez a blogbejegyzés tárgyalja,
az eredményhalmazt igény szerint szűrhetjük.

```rust
for expr in exprs {
    if let syn::Expr::Macro(expr_macro) = expr {
        // Itt történik a `&mut expr_macro.mac.tokens` módosítása
    }
}
```

[syn]: https://crates.io/crates/syn

### Ami opcionális, az iterátorrá alakítható

A különböző típusok adatstruktúráját végignézve láthatjuk, hogy milyen változatos mezőtípusokban
található kifejezés:

* Egyes adatmezők típusa egyszerűen kifejezés, másoké ugyanez, csak indirekcióval: `Box<Expr>`
* Egyes adatmezők a számosságukat tekintve _1_ eleműek, mások _0_.._1_ eleműek, vagyis
  opcionálisak: `Option<Expr>`
* Ugyanez indirekcióval együtt is megtalálható: `Option<Box<Expr>>`
* Vannak az adatmezők között _n_ eleműek is: `Punctuated<Expr, Comma>`
* Ezek mellett komplex mezőtípusok is előfordulnak: `Option<(Eq, Expr)>`

Az ilyen mezőkből tartalmaznak egyet vagy többet a számunkra érdekes típusok. A feladat
legérdekesebb része annak a meghatározása volt, hogy milyen transzformációs logikával jutunk
`impl Iterator<Item = &mut Expr>` jellegű eredményre az egyes típusok esetében, ha egy-egy
argumentumként kapott `&mut node` a kiindulási pont.

Több módja is van például annak, hogy egy egyelemű iterátort létrehozzunk. Egy szeletliterál kódban
mérve kompaktabb, mint egy függvényhívás, ha `impl IntoIterator<Item = &mut Expr>` is elfogadott,
mint ahogyan az egy `for` ciklus esetében fennáll. Ezt akár két vagy többeleműre is kibővíthetjük.
Az `iter:once` függvénynek a meghívása másrészről viszont olvashatóbb.

```rust
// Megoldás #1 - Nem feltétlenül kell az .into_iter()
let exprs = [expr].into_iter();

// Megoldás #2
let exprs = iter::once(expr);
```

Egy harmadik megoldás lehetne az, hogy a kifejezést opcionális típusba csomagoljuk:
`Some(expr).into_iter()`

Ez azért működne, mert ha valami opcionális, akkor az egyúttal iterátorrá is alakítható. Azonban
nemcsak iterátorrá, hanem szeletté is alakítható az opcionális érték, és egy `for` ciklus esetében
inkább ez javasolt, ellenkező esetben [clippy] figyelmeztetne minket - *for_loops_over_fallibles*.

[clippy]: https://github.com/rust-lang/rust-clippy

## Az attribútumokat hordozó és kifejezéseket tartalmazó típusok listája

### 1. Változókat és konstansokat reprezentáló típusok

A feldolgozás során leggyakrabban valamilyen értékadás kontextusában fogunk azzal találkozni, hogy
az attribútumunkat használják, így elsőként azt nézzük meg, hogy ilyen esetben miként gyűjthetünk
kifejezéseket.

#### 1.1. Helyi változók memóriacím-kötése

* [Local](local/) - Ez _0_.._1_ db kezdeti értékadást tartalmaz, a kezdeti értékadás pedig _1_ db
  kifejezést tartalmaz a `=` token után, illetve további _0_.._1_ db kifejezést az opcionális
  `else` kulcsszó után (a *diverge* kifejezést, amelynek neve külön irányba haladást jelent, és ez
  arra utal, hogy a vezérlés nem folytatódhat a `let` kötés utáni utasításokkal).

#### 1.2. Statikusok inicializációja

* [ItemStatic](item-static/) - Ez _1_ db konstans kifejezést tartalmaz a `=` token után.

#### 1.3. Konstansok deklarációja

* [ItemConst](item-const/) - Ez _1_ db konstans kifejezést tartalmaz a `=` token után.
* [ImplItemConst](impl-item-const/) - Ez _1_ db konstans kifejezést tartalmaz a `=` token után (az
  `impl` blokkon belüli előfordulás esete).
* [TraitItemConst](trait-item-const/) - Ez _0_.._1_ db konstans kifejezést tartalmaz az opcionális
  `=` token után (a *default* konstans kifejezést, amelynek neve alapértelmezettet jelent, és ennek
  az értéknek a megadása egy trait, vagyis „vonás, jellemvonás” definiálásánál nem kötelező).

### 2. Típusdefiníciókat reprezentáló típusok

A Rust nyelvben konstans kifejezések néhány olyan helyen is előfordulhatnak, mint a szintaxisfának
egy-egy összetettebb csomópontja.

#### 2.1. Konstans paraméterek generikus típusokhoz

* [ConstParam](const-param/) - Ez _0_.._1_ konstans kifejezést tartalmaz az opcionális a `=` token
  után (a *default* konstans kifejezést, amelynek a megadása nem kötelező).

#### 2.2. Enum (felsorolási típusok) definíciója

* [ItemEnum](item-enum/) - Ez _n_ db variánst tartalmaz.
* [Variant](variant/) - Minden egyes variáns _0_.._1_ db konstans kifejezést tartalmaz az
  opcionális `=` token után (a variáns diszkriminánsa, vagyis a megkülönböztető értéke, amely
  explicit módon is megadható).

### 3. Kifejezéseket reprezentáló típusok

A szintaxisfa csomópontjainak az összes többi, itt felsorolt típusa olyan, amely kifejezést
reprezentál, és a típus adatmezői között vannak olyanok, amelyek típusa szintén kifejezést
reprezentál.

#### 3.1. Slice (tömbszeletek) and tuple (rendezett n-esek)

* [ExprArray](expr-array/) - Ez _n_ db kifejezést tartalmaz a `[]` tokenek között (a tömbszelet
  elemeit).
* [ExprTuple](expr-tuple/) - Ez _n_ db kifejezést tartalmaz a `()` tokenek között (a rendezett n-es
  elemeit).

#### 3.2. Struktúrák

* [ExprStruct](expr-struct/) - Ez _n_ db mezőnévből és hozzá tartozó értékből álló párost
  tartalmaz, illetve _0_.._1_ db kifejezést az opcionális `..` token után (a bázisstruktúrát,
  amelynek *rest* mezőneve arra utal, hogy a többi mező értékét ez a struktúra szolgáltatja).
* [FieldValue](field-value/) - Minden egyes mezőnévből és hozzá tartozó értékből álló páros _1_ db
  kifejezést tartalmaz a `:` token után.

#### 3.3. If (elágazások) és while (elöltesztelő ciklusok)

* [ExprIf](expr-if/) - Ez _1_ db kifejezést tartalmaz az `if` kulcsszó után (a *cond* kifejezést,
  amelynek kiértékelése után *true* vagy *false* értéket kapunk), amelyet először egy utasításblokk
  követ (a *then_branch* blokk, amely maga **nem kifejezés**), utána viszont tartalmaz további
  _0_.._1_ db kifejezést az opcionális `else` kulcsszó után (az *else_branch* kifejezést, amely
  lehet utasításblokk-kifejezés, de lehet ettől eltérő típusú kifejezés is).
* [ExprWhile](expr-while/) - Ez _1_ db kifejezést tartalmaz a `while` kulcsszó után (a *cond*
  kifejezést), amelyet egy utasításblokk követ (a *body* blokk, amely maga **nem kifejezés**).
* [ExprLet](expr-let/) - Ez _1_ db kifejezést tartalmaz a `=` token után, amelynek neve scrutinee,
  vagyis egy adott vizsgálat alanya, és ez arra utal, hogy az értéknek illeszkednie kell a `let`
  kulcsszó után megadott mintára.

#### 3.4. For loop (számláló ciklusok)

* [ExprForLoop](expr-for-loop/) - Ez _1_ db kifejezést tartalmaz az `in` kulcsszó után (egy olyan
  kifejezést, amely vagy maga egy iterátor, vagy pedig egy iterátorrá alakítható kifejezés).

#### 3.5. Range (értékkészletek)

* [ExprRange](expr-range/) - Ez _0_.._1_ db kifejezést tartalmaz a `..` vagy `..=` token előtt (a
  *start* kifejezést), valamint _0_.._1_ db kifejezést utána (az *end* kifejezést).
* [ExprRepeat](expr-repeat/) - Ez _1_ db kifejezést tartalmaz a `;` token előtt, valamint _1_ db
  kifejezést utána.

#### 3.6. Match (többirányú elágazások)

* [ExprMatch](expr-match/) - Ez _1_ db kifejezést tartalmaz a `match` kulcsszó után, amelynek neve
  scrutinee, illetve _n_ db kart, amelyek közül pontosan _1_ db lesz végrehajtva.
* [Arm](arm/) - Minden egyes `match` kar _0_.._1_ db kifejezést tartalmaz az opcionális `if`
  kulcsszó után (a *guard* kifejezést, amelynek neve arra utal, hogy ez a feltétel védi a kart,
  akár egy „őr, pajzs”), illetve _1_ db kifejezést a `=>` token után (a *body* kifejezést, amely
  lehet utasításblokk-kifejezés, de lehet ettől eltérő típusú kifejezés is).

#### 3.7. Break (ciklusmegszakítások) és return (visszatérések)

* [ExprBreak](expr-break/) - Ez _0_.._1_ db kifejezést tartalmaz a `break` kulcsszó és az
  opcionális *label* után (ha feltüntetjük, akkor a hivatkozott címkével jelölt ciklus utáni
  utasításokkal folytatódik a vezérlés, egyéb esetben pedig az aktuális ciklus utániakkal).
* [ExprReturn](expr-return/) - Ez _0_.._1_ db kifejezést tartalmaz a `return` kulcsszó után.
* [ExprYield](expr-yield/) - Ez _0_.._1_ db kifejezést tartalmaz a `yield` kulcsszó után.

#### 3.8. Closure (lezárási típusok)

* [ExprClosure](expr-closure/) - Ez _1_ db kifejezést tartalmaz a `||` tokenek után (a *body*
  kifejezést, amely lehet utasításblokk-kifejezés, de lehet ettől eltérő típusú kifejezés is).

#### 3.9. Cast (típuskonverziók)

* [ExprCast](expr-cast/) - Ez _1_ db kifejezést tartalmaz az `as` kulcsszó előtt.

#### 3.10. Hivatkozási és memóriacím-lekérési műveletek

* [ExprReference](expr-reference/) - Ez _1_ db kifejezést tartalmaz a `&` token és az opcionális
  `mut` kulcsszó után.
* [ExprRawAddr](expr-raw-addr/) - Ez _1_ db kifejezést tartalmaz.

#### 3.11. Try (feltételes visszatérések) és await (művelet befejezésére várakozások)

* [ExprTry](expr-try/) - Ez _1_ db kifejezést tartalmaz a `?` token előtt.
* [ExprAwait](expr-await/) - Ez _1_ db kifejezést tartalmaz a `.` token és az `await` kulcsszó
  előtt (a `base` kifejezést).

#### 3.12. Adatmezőhöz történő hozzáférések

* [ExprField](expr-field/) - Ez _1_ db kifejezést tartalmaz a `.` token előtt (a `base`
  kifejezést).

#### 3.13. Függvényhívások és tagfüggvényhívások

* [ExprCall](expr-call/) - Ez _1_ db kifejezést tartalmaz a `()` tokenek előtt (a `func`
  kifejezést), illetve _n_ db kifejezést a `()` tokenek között (a függvényhívás
  argumentumait).
* [ExprMethodCall](expr-method-call/) - Ez _1_ db kifejezést tartalmaz a `.` token és a metódusnév
  előtt (a *receiver* kifejezést, amely a metódusnak a `self` argumentuma lesz), illetve _n_ db
  kifejezést a `()` tokenek között (a metódushívás argumentumait).

#### 3.14. Indexelések

* [ExprIndex](expr-index/) - Ez _1_ db kifejezést tartalmaz a `[]` tokenek előtt, illetve _1_ db
  kifejezést a `[]` tokenek között (az *index* kifejezést).

#### 3.15. Unary (egyoperandusú) és binary (kétoperandusú) műveletek

* [ExprUnary](expr-unary/) - Ez _1_ db kifejezést tartalmaz az egyoperandusú operátor után.
* [ExprBinary](expr-binary/) - Ez _1_ db kifejezést tartalmaz a kétoperandusú operátor előtt (a
  *left* kifejezést), valamint _1_ db kifejezést utána (a *right* kifejezést).

#### 3.16. Assignment (értékadások)

* [ExprAssign](expr-assign/) - Ez _1_ db kifejezést tartalmaz a `=` token előtt, valamint _1_ db
  kifejezést utána.

#### 3.17. Zárójeles és zárójel nélküli csoportosítások

* [ExprParen](expr-paren/) - Ez _1_ db kifejezést tartalmaz a `()` tokenek között.
* [ExprGroup](expr-group/) - Ez _1_ db kifejezést tartalmaz.

#### 3.18. Utasításblokkok, feltételes megszakítások, ciklusmagok stb.

Létezhetnek olyan csomópontok a szintaxisfában, amelyekre bár lehet attribútumot alkalmaznunk,
mivel ezek utasításblokkot tartalmazó kifejezések (mint a *then_branch* blokk az `if` kifejezések
esetében), a közvetlen leszármazottai között nem találunk kifejezést.

* [ExprBlock](expr-block/), [ExprConst](expr-const/), [ExprUnsafe](expr-unsafe/),
  [ExprTryBlock](expr-try-block/), [ExprAsync](expr-async/), [ExprLoop](expr-loop/) - Ezek _0_ db
  kifejezést tartalmaznak.

#### 3.19. Makróhívások

* [ExprMacro](expr-macro/) - Ez részfákat tartalmaz, amelyek a hívásának bemeneteként szolgálnak,
  és a részfák tetszőleges csomópontokból állhatnak.

Mivel azonban ez a blogbejegyzés egy olyan esetet ír le, ahol a kinyert kifejezések közül eleve
csak a makróhívásokat vesszük figyelembe a feldolgozás során, a makróhívásokban található
kifejezések kinyerését nem részletezem ebben a bejegyzésben.
