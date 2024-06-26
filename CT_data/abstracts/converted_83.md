



We introduce a simple natural deduction system for reasoning with judgments of the form "there exists a proof of $$\varphi$$" to explore the notion of judgmental existence, following Martin-Löf's methodology of distinguishing between judgments and propositions. In this system, the existential judgment denoted as $$\varphi $$ _exist_ (or with explicit proof expressions as $$e \therefore \varphi$$) can be internalized into a modal notion of propositional existence denoted as $$\textsf{E} \varphi$$. This modality is closely related to truncation modality, a key tool for obtaining proof irrelevance. We provide a constructive meaning explanation for existential judgments and computational interpretation in the style of the Curry-Howard isomorphism for the corresponding existence modality.

The investigation of judgmental existence is directly motivated by [2] who informally considers a new judgment of the form $$\varphi$$ _exists_ as expressing the notion of "bare existence". The logic of judgmental existence itself is inspired by [1] and their judgmental reconstruction of modal logic. Formally, our system shares the most resemblance with their possibility logic and lax logic, however, we also allow existence premises of the form $$\varphi$$ _exists_ for elimination rules, not only true premises of the form $$\varphi$$ _true_. 

In its present form, our logic deals only with a fragment of propositional logic containing the existence modality $$\textsf{E}$$ and implication $$\to$$. We show that both logical connectives are locally sound and complete in this system. Furthermore, we show that the system satisfies the structural properties of exchange, weakening, and contraction and we prove substitution lemma, subject reduction, and the strong normalization property. We do not consider dependent types and proof irrelevance is assumed to be propositional, not judgmental.


## Bibliography















1.  Frank Pfenning and Rowan Davies,_A judgmental reconstruction of modal logic_,**_Mathematical Structures in Computer Science_**,vol. 11 (2001), no. 4, pp. 511--540.
2.  Per Martin-Löf,**_Philosophical aspects of intuitionistic type theory. Lecture notes_**,Per Martin-Löf: Transcriptions archive,{https://pml.flu.cas.cz/uploads/PML-LeidenLectures93.pdf},1993.





