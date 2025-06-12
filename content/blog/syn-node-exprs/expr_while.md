+++
title = "Struct ExprWhile"
template = "mermaid-page.html"
+++

[docs.rs](https://docs.rs/syn/latest/syn/struct.ExprWhile.html)

```rust
pub struct ExprWhile {
    pub attrs: Vec<Attribute>,
    pub label: Option<Label>,
    pub while_token: While,
    pub cond: Box<Expr>,
    pub body: Block,
}
```

## Iterator<Item = &Expr>

node: *&ExprWhile*

```rust
[node.cond.as_ref()]
```

<center>

{% mermaid() %}
    flowchart TD
        subgraph 1["<code><em>[&Expr;#nbsp;1]</em></code>"]
            direction LR
            101("<code>node.cond:#nbsp;<em>&Box#lt;Expr#gt;</em></code>") --- 102
            102(["<code>.as_ref()</code>"]) --> 103
            103("<code><em>&Expr</em></code>")
        end
        1 -.- 201
        201(["<code>.into_iter()</code>"]) -.-> 202
        202("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&Expr#gt;</em></code>")
{% end %}

</center>

## Iterator<Item = &mut Expr>

node: *&mut ExprWhile*

```rust
[node.cond.as_mut()]
```

<center>

{% mermaid() %}
    flowchart TD
        subgraph 1["<code><em>[&mut#nbsp;Expr;#nbsp;1]</em></code>"]
            direction LR
            101("<code>node.cond:#nbsp;<em>&mut#nbsp;Box#lt;Expr#gt;</em></code>") --- 102
            102(["<code>.as_mut()</code>"]) --> 103
            103("<code><em>&mut#nbsp;Expr</em></code>")
        end
        1 -.- 201
        201(["<code>.into_iter()</code>"]) -.-> 202
        202("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&mut#nbsp;Expr#gt;</em></code>")
{% end %}

</center>
