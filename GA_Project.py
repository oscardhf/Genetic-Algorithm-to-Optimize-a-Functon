import random
from tkinter import *
from tkinter import Checkbutton, Entry, messagebox

import matplotlib.pyplot as plt
from sympy import *
from sympy.combinatorics.graycode import bin_to_gray
import math
import cmath

class GUI():
    def partition(self, arr, low, high): 
        i = (low-1)         # index of smaller element pivot
        pivot = arr[high] 
    
        for j in range(low , high): 
    
            # If current element is smaller than the pivot 
            if   arr[j] < pivot: 
            
                # increment index of smaller element 
                i = i+1 
                arr[i],arr[j] = arr[j],arr[i] 
    
        arr[i+1],arr[high] = arr[high],arr[i+1]

        return (i+1)

    def quickSort(self, arr,low,high): 
        if low < high: 
    
            # pi is partitioning index, arr[p] is now at right place 
            pi = self.partition(arr,low,high) 
    
            # Separately sort elements before partition and after partition 
            self.quickSort(arr, low, pi-1) 
            self.quickSort(arr, pi+1, high) 

    #This function transform a list in a string reading each data in the list
    def listToString(self, s):
        str1 = ''
        for ele in s:
            str1 += str(ele)

        return str1

    #This function transform a list in a string reading each data in the list separating by a comma and a space
    #each data with the next to avoid confusion when the text is showed
    def listToString4Real(self, s):
        str1 = ''
        for ele in s:
            str1 += str(ele)+', '

        return str1

    #This function give us the size of the list we need based on the range that user specified
    def cuentaBits(self, n):
        aux = 0
        while n>0:
            n = n>>1
            aux+=1
        
        return aux

    #Given a number n returns a string with n zeros
    def sizeZero(self, n):
        s = ''
        while n > 0:
            s += '0'
            n -= 1
        
        return s

    #Given a list L with elements type int returns a list with elements type binary string
    def int2Bin(self, L):
        L1 = []
        aux = 0
        cad = ''

        for i in L:
            if aux < len(bin(i).split('0b')[1]):
                aux = len(bin(i).split('0b')[1])
        
        for i in L:
            cad = self.sizeZero(aux-len(bin(i).split('0b')[1])) + bin(i).split('0b')[1]
            L1.append(cad)

        return L1

    #This function apply a sin(x) function to each data in the list
    def sinFunction(self, L):
        aux = 0
        for i in L:
            aux = math.sin(i)
            self.L2.append(aux)

        return self.L2

    #This function apply a sin^2(x) function to each data in the list
    def sin2Function(self, L):
        aux = 0
        for i in L:
            aux = pow(math.sin(i), 2)
            self.L2.append(aux)

        return self.L2

    #This function apply a cos(x) function to each data in the list
    def cosFunction(self, L):
        aux = 0
        for i in L:
            aux = math.cos(i)
            self.L2.append(aux)

        return self.L2

    #This function apply a cos^2(x) function to each data in the list
    def cos2Function(self, L):
        aux = 0
        for i in L:
            aux = pow(math.cos(i), 2)
            self.L2.append(aux)

        return self.L2

    #This function read the entry line that user write to generate a new fit function
    def fitFunction(self, L):
        aux = 0
        try:
            for x in L:
                aux = eval(self.fitFunc.get())
                self.L2.append(aux)
        except:
            self.info1 = messagebox.showerror('Ooops!', 'That kind of instruction is not supported! :(')
            self.root.destroy()
        
        return self.L2

    #This function generate randomly data in type binary
    def binData(self, r, q1):
        self.r = int(r)
        self.q1 = int(q1)
        self.r = self.cuentaBits(self.r)
        #print(self.r)
        for _ in range(self.q1):
            for _ in range(self.r):
                if(random.random()>0.5):
                    self.L.append(1)
                else:
                    self.L.append(0)
            self.L1.append(self.listToString(self.L))
            self.L.clear()
        
        self.info1 = messagebox.showinfo('Binary Data', self.L1)

        for i in self.L1:
            self.valInt = int(i, 2)
            self.L.append(self.valInt)
        
        self.info1 = messagebox.showinfo('Binary Int Representation Data', self.L)

        #plt.plot(self.sinFunction(self.L), 'c--v')
        self.quickSort(self.L,0,len(self.L)-1)


        #plt.plot(self.sinFunction(self.L), 'g--^')
        self.L1.clear()
        self.L1 = self.int2Bin(self.L).copy()

        #plt.figure(1)
        self.info2 = messagebox.showinfo('Binary Sorted Data', self.L1)
        self.info2 = messagebox.showinfo('Binary Sorted Int Representation Data', self.L)

        return self.L

    #This function generate randomly data in type gray code
    def grayData(self, r, q):
        self.r = int(r)
        self.q1 = int(q)
        self.r = self.cuentaBits(self.r)
        #print(self.r)
        for _ in range(self.q1):
            for _ in range(self.r):
                if(random.random()>0.5):
                    self.L.append(1)
                else:
                    self.L.append(0)
            self.L1.append(self.listToString(self.L))
            self.L.clear()
            
        for i in self.L1:
            self.valGray = bin_to_gray(i)
            self.L.append(self.valGray)
            
        # print('Binary', self.L1)
        # print('Gray code', self.L)
        self.info1 = messagebox.showinfo('Binary Data', self.L1)

        for i in self.L1:
            self.valInt = int(i, 2)
            self.L2.append(self.valInt)
        
        self.info1 = messagebox.showinfo('Binary Int Representation Data', self.L2)

        self.L1.clear()
            
        for i in self.L:
            self.valInt = int(i, 2)
            self.L1.append(self.valInt)
            
        #plt.plot(self.L1, 'r--d')

        self.quickSort(self.L1,0,len(self.L1)-1)

        self.L.clear()
        self.L = self.int2Bin(self.L1).copy()

        self.info2 = messagebox.showinfo('Gray Code Data', self.L)
        self.info2 = messagebox.showinfo('Gray Code Int Representation Data', self.L1)       

        return self.L1

    #This function execute the Roulette Selection Operation
    def roulOp(self, L):
        counter = 0
        prob = 0
        L1 = L.copy()

        for i in L:
            counter += i

        print(counter)

        for i in L:
            prob = i/counter
            self.L3.append(prob)

        counter = 0

        for i in self.L3:
            counter += i
            self.L5.append(counter)

        counter = 0

        for i in self.L5:
            counter += i

        print(self.L3)
        print(self.L5)
        print(counter)

        self.L3.clear()
        ran = 0

        print('----------------------------------')

        tam = len(L)

        while len(self.L3) < tam:
            ran = random.uniform(0, counter)
            for i in self.L5:
                if i < ran:
                    print(i)
                    print(ran)
                    print('--------------------------------------')
                    print()
                else:
                    print(self.L5.index(i))
                    print()
                    self.L3.append(L[self.L5.index(i)])
                    L.pop(self.L5.index(i))
                    self.L5.remove(i)
                    print(ran)
                    print('--------------------------------------')

        print('Esto es la copia de L en roulOp')
        print(L1)
        print('Esto es L4 en roulOp')
        print(self.L4)
        print()
        print('Esto es el mensaje de roulOp')
        print(self.L3)

        for i in self.L3:
            self.L5.append(L1.index(i))
        
        print()
        print('Esto es el retorno de roulOp')
        print(self.L5)

        return self.L5

    #Tournament Selection Operator
    def tournament(self, L):
        aux = 0
        aux1 = 0
        L1 = L.copy()

        print('Esto es L')
        print(L)
        random.shuffle(L)
        print('Esto es shuffle(L)')
        print(L)
        
        for _ in range(len(L)):
            aux = random.choice(L)
            aux1 = random.choice(L)
            if  float(aux) < float(aux1):
                self.L3.append(aux1)
            else:
                self.L3.append(aux)
                
        print('Esto es el mensaje de Tournament')
        print(self.L3)

        for i in self.L3:
            self.L5.append(L1.index(i))
        
        print()
        print('Esto es el retorno de Tournament')
        print(self.L5)

        return self.L5

    #Probabilistic Tournament Selection
    def tournamentProb(self, L):
        aux = 0
        aux1 = 0
        L1 = L.copy()

        print('Esto es L')
        print(L)
        random.shuffle(L)
        print('Esto es shuffle(L)')
        print(L)
        
        for _ in range(len(L)):
            aux = random.choice(L)
            aux1 = random.choice(L)

            if(random.random()>0.5):
                if  float(aux) < float(aux1):
                    self.L3.append(aux1)
                else:
                    self.L3.append(aux)
            else:
                if  float(aux) > float(aux1):
                    self.L3.append(aux1)
                else:
                    self.L3.append(aux)
                
        print('Esto es el mensaje de TournamentProb')
        print(self.L3)

        for i in self.L3:
            self.L5.append(L1.index(i))
        
        print()
        print('Esto es el retorno de TournamentProb')
        print(self.L5)

        return self.L5

    #1 Point Mating Operator
    def point(self, Li, Ls, n):
        aux = []
        aux1 = []
        L = []
        num = random.randint(1, len(Li)-1)

        print(num)
        print(Li)
        print(Ls)

        if n > 0:
            for i in range(num):
                print(i)
                aux.append(Li[i])
                aux1.append(Ls[i])
            
            Li.reverse()
            Ls.reverse()
            
            for i in range(num):
                Li.pop()
                Ls.pop()

            print(aux)
            print(aux1)

            Li.reverse()
            Ls.reverse()

            for i in Li:
                aux1.append(i)
            
            for i in Ls:
                aux.append(i)

            print(aux)
            print(aux1)

            return self.point(aux, aux1, n-1)
        else:
            L.append(self.listToString(Li))
            L.append(self.listToString(Ls))

            return L

    #This Function choose the pairs that will mating
    def matPoint(self, Li, Ls, n):
        L = []

        #From Li we take the index for each pair that will mating
        for i in range(0, len(Li), 2):
            print('Esto es el valor de i en Li')
            print(Li[i])
            print('Esto es el valor de i+1 en Li')
            print(Li[i+1])
            print('Esto es el valor de de Ls[Li[i]]')
            print(Ls[int(Li[i])])
            print('Esto es el valor de Ls[Li[i+1]]')
            print(Ls[int(Li[i+1])])
            L.extend(self.point(list(Ls[int(Li[i])]), list(Ls[int(Li[i+1])]), n))
        
        print(L)

        for i in L:
            self.valInt = int(i, 2)
            self.L4.append(self.valInt)

        return L

    #With this function we can make the insertion and displacement mutation
    def Insert(self, L, n):
        aux = 0
        aux1 = 0
        aux2 = 0

        if random.random() < 0.3:
            while n > 0:
                aux = random.randint(0, len(L)-1)
                aux1 = L[aux]
                L.pop(aux)
                aux2 = random.randint(0, len(L)-1)

                while aux2 == aux:
                    aux2 = random.randint(0, len(L)-1)

                L.insert(aux2, aux1)

                print(L)
            
                n -= 1
            
            return L
        else:
            return L

    def mutInsert(self, L, n):
        L1 = []
        L2 = []
        valInt = 0

        for i in L:
            L1 = self.Insert(list(i), n).copy()
            print('Esto es L1 de la función mutInsert')
            print(L1)
            L2.append(self.listToString(L1))
            L1.clear()
        
        for i in L2:
            valInt = int(i, 2)
            self.L4.append(valInt)
        
        return L2

    #Reciprocal Exchange Mutation
    def Exchange(self, L):
        aux = 0
        aux1 = 0
        aux2 = 0
        aux3 = 0

        if random.random() < 0.3:
            aux = random.randint(0, len(L)-1)
            aux1 = L[aux]
            L.pop(aux)
            aux2 = random.randint(0, len(L)-1)

            while aux2 == aux:
                aux2 = random.randint(0, len(L)-1)
            
            aux3 = L[aux2]

            L.pop(aux2)
            L.insert(aux2, aux1)
            L.insert(aux, aux3)

            print('Esto es L en if')
            print(L)
            return L
        else:
            print('Esto es L en else')
            print(L)
            return L

    def mutExchange(self, L):
        L1 = []
        L2 = []
        valInt = 0

        for i in L:
            L1 = self.Exchange(list(i)).copy()
            print('Esto es L1 de la función mutExchange')
            print(L1)
            L2.append(self.listToString(L1))
            L1.clear()
        
        for i in L2:
            valInt = int(i, 2)
            self.L4.append(valInt)
        
        return L2

    #This function permits that the program know what kind of mutation operator will be use in the GA
    def mutOP(self, L, n):
        aux = random.randint(0, len(L)-2)

        if self.mutType.get()==1:
            print('Esto es L en mutType')
            print(self.L)
            self.L.clear()
            print('Esto es L1 en mutType')
            print(self.L1)
            self.L1.clear()
            self.L = self.mutInsert(L, 1).copy()
            print('Esto es L2 en mutOP')
            print(self.L2)
            self.L2.clear()
            print('Esto es L3 en mutOp')
            print(self.L3)
            self.L3.clear()
            print('Esto es L4 en mutOP')
            plt.plot(self.L4, 'c--*')
            print(self.L4)
            self.L4.clear()
            print('Esto es L5 en mutOp')
            print(self.L5)
            self.L5.clear()
            self.info1 = messagebox.showinfo('Insertion Mutation Generated Data', self.L)
            plt.title('Genetic Algorithm')
            plt.legend(('Original Data', 'Fitness Data', 'Selected Parents', 'Generated Sons', 'Mutated Sons'), prop = {'size': 10}, loc='upper left')
            plt.show()
            self.info1 = messagebox.showinfo('New Generation', 'Click next')
            self.newGen(self.L, n-1)

        elif self.mutType.get()==2:
            print('Esto es L en mutType')
            print(self.L)
            self.L.clear()
            print('Esto es L1 en mutType')
            print(self.L1)
            self.L1.clear()
            self.L = self.mutInsert(L, aux).copy()
            print('Esto es L2 en mutOP')
            print(self.L2)
            self.L2.clear()
            print('Esto es L3 en mutOp')
            print(self.L3)
            self.L3.clear()
            print('Esto es L4 en mutOP')
            plt.plot(self.L4, 'c--*')
            print(self.L4)
            self.L4.clear()
            print('Esto es L5 en mutOp')
            print(self.L5)
            self.L5.clear()
            self.info1 = messagebox.showinfo('Displacement Mutation Generated Data', self.L)
            plt.title('Genetic Algorithm')
            plt.legend(('Original Data', 'Fitness Data', 'Selected Parents', 'Generated Sons', 'Mutated Sons'), prop = {'size': 10}, loc='upper left')
            plt.show()
            self.info1 = messagebox.showinfo('New Generation', 'Click next')
            self.newGen(self.L, n-1)

        elif self.mutType.get()==3:
            print('Esto es L en mutType')
            print(self.L)
            self.L.clear()
            print('Esto es L1 en mutType')
            print(self.L1)
            self.L1.clear()
            self.L = self.mutExchange(L).copy()
            print('Esto es L2 en mutOP')
            print(self.L2)
            self.L2.clear()
            print('Esto es L3 en mutOp')
            print(self.L3)
            self.L3.clear()
            print('Esto es L4 en mutOP')
            plt.plot(self.L4, 'c--*')
            print(self.L4)
            self.L4.clear()
            print('Esto es L5 en mutOp')
            print(self.L5)
            self.L5.clear()
            self.info1 = messagebox.showinfo('Reciprocal Mutation Generated Data', self.L)
            plt.title('Genetic Algorithm')
            plt.legend(('Original Data', 'Fitness Data', 'Selected Parents', 'Generated Sons', 'Mutated Sons'), prop = {'size': 10}, loc='upper left')
            plt.show()
            self.info1 = messagebox.showinfo('New Generation', 'Click next')
            self.newGen(self.L, n-1)

        else:
            self.info1 = messagebox.showerror('No Mutation Operator Selected!', 'Select a Mutation Operator')

    #This function permits that the program know what kind of pairing operator will be use in the GA
    def matingOp(self, L, n):
        aux = 0

        if self.matingType.get()==1:
            if len(self.L) == 0:
                self.L3 = self.matPoint(L, self.L1, 1).copy()
            else:
                self.L3 = self.matPoint(L, self.L, 1).copy()
            
            print('Esto es L2 en matingOP')
            print(self.L2)
            self.L2.clear()
            print('Esto es L3 en matingOp')
            print(self.L3)
            print('Esto es L4 en matingOP')
            plt.plot(self.L4, 'y--^')
            print(self.L4)
            self.L4.clear()
            print('Esto es L5 en matingOp')
            print(self.L5)
            self.L5.clear()
            self.info1 = messagebox.showinfo('1 Point Mating Generated Data', self.L3)
            self.mutOP(self.L3, n)

        elif self.matingType.get()==2:
            if len(self.L) == 0:
                self.L3 = self.matPoint(L, self.L1, 2).copy()
            else:
                self.L3 = self.matPoint(L, self.L, 2).copy()
            
            print('Esto es L2 en matingOP')
            print(self.L2)
            self.L2.clear()
            print('Esto es L3 en matingOp')
            print(self.L3)
            print('Esto es L4 en matingOP')
            plt.plot(self.L4, 'y--^')
            print(self.L4)
            self.L4.clear()
            print('Esto es L5 en matingOp')
            print(self.L5)
            self.L5.clear()
            self.info1 = messagebox.showinfo('2 Points Mating Generated Data', self.L3)
            self.mutOP(self.L3, n)

        elif self.matingType.get()==3:
            aux = random.randint(1, len(L)-2)
            if len(self.L) == 0:
                self.L3 = self.matPoint(L, self.L1, aux).copy()
            else:
                self.L3 = self.matPoint(L, self.L, aux).copy()
            
            print('Esto es L2 en matingOP')
            print(self.L2)
            self.L2.clear()
            print('Esto es L3 en matingOp')
            print(self.L3)
            print('Esto es L4 en matingOP')
            plt.plot(self.L4, 'y--^')
            print(self.L4)
            self.L4.clear()
            print('Esto es L5 en matingOp')
            print(self.L5)
            self.L5.clear()
            self.info1 = messagebox.showinfo('Uniform Mating Generated Data for '+str(aux)+' Points', self.L3)
            self.mutOP(self.L3, n)
        
        else:
            self.info1 = messagebox.showerror('No Mating Operator Selected!', 'Select a Mating Operator')

    #This function permits that the program know what kind of selection operator will be use in the GA
    def selecOp(self, L, n):
        if self.selecType.get()==1:
            self.L2 = self.roulOp(L).copy()
            self.info1 = messagebox.showinfo('Roulette Selection', self.listToString4Real(self.L3))
            print('Esto es L en selecOp')
            print(self.L)
            print('Esto es L1 en selecOp')
            print(self.L1)
            print('Esto es L2 en selecOp')
            print(self.L2)
            print('Esto es L3 en selecOp')
            print(self.L3)
            plt.plot(self.L3, 'g--v')
            self.L3.clear()
            print('Esto es L4 en selecOp')
            print(self.L4)
            self.L4.clear()
            self.matingOp(self.L2, n)

        elif self.selecType.get()==2:
            self.L2 = self.tournament(L).copy()
            self.info1 = messagebox.showinfo('Tournament Selection', self.listToString4Real(self.L3))
            print('Esto es L en selecOp')
            print(self.L)
            print('Esto es L1 en selecOp')
            print(self.L1)
            print('Esto es L2 en selecOp')
            print(self.L2)
            print('Esto es L3 en selecOp')
            print(self.L3)
            plt.plot(self.L3, 'g--v')
            self.L3.clear()
            print('Esto es L4 en selecOp')
            print(self.L4)
            self.L4.clear()
            self.matingOp(self.L2, n)

        elif self.selecType.get()==3:
            self.L2 = self.tournamentProb(L).copy()
            self.info1 = messagebox.showinfo('Probabilistic Tournament Selection', self.listToString4Real(self.L3))
            print('Esto es L en selecOp')
            print(self.L)
            print('Esto es L1 en selecOp')
            print(self.L1)
            print('Esto es L2 en selecOp')
            print(self.L2)
            print('Esto es L3 en selecOp')
            print(self.L3)
            plt.plot(self.L3, 'g--v')
            self.L3.clear()
            print('Esto es L4 en selecOp')
            print(self.L4)
            self.L4.clear()
            self.matingOp(self.L2, n)

        else:
            self.info1 = messagebox.showerror('No Selection Operator Selected!', 'Select a Selection Operator')

    #This function permits that the program know what kind of fit function will be use to implement in the GA
    def function(self, L, n):
        if self.fitFun.get()==1:
            self.L4 = self.sinFunction(L).copy()
            plt.plot(self.L4, 'r--d')
            self.info1 = messagebox.showinfo('Sin(x) Function of Generated Data', self.listToString4Real(self.L4))
            print('Esto es L en function')
            print(self.L)
            print('Esto es L1 en function')
            print(self.L1)
            print('Esto es L2 en function')
            print(self.L2)
            self.L2.clear()
            print('Esto es L3 en function')
            print(self.L3)
            self.L3.clear()
            print('Esto es L4 en function')
            print(self.L4)
            self.selecOp(self.L4, n)

        elif self.fitFun.get()==2:
            self.L4 = self.sin2Function(L).copy()
            plt.plot(self.L4, 'r--d')
            self.info1 = messagebox.showinfo('Sin^2(x) Function of Generated Data', self.listToString4Real(self.L4))
            print('Esto es L en function')
            print(self.L)
            print('Esto es L1 en function')
            print(self.L1)
            print('Esto es L2 en function')
            print(self.L2)
            self.L2.clear()
            print('Esto es L3 en function')
            print(self.L3)
            self.L3.clear()
            print('Esto es L4 en function')
            print(self.L4)
            self.selecOp(self.L4, n)

        elif self.fitFun.get()==3:
            self.L4 = self.cosFunction(L).copy()
            plt.plot(self.L4, 'r--d')
            self.info1 = messagebox.showinfo('Cos(x) Function of Generated Data', self.listToString4Real(self.L4))
            print('Esto es L en function')
            print(self.L)
            print('Esto es L1 en function')
            print(self.L1)
            print('Esto es L2 en function')
            print(self.L2)
            self.L2.clear()
            print('Esto es L3 en function')
            print(self.L3)
            self.L3.clear()
            print('Esto es L4 en function')
            print(self.L4)
            self.selecOp(self.L4, n)

        elif self.fitFun.get()==4:
            self.L4 = self.cos2Function(L).copy()
            plt.plot(self.L4, 'r--d')
            self.info1 = messagebox.showinfo('Cos^2(x)Function of Generated Data', self.listToString4Real(self.L4))
            print('Esto es L en function')
            print(self.L)
            print('Esto es L1 en function')
            print(self.L1)
            print('Esto es L2 en function')
            print(self.L2)
            self.L2.clear()
            print('Esto es L3 en function')
            print(self.L3)
            self.L3.clear()
            print('Esto es L4 en function')
            print(self.L4)
            self.selecOp(self.L4, n)

        elif self.fitFunc.get() == '':
            self.info1 = messagebox.showerror('No Fit Function Specified!', 'Select or write a fit function')

        else:
            self.L4 = self.fitFunction(L).copy()
            plt.plot(self.L4, 'r--d')
            self.txt = self.fitFunc.get() + ' Function of Generated data'
            self.info1 = messagebox.showinfo(self.txt, self.listToString4Real(self.L4))
            print('Esto es L en function')
            print(self.L)
            print('Esto es L1 en function')
            print(self.L1)
            print('Esto es L2 en function')
            print(self.L2)
            self.L2.clear()
            print('Esto es L3 en function')
            print(self.L3)
            self.L3.clear()
            print('Esto es L4 en function')
            print(self.L4)
            self.selecOp(self.L4, n)

    def newGen(self, L, n):
        valInt = 0
        if n > 0:
            L1 = []

            for i in L:
                valInt = int(i, 2)
                L1.append(valInt)
            
            plt.plot(L1, 'b--o')
            self.function(L1, n)
        else:
            self.info1 = messagebox.showinfo('End of Genetic Algorithm')

    #This function permits that the program knows what kind of data will be use to work
    def dataSelec(self):
        if self.dataType.get()==1:
            self.L3 = self.binData(self.ran.get(), self.q.get()).copy()
            plt.plot(self.L3, 'b--o')
            print('Esto es L en dataSelec')
            print(self.L)
            self.L.clear()
            print('Esto es L1 en dataSelec')
            print(self.L1)
            print('Esto es L2 en dataSelec')
            print(self.L2)
            self.L2.clear()
            self.function(self.L3, int(self.generations.get()))

        elif self.dataType.get()==2:
            self.L3 = self.grayData(self.ran.get(), self.q.get()).copy()
            plt.plot(self.L3, 'b--o')
            print('Esto es L en dataSelec')
            print(self.L)
            print('Esto es L1 en dataSelec')
            print(self.L1)
            self.L1.clear()
            print('Esto es L2 en dataSelec')
            print(self.L2)
            self.L2.clear()
            self.function(self.L3, int(self.generations.get()))

        else:
            self.info1 = messagebox.showerror('No Data Type Selected!', 'Select a Data Type')

    def reset(self):
        self.txt = ''
        self.L = []
        self.L1 = []
        self.L2 = []
        self.L3 = []
        self.L4 = []
        self.L5 = []
        self.dataType.set(None)
        self.fitFun.set(0)
        self.selecType.set(None)
        self.matingType.set(None)
        self.mutType.set(None)

    #GUI function to generate a new window for users
    def __init__(self):
        #GUI Specs
        self.root = Tk()
        self.root.title('Genetic Algorithm Implementation')
        self.root.iconbitmap('C:/Users/Oscar/OneDrive/Documentos/ESCOM/GENETIC_ALGORITHMS/SimpleAG/pythonIcon.ico')
        self.frame = Frame()
        self.frame.pack()
        self.frame.config(bd=20)

        #Range between 0 and user entry data
        self.lblRange = Label(self.frame, text = 'Insert the limit range of random numbers!')
        self.lblRange.grid(row=0, column=0, sticky='N')
        self.ran = Entry(self.frame)
        self.ran.grid(row=1, column=0, sticky='N')

        #Quantity of random data
        self.lblQuantity = Label(self.frame, text = 'Insert how many random numbers you want!')
        self.lblQuantity.grid(row=2, column=0, sticky='N')
        self.q = Entry(self.frame)
        self.q.grid(row=3, column=0, sticky='N')

        #Quantity of random data
        self.lblQuantity = Label(self.frame, text = 'Insert how many generations you want!')
        self.lblQuantity.grid(row=4, column=0, sticky='N')
        self.generations = Entry(self.frame)
        self.generations.grid(row=5, column=0, sticky='N')

        #Data type
        self.lblDataType = Label(self.frame, text="Select data type you want to show!")
        self.lblDataType.grid(row=6, column=0, sticky='N')
        self.dataType = IntVar()
        self.binButton = Radiobutton(self.frame, text='Binary', variable = self.dataType, value = 1)
        self.binButton.grid(row=7, column=0, sticky='W')
        self.grayButton = Radiobutton(self.frame, text='Gray Code', variable = self.dataType, value = 2)
        self.grayButton.grid(row=8, column=0, sticky='W')

        #Fit Function
        self.lblFunction = Label(self.frame, text='Select defined fitness function below...')
        self.lblFunction.grid(row=0, column=1, sticky='N')
        self.fitFun = IntVar()
        self.sinButton = Radiobutton(self.frame, text='sin(x)', variable = self.fitFun, value = 1)
        self.sinButton.grid(row=1, column=1, sticky='N')
        self.sin2Button = Radiobutton(self.frame, text='sin^2(x)', variable = self.fitFun, value = 2)
        self.sin2Button.grid(row=2, column=1, sticky='N')
        self.cosButton = Radiobutton(self.frame, text='cos(x)', variable = self.fitFun, value = 3)
        self.cosButton.grid(row=3, column=1, sticky='N')
        self.cos2Button = Radiobutton(self.frame, text='cos^2(x)', variable = self.fitFun, value = 4)
        self.cos2Button.grid(row=4, column=1, sticky='N')
        self.lblFunction2 = Label(self.frame, text='Or you can introduce your own function in Python syntax     ')
        self.lblFunction2.grid(row=5, column=1, sticky='N')
        self.fitFunc = Entry(self.frame)
        self.fitFunc.grid(row=6, column=1, sticky='N')
        self.lblFunction2 = Label(self.frame, text='Warning! Roulette Selection is inestable if your fitness function \ngenerates negative numbers or zeros')
        self.lblFunction2.grid(row=8, column=1, sticky='N')

        #Selection Operators
        self.lblSelec = Label(self.frame, text = 'Select the selection method that you want to use')
        self.lblSelec.grid(row=0, column=2, sticky='N')
        self.selecType = IntVar()
        self.roulButton = Radiobutton(self.frame, text='Roulette Wheel Selection', variable = self.selecType, value = 1)
        self.roulButton.grid(row=1, column=2, sticky='W')
        self.stocButton = Radiobutton(self.frame, text='Tournament Selection', variable = self.selecType, value = 2)
        self.stocButton.grid(row=1, column=2, sticky='E')
        self.otherButton = Radiobutton(self.frame, text='Probabilistic Tournament', variable = self.selecType, value = 3)
        self.otherButton.grid(row=2, column=2, sticky='W')

        #Mating Operators
        self.lblPair = Label(self.frame, text = 'Select the Mating method that you want to use')
        self.lblPair.grid(row=3, column=2, sticky='N')
        self.matingType = IntVar()
        self.pointButton = Radiobutton(self.frame, text='1 Point', variable = self.matingType, value = 1)
        self.pointButton.grid(row=4, column=2, sticky='W')
        self.npointsButton = Radiobutton(self.frame, text='2 Points', variable = self.matingType, value = 2)
        self.npointsButton.grid(row=4, column=2, sticky='E')
        self.uniformButton = Radiobutton(self.frame, text='Uniform', variable = self.matingType, value = 3)
        self.uniformButton.grid(row=5, column=2, sticky='W')

        #Mutation Operators
        self.lblMutation = Label(self.frame, text = 'Select the mutation method that you want to use')
        self.lblMutation.grid(row=6, column=2, sticky='N')
        self.mutType = IntVar()
        self.insertButton = Radiobutton(self.frame, text='Insertion', variable = self.mutType, value = 1)
        self.insertButton.grid(row=7, column=2, sticky='W')
        self.dispButton = Radiobutton(self.frame, text='Displacement', variable = self.mutType, value = 2)
        self.dispButton.grid(row=7, column=2, sticky='E')
        self.exchangeButton = Radiobutton(self.frame, text='Reciprocal Exchange', variable = self.mutType, value = 3)
        self.exchangeButton.grid(row=8, column=2, sticky='W')

        #Start and Finish of Program
        self.b1 = Button(self.frame, text = 'Go!', command = lambda: self.dataSelec())
        self.b1.grid(row=10, column=2, pady=5)
        self.b2 = Button(self.frame, text = 'Exit', command = self.root.destroy)
        self.b2.grid(row=10, column=2, pady=5, sticky='E')
        self.b3 = Button(self.frame, text = 'Reset', command = lambda: self.reset())
        self.b3.grid(row=10, column=0, pady=5, sticky='N')

        #Miscellaneous data
        self.txt = ''
        self.L = []
        self.L1 = []
        self.L2 = []
        self.L3 = []
        self.L4 = []
        self.L5 = []

        #Linecode to keep open the window while program is executing
        self.root.mainloop()

#New instance of a GUI() function to start the execution of program
gui = GUI()