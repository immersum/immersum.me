+++
title = "Struct ItemStatic"
template = "mermaid-page.html"
+++

[docs.rs](https://docs.rs/syn/latest/syn/struct.ItemStatic.html)

```rust
pub struct ItemStatic {
    pub attrs: Vec<Attribute>,
    pub vis: Visibility,
    pub static_token: Static,
    pub mutability: StaticMutability,
    pub ident: Ident,
    pub colon_token: Colon,
    pub ty: Box<Type>,
    pub eq_token: Eq,
    pub expr: Box<Expr>,
    pub semi_token: Semi,
}
```

## Iterator<Item = &Expr>

node: *&ItemStatic*

```rust
[node.expr.as_ref()]
```

<center>

{% mermaid() %}
    flowchart TD
        subgraph 1["<code><em>[&Expr;#nbsp;1]</em></code>"]
            direction LR
            101("<code>node.expr:#nbsp;<em>&Box#lt;Expr#gt;</em></code>") --- 102
            102(["<code>.as_ref()</code>"]) --> 103
            103("<code><em>&Expr</em></code>")
        end
        1 -.- 201
        201(["<code>.into_iter()</code>"]) -.-> 202
        202("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&Expr#gt;</em></code>")
{% end %}

</center>

## Iterator<Item = &mut Expr>

node: *&mut ItemStatic*

```rust
[node.expr.as_mut()]
```

<center>

{% mermaid() %}
    flowchart TD
        subgraph 1["<code><em>[&mut#nbsp;Expr;#nbsp;1]</em></code>"]
            direction LR
            101("<code>node.expr:#nbsp;<em>&mut#nbsp;Box#lt;Expr#gt;</em></code>") --- 102
            102(["<code>.as_mut()</code>"]) --> 103
            103("<code><em>&mut#nbsp;Expr</em></code>")
        end
        1 -.- 201
        201(["<code>.into_iter()</code>"]) -.-> 202
        202("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&mut#nbsp;Expr#gt;</em></code>")
{% end %}

</center>
