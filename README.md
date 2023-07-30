# Binary-Coded_Genetic_Algorithm
  It is a generalised optimisation framework where the solution (otherwise referred to as the genetics) is represented using binary strings. The decision variables for a binary-coded generic algorithm are represented using boolean variables.

## **Evaluation of initial population**
  ### Sample binary chromosomes taken into account
  | Index  | Chromosomes |
  | :-------------: | :-------------: |
  | 1 | 0110011010 |
  | 2 | 1100001011 |
  | 3 | 0011000110 |
  | 4 | 0100010111 |
  | 5 | 1010011101 |
  | 6 | 0110101000 |
  | 7 | 0010111011 |
  | 8 | 1110011000 |
  
  Here,
  l (Length of the string)= 10,
  N (No.of chromosomes)= 8 and
  T (No.of Generations)= 250.
  
  ### Determining the DV() values i.e Decoded values
  The decoded values of a binary chromosome is nothing but it's decimal value
  Example: DV(11011)= 27
  
  ### Determining the decision variables x1 and x2
  For easier computation, we split the binary chromosomes in to two strings and compute their DV() value as well as their decision variables individually.
  Decision varibles are calculated using the formula: 
  
  ![image](https://github.com/NakulSK221B/Binary-Coded_Genetic_Algorithm/assets/95758559/d5c96683-03f7-459f-8e94-19d6b7dad28e)
  
  Where U and L represent the maximum and minimum value combination of a binary string (i.e all 1's or all 0's)
  
  ### Calculating the objective function value
  The objective fitness value is then calculted using the Rosenbrock function
  
  ![image](https://github.com/NakulSK221B/Binary-Coded_Genetic_Algorithm/assets/95758559/67b0f486-f1dc-4d9b-b754-ece8c379af1e)
  
  
  ### The chromosome table generated after the previous steps:
  
  | Index  | Chromosomes | DV(x1) | DV(x2) | x1 | x2 | f(x1,x2) |
  | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: |
  | 1 | 01100 11010 | 12 | 26 | -1.129 | 2.710 | 210.445 |
  | 2 | 11000 01011 | 24 | 11 | 2.742 | -1.161 | 7536.407 |
  | 3 | 00110 00110 | 6 | 6 | -3.065 | -2.452 | 14041.882 |
  | 4 | 01000 10111 | 8 | 23 | -2.419 | 1.935 | 1546.7618 |
  | 5 | 10100 11101 | 20 | 29 | 1.4516 | 3.4839 | 189.75 |
  | 6 | 01101 01000 | 13 | 8 | -0.8065 | -1.9355 | 671.9732 |
  | 7 | 00101 11011 | 5 | 27  | -3.3871 | 2.9677 | 7252.3178 |
  | 8 | 11100 11000 | 28 | 24 | 4.0323 | 2.1935 | 19794.2709 |

## **Selection**
  The prupose of this step is to identify the good (usually above-average) solutions in the population. In this process, we eliminate the bad solutions.
  If a selection process takes place before search/variation operator, it is known as reproduction and the resultant set of solutions are called the _mating pool_.
  
  The selection noperator used in this algorithm is the **Binary Tournament Selection Operator**.
  
  ### Binary Tournament Selection Operator
  
  In this operator, 2 solutions are picked randomly and the better solution is picked i.e it is stochastic in nature
  
  Now considering the previously generated generation table, The Fitness values of the 8 chrosomes can be considered.
  
  | Index | Fitness |
  | :-------------: | :-------------: |
  | 1 | 210.445 |
  | 2 | 7536.407 |
  | 3 | 14041.882 |
  | 4 | 1546.7618 |
  | 5 | 189.75 |
  | 6 | 671.9732 |
  | 7 | 7252.3178 |
  | 8 | 19794.2709 |
  
  Now suppose the selection operator picks the solutions for index **2** and **4**:
  
  | Index | Fitness | Winner |
  | :-------------: | :-------------: | :-------------: |
  | 2 | 7536.407 | Index 4 |
  | 4 | 1546.7618 |
  
  Then **Index 4** is picked as the winner since its value is lesser than that of **Index 2**
  
  **First Interation**:
  
  ![image](https://github.com/NakulSK221B/Binary-Coded_Genetic_Algorithm/assets/95758559/cfcddfeb-c7c4-46ed-bf5c-32b3119c8051)
  
  
  This is done until all the solutions have been picked for comparision.(Whether they win or not)
  This however, minimizes the size of the population by half.
  Hence, it is repeated once again so as to maintain the same population count as the previous generation.
  
  **Second Iteration**:
  
  ![image](https://github.com/NakulSK221B/Binary-Coded_Genetic_Algorithm/assets/95758559/712280bb-7f0b-4e4a-97c2-7c64058cb063)
  
  Based on their number of occurences, The solutions can be evaluated as:
  1. _Bad solution_: Does not repeat in the 2nd iteration.
  2. _Good solution_: Does repeat in the 2nd iteration.
  
  Finally, a mating pool is generated as the result of the selection operator:
  
  ![image](https://github.com/NakulSK221B/Binary-Coded_Genetic_Algorithm/assets/95758559/1550c28d-fed5-4bed-8927-5be8caa5fb7e)

## **Crossover**:
 Crossover Operators are responsible for the generation of new solutions from a set of prexisting ones (in this case from the mating pool).
 It is performed with a greater factor of crossover probabilty, _Pc_. Generally, the value of _Pc_ is kept high so as to accomodate a loarger area of the search space.
 Here, Pc= 0.9.

 In this algorithm, we use the _single-point crossover operator_.

 ### **Single-Point Crossover Operator**

 Once the mating pool has been generated, random pairs of solutions with the _new indexes_ are picked for performing the crossover.
 
 A random probabilistic value, _R_ is generated for each pair.
 If R < Pc,
   Then the crossover operation is performed.
 Else,
   The pairs are copied to the new offspring generation table unchanged.

 In the crossover operation, a random number, _n_ in the range of (0,l) is considered and the chromosomes of the pair is split at the  _n_ th place and the first n binaries of are swapped. This creates a completly new chromosome whose decision values and fitness values are recalculated.

 Due to its stochastic nature, the crossover operator could either produce a _good_ solution or a _bad_ solution.
 * If a good solution is generated, it will have multiple copies in the further generations.
 * If a bad solution is generated, it will be eliminated in the selection process of further generations.

 Offspring generation:

 ![image](https://github.com/NakulSK221B/Binary-Coded_Genetic_Algorithm/assets/95758559/178a90ba-950a-4350-bf0b-20e5fc904621)

## **Mutation**.

  It is responsible for the search operation of the algorithm. The purpose is to maintain diversity in the population.
  It is usually decided by a lesser probabilistic factor, _Pm_.
  
  In this algorithm, we employ _Bit-Wise Mutation Operator._
  
  ### Bit-Wise Mutation Operator
  
  Similar to the Single-Point Crossover Operator, a random probabilistic number, _r_ is generated for each chromosome.
  
  If r < Pm,
   Then the mutation operation is performed.
  Else,
    The chromosome is copied to the new offspring generation table  unchanged.

  In the mutation operator, a random number, _n_ in the range of (0,l) is considered and the _n_th bit-position is mutated from 0 to 1 or 1 to 0.

  
  Similar to crossover and due to its stochastic nature, the muation operator could either produce a _good_ solution or a _bad_ solution.
 * If a good solution is generated, it will have multiple copies in the further generations.
 * If a bad solution is generated, it will be eliminated in the selection process of further generations.
  
  Offspring population after mutation:

  ![image](https://github.com/NakulSK221B/Binary-Coded_Genetic_Algorithm/assets/95758559/f994eb7d-f306-404e-8600-c0d9d54c4fcf)

## Survivor:
  This operation is used to preserve good solutions for the next generation. It is also referred to as Environmental Selection.
  
  In this Algorithm we utilize the _(μ+λ) Stratergy_, where μ represents the parent population and λ represents the offspring population.

  ### (μ+λ) Stratergy

  We consider the fitness values of the parent poulation as well as those of the offspring.
  Since it is a minimization problem, we select the solutions in an ascending order of their fitness values.
  This produces a new generation of chromosomes that represent the best soultions in the parent and offspring generations.

  New Generation:

  ![image](https://github.com/NakulSK221B/Binary-Coded_Genetic_Algorithm/assets/95758559/9113cb63-11d3-419a-a3a2-c8d6fce49318)

After the completion of the survivor phase the algorithm re-iterates the entire process yet again. This time the final population of the former iteration is considered as the parent.

This repeats for T no.of generations.


  

  

  
    


  



 


