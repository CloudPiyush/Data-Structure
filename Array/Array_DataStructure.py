"""1st Exercise of codebasics"""

# Expence = [2200 , 2350 , 2600 , 2130 , 2190]

# First_Answer = 'In feb I spent Extra {0} Dollers as compare to Januart'.format(Expence[1]-Expence[0])
# print(First_Answer)

# Second_Ans = "The total expense in first quarter (first three months) of the year is {0}".format(Expence[0]+Expence[1]+Expence[2])
# print(Second_Ans)

# print("Did I spent 2000$ in any month? ", 2000 in Expence)

# June = Expence.insert(5 , 1980)
# print(Expence)

# Expence[3] = Expence[3]-200
# print(Expence)

"""2ND Exercise from Code Basics"""

# Marvels = ['spider man','thor','hulk','iron man','captain america']

# print('\nThe Length of list is :{0}.'.format(len(Marvels)))
# Marvels.append('Black Panther')
# print(Marvels)
# Marvels.remove('Black Panther')
# Marvels.insert(3,'Black Panther')
# print(Marvels)
# A = ['DocterStrange']
# Marvels[1:3] = A 
# print(Marvels)
# Marvels.sort()
# print(Marvels)

"""3rd Assignment from code Basics."""

Start = int(input('\nEnter the Starting Number :->'))
End   = int(input('\nEnter the Ending   Number :->'))
lst = []
for i in range(Start,End+1):
    if i % 2 == 0:
        lst.append(i)

print('\nThe Generated Even Number of List between the {0} to {1} are :{2}'.format(Start,End,lst))
print(type(lst))