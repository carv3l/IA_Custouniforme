MN = NM = 6
NK = KN = IF = FI = KG = GK = 4
JG = GJ = CD = DC = DE = ED = CB = BC = 3
ML = LM = AI = IA = AH = HA = AB = BA = FE = EF = 2
LA = AL = AK = KA = IG = JK = 1

a = [["MN", "NM", "NK", "KN", "IF", "FI", "KG", "GK", "JG", "GJ", "CD", "DC", "DE", "ED", "CB", "BC", "ML", "LM", "AI", "IA", "AH", "HA", "AB", "BA",
      "FE", "EF", "LA", "AL", "AK", "KA", "IG", "GI", "JK"], [6, 6, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1]]

b = []
c = []

# print(a[0][0],a[1][0])
mystring_value_soma=0
Final = ""
boolean = 0
Keyword ="FOUND"

def sortlist(listarray):
    listarray.sort(key=lambda x: x[1])
    print(listarray)
    return listarray


def iteration(Initial,value):
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

def tupple(operation,listarray):
    if operation == 1:
        mystring = listarray[0][0]
        if mystring[1] == Final:
            mystring = "FOUND"
            return mystring
        #mystring_value = a[1][j]I

        return mystring[1]
    if operation == 2:
        print("Array",len(listarray))
        for j in range(len(listarray)):
                mystring = listarray[j][0]
                if str(mystring).isalpha():
                    value = listarray[j][1]
                    c.append([mystring[1], value])
                    # .insert(mystring_value)
                print("C:",c)
    


# key=lambda x: x[1]


Initial = input("Enter First Letter:")
print("Username is: " + Final)
Final = input("Enter Letter to Find:")
print("Final is: " + Final)
while boolean != 1:
    iteration(Initial,mystring_value_soma)
# print("Username is: " + Initial)
    array_sorted = sortlist(b)
    Initial = tupple(1,array_sorted)
    tupple(2,array_sorted)
    mystring_value_soma = remove(array_sorted)
    if Initial == "FOUND":
        boolean = 1


##sortlist(b)



#print(array_sorted)


# print(b)


# print("Username is: " + username)


k = input("Press key to exit")
