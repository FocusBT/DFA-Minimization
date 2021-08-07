import pprint

partion = 3


def swap (list, i, n, Blist):
    while i + 1 != n:
        list[i][0] = list[i + 1][0]
        list[i][1] = list[i + 1][1]
        list[i][2] = list[i + 1][2]
        Blist[i][0] = Blist[i + 1][0]
        Blist[i][1] = Blist[i + 1][1]
        Blist[i][2] = Blist[i + 1][2]
        i = i + 1

n = int (input ("Enter Number of total states : "))
F = int (input ("Enter number if final states :"))
Nstates = [[0 for i in range (n)] for j in range (n)]
BNstates = [[0 for i in range (n)] for j in range (n)]

print ("Non-final States ")
for i in range (0, n):
    print("For State Q{0}: ".format(i))
    if i == n - F:
        print ("Final States")

    if i < n - F:
        BNstates[i][0] = 1
        Nstates[i][1] = int (input ("for a : "))
        Nstates[i][2] = int (input ("for b : "))
    if i >= n - F:
        BNstates[i][0] = 2
        Nstates[i][1] = int (input ("for a : "))
        Nstates[i][2] = int (input ("for b : "))
    Nstates[i][0] = i


for i in range (0, n):
    if Nstates[i][1] >= n - F:
        BNstates[i][1] = 2
    else:
        BNstates[i][1] = 1

    if Nstates[i][2] >= n - F:
        BNstates[i][2] = 2
    else:
        BNstates[i][2] = 1

print ("states\t\ta\t\t\tb\t")
for i in range (0, n):
    print ("q{0}({1})\t\t{2}({3})\t\t{4}({5})\t".format (Nstates[i][0], BNstates[i][0], Nstates[i][1], BNstates[i][1],
                                                         Nstates[i][2], BNstates[i][2]))

counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0
save = 0
save1 = 0

temp = [[0 for i in range (n)] for j in range (n)]
temp1 = [[0 for i in range (n)] for j in range (n)]

Btemp = [[0 for i in range (n)] for j in range (n)]
Btemp1 = [[0 for i in range (n)] for j in range (n)]
saveL = [0 for i in range (10)]
i = 0
checking = 0


while i < n:
    if i + 1 == n:
        break
    if ((BNstates[i][0] != BNstates[i + 1][0])):
        print (" ")
    elif ((BNstates[i][1] == BNstates[i + 1][1]) and (BNstates[i][2] == BNstates[i + 1][2])):
        counter1 = counter1 + 1
    else:
        save = i
        ko = i
        a = 0
        b = 0
        while (BNstates[i][0] == BNstates[i + 1][0]):
            if ((BNstates[save][1] == BNstates[i + 1][1]) and (BNstates[save][2] == BNstates[i + 1][2])):
                counter2 = counter2 + 1
                temp[a][0] = Nstates[i + 1][0]
                temp[a][1] = Nstates[i + 1][1]
                temp[a][2] = Nstates[i + 1][2]
                Btemp[a][0] = BNstates[i + 1][0]
                Btemp[a][1] = BNstates[i + 1][1]
                Btemp[a][2] = BNstates[i + 1][2]
                a = a + 1
            else:
                counter3 = counter3 + 1
                temp1[b][0] = Nstates[i + 1][0]
                temp1[b][1] = Nstates[i + 1][1]
                temp1[b][2] = Nstates[i + 1][2]
                Btemp1[b][0] = BNstates[i + 1][0]
                Btemp1[b][1] = BNstates[i + 1][1]
                Btemp1[b][2] = BNstates[i + 1][2]
                b = b + 1

            i = i + 1
            if i + 1 == n:
                break
        i = ko

        i = i + 1

        a = 0
        b = 0

        if counter3 > counter2:
            while i < n:
                if counter3 == 0:
                    break
                if Nstates[i][0] == temp1[a][0]:
                    swap (Nstates, i, n, BNstates)
                    Nstates[n - 1][0] = temp1[a][0]
                    Nstates[n - 1][1] = temp1[a][1]
                    Nstates[n - 1][2] = temp1[a][2]

                    save1 = temp1[a][0]

                    BNstates[n - 1][0] = partion
                    BNstates[n - 1][1] = Btemp1[a][1]
                    BNstates[n - 1][2] = Btemp1[a][2]

                    for i in range (0, n):
                        for j in range (1, 3):
                            if Nstates[i][j] == save1:
                                BNstates[i][j] = partion
                    a = a + 1
                    counter3 = counter3 - 1
                    i = 0
                i = i + 1
            i = -1
            counter2 = 0
            counter3 = 0
            coutner4 = 0
            counter1 = 0
            partion = partion + 1
        if counter3 < counter2:
            for i in range (0, n):
                if counter3 == 0:
                    break
                if Nstates[i][0] == temp1[a][0]:
                    swap (Nstates, i, n, BNstates)
                    Nstates[n - 1][0] = temp1[a][0]
                    Nstates[n - 1][1] = temp1[a][1]
                    Nstates[n - 1][2] = temp1[a][2]

                    save1 = temp1[a][0]

                    BNstates[n - 1][0] = partion
                    BNstates[n - 1][1] = Btemp1[a][1]
                    BNstates[n - 1][2] = Btemp1[a][2]

                    for i in range (0, n):
                        for j in range (1, 3):
                            if Nstates[i][j] == save1:
                                BNstates[i][j] = partion
                    a = a + 1
                    counter3 = counter3 - 1
            i = -1
            counter2 = 0
            counter3 = 0
            coutner4 = 0
            counter1 = 0
            partion = partion + 1
    i = i + 1
# printing output
print ("-------------------Minimized DFA--------------------")
print ("States\t\ta\t\t\tb\t")
for i in range (0, n):
    if Nstates[i][0] >= n - F:
        print (
            "*q{0}({1})\t\t{2}({3})\t\t{4}({5})\t".format (Nstates[i][0], BNstates[i][0], Nstates[i][1], BNstates[i][1],
                                                           Nstates[i][2], BNstates[i][2]))
    else:
        print (
            "q{0}({1})\t\t{2}({3})\t\t{4}({5})\t".format (Nstates[i][0], BNstates[i][0], Nstates[i][1], BNstates[i][1],
                                                          Nstates[i][2], BNstates[i][2]))
i = 0
print ("\n\n-------------------Partions--------------------------")
print ("Partion a\tb")
while i < n:
    if i + 1 == n:
        print ("{0}\t\t{1}\t{2}".format (BNstates[i][0], BNstates[i][1], BNstates[i][2]))
        break
    if BNstates[i][0] == BNstates[i + 1][0]:
        while (BNstates[i][0] == BNstates[i + 1][0]):
            i = i + 1
            if i + 1 == n:
                print ("{0}\t\t{1}\t{2}".format (BNstates[i][0], BNstates[i][1], BNstates[i][2]))
                break
    print ("{0}\t\t{1}\t{2}".format (BNstates[i][0], BNstates[i][1], BNstates[i][2]))
    i = i + 1
