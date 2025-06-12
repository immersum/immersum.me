+++
title = "Struct ExprCall"
template = "mermaid-page.html"
+++

[docs.rs](https://docs.rs/syn/latest/syn/struct.ExprCall.html)

```rust
pub struct ExprCall {
    pub attrs: Vec<Attribute>,
    pub func: Box<Expr>,
    pub paren_token: Paren,
    pub args: Punctuated<Expr, Comma>,
}
```

## Iterator<Item = &Expr>

node: *&ExprCall*

```rust
[node.func.as_ref()]
    .into_iter()
    .chain(node.args.iter())
```

<center>

{% mermaid() %}
    flowchart TD
        subgraph 1["<code><em>[&Expr;#nbsp;1]</em></code>"]
            direction LR
            101("<code>node.func:#nbsp;<em>&Box#lt;Expr#gt;</em></code>") --- 102
            102(["<code>.as_ref()</code>"]) --> 103
            103("<code><em>&Expr</em></code>")
        end
        1 --- 201
        201(["<code>.into_iter()</code>"]) --> 202
        202("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&Expr#gt;</em></code>") --- 203
        203(["<code>.chain()</code>"]) --> 204
        204("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&Expr#gt;</em></code>")
        205("<code>node.args:#nbsp;<em>&Punctuated#lt;Expr,#nbsp;Comma#gt;</em></code>") --- 206
        206(["<code>.iter()</code>"]) --> 207
        207("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&Expr#gt;</em></code>") --- 203
{% end %}

</center>

## Iterator<Item = &mut Expr>

node: *&mut ExprCall*

```rust
[node.func.as_mut()]
    .into_iter()
    .chain(node.args.iter_mut())
```

<center>

{% mermaid() %}
    flowchart TD
        subgraph 1["<code><em>[&mut#nbsp;Expr;#nbsp;1]</em></code>"]
            direction LR
            101("<code>node.func:#nbsp;<em>&mut#nbsp;Box#lt;Expr#gt;</em></code>") --- 102
            102(["<code>.as_mut()</code>"]) --> 103
            103("<code><em>&mut#nbsp;Expr</em></code>")
        end
        1 --- 201
        201(["<code>.into_iter()</code>"]) --> 202
        202("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&mut#nbsp;Expr#gt;</em></code>") --- 203
        203(["<code>.chain()</code>"]) --> 204
        204("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&mut#nbsp;Expr#gt;</em></code>")
        205("<code>node.args:#nbsp;<em>&mut#nbsp;Punctuated#lt;Expr,#nbsp;Comma#gt;</em></code>") --- 206
        206(["<code>.iter_mut()</code>"]) --> 207
        207("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&mut#nbsp;Expr#gt;</em></code>") --- 203
{% end %}

</center>
