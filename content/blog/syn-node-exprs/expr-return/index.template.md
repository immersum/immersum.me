+++
title = "Struct ExprReturn"
+++

[docs.rs](https://docs.rs/syn/latest/syn/struct.ExprReturn.html)

```rust
pub struct ExprReturn {
    pub attrs: Vec<Attribute>,
    pub return_token: Return,
    pub expr: Option<Box<Expr>>,
}
```

## Iterator<Item = &Expr>

node: *&ExprReturn*

```rust
node.expr
    .as_slice()
    .iter()
    .map(|expr| expr.as_ref())
```

```mermaid
flowchart TD
    101("<code>node.expr:#nbsp;<em>&Option#lt;Box#lt;Expr#gt;#gt;</em></code>") --- 102
    102(["<code>.as_slice()</code>"]) --> 103
    103("<code><em>&[Box#lt;Expr#gt;]</em></code>") --- 104
    104(["<code>.iter()</code>"]) --> 105
    105("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&Box#lt;Expr#gt;#gt;</em></code>") --- 2
    subgraph 2["<code>.map()</code>"]
        direction LR
        201("<code><em>&Box#lt;Expr#gt;</em></code>") --- 202
        202(["<code>.as_ref()</code>"]) --> 203
        203("<code><em>&Expr</em></code>")
    end
    2 --> 106
    106("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&Expr#gt;</em></code>")
```

## Iterator<Item = &mut Expr>

node: *&mut ExprReturn*

```rust
node.expr
    .as_mut_slice()
    .iter_mut()
    .map(|expr| expr.as_mut())
```

```mermaid
flowchart TD
    101("<code>node.expr:#nbsp;<em>&mut#nbsp;Option#lt;Box#lt;Expr#gt;#gt;</em></code>") --- 102
    102(["<code>.as_mut_slice()</code>"]) --> 103
    103("<code><em>&mut#nbsp;[Box#lt;Expr#gt;]</em></code>") --- 104
    104(["<code>.iter_mut()</code>"]) --> 105
    105("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&mut#nbsp;Box#lt;Expr#gt;#gt;</em></code>") --- 2
    subgraph 2["<code>.map()</code>"]
        direction LR
        201("<code><em>&mut#nbsp;Box#lt;Expr#gt;</em></code>") --- 202
        202(["<code>.as_mut()</code>"]) --> 203
        203("<code><em>&mut#nbsp;Expr</em></code>")
    end
    2 --> 106
    106("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&mut#nbsp;Expr#gt;</em></code>")
```
