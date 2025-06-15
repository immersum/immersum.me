+++
title = "Struct Local"
+++

[docs.rs](https://docs.rs/syn/latest/syn/struct.Local.html)

```rust
pub struct Local {
    pub attrs: Vec<Attribute>,
    pub let_token: Let,
    pub pat: Pat,
    pub init: Option<LocalInit>,
    pub semi_token: Semi,
}

pub struct LocalInit {
    pub eq_token: Eq,
    pub expr: Box<Expr>,
    pub diverge: Option<(Else, Box<Expr>)>,
}
```

## Iterator<Item = &Expr>

node: *&Local*

```rust
node.init
    .as_slice()
    .iter()
    .flat_map(|local_init| {
        [local_init.expr.as_ref()]
            .into_iter()
            .chain(
                local_init
                    .diverge
                    .as_ref()
                    .map(|(_, expr)| expr.as_ref()),
            )
    })
```

```mermaid
flowchart TD
    subgraph 1["<code>.flat_map()</code>"]
        subgraph 2["<code><em>[&Expr;#nbsp;1]</em></code>"]
            direction LR
            201("<code>local_init.expr:#nbsp;<em>&Box#lt;Expr#gt;</em></code>") --- 202
            202(["<code>.as_ref()</code>"]) --> 203
            203("<code><em>&Expr</em></code>")
        end
        2 ----- 101
        101(["<code>.into_iter()</code>"]) ----> 102
        102("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&Expr#gt;</em></code>") --- 103
        103(["<code>.chain()</code>"]) --> 104
        104("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&Expr#gt;</em></code>")
        105("<code>local_init.diverge:#nbsp;<em>&Option#lt;(Else,#nbsp;Box#lt;Expr#gt;)#gt;</em></code>") --- 106
        106(["<code>.as_ref()</code>"]) --> 107
        107("<code><em>Option#lt;&#zwnj;(Else,#nbsp;Box#lt;Expr#gt;)#gt;</em></code>") --- 3
        subgraph 3["<code>.map()</code>"]
            direction LR
            301("<code><em>&Box#lt;Expr#gt;</em></code>") --- 302
            302(["<code>.as_ref()</code>"]) --> 303
            303("<code><em>&Expr</em></code>")
        end
        3 --> 108
        108("<code><em>Option#lt;&Expr#gt;</em></code>") -.- 109
        109(["<code>.into_iter()</code>"]) -.-> 110
        110("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&Expr#gt;</em></code>") --- 103
    end
    401("<code>node.init:#nbsp;<em>&Option#lt;LocalInit#gt;</em></code>") --- 402
    402(["<code>.as_slice()</code>"]) --> 403
    403("<code><em>&[LocalInit]</em></code>") --- 404
    404(["<code>.iter()</code>"]) --> 405
    405("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&LocalInit#gt;</em></code>") --- 1
    1 --> 406
    406("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&Expr#gt;</em></code>")
```

## Iterator<Item = &mut Expr>

node: *&mut Local*

```rust
node.init
    .as_mut_slice()
    .iter_mut()
    .flat_map(|local_init| {
        [local_init.expr.as_mut()]
            .into_iter()
            .chain(
                local_init
                    .diverge
                    .as_mut()
                    .map(|(_, expr)| expr.as_mut()),
            )
    })
```

```mermaid
flowchart TD
    subgraph 1["<code>.flat_map()</code>"]
        subgraph 2["<code><em>[&mut#nbsp;Expr;#nbsp;1]</em></code>"]
            direction LR
            201("<code>local_init.expr:#nbsp;<em>&mut#nbsp;Box#lt;Expr#gt;</em></code>") --- 202
            202(["<code>.as_mut()</code>"]) --> 203
            203("<code><em>&mut#nbsp;Expr</em></code>")
        end
        2 ----- 101
        101(["<code>.into_iter()</code>"]) ----> 102
        102("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&mut#nbsp;Expr#gt;</em></code>") --- 103
        103(["<code>.chain()</code>"]) --> 104
        104("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&mut#nbsp;Expr#gt;</em></code>")
        105("<code>local_init.diverge:#nbsp;<em>&mut#nbsp;Option#lt;(Else,#nbsp;Box#lt;Expr#gt;)#gt;</em></code>") --- 106
        106(["<code>.as_mut()</code>"]) --> 107
        107("<code><em>Option#lt;&mut#nbsp;(Else,#nbsp;Box#lt;Expr#gt;)#gt;</em></code>") --- 3
        subgraph 3["<code>.map()</code>"]
            direction LR
            301("<code><em>&mut#nbsp;Box#lt;Expr#gt;</em></code>") --- 302
            302(["<code>.as_mut()</code>"]) --> 303
            303("<code><em>&mut#nbsp;Expr</em></code>")
        end
        3 --> 108
        108("<code><em>Option#lt;&mut#nbsp;Expr#gt;</em></code>") -.- 109
        109(["<code>.into_iter()</code>"]) -.-> 110
        110("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&mut#nbsp;Expr#gt;</em></code>") --- 103
    end
    401("<code>node.init:#nbsp;<em>&mut#nbsp;Option#lt;LocalInit#gt;</em></code>") --- 402
    402(["<code>.as_mut_slice()</code>"]) --> 403
    403("<code><em>&mut#nbsp;[LocalInit]</em></code>") --- 404
    404(["<code>.iter_mut()</code>"]) --> 405
    405("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&mut#nbsp;LocalInit#gt;</em></code>") --- 1
    1 --> 406
    406("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&mut#nbsp;Expr#gt;</em></code>")
```
