






A classical result of provability logic is the fixed point theorem, proved independently by D. de Jongh and G. Sambin [3] with various proof methods for it ever since. Its statement is the following: Given a modal formula $$\phi(p)$$ that is modalized for $$p$$ --- i.e. every occurrence of $$p$$ in $$\phi$$ occurs within the scope of a $$\Box$$ --- there is a formula $$\sigma$$ without $$p$$ occurring in it such that $$GL \vdash \phi(\sigma) \rightarrow \sigma$$. In fact, this fixed point is unique under equivalence over GL. Sambin's construction [3,4], gives a rough upper bound for succinctness of the fixed point $$\sigma$$ relative to the original formula $$\phi$$ of the scale of $$\mid\sigma\mid \leq n^{O(n)} $$ where $$n = \mid\phi\mid$$. However there was no known succinctness lower bound.

The methods that we use to obtain a succinctness lower bound are those of formula-size games that were developed in the setting of Boolean function complexity [1] and of first-order logic and some temporal logics [2]. By now, the formula-size games have been adapted to a host of modal logics and used to obtain lower bounds on modal formulas expressing properties of Kripke models. These methods work by selecting a formula $$\phi$$ of a language $$\mathcal{L}$$ and two sets of models $$\mathcal{A}, \mathcal{B}$$ that are separable by $$\phi$$. Then the game is setup and played with rules according to a language $$\mathcal{L}'$$. Once the game is concluded, we obtain a formula $$\psi$$ in $$\mathcal{L}'$$ equivalent to $$\phi$$ and the size of $$\psi$$ can be calculated by a careful analysis of the game on the sets $$\mathcal{A}$$ and $$ \mathcal{B}$$.

Let $$\mathcal L_\Diamond$$ be the standard modal language (with an irreflexive modality) and $$\mathcal L_\dot{\Diamond}$$ be the language which instead includes a reflexive modality as primitive. 
In the case of GL, P. Iliev and D. Fern\'andez-Duque have derived an exponential ($$2^{O(n)}$$) succinctness lower bound for $$\mathcal{L}_{\dot{\Diamond}}$$ over $$\mathcal{L}_\Diamond$$ in GL where $$\dot{\Diamond}\phi =: \phi \vee \Diamond \phi$$. The sequence of formulas they used were defined inductively as:

  -  $$\phi_1 = p_1$$;
  -  $$\phi_{n+1} = \dot{\Diamond} (p_{n+1} \wedge \phi_n )$$.

Their result can be easily reformulated to show a succinctness lower bound for formulas in $$\mathcal{L}_{\Diamond}$$, thus giving the following:  
**Theorem.**
There exists a sequence of formulas $$(\psi_n)_{n<\omega}$$ linear in $$n$$ such that any fixed point in $$\mathcal L_\Diamond$$ for $$\psi_n$$ over $$\sf GL$$ has size $$2^{O(n)}$$.

We expand this succinctness lower bound in the following sense, we write formulas of $$\mathcal{L}$$ whose fixed point in $$\mathcal{L}_{\Diamond\dot{\Diamond}}$$ (i.e., the bi-modal logic with a reflexive and an irreflexive modality) is of the scale $$2^{O({n})}$$. This is done with formulas expressing a kind of tree embeddability into our model.
With this, we may improve upon the above Theorem as follows.  
**Theorem.**
There exists a sequence of formulas $$(\gamma_n)_{n<\omega}$$ linear in $$n$$ such that any fixed point in $$\mathcal L_{\Diamond\dot{\Diamond}}$$ for $$\gamma_n$$ over $$\sf GL$$ has size $$2^{O(n)}$$.












## Bibliography

1. Razborov A. A. Applications of matrix methods to the theory of lower bounds in  computational complexity. {\em Combinatorica}, 10(1):81--93, 1990.
2. Micah Adler and Neil Immerman. An n! lower bound on formula size. {\em ACM Trans. Comput. Logic}, 4(3):296–314, jul 2003.
3. Sambin Giovanni and Valentini Silvio. {The modal logic of provability. The sequential approach}. {\em Journal of Philosophical Logic}, 11(3):311 -- 342, 1982.
4. Lisa Reidhaar-Olson. {A new proof of the fixed-point theorem of provability logic.} {\em Notre Dame Journal of Formal Logic}, 31(1):37 -- 43, 1989.





































