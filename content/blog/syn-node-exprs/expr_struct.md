+++
title = "Struct ExprStruct"
template = "mermaid-page.html"
+++

[docs.rs](https://docs.rs/syn/latest/syn/struct.ExprStruct.html)

```rust
pub struct ExprStruct {
    pub attrs: Vec<Attribute>,
    pub qself: Option<QSelf>,
    pub path: Path,
    pub brace_token: Brace,
    pub fields: Punctuated<FieldValue, Comma>,
    pub dot2_token: Option<DotDot>,
    pub rest: Option<Box<Expr>>,
}

pub struct FieldValue {
    pub attrs: Vec<Attribute>,
    pub member: Member,
    pub colon_token: Option<Colon>,
    pub expr: Expr,
}
```

## Iterator<Item = &Expr>

node: *&ExprStruct*

```rust
node.fields
    .iter()
    .map(|field_value| &field_value.expr)
    .chain(node.rest.as_deref())
```

<center>

{% mermaid() %}
    flowchart TD
        101("<code>node.fields:#nbsp;<em>&Punctuated#lt;FieldValue,#nbsp;Comma#gt;</em></code>") --- 102
        102(["<code>.iter()</code>"]) --> 103
        103("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&FieldValue#gt;</em></code>") --- 2
        subgraph 2["<code>.map()</code>"]
            201("<code>field_value.expr:#nbsp;<em>&Expr</em></code>")
        end
        2 --> 104
        104("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&Expr#gt;</em></code>") --- 105
        105(["<code>.chain()</code>"]) --> 106
        106("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&Expr#gt;</em></code>")
        107("<code>node.rest:#nbsp;<em>&Option#lt;Box#lt;Expr#gt;#gt;</em></code>") --- 108
        108(["<code>.as_deref()</code>"]) --> 109
        109("<code><em>Option#lt;&Expr#gt;</em></code>") -.- 110
        110(["<code>.into_iter()</code>"]) -.-> 111
        111("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&Expr#gt;</em></code>") -.- 105
{% end %}

</center>

## Iterator<Item = &mut Expr>

node: *&mut ExprStruct*

```rust
node.fields
    .iter_mut()
    .map(|field_value| &mut field_value.expr)
    .chain(node.rest.as_deref_mut())
```

<center>

{% mermaid() %}
    flowchart TD
        101("<code>node.fields:#nbsp;<em>&mut#nbsp;Punctuated#lt;FieldValue,#nbsp;Comma#gt;</em></code>") --- 102
        102(["<code>.iter_mut()</code>"]) --> 103
        103("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&mut#nbsp;FieldValue#gt;</em></code>") --- 2
        subgraph 2["<code>.map()</code>"]
            201("<code>field_value.expr:#nbsp;<em>&mut#nbsp;Expr</em></code>")
        end
        2 --> 104
        104("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&mut#nbsp;Expr#gt;</em></code>") --- 105
        105(["<code>.chain()</code>"]) --> 106
        106("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&mut#nbsp;Expr#gt;</em></code>")
        107("<code>node.rest:#nbsp;<em>&mut#nbsp;Option#lt;Box#lt;Expr#gt;#gt;</em></code>") --- 108
        108(["<code>.as_deref_mut()</code>"]) --> 109
        109("<code><em>Option#lt;&mut#nbsp;Expr#gt;</em></code>") -.- 110
        110(["<code>.into_iter()</code>"]) -.-> 111
        111("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&mut#nbsp;Expr#gt;</em></code>") -.- 105
{% end %}

</center>
