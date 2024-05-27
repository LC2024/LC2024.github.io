

A commonly used slogan in finite model theory is that the first order logic
cannot count.  A simple manifestation of this is that
equicardinality, i.e., that two definable sets have the same power,
is not definable in first order logic.  A minimal way to overcome
this shortcoming (simultaneously preserving the regularity of
the logic) is to enhance first order logic by
**the equicardinality, or Härtig, quantifier** $$\mathsf{I}$$, with the
assiocated semantic rule
$$
  \mathfrak{M}\models \mathsf{I}xy\;(U(x),V(y)) \text{ if and only if }
  |U^{\mathfrak{M}}|=|V^{\mathfrak{M}}|,
$$
introduced by Klaus Härtig in 1965 [1], leading to the
logic $$\mathsf{FO(I)}$$.  However, being able to express equicardinality
of sets does not result in being able to express equicardinality
of $$n$$-ary relations. Indeed, Risto Kaila showed in [2] that
the $$(n+1)^\mathrm{th}$$ vectorization $$\mathsf{I}^{(n+1)}$$ of the
Härtig quantifier is not
expressible in the logic $$\mathsf{FO}(\mathsf{I}^{(n)})$$.
Unfortunately, Kaila presented only the construction of the needed
structures and left the tedious calculations for the reader.

I shall revisit Kaila's hierarchy result, presenting a novel proof.
The construction is simplified, so that the cardinalities
of definable relations will be polynomials of two integer parametres.
Working in the polynomial ring $$\mathbb{Z}[x,y]$$, I shall find
values for the parametres that give the desired undefinability
result. I expect that this kind of algebraic techniques can be
applied in similar situations in quantifier definability theory
in the future.

## Bibliography

1. Klaus H{ä}rtig,_{\"U}ber eine Quantifikator mit zwei Wirkungsbereiche_,  **_Colloquiumon the foundations of Mathematics, Mathematical Machinesand their Applications_** (1965), 31--36, Akad. Kiad\'{o}, Budapest.
2. Risto Kaila,_On probabilistic elimination of generalized quantifiers_,**_Random Structures Algorithms_** 19 (2001), no. 1,pp. 1--36.



