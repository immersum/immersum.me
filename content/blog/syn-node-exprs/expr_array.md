+++
title = "Struct ExprArray"
template = "mermaid-page.html"
+++

[docs.rs](https://docs.rs/syn/latest/syn/struct.ExprArray.html)

```rust
pub struct ExprArray {
    pub attrs: Vec<Attribute>,
    pub bracket_token: Bracket,
    pub elems: Punctuated<Expr, Comma>,
}
```

## Iterator<Item = &Expr>

node: *&ExprArray*

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

node: *&mut ExprArray*

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
