+++
title = "Struct ExprIf"
+++

[docs.rs](https://docs.rs/syn/latest/syn/struct.ExprIf.html)

```rust
pub struct ExprIf {
    pub attrs: Vec<Attribute>,
    pub if_token: If,
    pub cond: Box<Expr>,
    pub then_branch: Block,
    pub else_branch: Option<(Else, Box<Expr>)>,
}
```

## Iterator<Item = &Expr>

node: *&ExprIf*

```rust
[node.cond.as_ref()]
    .into_iter()
    .chain(
        node.else_branch
            .as_ref()
            .map(|(_, expr)| expr.as_ref()),
    )
```

```mermaid
flowchart TD
    subgraph 1["<code><em>[&Expr;#nbsp;1]</em></code>"]
        direction LR
        101("<code>node.cond:#nbsp;<em>&Box#lt;Expr#gt;</em></code>") --- 102
        102(["<code>.as_ref()</code>"]) --> 103
        103("<code><em>&Expr</em></code>")
    end
    1 ----- 201
    201(["<code>.into_iter()</code>"]) ----> 202
    202("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&Expr#gt;</em></code>") --- 203
    203(["<code>.chain()</code>"]) --> 204
    204("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&Expr#gt;</em></code>")
    205("<code>node.else_branch:#nbsp;<em>&Option#lt;(Else,#nbsp;Box#lt;Expr#gt;)#gt;</em></code>") --- 206
    206(["<code>.as_ref()</code>"]) --> 207
    207("<code><em>Option#lt;&#zwnj;(Else,#nbsp;Box#lt;Expr#gt;)#gt;</em></code>") --- 3
    subgraph 3["<code>.map()</code>"]
        direction LR
        301("<code><em>&Box#lt;Expr#gt;</em></code>") --- 302
        302(["<code>.as_ref()</code>"]) --> 303
        303("<code><em>&Expr</em></code>")
    end
    3 --> 208
    208("<code><em>Option#lt;&Expr#gt;</em></code>") -.- 209
    209(["<code>.into_iter()</code>"]) -.-> 210
    210("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&Expr#gt;</em></code>") -.- 203
```

## Iterator<Item = &mut Expr>

node: *&mut ExprIf*

```rust
[node.cond.as_mut()]
    .into_iter()
    .chain(
        node.else_branch
            .as_mut()
            .map(|(_, expr)| expr.as_mut()),
    )
```

```mermaid
flowchart TD
    subgraph 1["<code><em>[&mut#nbsp;Expr;#nbsp;1]</em></code>"]
        direction LR
        101("<code>node.cond:#nbsp;<em>&mut#nbsp;Box#lt;Expr#gt;</em></code>") --- 102
        102(["<code>.as_mut()</code>"]) --> 103
        103("<code><em>&mut#nbsp;Expr</em></code>")
    end
    1 ----- 201
    201(["<code>.into_iter()</code>"]) ----> 202
    202("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&mut#nbsp;Expr#gt;</em></code>") --- 203
    203(["<code>.chain()</code>"]) --> 204
    204("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&mut#nbsp;Expr#gt;</em></code>")
    205("<code>node.else_branch:#nbsp;<em>&mut#nbsp;Option#lt;(Else,#nbsp;Box#lt;Expr#gt;)#gt;</em></code>") --- 206
    206(["<code>.as_mut()</code>"]) --> 207
    207("<code><em>Option#lt;&mut#nbsp;(Else,#nbsp;Box#lt;Expr#gt;)#gt;</em></code>") --- 3
    subgraph 3["<code>.map()</code>"]
        direction LR
        301("<code><em>&mut#nbsp;Box#lt;Expr#gt;</em></code>") --- 302
        302(["<code>.as_mut()</code>"]) --> 303
        303("<code><em>&mut#nbsp;Expr</em></code>")
    end
    3 --> 208
    208("<code><em>Option#lt;&mut#nbsp;Expr#gt;</em></code>") -.- 209
    209(["<code>.into_iter()</code>"]) -.-> 210
    210("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&mut#nbsp;Expr#gt;</em></code>") -.- 203
```
