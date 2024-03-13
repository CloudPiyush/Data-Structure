Start = int(input('\nEnter the Starting Number :-->'))
End   = int(input('\nEnter the Ending   Number :-->'))

for i in range(Start,End):
    if (i > 1):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            print(i)