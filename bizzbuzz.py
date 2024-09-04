import math
import sys

class bcolors:
    NORM = '\x1b[0m'
    BIZZ = '\x1b[1;30;46m'
    BIZZBIZZ = '\x1b[1;35;46m'
    BUZZ = '\x1b[1;30;43m'
    BUZZBUZZ = '\x1b[1;35;43m'
    BIZZBUZZ = '\x1b[1;30;41m'

def isPower (n, base):
    if base == 1 and n != 1:
        return False
    if base == 1 and n == 1:
        return True
    if base == 0 and n != 1:
        return False
    power = int (math.log(n, base) + 0.5)
    return base ** power == n

print(bcolors.BIZZ + 'BIZZ' + bcolors.NORM)
print(bcolors.BUZZ + 'BUZZ' + bcolors.NORM)
print(bcolors.BIZZBIZZ + 'BIZZBIZZ' + bcolors.NORM)
print(bcolors.BUZZBUZZ + 'BUZZBUZZ' + bcolors.NORM)
print(bcolors.BIZZBUZZ + 'BIZZBUZZ' + bcolors.NORM)

C = int(sys.argv[1])
N = int(sys.argv[2])

print('Printing the first ' + str(N) + ' bizzbuzz numbers in ' + str(C) + ' columns.')

for i in range(1,N):
    bizzm = 0
    buzzm = 0
    bizzd = 0
    buzzd = 0
    bizzb = 0
    buzzb = 0

    if i%5==0:
        bizzm+=1

    if isPower(i,5) and i>5:
        bizzb+=1
    
    if isPower(i,7) and i>7:
        buzzb+=1

    if i%7==0:
        buzzm+=1

    if '5' in str(i):
        bizzd+=1
    
    if '7' in str(i):
        buzzd+=1


    if bizzd+bizzm>0 and buzzd+buzzm>0: 
        print(bcolors.BIZZBUZZ + f'{i:<3}' + bcolors.NORM, end=' ')
    elif bizzb>0: 
        print(bcolors.BIZZBIZZ + f'{i:<3}' + bcolors.NORM, end=' ')
    elif buzzb>0: 
        print(bcolors.BUZZBUZZ + f'{i:<3}' + bcolors.NORM, end=' ')
    elif bizzd+bizzm>0: 
        print(bcolors.BIZZ + f'{i:<3}' + bcolors.NORM, end=' ')
    elif buzzd+buzzm>0: 
        print(bcolors.BUZZ + f'{i:<3}' + bcolors.NORM, end=' ')
    else: 
        print(f'{i:<3}', end=' ')

    if i%C==0:
        print('')
