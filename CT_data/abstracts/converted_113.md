

The finitary powerset operator $$\mathsf{P_f}$$ maps a quasi-order $$X$$ to the
collection of its finite subsets ordered by a certain _domination
  quasi-ordering_ (also called the _Hoare embedding_) while preserving
the property of being a _well-quasi-order_. This is a widely used and
studied operator in mathematics and computer science. This is extended to its
transfinite _hyperation_ $$\mathsf{P^\alpha_f}$$ for every ordinal
$$\alpha$$, a form of iteration that satisfies the compositional property
$$\mathsf{P^{\alpha+\beta}_f}(X) = \mathsf{P^\alpha_f}(\mathsf{P^\beta_f}(X))$$.
Hyperations of ordinal functions were introduced by Fernández-Duque and Joosten,
and can extended to operators on quasi-orders using techniques developed by
Provenzano.

If $$X$$ is a well-quasi-order, then so is $$\mathsf{P^\alpha_f}(X)$$ for every
$$\alpha$$. When $$X$$ is a well-order, this assertion is trivially provable. It
explodes in reverse-mathematical strength as soon as the width of $$X$$ is at
least 2; for example, the statement for $$\mathsf{P^\omega_f}$$ already reaches
$$\mathsf{ACA^+_0}$$. Using techniques from the study of maximal order types of
well-quasi-orders and of $$\mathsf{P_f}$$ specifically, the order type of
$$\mathsf{P^{\omega^\alpha}_f}$$ is shown to have (fixpoint-free) Veblen-ian lower
bounds when considering quasi-orders of the form $$\beta \oplus 1$$ (aka,
well-orders with one incomparable element).

This is part of an ongoing project with Fedor Pakhomov, Philipp Provenzano, and
Giovanni Soldà to study better-quasi-orders and their reverse-mathematical
strength, and can be considered a generalization of the $$\mathsf{H_f}$$ operator
previously studied by Anton Freund.

## Bibliography

1.   David Fernández-Duque, Joost J. Joosten,  _Hyperations, Veblen progressions and transfinite iteration of ordinal functions_,  **_Annals of Pure and Applied Logic_**,  vol. 164,  issues 7--8,  pp. 785--801.
2.   Philipp Provenzano,  _The reverse mathematical strength of hyperations_,  **_Master's Thesis_**,  2022,  _(Unpublished)_.




