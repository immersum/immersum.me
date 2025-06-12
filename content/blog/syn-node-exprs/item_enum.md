+++
title = "Struct ItemEnum"
template = "mermaid-page.html"
+++

[docs.rs](https://docs.rs/syn/latest/syn/struct.ItemEnum.html)

```rust
pub struct ItemEnum {
    pub attrs: Vec<Attribute>,
    pub vis: Visibility,
    pub enum_token: Enum,
    pub ident: Ident,
    pub generics: Generics,
    pub brace_token: Brace,
    pub variants: Punctuated<Variant, Comma>,
}

pub struct Variant {
    pub attrs: Vec<Attribute>,
    pub ident: Ident,
    pub fields: Fields,
    pub discriminant: Option<(Eq, Expr)>,
}
```

## Iterator<Item = &Expr>

node: *&ItemEnum*

```rust
node.variants
    .iter()
    .filter_map(|variant| {
        variant
            .discriminant
            .as_ref()
            .map(|(_, expr)| expr)
    })
```

<center>

{% mermaid() %}
    flowchart TD
        101("<code>node.variants:#nbsp;<em>&Punctuated#lt;Variant,#nbsp;Comma#gt;</em></code>") --- 102
        102(["<code>.iter()</code>"]) --> 103
        103("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&Variant#gt;</em></code>") --- 2
        subgraph 2["<code>.filter_map()</code>"]
            201("<code>variant.discriminant:#nbsp;<em>&Option#lt;(Eq,#nbsp;Expr)#gt;</em></code>") --- 202
            202(["<code>.as_ref()</code>"]) --> 203
            203("<code><em>Option#lt;&(Eq,#nbsp;Expr)#gt;</em></code>") --- 204
            204(["<code>.map()</code>"]) --> 205
            205("<code><em>Option#lt;&Expr#gt;</em></code>")
        end
        2 --> 104
        104("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&Expr#gt;</em></code>")
{% end %}

</center>

## Iterator<Item = &mut Expr>

node: *&mut ItemEnum*

```rust
node.variants
    .iter_mut()
    .filter_map(|variant| {
        variant
            .discriminant
            .as_mut()
            .map(|(_, expr)| expr)
    })
```

<center>

{% mermaid() %}
    flowchart TD
        101("<code>node.variants:#nbsp;<em>&mut#nbsp;Punctuated#lt;Variant,#nbsp;Comma#gt;</em></code>") --- 102
        102(["<code>.iter_mut()</code>"]) --> 103
        103("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&mut#nbsp;Variant#gt;</em></code>") --- 2
        subgraph 2["<code>.filter_map()</code>"]
            201("<code>variant.discriminant:#nbsp;<em>&mut#nbsp;Option#lt;(Eq,#nbsp;Expr)#gt;</em></code>") --- 202
            202(["<code>.as_mut()</code>"]) --> 203
            203("<code><em>Option#lt;&mut#nbsp;(Eq,#nbsp;Expr)#gt;</em></code>") --- 204
            204(["<code>.map()</code>"]) --> 205
            205("<code><em>Option#lt;&mut#nbsp;Expr#gt;</em></code>")
        end
        2 --> 104
        104("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&mut#nbsp;Expr#gt;</em></code>")
{% end %}

</center>
