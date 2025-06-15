+++
title = "Struct ExprAsync"
+++

[docs.rs](https://docs.rs/syn/latest/syn/struct.ExprAsync.html)

```rust
pub struct ExprAsync {
    pub attrs: Vec<Attribute>,
    pub async_token: Async,
    pub capture: Option<Move>,
    pub block: Block,
}
```
