+++
title = "Struct ExprRange"
template = "mermaid-page.html"
+++

[docs.rs](https://docs.rs/syn/latest/syn/struct.ExprRange.html)

```rust
pub struct ExprRange {
    pub attrs: Vec<Attribute>,
    pub start: Option<Box<Expr>>,
    pub limits: RangeLimits,
    pub end: Option<Box<Expr>>,
}
```

## Iterator<Item = &Expr>

node: *&ExprRange*

```rust
node.start
    .as_slice()
    .iter()
    .chain(node.end.as_deref())
```

<center>

{% mermaid() %}
    flowchart TD
        101("<code>node.start:#nbsp;<em>&Option#lt;Box#lt;Expr#gt;#gt;</em></code>") --- 102
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
        106("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&Expr#gt;</em></code>") --- 107
        107(["<code>.chain()</code>"]) --> 108
        108("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&Expr#gt;</em></code>")
        109("<code>node.end:#nbsp;<em>&Option#lt;Box#lt;Expr#gt;#gt;</em></code>") --- 110
        110(["<code>.as_deref()</code>"]) --> 111
        111("<code><em>Option#lt;&Expr#gt;</em></code>") -..- 112
        112(["<code>.into_iter()</code>"]) -..-> 113
        113("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&Expr#gt;</em></code>") -.- 107
{% end %}

</center>

## Iterator<Item = &mut Expr>

node: *&mut ExprRange*

```rust
node.start
    .as_mut_slice()
    .iter_mut()
    .chain(node.end.as_deref_mut())
```

<center>

{% mermaid() %}
    flowchart TD
        101("<code>node.start:#nbsp;<em>&mut#nbsp;Option#lt;Box#lt;Expr#gt;#gt;</em></code>") --- 102
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
        106("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&mut#nbsp;Expr#gt;</em></code>") --- 107
        107(["<code>.chain()</code>"]) --> 108
        108("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&mut#nbsp;Expr#gt;</em></code>")
        109("<code>node.end:#nbsp;<em>&mut#nbsp;Option#lt;Box#lt;Expr#gt;#gt;</em></code>") --- 110
        110(["<code>.as_deref()</code>"]) --> 111
        111("<code><em>Option#lt;&mut#nbsp;Expr#gt;</em></code>") -..- 112
        112(["<code>.into_iter()</code>"]) -..-> 113
        113("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&mut#nbsp;Expr#gt;</em></code>") -.- 107
{% end %}

</center>
