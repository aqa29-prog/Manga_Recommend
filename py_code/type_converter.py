# convert 'str' to 'int' (two-dimensional array)
def Converter_StrToInt_2dim(string):
    integral = [[0 for j in range(len(string[0]))] for i in range(len(string))]
    for line in range(len(string)):
        for column in range(len(string[0])):
            if type(string[line][column]) == str:
                integral[line][column] = int(string[line][column])

    return integral
