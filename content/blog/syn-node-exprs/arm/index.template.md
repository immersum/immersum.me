+++
title = "Struct Arm"
+++

[docs.rs](https://docs.rs/syn/latest/syn/struct.Arm.html)

```rust
pub struct Arm {
    pub attrs: Vec<Attribute>,
    pub pat: Pat,
    pub guard: Option<(If, Box<Expr>)>,
    pub fat_arrow_token: FatArrow,
    pub body: Box<Expr>,
    pub comma: Option<Comma>,
}
```

## Iterator<Item = &Expr>

node: *&Arm*

```rust
node.guard
    .as_slice()
    .iter()
    .map(|(_, expr)| expr.as_ref())
    .chain([node.body.as_ref()])
```

```mermaid
flowchart TD
    101("<code>node.guard:#nbsp;<em>&Option#lt;(If,#nbsp;Box#lt;Expr#gt;)#gt;</em></code>") --- 102
    102(["<code>.as_slice()</code>"]) --> 103
    103("<code><em>&[(If,#nbsp;Box#lt;Expr#gt;)]</em></code>") --- 104
    104(["<code>.iter()</code>"]) --> 105
    105("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&#zwnj;(If,#nbsp;Box#lt;Expr#gt;)#gt;</em></code>") --- 2
    subgraph 2["<code><em>.map()</em></code>"]
        direction LR
        201("<code><em>&Box#lt;Expr#gt;</em></code>") --- 202
        202(["<code>.as_ref()</code>"]) --> 203
        203("<code><em>&Expr</em></code>")
    end
    2 --> 106
    106("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&Expr#gt;</em></code>") --- 107
    107(["<code>.chain()</code>"]) --> 108
    108("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&Expr#gt;</em></code>")
    subgraph 3["<code><em>[&Expr;#nbsp;1]</em></code>"]
        direction LR
        301("<code>node.body:#nbsp;<em>&Box#lt;Expr#gt;</em></code>") --- 302
        302(["<code>.as_ref()</code>"]) --> 303
        303("<code><em>&Expr</em></code>")
    end
    3 -...- 109
    109(["<code>.into_iter()</code>"]) -...-> 110
    110("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&Expr#gt;</em></code>") -.- 107
```

## Iterator<Item = &mut Expr>

node: *&mut Arm*

```rust
node.guard
    .as_mut_slice()
    .iter_mut()
    .map(|(_, expr)| expr.as_mut())
    .chain([node.body.as_mut()])
```

```mermaid
flowchart TD
    101("<code>node.guard:#nbsp;<em>&mut#nbsp;Option#lt;(If,#nbsp;Box#lt;Expr#gt;)#gt;</em></code>") --- 102
    102(["<code>.as_mut_slice()</code>"]) --> 103
    103("<code><em>&mut#nbsp;[(If,#nbsp;Box#lt;Expr#gt;)]</em></code>") --- 104
    104(["<code>.iter_mut()</code>"]) --> 105
    105("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&mut#nbsp;(If,#nbsp;Box#lt;Expr#gt;)#gt;</em></code>") --- 2
    subgraph 2["<code><em>.map()</em></code>"]
        direction LR
        201("<code><em>&mut#nbsp;Box#lt;Expr#gt;</em></code>") --- 202
        202(["<code>.as_mut()</code>"]) --> 203
        203("<code><em>&mut#nbsp;Expr</em></code>")
    end
    2 --> 106
    106("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&mut#nbsp;Expr#gt;</em></code>") --- 107
    107(["<code>.chain()</code>"]) --> 108
    108("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&mut#nbsp;Expr#gt;</em></code>")
    subgraph 3["<code><em>[&mut#nbsp;Expr;#nbsp;1]</em></code>"]
        direction LR
        301("<code>node.body:#nbsp;<em>&mut#nbsp;Box#lt;Expr#gt;</em></code>") --- 302
        302(["<code>.as_mut()</code>"]) --> 303
        303("<code><em>&mut#nbsp;Expr</em></code>")
    end
    3 -...- 109
    109(["<code>.into_iter()</code>"]) -...-> 110
    110("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&mut#nbsp;Expr#gt;</em></code>") -.- 107
```
