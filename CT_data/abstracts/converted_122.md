














We present Pure-Past Action Masking (PPAM), a lightweight approach to action masking for reinforcement learning (RL). In PPAM, actions are disallowed ("masked") according to specifications expressed in Pure-Past Linear Temporal Logic (PPLTL) [3]. PPAM can enforce non-Markovian constraints, i.e., constraints based on the history of the system, rather than just the current state of the environment. The features used in the safety constraint need not be the same as those used by the learning agent, allowing a clear separation of concerns between the safety constraints and reward specifications of the (learning) agent. 

Via [4], we prove formally that PPAM is as expressive as shields [1], another approach to enforce non-Markovian constraints in RL. Then, thanks to a result from [2], we show that PPAM incur a single exponential blowup, instead of the double exponential one of shields. 


## Bibliography









1. Mohammed Alshiekh, Roderick Bloem, Rüdiger Ehlers, Bettina Könighofer, Scott Niekum, and Ufuk Topcu,_Safe reinforcement learning via shielding_,**_Proceedings of the Thirty-Second AAAI Conference on Artificial Intelligence_**(New Orleans, Louisiana, USA),(Sheila McIlraith, and Kilian Weirberger editors),vol. 32,AAAI Press,2018,pp. 2669–2678.
2. Luigi Bonassi, Giuseppe De Giacomo, Marco Favorito, Francesco Fuggitti, Alfonso Emilio Gerevini and Enrico Scala,_Planning for Temporally Extended Goals in Pure-Past Linear Temporal Logic_,**_Proceedings of the Thirty-Third International Conference on Automated Planning and Scheduling_**(Prague, Czech Republic),(Sven Koenig, Roni Stern, and Mauro Vallati editors),vol. 33,AAAI Press,2023,pp. 61-69.
3. Orna Lichtenstein, Amir Pnueli, and Lenore Zuck,_The glory of the past_,**_Logics of Programs_**(Brooklyn, NY, USA),(Rohit Parikh editor),vol. 193,Springer Berlin Heidelberg,1985,pp. 196–218.
4. Lenore Zuck,**_Past temporal logic_**,PhD thesis,The Weizmann Institute of Science,1986.





