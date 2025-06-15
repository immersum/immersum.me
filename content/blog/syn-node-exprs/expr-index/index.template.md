+++
title = "Struct ExprIndex"
+++

[docs.rs](https://docs.rs/syn/latest/syn/struct.ExprIndex.html)

```rust
pub struct ExprIndex {
    pub attrs: Vec<Attribute>,
    pub expr: Box<Expr>,
    pub bracket_token: Bracket,
    pub index: Box<Expr>,
}
```

## Iterator<Item = &Expr>

node: *&ExprIndex*

```rust
[node.expr.as_ref(), node.index.as_ref()]
```

```mermaid
flowchart TD
    subgraph 1["<code><em>[&Expr;#nbsp;2]</em></code>"]
        direction LR
        101("<code>node.expr:#nbsp;<em>&Box#lt;Expr#gt;</em></code>") --- 102
        102(["<code>.as_ref()</code>"]) --> 103
        103("<code><em>&Expr</em></code>")
        104("<code>node.index:#nbsp;<em>&Box#lt;Expr#gt;</em></code>") --- 105
        105(["<code>.as_ref()</code>"]) --> 106
        106("<code><em>&Expr</em></code>")
    end
    1 -.- 201
    201(["<code>.into_iter()</code>"]) -.-> 202
    202("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&Expr#gt;</em></code>")
```

## Iterator<Item = &mut Expr>

node: *&mut ExprIndex*

```rust
[node.expr.as_mut(), node.index.as_mut()]
```

```mermaid
flowchart TD
    subgraph 1["<code><em>[&mut#nbsp;Expr;#nbsp;2]</em></code>"]
        direction LR
        101("<code>node.expr:#nbsp;<em>&mut#nbsp;Box#lt;Expr#gt;</em></code>") --- 102
        102(["<code>.as_mut()</code>"]) --> 103
        103("<code><em>&mut#nbsp;Expr</em></code>")
        104("<code>node.index:#nbsp;<em>&mut#nbsp;Box#lt;Expr#gt;</em></code>") --- 105
        105(["<code>.as_mut()</code>"]) --> 106
        106("<code><em>&mut#nbsp;Expr</em></code>")
    end
    1 -.- 201
    201(["<code>.into_iter()</code>"]) -.-> 202
    202("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&mut#nbsp;Expr#gt;</em></code>")
```
