+++
title = "Struct ExprCast"
+++

[docs.rs](https://docs.rs/syn/latest/syn/struct.ExprCast.html)

```rust
pub struct ExprCast {
    pub attrs: Vec<Attribute>,
    pub expr: Box<Expr>,
    pub as_token: As,
    pub ty: Box<Type>,
}
```

## Iterator<Item = &Expr>

node: *&ExprCast*

```rust
[node.expr.as_ref()]
```

<center>

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

</center>

## Iterator<Item = &mut Expr>

node: *&mut ExprCast*

```rust
[node.expr.as_mut()]
```

<center>

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

</center>
