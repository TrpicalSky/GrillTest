import math
import statistics


files = ["Grill_1.txt","Grill_2.txt","Grill_3.txt","Grill_4.txt","Grill_5.txt"]

grillOne = []
grillTwo = []
grillThree = []
grillFour = []
grillFive = []

def Calculate(grill): 
    maxnum = max(grill)
    minnum = min(grill)
    meannum = sum(grill) / len(grill)
    devationNum = statistics.stdev(grill)
    maxcrit = meannum + (devationNum*2)
    mincrit = meannum - (devationNum*2)
    return f'Min: {minnum}\nMax: {maxnum}\nMean: {meannum}\nStandard Deviation of temps is {devationNum}'


def printData(statment:str,grillnum:int):
    print(f'Grill {grillnum}:\n{statment}')

    


def readValues(file:list[str]):
    global grillOne,grillTwo,grillThree,grillFour,grillFive
    for i in range(len(file)):
        txtFile = file[i]
        with open(txtFile, 'r') as f:
            if (i+1) == 1:
                for line in f:
                    new_line = int(line.strip())
                    grillOne.append(new_line)
                # print(grillOne)
                res = Calculate(grillOne)
                printData(res,1)
            elif (i+1) == 2:
                for line in f:
                    new_line = int(line.strip())
                    grillTwo.append(new_line)
                #print(grillTwo)
                res = Calculate(grillTwo)
                printData(res,2)
            elif (i+1) == 3:
                for line in f:
                    new_line = int(line.strip())
                    grillThree.append(new_line)
                #print(grillThree)
                res = Calculate(grillThree)
                printData(res,3)
            elif (i+1) == 4:
                for line in f:
                    new_line = int(line.strip())
                    grillFour.append(new_line)
                #print(grillFour)
                res = Calculate(grillFour)
                printData(res,4)
            elif (i+1) == 5:
                for line in f:
                    new_line = int(line.strip())
                    grillFive.append(new_line)
                #print(grillFive)
                res = Calculate(grillFive)
                printData(res,5)
        f.close()
        
        

readValues(files)