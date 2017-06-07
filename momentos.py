
X = [1,1,2,1,3,4,2,1,3,2]
Y = [4,2,2,2,1,2,1,2,4,3,3,3,1,3,3,4,3,3,1,4,5,5,2,1,5,1,4,2,5,3,2,5,3,1,5,3,2,3,2,4,3,3,2,3,1,3,1,3,5,2,1,1,5,5,5,2,5,2,1,4,5,3,3,1,1,3,2,1,4,1,4,3,3,3,5,4,1,5,4,1,2,2, 4,1,3,1,2,3,1,3,4,2,3,5,4,1,3,1,3,4]
Z = [11, 4, 2, 6, 10, 8, 2, 3, 1, 4, 5, 3, 4, 6, 2, 3, 4, 5, 7, 9, 3, 3, 1, 4, 7, 2, 3, 2, 1, 5, 5, 7, 8, 9, 10, 4, 3, 2, 9, 11,3, 3, 4, 12, 5, 6, 8, 30, 6, 13]

numbers = {}
k_values = []
probabilities = []
m1 = 0
m2 = 0
m3 = 0
m4 = 0
var = 0


def getVar(m1, m2):
    var = m2 - (m1 * m1)
    return var

def check_for_and_add(element, key):
    try:
        numbers[key] += 1
    except:
        numbers[key] = 1

def filtraEntrada( inputList ):
    for element in inputList:
        check_for_and_add(numbers, element)

def findsKValues (dic):
    for value in dic:
        k_values.append(value)
        print value

def findsProbabilities(numbers, original_list):

    for number in numbers:
        probabilities.append(numbers[number] / float(len(original_list)))
        print str(number) +  " - " + str(numbers[number] / float(len(original_list)))


def getM(numberOfMoment, original_list):

    counter = 0

    for number in original_list:
        counter = counter + (number**numberOfMoment)

    return counter / float(len(original_list))



str_arr = raw_input().split(',')
arr = [int(num) for num in str_arr]


original_list = arr

filtraEntrada(original_list)

print "Possible 'K' values: "
findsKValues (numbers)

print '\n' + "Probabilities: "
findsProbabilities (numbers, original_list)

print '\n' + "M1 (Averge): "
m1 = getM(1, original_list)
print m1

print '\n' + "M2: (Dispersion)"
m2 = getM(2, original_list)
print m2

print '\n' + "VAR: "
print getVar(m1, m2)

print '\n' + "M3: (Asymmetry)"
m3 = getM(3, original_list)
print m3

print '\n' + "M4: (Curtosis)"
m4 = getM(4, original_list)
print m4
