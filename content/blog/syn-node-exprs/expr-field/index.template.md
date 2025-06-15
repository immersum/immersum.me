+++
title = "Struct ExprField"
+++

[docs.rs](https://docs.rs/syn/latest/syn/struct.ExprField.html)

```rust
pub struct ExprField {
    pub attrs: Vec<Attribute>,
    pub base: Box<Expr>,
    pub dot_token: Dot,
    pub member: Member,
}
```

## Iterator<Item = &Expr>

node: *&ExprField*

```rust
[node.base.as_ref()]
```

```mermaid
flowchart TD
    subgraph 1["<code><em>[&Expr;#nbsp;1]</em></code>"]
        direction LR
        101("<code>node.base:#nbsp;<em>&Box#lt;Expr#gt;</em></code>") --- 102
        102(["<code>.as_ref()</code>"]) --> 103
        103("<code><em>&Expr</em></code>")
    end
    1 -.- 201
    201(["<code>.into_iter()</code>"]) -.-> 202
    202("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&Expr#gt;</em></code>")
```

## Iterator<Item = &mut Expr>

node: *&mut ExprField*

```rust
[node.base.as_mut()]
```

```mermaid
flowchart TD
    subgraph 1["<code><em>[&mut#nbsp;Expr;#nbsp;1]</em></code>"]
        direction LR
        101("<code>node.base:#nbsp;<em>&mut#nbsp;Box#lt;Expr#gt;</em></code>") --- 102
        102(["<code>.as_mut()</code>"]) --> 103
        103("<code><em>&mut#nbsp;Expr</em></code>")
    end
    1 -.- 201
    201(["<code>.into_iter()</code>"]) -.-> 202
    202("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&mut#nbsp;Expr#gt;</em></code>")
```
