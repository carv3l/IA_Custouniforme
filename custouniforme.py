import os
import re
import csv
import numpy as np



try:
    os.remove("your_file.txt")
    os.remove("tree_file.txt")
except:
    print("NO FILE FOUND, NO PROBLEM")

###DECLARAÇÃO DE VARIAVEIS####

MN = NM = 6
NK = KN = IF = FI = KG = GK = 4
JG = GJ = CD = DC = DE = ED = CB = BC = 3
ML = LM = AI = IA = AH = HA = AB = BA = FE = EF = FH = HF  = 2
LA = AL = AK = KA = IG = GI = JK = KJ = 1

a = [["MN", "NM", "NK", "KN", "IF", "FI", "KG", "GK", "JG", "GJ", "CD", "DC", "DE", "ED", "CB", "BC", "ML", "LM", "AI", "IA", "AH", "HA", "AB", "BA",
      "FE", "EF","FH","HF", "LA", "AL", "AK", "KA", "IG", "GI", "JK","KJ"], [6, 6, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 2,2,2,2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1,1]]

b = []
c = []
d = []

var_possiblepaths = 0

# print(a[0][0],a[1][0])
mystring_value_soma = 0
Final = ""
boolean = 0
contador = 0


###########################        FUNÇÕES              ############################################


def sortlist(listarray):
    listarray.sort(key=lambda x: x[1]) #1 é os valores, 0 é as letras
    
    #print("This is Sorted", listarray)
    return listarray

def possiblepaths(array,Final):
    soma = 0
    for j in range(len(array[0])):
        if Final in array[0][j]:
        #    print("Value",array[0][j])
            soma+=1
    soma=int(soma/2)
    print("Caminhos possiveis:", soma)
    return soma

def iteration(Initial, value):
    for j in range(len(a[0])):
        if Initial in a[0][j]:
            mystring = a[0][j]
            mystring_value = a[1][j]
            if mystring[0] == Initial:
                # print(mystring)
                b.append([mystring, mystring_value+value])
                # .insert(mystring_value)


def remove(listarray):
    mystring_value_soma = listarray[0][1]
    del listarray[0]
    return int(mystring_value_soma)


def generatetofile(c_list, contador):
    with open('your_file.txt', 'a') as f:
        f.write(str(contador))
        f.write(" | ")
        for item in c_list:
            f.write("%s" % item)
        f.write("\n")

def savetreefile(c_list):         
    with open('tree_file.txt', 'a') as f:
        for item in c_list:
            f.write("%s" % item)
        f.write("\n")

def escrevercusto(sequencia, custo):
 with open('your_file.txt', 'a') as f:
        f.write("\n")
        f.write("SOLUCAO \n")
        f.write("%s" % sequencia)
        f.write("\n")
        f.write("CUSTO \n")
        f.write(str(custo))

def tupple(operation, listarray):
    if operation == 1:
        mystring = listarray[0][0]
        if mystring[1] == Final:
            mystring = "FOUND"
            return mystring
        return mystring[1]
    
    if operation == 2:
        c = []
        for j in range(len(listarray)):  # Array Size
            mystring = listarray[j][0]
            value = listarray[j][1]
            c.append([mystring[1], value])
        savetreefile(c)
        generatetofile(c, contador)

 
def Scalate(order):
    with open('your_file.txt', 'r') as searchfile:

     # Clear variable names
        partname = None

        # Search file for strings, trim lines and save as variables
        for line in searchfile:

            if order in line and partname is None:
                x = line
                partname = x[0:-1]
  #  print("LINE IS:", partname)


def Scalated(order):
    index_list = []
    line_list = []
    with open('your_file.txt') as f:
        partname = None
        for index, line in enumerate(f):
            line_list.append(line)
            if order in line and partname is None:
                index_list.append(index)
                x = line
                partname = x[0:-1]
   # print(line_list)
    for index in index_list:
       # print("LINES:", line_list[index-1], line_list[index])
        letter = line_list[index-1]
        number = letter[0:3]
        letter = letter[0:14]

        cost = line_list[index]
        cost = cost.split(',')
    #    print("Custo",cost)
      #  print(re.findall(r'\d+',number)) #Find previous letter before the final
        letter = re.findall('[a-zA-Z]', letter)
        number = re.findall(r'\d+',number)
   ##     print(letter[0])
 ##       print(number[0])
    if int(number[0]) == 0:
        letter.append(0)
        return letter
    else:
        return letter    

# key=lambda x: x[1]

#########################################             START OF CODE           ######################################

Initial = input("Enter First Letter:")
print("Initial is: " + Initial)
Final = input("Enter Letter to Find:")
print("Final is: " + Final)

#Determinar os Caminhos possiveis até à letra final
var_possiblepaths = possiblepaths(a,Final)


c = [[Initial, 0]]
generatetofile(c, contador)

while boolean != 1:
    contador += 1
    iteration(Initial, mystring_value_soma)
    array_sorted = sortlist(b)
   # print(array_sorted)
    tupple(2, array_sorted)
    Initial= tupple(1, array_sorted)
    mystring_value_soma = remove(array_sorted)
    if Initial == "FOUND":
        boolean = 1
d.append(Final)

while boolean != 0:
    bsearch = Scalated(Final)
    Final = bsearch[0]
    d.insert(0,Final)
    if len(bsearch) > 1:
        boolean = 0

print("SOLUCAO: ",d)
print("CUSTO: ",mystring_value_soma)

escrevercusto(d,mystring_value_soma)

k = input("Press key to exit")
