+++
title = "Struct ExprClosure"
template = "mermaid-page.html"
+++

[docs.rs](https://docs.rs/syn/latest/syn/struct.ExprClosure.html)

```rust
pub struct ExprClosure {
    pub attrs: Vec<Attribute>,
    pub lifetimes: Option<BoundLifetimes>,
    pub constness: Option<Const>,
    pub movability: Option<Static>,
    pub asyncness: Option<Async>,
    pub capture: Option<Move>,
    pub or1_token: Or,
    pub inputs: Punctuated<Pat, Comma>,
    pub or2_token: Or,
    pub output: ReturnType,
    pub body: Box<Expr>,
}
```

## Iterator<Item = &Expr>

node: *&ExprClosure*

```rust
[node.body.as_ref()]
```

<center>

{% mermaid() %}
    flowchart TD
        subgraph 1["<code><em>[&Expr;#nbsp;1]</em></code>"]
            direction LR
            101("<code>node.body:#nbsp;<em>&Box#lt;Expr#gt;</em></code>") --- 102
            102(["<code>.as_ref()</code>"]) --> 103
            103("<code><em>&Expr</em></code>")
        end
        1 -.- 201
        201(["<code>.into_iter()</code>"]) -.-> 202
        202("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&Expr#gt;</em></code>")
{% end %}

</center>

## Iterator<Item = &mut Expr>

node: *&mut ExprClosure*

```rust
[node.body.as_mut()]
```

<center>

{% mermaid() %}
    flowchart TD
        subgraph 1["<code><em>[&mut#nbsp;Expr;#nbsp;1]</em></code>"]
            direction LR
            101("<code>node.body:#nbsp;<em>&mut#nbsp;Box#lt;Expr#gt;</em></code>") --- 102
            102(["<code>.as_mut()</code>"]) --> 103
            103("<code><em>&mut#nbsp;Expr</em></code>")
        end
        1 -.- 201
        201(["<code>.into_iter()</code>"]) -.-> 202
        202("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&mut#nbsp;Expr#gt;</em></code>")
{% end %}

</center>
