+++
title = "Struct ExprTuple"
template = "mermaid-page.html"
+++

[docs.rs](https://docs.rs/syn/latest/syn/struct.ExprTuple.html)

```rust
pub struct ExprTuple {
    pub attrs: Vec<Attribute>,
    pub paren_token: Paren,
    pub elems: Punctuated<Expr, Comma>,
}
```

## Iterator<Item = &Expr>

node: *&ExprTuple*

```rust
node.elems.iter()
```

<center>

{% mermaid() %}
    flowchart TD
        101("<code>node.elems:#nbsp;<em>&Punctuated#lt;Expr,#nbsp;Comma#gt;</em></code>") --- 102
        102(["<code>.iter()</code>"]) --> 103
        103("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&Expr#gt;</em></code>")
{% end %}

</center>

## Iterator<Item = &mut Expr>

node: *&mut ExprTuple*

```rust
node.elems.iter_mut()
```

<center>

{% mermaid() %}
    flowchart TD
        101("<code>node.elems:#nbsp;<em>&mut#nbsp;Punctuated#lt;Expr,#nbsp;Comma#gt;</em></code>") --- 102
        102(["<code>.iter_mut()</code>"]) --> 103
        103("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&mut#nbsp;Expr#gt;</em></code>")
{% end %}

</center>
