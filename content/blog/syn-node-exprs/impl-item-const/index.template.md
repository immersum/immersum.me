+++
title = "Struct ImplItemConst"
+++

[docs.rs](https://docs.rs/syn/latest/syn/struct.ImplItemConst.html)

```rust
pub struct ImplItemConst {
    pub attrs: Vec<Attribute>,
    pub vis: Visibility,
    pub defaultness: Option<Default>,
    pub const_token: Const,
    pub ident: Ident,
    pub generics: Generics,
    pub colon_token: Colon,
    pub ty: Type,
    pub eq_token: Eq,
    pub expr: Expr,
    pub semi_token: Semi,
}
```

## Iterator<Item = &Expr>

node: *&ImplItemConst*

```rust
[&node.expr]
```

```mermaid
flowchart TD
    subgraph 1["<code><em>[&Expr;#nbsp;1]</em></code>"]
        101("<code>node.expr:#nbsp;<em>&Expr</em></code>")
    end
    1 -.- 201
    201(["<code>.into_iter()</code>"]) -.-> 202
    202("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&Expr#gt;</em></code>")
```

## Iterator<Item = &mut Expr>

node: *&mut ImplItemConst*

```rust
[&mut node.expr]
```

```mermaid
flowchart TD
    subgraph 1["<code><em>[&mut#nbsp;Expr;#nbsp;1]</em></code>"]
        101("<code>node.expr:#nbsp;<em>&mut#nbsp;Expr</em></code>")
    end
    1 -.- 201
    201(["<code>.into_iter()</code>"]) -.-> 202
    202("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&mut#nbsp;Expr#gt;</em></code>")
```
