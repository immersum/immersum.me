+++
title = "Struct FieldValue"
+++

[docs.rs](https://docs.rs/syn/latest/syn/struct.FieldValue.html)

```rust
pub struct FieldValue {
    pub attrs: Vec<Attribute>,
    pub member: Member,
    pub colon_token: Option<Colon>,
    pub expr: Expr,
}
```

## Iterator<Item = &Expr>

node: *&FieldValue*

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

node: *&mut FieldValue*

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
