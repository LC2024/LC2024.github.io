---
name: Models of arithmetic that satisfy more collection than induction
speakers:
  - Leszek Kołodziejczyk
chairs:
  - Johanna Franklin
categories:
  - Plenary Talk
time_start: '09:00'
time_end: '10:00'
talk_date: 2024-06-24
room: J222
---

Consider a model $$\mathbb{M}$$ of some amount of arithmetic, say induction for bounded 
formulas and the totality of the exponential function. This could be a structure in the basic language of ordered rings $$\{+,\cdot, 0,1, \le\}$$ or in $$\{+,\cdot, 0,1, \le\} \cup \{A_1,\ldots,A_k\}$$ for some finite number of unary predicates $$A_i$$ that can be treated as "oracles". The latter case has become important in recent decades due e.g. to its relevance for reverse mathematics: we may want to expand $$\mathbb{M}$$ by adding more oracle predicates to the language and eventually declare all the $$A_i$$ to be **bona fide** objects of a "second-order" sort, turning $$\mathbb{M}$$ into a model of some fragment of second-order arithmetic. This is a very natural technique in the study of the first-order strength of second-order arithmetic theories.

If $$\mathbb{M}$$ does not satisfy the full induction scheme in its language -- in the language of ordered rings, that would be Peano Arithmetic -- then exactly one of two things must hold. Either there is $$n \ge 0$$ such that $$\mathbb{M}$$ satisfies $$\Sigma^0_n$$-induction, $$\mathrm{I}\Sigma^0_n$$, but not the $$\Sigma^0_{n+1}$$-bounding (or collection) scheme, $$\mathrm{B}\Sigma^0_{n+1}$$, i.e.
$$ \forall x \! \le \! a   \exists y   \psi(x,y) \to \exists b  \forall x \! \le \! a   \exists y \! \le \! b   \psi(x,y),$$ 
for $$\Sigma^0_{n+1}$$ formulas $$\psi$$; or there is $$n \ge 1$$ such that  $$\mathbb{M}$$ satisfies $$\mathrm{B}\Sigma^0_n$$ but not $$\mathrm{I}\Sigma^0_{n}$$. Sometimes, one refers to models of the first kind as I-models and to those of the second kind as B-models.

A typical example of an I-model is a nonstandard **pointwise $$\Sigma^0_n$$-definable** one, i.e. one in which every singleton subset can be defined without using parameters. Not every I-model is elementarily equivalent to a {pointwise $$\Sigma^0_n$$-definable} one, but the example is canonical at least in the following sense:
every countable model of $$\Sigma^0_n$$-induction can be expanded (by adding a new oracle predicate)
to a pointwise $$\Sigma^0_n$$-definable model. (This is implicit in a theorem proved in 2015 by Towsner.)

B-models, on the other hand, are not particularly well-understood and have a number of surprising properties. For example,
it has been known since the 1990's that each countable B-model has continuum many automorphisms. Moreover,
no B-model admits a definable injection from the universe into a bounded initial segment, regardless of the complexity of the definition. Neither of these things is true in a pointwise definable model. More recently, some results have emerged showing that, in contrast to the case of I-models, the possibilities of expanding a B-model so that the expanded structure remains a B-model are quite restricted.

In my talk, I will discuss some old and new results on the specific features of B-models, as well as some open problems.
The emphasis will be on countable models and on features that have relevance to proof-theoretic issues such as provability and conservativity.


