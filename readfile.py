import os
import re
import difflib
import fileinput
import sys

try:
    os.remove("tree.txt")
except:
    print("NO FILE FOUND, NO PROBLEM")


places = []
first_array = []
second_array = []
results = []
resultado = []

def replaceAll(file,searchExp,replaceExp):
    for line in fileinput.input(file, inplace=1):
        if searchExp in line:
            line = line.replace(searchExp,replaceExp)
        sys.stdout.write(line)

def FiletoArray():
   
   with open('tree_file.txt', 'rt') as f:
       for line in f:
           line.rstrip('\'')
            # add item to the list
           # line_list.append(places[i].split("]["))
     
   
   with open('tree_file.txt', 'r') as filehandle:
        for line in filehandle:
            # remove linebreak which is the last character of the string
            currentPlace = line[:-1]
            # add item to the list
            places.append(currentPlace.split("]"))
         

   for i in range(len(places)):
      # print(len(places[i]))
       places[i].pop(len(places[i])-1) # Remove '' from array
       print(places[i])
       #print("Dos",places[i])

       #output_list = [li for li in difflib.ndiff(places[i], places[i+1]) if li[0] != ' ']
       #print(output_list)

def comparer(array):
    for i in range(len(array)):
        st_array = list(array[i])
        first = st_array[0][0]
        print("first",first)
        nd_array = list(array[i+1])
        ##print("ST",st_array)
        ##print("ND",nd_array)
        for k in range(0,len(st_array)):
            try:
                if st_array[k] == st_array[k+1]:
          ##          print("bip bop")
          ##          print("ST",st_array)
                    k+=1
            except IndexError:
                k=k
            for j in range(0,len(nd_array)):
            #    print(st_array[k],"!=",nd_array[j])
                if st_array[k] != nd_array[j]:

                   #extracted = nd_array[j][0]
                  # print("extr",extracted)
                  # extract = first + extracted
                 #  nd_array[j][0] = extract

                   results.append(nd_array[j])

                    #print("result",results)
            nd_array.clear()
            nd_array = list(results)
            #print("nd",nd_array)
            print("final",results)
            resultado = list(results)
            results.clear()
        savetreefile(resultado)
    



def savetreefile(c_list):
    with open('tree.txt', 'a') as f:
        for item in c_list:
            f.write("%s" % item)
        f.write("\n")

replaceAll("tree_file.txt","[","")
replaceAll("tree_file.txt","\'","")
replaceAll("tree_file.txt",", ","")
FiletoArray()
comparer(places)

print(places)

k = input("Press key to exit")

