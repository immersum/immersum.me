+++
title = """
One-liners for getting iterators over the expressions contained in the various types used in syn
"""
date = "2025-06-12"

[taxonomies]
blog-tags = ["Rust"]

[extra]
comments.host = "noc.social"
comments.username = "immersum"
comments.id = "114669335434162042"
+++

### What I wanted to achieve

In a recent project, [mplusfonts](/projects/mplusfonts/), which is an adaptation of a TrueType font
of the same name for use with a `no_std` graphics library, one of the things I wanted was to enable
users of the *#[strings::emit]* helper attribute to apply the attribute to the statement where the
result of a given expression is assigned to a variable; otherwise, users would have had to apply it
to the expression itself. My goal was to allow for the parent of any expression in general to carry
the attribute as shown in the example below.

```rust
// Before
let bitmap_font =
    #[strings::emit]
    mplus!(2, 500, 25, false, 1, 4);

// After
#[strings::emit]
let bitmap_font = mplus!(2, 500, 25, false, 1, 4);
```

The expression in this example is the invocation of the *mplus!* function-like macro; this is the
expression that we will want to operate on when expanding the *#[strings]* macro.

### How I got there

The [syn] crate offers a triplet of interfaces for traversing and manipulating the syntax tree:

* Functions in the [fold](https://docs.rs/syn/latest/syn/fold/index.html) module receive ownership
  of the node and are expected to return a value of the same type.
* Functions in the [visit](https://docs.rs/syn/latest/syn/visit/index.html) module get to borrow
  the node and inspect its value without modifying it.
* Functions in the [visit_mut](https://docs.rs/syn/latest/syn/visit_mut/index.html) module get to
  borrow the node and can also mutate its fields.

The third module contains the trait that *MacroVisitor* implements.

{{ icon(type="github") }}
<https://github.com/immersum/mplusfonts/blob/v0.2.0/macros/src/strings/visitor/mac.rs>

Although I could have reused the functions from the module that the trait methods call by default,
I wanted to implement a solution that involved writing call chains for gathering child expressions
from the various types of nodes; these would be run when a node was found that had been marked with
the helper attribute.

While iterating over the expressions that we got, which is the subject of this blog post, we can
filter the result set as needed.

```rust
for expr in exprs {
    if let syn::Expr::Macro(expr_macro) = expr {
        // Make changes to `&mut expr_macro.mac.tokens` here
    }
}
```

[syn]: https://crates.io/crates/syn

### Options can be turned into iterators

As we look through the data structures of the node types, we can see the various field types that
contain expressions:

* Some field types are simple expressions, others are the same with indirection: `Box<Expr>`
* Some field types have a cardinality of _1_ element, others contain _0_.._1_ elements wrapped in
  an option: `Option<Expr>`
* Options may also be combined with indirection: `Option<Box<Expr>>`
* There are field types that contain _n_ elements: `Punctuated<Expr, Comma>`
* Other field types include a few that are complex ones: `Option<(Eq, Expr)>`

The node types that interest us will have one or more of such fields. The most interesting part of
the task was determining the transformation logic to get an `impl Iterator<Item = &mut Expr>`
result for each node type when we have a `&mut node` argument.

There are multiple ways to get an iterator over a single value for example. A slice literal is more
compact in code size than a function call when an `impl IntoIterator<Item = &mut Expr>` is
sufficient, such as in case of a `for` loop. It can also be extended to two or more elements.
The *iter::once* function call is more readable on the other hand.

```rust
// Solution #1 - May also be written without .into_iter()
let exprs = [expr].into_iter();

// Solution #2
let exprs = iter::once(expr);
```

A third solution would be to wrap the expression in an option: `Some(expr).into_iter()`

This works because options can also be turned into iterators. While we are on the subject of
options, it is worth mentioning that an optional value can also be converted to a slice that is
either empty or has one element. Having a slice turned into an iterator is the preferred solution
in case of a `for` loop; otherwise, [clippy] would give us a warning - *for_loops_over_fallibles*.

[clippy]: https://github.com/rust-lang/rust-clippy

## List of types that carry attributes and contain expressions

### 1. Types representing variables and constants

The most common use case of the attribute is going to be in the context of some sort of
initialization, so that is where we will first have a look at gathering expressions.

#### 1.1. Local let bindings

* [Local](local/) - Contains _0_.._1_ initializations, which in turn contains _1_ expression after
  the `=` token, then _0_.._1_ expressions after an optional `else` keyword (the *diverge*
  expression).

#### 1.2. Static initializations

* [ItemStatic](item-static/) - Contains _1_ constant expression after the `=` token.

#### 1.3. Constant declarations

* [ItemConst](item-const/) - Contains _1_ constant expression after the `=` token.
* [ImplItemConst](impl-item-const/) - Contains _1_ constant expression after the `=` token (inside
  an `impl` block).
* [TraitItemConst](trait-item-const/) - Contains _0_.._1_ constant expressions after an optional
  `=` token (the *default* constant expression, which may be omitted in a trait definition).

### 2. Types representing type definitions

There are a few places in Rust where constant expressions can be parts of more complex syntax tree
nodes.

#### 2.1. Const generic parameters

* [ConstParam](const-param/) - Contains _0_.._1_ constant expressions after an optional `=` token
  (the *default* constant expression, which may be omitted).

#### 2.2. Enum definitions

* [ItemEnum](item-enum/) - Contains _n_ variants.
* [Variant](variant/) - Each variant contains _0_.._1_ constant expressions after an optional `=`
  token (the *discriminant* of the variant, which may have an explicit value set).

### 3. Types representing expressions

The rest are the types of syntax tree nodes listed here are the ones that represent expressions and
have fields with types that also represent expressions.

#### 3.1. Slice and tuple expressions

* [ExprArray](expr-array/) - Contains _n_ expressions inside the `[]` tokens (the *elems*).
* [ExprTuple](expr-tuple/) - Contains _n_ expressions inside the `()` tokens (the *elems*).

#### 3.2. Struct expressions

* [ExprStruct](expr-struct/) - Contains _n_ field-value pairs, followed by _0_.._1_ expressions
  after an optional `..` token (the base struct, which provides the *rest* of the values).
* [FieldValue](field-value/) - Each field-value pair contains _1_ expression after the `:` token.

#### 3.3. If and while expressions

* [ExprIf](expr-if/) - Contains _1_ expression after the `if` keyword (the *cond* expression),
  which is first followed by a block (the *then_branch*, which is itself **not an expression**),
  then another _0_.._1_ expressions after an optional `else` keyword (the *else_branch*, which can
  be a block expression, but it can also be a different type of expression).
* [ExprWhile](expr-while/) - Contains _1_ expression after the `while` keyword (the *cond*
  expression), which is followed by a block (the *body*, which is itself **not an expression**).
* [ExprLet](expr-let/) - Contains _1_ expression after the `=` token, called the scrutinee.

#### 3.4. For loop expressions

* [ExprForLoop](expr-for-loop/) - Contains _1_ expression after the `in` keyword (an expression
  that is either itself an iterator, or it can be turned into an iterator).

#### 3.5. Range expressions

* [ExprRange](expr-range/) - Contains _0_.._1_ expressions before and _0_.._1_ expressions after
  the `..` or `..=` token (the *start* and *end* expressions).
* [ExprRepeat](expr-repeat/) - Contains _1_ expression before and _1_ expression after the `;`
  token.

#### 3.6. Match expressions

* [ExprMatch](expr-match/) - Contains _1_ expression after the `match` keyword, called the
  scrutinee, followed by _n_ arms.
* [Arm](arm/) - Each `match` arm contains _0_.._1_ expressions after an optional `if` keyword (the
  *guard* expression), followed by _1_ expression after the `=>` token (the *body* expression,
  which can be a block, but it can also be a different type of expression).

#### 3.7. Break and return expressions

* [ExprBreak](expr-break/) - Contains _0_.._1_ expressions after the `break` keyword and an
  optional *label*.
* [ExprReturn](expr-return/) - Contains _0_.._1_ expressions after the `return` keyword.
* [ExprYield](expr-yield/) - Contains _0_.._1_ expressions after the `yield` keyword.

#### 3.8. Closure expressions

* [ExprClosure](expr-closure/) - Contains _1_ expression after the `||` tokens (the *body*
  expression, which can be a block, but it can also be a different type of expression).

#### 3.9. Cast expressions

* [ExprCast](expr-cast/) - Contains _1_ expression before the `as` keyword.

#### 3.10. Referencing and address-of operations

* [ExprReference](expr-reference/) - Contains _1_ expression after the `&` token and an optional
  `mut` keyword.
* [ExprRawAddr](expr-raw-addr/) - Contains _1_ expression.

#### 3.11. Try and await expressions

* [ExprTry](expr-try/) - Contains _1_ expression before the `?` token.
* [ExprAwait](expr-await/) - Contains _1_ expression before the `.` token and the `await` keyword
  (the `base` expression).

#### 3.12. Field access expressions

* [ExprField](expr-field/) - Contains _1_ expression before the `.` token (the `base` expression).

#### 3.13. Function and method call expressions

* [ExprCall](expr-call/) - Contains _1_ expression before the `()` tokens (the `func` expression),
  followed by _n_ expressions inside the `()` tokens (the *args*).
* [ExprMethodCall](expr-method-call/) - Contains _1_ expression before the `.` token and the method
  identifier (the *receiver*, which will become the `self` argument of the method), followed by _n_
  expressions inside the `()` tokens (the *args*).

#### 3.14. Index expressions

* [ExprIndex](expr-index/) - Contains _1_ expression before the `[]` tokens, followed by _1_
  expression inside the `[]` tokens (the *index*).

#### 3.15. Unary and binary operations

* [ExprUnary](expr-unary/) - Contains _1_ expression after the unary operator, called the operand.
* [ExprBinary](expr-binary/) - Contains _1_ expression before and _1_ expression after the binary
  operator, called the *left* and *right* operands.

#### 3.16. Assignment expressions

* [ExprAssign](expr-assign/) - Contains _1_ expression before and _1_ expression after the `=`
  token.

#### 3.17. Parenthesized and non-parenthesized group expressions

* [ExprParen](expr-paren/) - Contains _1_ expression inside the `()` tokens.
* [ExprGroup](expr-group/) - Contains _1_ expression.

#### 3.18. Blocks, try blocks, bodies of loops, etc.

There are syntax tree nodes that can have attributes applied, but these are expressions that
contain a block instead of a child expression (like the *then_branch* of `if` expressions).

* [ExprBlock](expr-block/), [ExprConst](expr-const/), [ExprUnsafe](expr-unsafe/),
  [ExprTryBlock](expr-try-block/), [ExprAsync](expr-async/), [ExprLoop](expr-loop/) - Contain _0_
  expressions.

#### 3.19. Macro invocations

* [ExprMacro](expr-macro/) - Contains a stream of subtrees with arbitrary nodes that serve as input
  to its invocation.

However, since this blog post describes a scenario where the expressions that we got to iterate
over were going to be narrowed down to macro invocations in the first place, finding expressions
nested in macro invocations would be something for another post.
