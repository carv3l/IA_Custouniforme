MN = NM = 6
NK = KN = IF = FI = KG = GK = 4
JG = GJ = CD = DC = DE = ED = CB = BC = 3
ML = LM = AI = IA = AH = HA = AB = BA = FE = EF = 2
LA = AL = AK= KA = IG = JK = 1

a = [["MN","NM","NK","KN","IF","FI","KG","GK","JG","GJ","CD","DC","DE","ED","CB","BC","ML","LM","AI","IA","AH","HA","AB","BA","FE","EF","LA","AL","AK","KA","IG","JK"], [6,6,4,4,4,4,4,4,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1]]
b = [[],[]]
c = []

#print(a[0][0],a[1][0])
Initial = input("Enter First Letter:")
print("Username is: " + Initial)

for i in range(len(a)):
    for j in range(len(a[i])):
        if Initial in a[0][j]:
           # print(a[0][j])
            mystring = a[0][j]
            mystring_value = a[1][j]
            if mystring[0] == Initial:
                print(mystring)
                b.insert(mystring)
                #.insert(mystring_value)
    

            


print(b)
        


#print("Username is: " + username)






k=input("Press key to exit") 