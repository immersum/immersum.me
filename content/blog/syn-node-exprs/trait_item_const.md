+++
title = "Struct TraitItemConst"
template = "mermaid-page.html"
+++

[docs.rs](https://docs.rs/syn/latest/syn/struct.TraitItemConst.html)

```rust
pub struct TraitItemConst {
    pub attrs: Vec<Attribute>,
    pub const_token: Const,
    pub ident: Ident,
    pub generics: Generics,
    pub colon_token: Colon,
    pub ty: Type,
    pub default: Option<(Eq, Expr)>,
    pub semi_token: Semi,
} 
```

## Iterator<Item = &Expr>

node: *&TraitItemConst*

```rust
node.default
    .as_slice()
    .iter()
    .map(|(_, expr)| expr)
```

<center>

{% mermaid() %}
    flowchart TD
        101("<code>node.default:#nbsp;<em>&Option#lt;(Eq,#nbsp;Expr)#gt;</em></code>") --- 102
        102(["<code>.as_slice()</code>"]) --> 103
        103("<code><em>&[(Eq,#nbsp;Expr)]</em></code>") --- 104
        104(["<code>.iter()</code>"]) --> 105
        105("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&(Eq,#nbsp;Expr)#gt;</em></code>") --- 2
        subgraph 2["<code>.map()</code>"]
            201("<code><em>&Expr</em></code>")
        end
        2 --> 106
        106("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&Expr#gt;</em></code>")
{% end %}

</center>

## Iterator<Item = &mut Expr>

node: *&mut TraitItemConst*

```rust
node.default
    .as_mut_slice()
    .iter_mut()
    .map(|(_, expr)| expr)
```

<center>

{% mermaid() %}
    flowchart TD
        101("<code>node.default:#nbsp;<em>&mut#nbsp;Option#lt;(Eq,#nbsp;Expr)#gt;</em></code>") --- 102
        102(["<code>.as_mut_slice()</code>"]) --> 103
        103("<code><em>&mut#nbsp;[(Eq,#nbsp;Expr)]</em></code>") --- 104
        104(["<code>.iter_mut()</code>"]) --> 105
        105("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&mut#nbsp;(Eq,#nbsp;Expr)#gt;</em></code>") --- 2
        subgraph 2["<code>.map()</code>"]
            201("<code><em>&mut#nbsp;Expr</em></code>")
        end
        2 --> 106
        106("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&mut#nbsp;Expr#gt;</em></code>")
{% end %}

</center>
