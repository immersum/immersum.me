+++
title = "Struct ItemConst"
+++

[docs.rs](https://docs.rs/syn/latest/syn/struct.ItemConst.html)

```rust
pub struct ItemConst {
    pub attrs: Vec<Attribute>,
    pub vis: Visibility,
    pub const_token: Const,
    pub ident: Ident,
    pub generics: Generics,
    pub colon_token: Colon,
    pub ty: Box<Type>,
    pub eq_token: Eq,
    pub expr: Box<Expr>,
    pub semi_token: Semi,
}
```

## Iterator<Item = &Expr>

node: *&ItemConst*

```rust
[node.expr.as_ref()]
```

```mermaid
flowchart TD
    subgraph 1["<code><em>[&Expr;#nbsp;1]</em></code>"]
        direction LR
        101("<code>node.expr:#nbsp;<em>&Box#lt;Expr#gt;</em></code>") --- 102
        102(["<code>.as_ref()</code>"]) --> 103
        103("<code><em>&Expr</em></code>")
    end
    1 -.- 201
    201(["<code>.into_iter()</code>"]) -.-> 202
    202("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&Expr#gt;</em></code>")
```

## Iterator<Item = &mut Expr>

node: *&mut ItemConst*

```rust
[node.expr.as_mut()]
```

```mermaid
flowchart TD
    subgraph 1["<code><em>[&mut#nbsp;Expr;#nbsp;1]</em></code>"]
        direction LR
        101("<code>node.expr:#nbsp;<em>&mut#nbsp;Box#lt;Expr#gt;</em></code>") --- 102
        102(["<code>.as_mut()</code>"]) --> 103
        103("<code><em>&mut#nbsp;Expr</em></code>")
    end
    1 -.- 201
    201(["<code>.into_iter()</code>"]) -.-> 202
    202("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&mut#nbsp;Expr#gt;</em></code>")
```
