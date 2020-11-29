MN = NM = 6
NK = KN = IF = FI = KG = GK = 4
JG = GJ = CD = DC = DE = ED = CB = BC = 3
ML = LM = AI = IA = AH = HA = AB = BA = FE = EF = 2
LA = AL = AK = KA = IG = JK = 1

a = [["MN", "NM", "NK", "KN", "IF", "FI", "KG", "GK", "JG", "GJ", "CD", "DC", "DE", "ED", "CB", "BC", "ML", "LM", "AI", "IA", "AH", "HA", "AB", "BA",
      "FE", "EF", "LA", "AL", "AK", "KA", "IG", "JK"], [6, 6, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1]]

a = [["LA", "AL", "AK", "KA", "IG", "JK","MN", "NM", "NK", "KN", "IF", "FI", "KG", "GK", "JG", "GJ", "CD", "DC", "DE", "ED", "CB", "BC", "ML", "LM", "AI", "IA", "AH", "HA", "AB", "BA",
      "FE", "EF"], [1, 1, 1, 1, 1, 1, 6, 6, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]]

b = []
c = []

# print(a[0][0],a[1][0])

def sortlist(listarray):
    #for j in range(len(listarray[1])):
     #   if listarray[][j] 

    listarray.sort(key=lambda x: x[1])
    print(listarray)
  

#key=lambda x: x[1]


Initial = input("Enter First Letter:")
print("Username is: " + Initial)

for j in range(len(a[0])):
    if Initial in a[0][j]:
        # print(a[0][j])
        mystring = a[0][j]
        mystring_value = a[1][j]
        if mystring[0] == Initial:
            # print(mystring)
            b.append([mystring, mystring_value])
            # .insert(mystring_value)


sortlist(b)

#print(b)



#print("Username is: " + username)


k = input("Press key to exit")
