+++
title = "Struct ExprRepeat"
template = "mermaid-page.html"
+++

[docs.rs](https://docs.rs/syn/latest/syn/struct.ExprRepeat.html)

```rust
pub struct ExprRepeat {
    pub attrs: Vec<Attribute>,
    pub bracket_token: Bracket,
    pub expr: Box<Expr>,
    pub semi_token: Semi,
    pub len: Box<Expr>,
}
```

## Iterator<Item = &Expr>

node: *&ExprRepeat*

```rust
[node.expr.as_ref(), node.len.as_ref()]
```

<center>

{% mermaid() %}
    flowchart TD
        subgraph 1["<code><em>[&Expr;#nbsp;2]</em></code>"]
            direction LR
            101("<code>node.expr:#nbsp;<em>&Box#lt;Expr#gt;</em></code>") --- 102
            102(["<code>.as_ref()</code>"]) --> 103
            103("<code><em>&Expr</em></code>")
            104("<code>node.len:#nbsp;<em>&Box#lt;Expr#gt;</em></code>") --- 105
            105(["<code>.as_ref()</code>"]) --> 106
            106("<code><em>&Expr</em></code>")
        end
        1 -.- 201
        201(["<code>.into_iter()</code>"]) -.-> 202
        202("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&Expr#gt;</em></code>")
{% end %}

</center>

## Iterator<Item = &mut Expr>

node: *&mut ExprRepeat*

```rust
[node.expr.as_mut(), node.len.as_mut()]
```

<center>

{% mermaid() %}
    flowchart TD
        subgraph 1["<code><em>[&mut#nbsp;Expr;#nbsp;2]</em></code>"]
            direction LR
            101("<code>node.expr:#nbsp;<em>&mut#nbsp;Box#lt;Expr#gt;</em></code>") --- 102
            102(["<code>.as_mut()</code>"]) --> 103
            103("<code><em>&mut#nbsp;Expr</em></code>")
            104("<code>node.len:#nbsp;<em>&mut#nbsp;Box#lt;Expr#gt;</em></code>") --- 105
            105(["<code>.as_mut()</code>"]) --> 106
            106("<code><em>&mut#nbsp;Expr</em></code>")
        end
        1 -.- 201
        201(["<code>.into_iter()</code>"]) -.-> 202
        202("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&mut#nbsp;Expr#gt;</em></code>")
{% end %}

</center>
