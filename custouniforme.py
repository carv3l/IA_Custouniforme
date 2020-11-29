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


def sortlist(listarray):
    listarray.sort(key=lambda x: x[1])
    print(listarray)
    return listarray


def iteration(Initial):
    for j in range(len(a[0])):
        if Initial in a[0][j]:
            mystring = a[0][j]
            mystring_value = a[1][j]
            if mystring[0] == Initial:
                # print(mystring)
                b.append([mystring, mystring_value])
                # .insert(mystring_value)


def tupple(operation,listarray):
    if operation == 1:
        mystring = listarray[0][0]
        #mystring_value = a[1][j]I

        return mystring[1]
    if operation == 2:

        for j in range(len(listarray[0])):
                mystring = listarray[0][j]
                if mystring.isalpha()
                print("Mystring",mystring)
                value = listarray[1][j]
                letter = str(mystring)[1]
                print(letter)
                c.append([letter, value])
                # .insert(mystring_value)
        print(c)
    


# key=lambda x: x[1]


Initial = input("Enter First Letter:")
iteration(Initial)
# print("Username is: " + Initial)

array_sorted = sortlist(b)

Initial = tupple(1,array_sorted)
tupple(2,array_sorted)
iteration(Initial)
sortlist(b)
isal
#print(array_sorted)


# print(b)


# print("Username is: " + username)


k = input("Press key to exit")
