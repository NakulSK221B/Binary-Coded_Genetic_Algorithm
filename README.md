# Binary-Coded_Genetic_Algorithm
It is a generalised optimisation framework where the solution (otherwise referred to as the genetics) is represented using binary strings. The decision variables for a binary-coded generic algorithm are represented using boolean variables.

## Evaluation of initial population
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
