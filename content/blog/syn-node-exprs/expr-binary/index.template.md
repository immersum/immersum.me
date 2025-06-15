+++
title = "Struct ExprBinary"
+++

[docs.rs](https://docs.rs/syn/latest/syn/struct.ExprBinary.html)

```rust
pub struct ExprBinary {
    pub attrs: Vec<Attribute>,
    pub left: Box<Expr>,
    pub op: BinOp,
    pub right: Box<Expr>,
}
```

## Iterator<Item = &Expr>

node: *&ExprBinary*

```rust
[node.left.as_ref(), node.right.as_ref()]
```

```mermaid
flowchart TD
    subgraph 1["<code><em>[&Expr;#nbsp;2]</em></code>"]
        direction LR
        101("<code>node.left:#nbsp;<em>&Box#lt;Expr#gt;</em></code>") --- 102
        102(["<code>.as_ref()</code>"]) --> 103
        103("<code><em>&Expr</em></code>")
        104("<code>node.right:#nbsp;<em>&Box#lt;Expr#gt;</em></code>") --- 105
        105(["<code>.as_ref()</code>"]) --> 106
        106("<code><em>&Expr</em></code>")
    end
    1 -.- 201
    201(["<code>.into_iter()</code>"]) -.-> 202
    202("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&Expr#gt;</em></code>")
```

## Iterator<Item = &mut Expr>

node: *&mut ExprBinary*

```rust
[node.left.as_mut(), node.right.as_mut()]
```

```mermaid
flowchart TD
    subgraph 1["<code><em>[&mut#nbsp;Expr;#nbsp;2]</em></code>"]
        direction LR
        101("<code>node.left:#nbsp;<em>&mut#nbsp;Box#lt;Expr#gt;</em></code>") --- 102
        102(["<code>.as_mut()</code>"]) --> 103
        103("<code><em>&mut#nbsp;Expr</em></code>")
        104("<code>node.right:#nbsp;<em>&mut#nbsp;Box#lt;Expr#gt;</em></code>") --- 105
        105(["<code>.as_mut()</code>"]) --> 106
        106("<code><em>&mut#nbsp;Expr</em></code>")
    end
    1 -.- 201
    201(["<code>.into_iter()</code>"]) -.-> 202
    202("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&mut#nbsp;Expr#gt;</em></code>")
```
