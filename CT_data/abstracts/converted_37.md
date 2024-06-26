




This talk presents an application of proof mining to the viscosity approximation method (VAM) for accretive operators in Banach spaces, 
studied recently by Xu et al. [5]. Proof mining is a research program  concerned with the extraction, by using proof-theoretic techniques, of new quantitative and qualitative information from mathematical proofs. We refer to Kohlenbach's textbook [2] for details on proof mining.

Let $$X$$ be a normed space and $$A:X\to 2^X$$ be an accretive operator with a nonempty set of zeros. The VAMe iteration, a generalization of VAM obtained 
by adding error terms,  is defined as follows:

$$
\text{VAMe} \qquad x_0=x\in X, \quad x_{n+1}=\alpha_n f(x_n) +(1-\alpha_n)J_{\lambda_n}^Ax_n + e_n,
$$
where $$f:X\to X$$ is an $$\alpha$$-contraction for $$\alpha\in[0,1)$$, $$(\alpha_n)_{n\in\mathbb{N}}$$ is a sequence in $$[0,1]$$,  $$(\lambda_n)_{n\in\mathbb{N}}$$ is a sequence in $$(0,\infty)$$,  $$(e_n)_{n\in\mathbb{N}}$$ is a sequence in $$X$$,  and, for every $$n\in\mathbb{N}$$, $$J_{\lambda_n}^A$$ is 
the resolvent of order $$\lambda_n$$ of $$A$$.

In [1] we apply proof mining methods to obtain quantitative asymptotic regularity  results for the VAMe iteration, providing uniform rates of 
asymptotic regularity, $$\left(J_{\lambda_n}^A\right)$$-asymptotic regularity and, for all 
$$m\in\mathbb{N}$$,  $$J_{\lambda_m}^A$$-asymptotic regularity of VAMe. For concrete instances of the parameter sequences, linear rates are computed by applying \cite[Lemma 2.8]{LeuPin23}, a slight variation of a lemma due to Sabach and Shtern [4].  



 
## Bibliography

1.  P. Firmino, L. Leuştean, _Quantitative asymptotic regularity of the VAM iteration with error  terms for accretive operators in Banach spaces_, arXiv:2402.17947 [math.OC], 2024. 
2. U. Kohlenbach, **_Applied Proof Theory: Proof Interpretations and their Use in Mathematics_**, Springer Monographs in Mathematics, Springer, 2008.
3. L. Leuştean, P. Pinto _Rates of asymptotic regularity for the alternating Halpern-Mann  iteration_, **_Optimization Letters_**,  https://doi.org/10.1007/s11590-023-02002-y, 2023.  
4. S. Sabach, S. Shtern, _A first order method for solving convex bilevel optimization  problems_, **_SIAM Journal on Optimization_**,vol. 27 (2017), no. 2, pp. 640--660.
5. H.-K. Xu, N. Altwaijry, I. Alughaibi, S. Chebbi,  _The viscosity approximation method for accretive operators in Banach spaces_, **_Journal of Nonlinear and Variational Analysis_**, vol.  6 (2022), no.  1, pp. 37--50.




