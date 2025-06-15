+++
title = "Struct ConstParam"
+++

[docs.rs](https://docs.rs/syn/latest/syn/struct.ConstParam.html)

```rust
pub struct ConstParam {
    pub attrs: Vec<Attribute>,
    pub const_token: Const,
    pub ident: Ident,
    pub colon_token: Colon,
    pub ty: Type,
    pub eq_token: Option<Eq>,
    pub default: Option<Expr>,
}
```

## Iterator<Item = &Expr>

node: *&ConstParam*

```rust
node.default.as_slice()
```

```mermaid
flowchart TD
    101("<code>node.default:#nbsp;<em>&Option#lt;Expr#gt;</em></code>") --- 102
    102(["<code>.as_slice()</code>"]) --> 103
    103("<code><em>&[Expr]</em></code>") -.- 104
    104(["<code>.into_iter()</code>"]) -.-> 105
    105("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&Expr#gt;</em></code>")
```

## Iterator<Item = &mut Expr>

node: *&mut ConstParam*

```rust
node.default.as_mut_slice()
```

```mermaid
flowchart TD
    101("<code>node.default:#nbsp;<em>&mut#nbsp;Option#lt;Expr#gt;</em></code>") --- 102
    102(["<code>.as_mut_slice()</code>"]) --> 103
    103("<code><em>&mut [Expr]</em></code>") -.- 104
    104(["<code>.into_iter()</code>"]) -.-> 105
    105("<code><em>impl#nbsp;Iterator#lt;Item#nbsp;=#nbsp;&mut#nbsp;Expr#gt;</em></code>")
```
