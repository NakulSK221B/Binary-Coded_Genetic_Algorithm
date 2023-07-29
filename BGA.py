# Skip to content
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 19:38:59 2022
@author: NAKUL
"""

"""
Created on Sun Jul  3 14:19:48 2022
@author: NAKUL
"""
from tabulate import tabulate
import math
import random
import matplotlib.pyplot

Chromosomes = ['0110011010', '1100001011', '0011000110', '0100010111', '1010011101', '0110101000', '0010111011',
               '1110011000']
Binary_Chromosomes = [format(int(str(Chromosomes[0]), 2), '010b'), format(int(str(Chromosomes[1]), 2), '010b'),
                      format(int(str(Chromosomes[2]), 2), '010b'), format(int(str(Chromosomes[3]), 2), '010b'),
                      format(int(str(Chromosomes[4]), 2), '010b'), format(int(str(Chromosomes[5]), 2), '010b'),
                      format(int(str(Chromosomes[6]), 2), '010b'), format(int(str(Chromosomes[7]), 2), '010b')]
Selected_Solutions = []
Mating_Pool = {"Old Index": [], "New Index": [], "Chromosomes": [], "DX(x1)": [], "DX(x2)": [], "x1": [], "x2": [],
               "f(x1,x2)": []}
Offspring = {"Index": [], "Chromosomes": [], "DX(x1)": [], "DX(x2)": [], "x1": [], "x2": [], "f(x1,x2)": []}
Offspring_M = {"Index": [], "Chromosomes": [], "DX(x1)": [], "DX(x2)": [], "x1": [], "x2": [], "f(x1,x2)": []}
New_Gen = {"Index": [], "Chromosomes": [], "DX(x1)": [], "DX(x2)": [], "x1": [], "x2": [], "f(x1,x2)": []}
Graph_x1 = []
Graph_x2 = []
Graph_fx = []
Graph_Iteration = []


class Operations():
    Current_Min_Sol = 0
    Previous_Min_Sol = 0
    Min_Sol_Repeat = 0
    Minimum_Solutions = []

    def __init__(self, l, N, T):
        # l--> Length of string
        # N--> No of samples
        # T--> No of iterations
        Break_Loop = False

        Parent = {"Index": [1, 2, 3, 4, 5, 6, 7, 8],
                  "Chromosomes": [Binary_Chromosomes[0], Binary_Chromosomes[1], Binary_Chromosomes[2],
                                  Binary_Chromosomes[3], Binary_Chromosomes[4], Binary_Chromosomes[5],
                                  Binary_Chromosomes[6], Binary_Chromosomes[7]],
                  "DX(x1)": [int(Binary_Chromosomes[0][:int((l / 2))], 2), int(Binary_Chromosomes[1][:int((l / 2))], 2),
                             int(Binary_Chromosomes[2][:int((l / 2))], 2), int(Binary_Chromosomes[3][:int((l / 2))], 2),
                             int(Binary_Chromosomes[4][:int((l / 2))], 2), int(Binary_Chromosomes[5][:int((l / 2))], 2),
                             int(Binary_Chromosomes[6][:int((l / 2))], 2),
                             int(Binary_Chromosomes[7][:int((l / 2))], 2)],
                  "DX(x2)": [int(Binary_Chromosomes[0][int((l / 2)):], 2), int(Binary_Chromosomes[1][int((l / 2)):], 2),
                             int(Binary_Chromosomes[2][int((l / 2)):], 2), int(Binary_Chromosomes[3][int((l / 2)):], 2),
                             int(Binary_Chromosomes[4][int((l / 2)):], 2), int(Binary_Chromosomes[5][int((l / 2)):], 2),
                             int(Binary_Chromosomes[6][int((l / 2)):], 2),
                             int(Binary_Chromosomes[7][int((l / 2)):], 2), ], "x1": [], "x2": [], "f(x1,x2)": []}
        Iteration_Count = 1
        for Iteration_Count in range(1, T + 1):
            # Re-defining the dictionaries
            Mating_Pool = {"Old Index": [], "New Index": [], "Chromosomes": [], "DX(x1)": [], "DX(x2)": [], "x1": [],
                           "x2": [], "f(x1,x2)": []}
            Offspring = {"Index": [], "Chromosomes": [], "DX(x1)": [], "DX(x2)": [], "x1": [], "x2": [], "f(x1,x2)": []}
            Offspring_M = {"Index": [], "Chromosomes": [], "DX(x1)": [], "DX(x2)": [], "x1": [], "x2": [],
                           "f(x1,x2)": []}
            New_Gen = {"Index": [], "Chromosomes": [], "DX(x1)": [], "DX(x2)": [], "x1": [], "x2": [], "f(x1,x2)": []}

            Operations.Initial_Population(self, l, N, Parent)
            Operations.Evaluate(self, l, N, Parent)
            Operations.Penalty_Check(self, N, Parent)
            Operations.Selection(self, l, N, Parent, Selected_Solutions, Mating_Pool)
            Operations.Penalty_Check(self, N, Mating_Pool)
            Operations.Crossover(self, l, N, Mating_Pool, Offspring)
            Operations.Penalty_Check(self, N, Offspring)
            Operations.Mutation(self, l, N, Mating_Pool, Offspring, Offspring_M)
            Operations.Penalty_Check(self, N, Offspring_M)
            Operations.Survival(self, l, N, Parent, Offspring_M, New_Gen)
            Operations.Penalty_Check(self, N, New_Gen)
            Parent = {"Index": [], "Chromosomes": [], "DX(x1)": [], "DX(x2)": [], "x1": [], "x2": [], "f(x1,x2)": []}
            # Copying contents from new gen to Parent
            for Copy_Count in range(0, N):
                Parent["Index"].append(New_Gen["Index"][Copy_Count])
                Parent["Chromosomes"].append(New_Gen["Chromosomes"][Copy_Count])
                Parent["DX(x1)"].append(New_Gen["DX(x1)"][Copy_Count])
                Parent["DX(x2)"].append(New_Gen["DX(x2)"][Copy_Count])

            if float(Operations.Current_Min_Sol) == float(Operations.Previous_Min_Sol):
                if Operations.Min_Sol_Repeat <= 2:
                    Operations.Min_Sol_Repeat += 1
                    Operations.Previous_Min_Sol == Operations.Current_Min_Sol
                else:
                    Break_Loop = True

            else:
                Operations.Minimum_Solutions.append(Operations.Current_Min_Sol)
                Operations.Previous_Min_Sol == Operations.Current_Min_Sol
            # Resetting the dictionaries
            Mating_Pool.clear()
            Offspring.clear()
            Offspring_M.clear()
            if Iteration_Count < T:
                New_Gen.clear()
            else:
                pass
            # Iteration_Count+=1
            Graph_Iteration.append(Iteration_Count)
            if Break_Loop:
                break
            else:
                pass

        print("After " + str(Iteration_Count) + " Iterations...")
        if len(Operations.Minimum_Solutions) == 0:
            print("\nThe Minimum Solution Is: ", Operations.Current_Min_Sol)
        else:
            print("\nThe Minimum Solution Is: ", min(Operations.Minimum_Solutions))

        # print("\nx1:",Graph_x1,"\nx2:",Graph_x2,"\nfx:",Graph_fx,"\nN:",Graph_Iteration)

        matplotlib.pyplot.scatter(Graph_x1, Graph_x2)
        matplotlib.pyplot.title("X1 V/s X2")
        matplotlib.pyplot.xlabel("X1")
        matplotlib.pyplot.ylabel("X2")

        matplotlib.pyplot.show()

        matplotlib.pyplot.plot(Graph_Iteration, Graph_fx)
        matplotlib.pyplot.title("f(x1,x2) V/s No.of Iterations")
        matplotlib.pyplot.xlabel("No.of Iterations")
        matplotlib.pyplot.ylabel("f(x1,x2)")
        matplotlib.pyplot.show()

    def Penalty_Check(self, N, Parent):
        for penalty_Check_count in range(0, N):
            Check_X1 = float(Parent["x1"][penalty_Check_count])
            Check_X2 = float(Parent["x2"][penalty_Check_count])
            if Check_X1 < -5 or Check_X2 < -4:
                Parent["f(x1,x2)"][penalty_Check_count] = str(float(Parent["f(x1,x2)"][penalty_Check_count]) + 500)
            elif Check_X1 > 5 or Check_X2 > 4:
                Parent["f(x1,x2)"][penalty_Check_count] = str(float(Parent["f(x1,x2)"][penalty_Check_count]) + 500)
            else:
                pass
            penalty_Check_count += 1

    def Initial_Population(self, l, N, Parent):

        # Operations.Chromosomes=['0110011010','1100001011','0011000110','0100010111','1010011101','0110101000','0010111011','1110011000']
        # Operations.Binary_Chromosomes=[format(int(str(Operations.Chromosomes[0]),2),'010b'),format(int(str(Operations.Chromosomes[1]),2),'010b'),format(int(str(Operations.Chromosomes[2]),2),'010b'),format(int(str(Operations.Chromosomes[3]),2),'010b'),format(int(str(Operations.Chromosomes[4]),2),'010b'),format(int(str(Operations.Chromosomes[5]),2),'010b'),format(int(str(Operations.Chromosomes[6]),2),'010b'),format(int(str(Operations.Chromosomes[7]),2),'010b')]
        # # print(Binary_Chromosomes[0][:int((l/2))])
        # #Operations.Parent ={"Index Number":["Chromosome", "DV(x1)","DV(x2)","x1","x2","f(x1,x2)"], 1:[Operations.Binary_Chromosomes[0] , int(Operations.Binary_Chromosomes[0][:int((l/2))],2) , int(Operations.Binary_Chromosomes[0][int((l/2)):],2)],2:[Operations.Binary_Chromosomes[1] , int(Operations.Binary_Chromosomes[1][:int((l/2))],2) , int(Operations.Binary_Chromosomes[1][int((l/2)):],2),],3:[Operations.Binary_Chromosomes[2] , int(Operations.Binary_Chromosomes[2][:int((l/2))],2) , int(Operations.Binary_Chromosomes[2][int((l/2)):],2),],4:[Operations.Binary_Chromosomes[3] ,int(Operations.Binary_Chromosomes[3][:int((l/2))],2) , int(Operations.Binary_Chromosomes[3][int((l/2)):],2),],5:[Operations.Binary_Chromosomes[4] , int(Operations.Binary_Chromosomes[4][:int((l/2))],2) , int(Operations.Binary_Chromosomes[4][int((l/2)):],2),],6:[Operations.Binary_Chromosomes[5] , int(Operations.Binary_Chromosomes[5][:int((l/2))],2) , int(Operations.Binary_Chromosomes[5][int((l/2)):],2),],7:[Operations.Binary_Chromosomes[6] , int(Operations.Binary_Chromosomes[6][:int((l/2))],2) , int(Operations.Binary_Chromosomes[6][int((l/2)):],2),],8:[Operations.Binary_Chromosomes[7] , int(Operations.Binary_Chromosomes[7][:int((l/2))],2) , int(Operations.Binary_Chromosomes[7][int((l/2)):],2),]}

        # Operations.Parent ={"Index":[1,2,3,4,5,6,7,8], "Chromosomes":[Operations.Binary_Chromosomes[0],Operations.Binary_Chromosomes[1],Operations.Binary_Chromosomes[2],Operations.Binary_Chromosomes[3],Operations.Binary_Chromosomes[4],Operations.Binary_Chromosomes[5],Operations.Binary_Chromosomes[6],Operations.Binary_Chromosomes[7]],"DX(x1)":[int(Operations.Binary_Chromosomes[0][:int((l/2))],2),int(Operations.Binary_Chromosomes[1][:int((l/2))],2),int(Operations.Binary_Chromosomes[2][:int((l/2))],2),int(Operations.Binary_Chromosomes[3][:int((l/2))],2),int(Operations.Binary_Chromosomes[4][:int((l/2))],2),int(Operations.Binary_Chromosomes[5][:int((l/2))],2),int(Operations.Binary_Chromosomes[6][:int((l/2))],2),int(Operations.Binary_Chromosomes[7][:int((l/2))],2)],"DX(x2)":[int(Operations.Binary_Chromosomes[0][int((l/2)):],2),int(Operations.Binary_Chromosomes[1][int((l/2)):],2),int(Operations.Binary_Chromosomes[2][int((l/2)):],2),int(Operations.Binary_Chromosomes[3][int((l/2)):],2),int(Operations.Binary_Chromosomes[4][int((l/2)):],2),int(Operations.Binary_Chromosomes[5][int((l/2)):],2),int(Operations.Binary_Chromosomes[6][int((l/2)):],2),int(Operations.Binary_Chromosomes[7][int((l/2)):],2),],"x1":[0,0,0,0,0,0,0,0],"x2":[0,0,0,0,0,0,0,0],"f(x1,x2)":[0,0,0,0,0,0,0,0]}

        # For X1
        for i in range(1, (N + 1)):
            x1 = -(5 - ((10 / ((pow(2, int(l / 2))) - 1)) * Parent["DX(x1)"][i - 1]))
            Parent["x1"].append(str(round(x1, 4)))
            i = i + 1

        # For X2
        for j in range(1, (N + 1)):
            x2 = -(4 - ((8 / ((pow(2, int((l / 2)))) - 1)) * Parent["DX(x2)"][j - 1]))
            Parent["x2"].append(str(round(x2, 4)))
            j = j + 1

        # print("Initial Population:\n",tabulate(Parent.items(), headers ="firstrow", tablefmt='psql'))

    def Evaluate(self, l, N, Parent):
        for i in range(1, (N + 1)):
            x1 = (Parent["x1"][i - 1])
            x2 = (Parent["x2"][i - 1])
            # print(x1,x2)
            fitness_Value = ((100 * (pow((float(x2) - pow(float(x1), 2)), 2))) + (pow((1 - float(x1)), 2)))
            fitness_Value = str(round(fitness_Value, 4))
            Parent["f(x1,x2)"].append(fitness_Value)
            i = i + 1

        print("Population after Evaluation:\n", tabulate(Parent.items(), headers="firstrow", tablefmt='psql'))

    def Selection(self, l, N, Parent, Selected_Solutions, Mating_Pool):
        Selected_Solutions = []
        sample_Count = 0
        j = 1
        for j in range(1, 3):
            Index_No = []
            Index_No = Parent["Index"]
            # print(Index_No)
            for k in range(0, round(N / 2)):
                Sample_Pair = tuple(random.sample(Index_No, 2))
                Index_No = set(Index_No) - set(Sample_Pair)
                print("\nSelected Sample Pair:", Sample_Pair)
                Selected_Solutions.append(min(Sample_Pair))
                print("Winner=", Selected_Solutions[sample_Count])
                sample_Count += 1
                k += 1
            j += 1
        Mating_Pool["Old Index"] = Selected_Solutions
        for i in range(0, sample_Count):
            Parent_Index = int(Selected_Solutions[i])
            Mating_Pool["Chromosomes"].append(Parent["Chromosomes"][Parent_Index - 1])
            Mating_Pool["DX(x1)"].append(Parent["DX(x1)"][Parent_Index - 1])
            Mating_Pool["DX(x2)"].append(Parent["DX(x2)"][Parent_Index - 1])
            Mating_Pool["New Index"].append(i + 1)
            Mating_Pool["x1"].append(Parent["x1"][Parent_Index - 1])
            Mating_Pool["x2"].append(Parent["x2"][Parent_Index - 1])
            Mating_Pool["f(x1,x2)"].append(Parent["f(x1,x2)"][Parent_Index - 1])
            i += 1

        print("\nMating pool:\n", tabulate(Mating_Pool.items(), headers="firstrow", tablefmt='psql'))

    def Crossover(self, l, N, Mating_Pool, Offspring):
        # Pc=round(random.uniform(0.800,0.999),1)
        Pc = 0.9
        Crossover_Pairs = []
        # Cross_Chromosomes=[]
        CrossOver_Count = 0
        # print(Index_No)
        Index_No = []
        Index_No = Mating_Pool["New Index"]
        print(Index_No)
        print(type(Index_No))
        for j in range(0, int(N / 2)):
            if bool(Index_No) == False:
                print("Index list empty")
            else:
                Sample_Pair = tuple(random.sample(Index_No, 2))
                Index_No = set(Index_No) - set(Sample_Pair)
                print("\nSelected Sample Pair:", Sample_Pair)
                Offspring["Index"].append(Sample_Pair[0])
                Offspring["Index"].append(Sample_Pair[1])
                r = round(random.uniform(0.0, 0.999), 2)
                if r < Pc:  # Perform CrossOver
                    Index_1 = Mating_Pool["New Index"].index(Sample_Pair[0])
                    Index_2 = Mating_Pool["New Index"].index(Sample_Pair[1])
                    Bin_1 = format(int(Mating_Pool["Chromosomes"][Index_1], 2), '010b')
                    Bin_2 = format(int(Mating_Pool["Chromosomes"][Index_2], 2), '010b')
                    # print("Before:\n",Bin_1,"\n",Bin_2)
                    Crossover_site = (random.randint(1, l))
                    # print(type(Mating_Pool["Chromosomes"][Index_1]))
                    Bin_1_Const = str(Bin_1[:Crossover_site])
                    Bin_1_Swap = str(Bin_1[Crossover_site:])
                    Bin_2_Const = str(Bin_2[:Crossover_site])
                    Bin_2_Swap = str(Bin_2[Crossover_site:])
                    # Bin_1=format(int(Bin_1_Const+Bin_2_Swap,2),'010b')
                    # Bin_2=format(int(Bin_2_Const+Bin_1_Swap,2),'010b')
                    Bin_1 = (Bin_1_Const + Bin_2_Swap)
                    Bin_2 = (Bin_2_Const + Bin_1_Swap)
                    Offspring["Chromosomes"].append(Bin_1)
                    Offspring["Chromosomes"].append(Bin_2)

                    CrossOver_Count += 1
                    # print("After:\n",Bin_1,"\n",Bin_2)
                else:
                    Index_1 = Mating_Pool["New Index"].index(Sample_Pair[0])
                    Index_2 = Mating_Pool["New Index"].index(Sample_Pair[1])
                    Bin_1 = format(int(Mating_Pool["Chromosomes"][Index_1], 2), '010b')
                    Bin_2 = format(int(Mating_Pool["Chromosomes"][Index_2], 2), '010b')
                    Offspring["Chromosomes"].append(Bin_1)
                    Offspring["Chromosomes"].append(Bin_2)

        # print(Crossover_Pairs)
        # print(Cross_Chromosomes)
        print("\nOffspring Population(After Crossover):...\n")
        Offspring["Index"].append(Crossover_Pairs)
        # Offspring["Chromosomes"].append(Cross_Chromosomes)
        for i in range(0, N):
            # print(i)
            # print(Offspring["Chromosomes"][i][:int((l/2))])
            # print(type(Offspring["Chromosomes"][i][:int((l/2))]))
            OFF_Bin_1 = Offspring["Chromosomes"][i][:int((l / 2))]
            OFF_Bin_2 = Offspring["Chromosomes"][i][int((l / 2)):]
            Offspring["DX(x1)"].append(int(format(int(OFF_Bin_1, 2), '05b'), 2))
            Offspring["DX(x2)"].append(int(format(int(OFF_Bin_2, 2), '05b'), 2))
            i += 1
        Operations.Initial_Population(self, l, N, Offspring)
        Operations.Evaluate(self, l, N, Offspring)

    def Mutation(self, l, N, Mating_Pool, Offspring, Offspring_M):
        # Pm=round(random.uniform(0.000,0.199),1)
        Pm = 0.15
        Index_No = []
        Index_No = Offspring["Index"][:8]
        print(Index_No)
        print(type(Index_No))
        for j in range(0, int(N)):
            Sample = (random.sample(Index_No, 1))
            # print(type(Sample))
            Index_No = set(Index_No) - set(Sample)
            print("\nSelected Solution Number:", Sample)
            r = round(random.uniform(0.0, 0.999), 2)
            if r < Pm:  # Perform CrossOver
                Index = Offspring["Index"].index(Sample[0])
                Bin_1 = Offspring["Chromosomes"][Index]
                # print("Before:\n",Bin_1)
                Mutation_site = (random.randint(1, l))
                # print(Mutation_site)
                # print(type(Mating_Pool["Chromosomes"][Index_1]))
                Bin_1_Left = str(Bin_1[:(Mutation_site)])
                Bin_1_Mutate = str(Bin_1[(Mutation_site):Mutation_site + 1])
                Bin_1_Right = str(Bin_1[(Mutation_site):])
                # print(Bin_1_Left,Bin_1_Mutate,Bin_1_Right)
                if Bin_1_Mutate == '0':
                    Bin_1_Mutate = '1'
                else:
                    Bin_1_Mutate = '0'
                Bin_1 = Bin_1_Left + Bin_1_Mutate + Bin_1_Right

                Offspring["Chromosomes"][Index] = Bin_1
                # print("After:\n",Bin_1)
            else:
                print("\nMutation Not Required....")

        for i in range(0, N):
            Index = Offspring["Index"].index(int(i + 1))
            Offspring_M["Chromosomes"].append(Offspring["Chromosomes"][Index])
            i += 1
        print(Offspring_M["Chromosomes"])
        print("\nOffspring Population(After Mutation):...\n")
        for i in range(0, N):
            # print(i)
            # print(Offspring["Chromosomes"][i][:int((l/2))])
            # print(type(Offspring["Chromosomes"][i][:int((l/2))]))
            Offspring_M["Index"].append('O' + str(i + 1))
            OFF_Bin_1 = Offspring_M["Chromosomes"][i][:int((l / 2))]
            OFF_Bin_2 = Offspring_M["Chromosomes"][i][int((l / 2)):]
            # print(type(OFF_Bin_2))
            Offspring_M["DX(x1)"].append(int(format(int(OFF_Bin_1, 2), '05b'), 2))
            Offspring_M["DX(x2)"].append(int(format(int(OFF_Bin_2, 2), '05b'), 2))
            i += 1
        Operations.Initial_Population(self, l, N, Offspring_M)
        Operations.Evaluate(self, l, N, Offspring_M)

    def Survival(self, l, N, Parent, Offspring_M, New_Gen):
        Survivors = []
        Survivors_less = []
        Survivor_Chromosome = []
        Solution_Count = 0
        less_sol_count = 0
        # Values=[]
        # for i in range(0,int(2*N)):

        #     Survivors["Index"].append(Parent["Index"][i-1:i])
        #     Survivors["f(x1,x2)"].append(Parent["f(x1,x2)"][i-1:i])
        #     Values.append(Parent["f(x1,x2)"][i-1:i])
        #     Survivors["Index"].append(Offspring_M["Index"][i-1:i])
        #     Survivors["f(x1,x2)"].append(Offspring_M["f(x1,x2)"][i-1:i])
        #     Values.append(Offspring_M["f(x1,x2)"][i-1:i])
        #     i+=1
        # print(Survivors)
        for j in range(0, 5):
            # Values.sort()
            # pint
            Survivors = Parent["f(x1,x2)"] + Offspring_M["f(x1,x2)"]
            Survivor_Chromosome = Parent["Chromosomes"] + Offspring_M["Chromosomes"]
            Survivors = [float(x) for x in Survivors]
            # print(Survivor_Chromosome)
            # for a in range(0,len(Survivor_Chromosome)):
            #     print(type(Survivor_Chromosome[a]))
        print(Survivors, Survivor_Chromosome)
        print("\nSuitable Fitness Values....")
        print(Survivors)
        Operations.Current_Min_Sol = min(Survivors)
        Min_Sol = min(Survivors)
        if Survivors.index(Min_Sol) < N:
            Graph_Index = Parent["f(x1,x2)"].index(str(Min_Sol))
            Graph_fx.append(Min_Sol)
            Graph_x1.append(Parent["x1"][Graph_Index])
            Graph_x2.append(Parent["x2"][Graph_Index])
        else:
            Graph_Index = Offspring_M["f(x1,x2)"].index(str(Min_Sol))
            Graph_fx.append(Min_Sol)
            Graph_x1.append(Offspring_M["x1"][Graph_Index])
            Graph_x2.append(Offspring_M["x2"][Graph_Index])
        for o in range(0, N):
            sol = min(Survivors)
            if sol != None:
                Survivors_less.append(sol)
                less_sol_count += 1
            else:
                pass
            o += 1
        print()
        for k in range(0, int(less_sol_count)):
            # print(Survivors,Survivor_Chromosome)
            if Survivors == None:
                print("\nCompletely Optimised Solution.....\n")

            else:

                print(min(Survivors))
                Optimum = float(min(Survivors))

                Solution_Count += 1
                New_Gen["Index"].append(k)
                print("\nOptimum Solution No." + str(k) + ": ", Optimum)
                Index = Survivors.index(Optimum)
                New_Chromosome = Survivor_Chromosome[Index]
                New_Bin_1 = (Survivor_Chromosome[Index][0:int((l / 2))])
                New_Bin_2 = (Survivor_Chromosome[Index][int((l / 2)):])
                print(Index, New_Chromosome, New_Bin_1, New_Bin_2)
                New_Gen["DX(x1)"].append(int(format(int(New_Bin_1, 2), '05b'), 2))
                New_Gen["DX(x2)"].append(int(format(int(New_Bin_2, 2), '05b'), 2))
                New_Gen["Chromosomes"].append(New_Chromosome)
                New_Gen["f(x1,x2)"].append(Optimum)
                # New_Chromosome=Operations.Chromosome_of_element(Survivors,Optimum,Parent,Offspring_M,l)
                # print(New_Chromosome)
                # print(type(New_Chromosome))
                # New_Gen["Chromosomes"].append(New_Chromosome)
                # print(type(New_Chromosome))
                # New_Ch_left=New_Gen["Chromosomes"][k-1][:int((l/2))]
                # New_Ch_right=New_Gen["Chromosomes"][k-1][int((l/2)):]
                # New_Gen["DX(x1)"].append(int(New_Chromosome[:int((l/2))]))
                # New_Gen["DX(x1)"].append(int(format(int(New_Chromosome[:int((l/2))],2),'05b'),2))
                # New_Gen["DX(x2)"].append(int(format(int(New_Chromosome[int((l/2)):],2),'05b'),2))
                occurence_sol = Survivors.count(Optimum)
                for n in range(occurence_sol):
                    Survivors.remove(Optimum)
                occurence_bin = Survivor_Chromosome.count(New_Chromosome)
                for m in range(occurence_bin):
                    Survivor_Chromosome.remove(New_Chromosome)

            k += 1

        # print(Op_Value)
        # print(Op_Chromosome)
        Operations.Initial_Population(self, l, Solution_Count, New_Gen)
        # Operations.Evaluate(self,l,Solution_Count,New_Gen)
        print("Final Population:\n", tabulate(New_Gen.items(), headers="firstrow", tablefmt='psql'))


op = Operations(10, 8, 2)
# op.Initial_Population(10,8,Parent)
# op.Evaluate(10,8,Parent)
# op.Selection(10,8)
