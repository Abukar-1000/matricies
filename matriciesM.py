"""
create a user interface to take in the dimensions of two matricies and multiply them 

get the dimensions 
check if the computation can be done 
compute 
save answers in a string format 
display anser in a matricies grid format 

"""
print("First matrix")
first =  input("Dimensions:    ")
print("Second matrix")
second =  input("Dimensions:    ")

firstDimen = first.split("x")
secondDimen = second.split("x")

# convert string to intigers
firstDimen = [int(x) for x in firstDimen]
secondDimen = [int(x) for x in secondDimen]
print(firstDimen,secondDimen)

# get the contents of the matricies 

def getContents(dimensions = []):

    # get entries row by row 
    values = input("enter all values for the matrix:    ")

    # create an list to contain the matrix 
    matrix = [int(x) for x in values.strip()]

    return matrix

def printMatrix(matrix = [],dimensions = []):

    # set the rows and columns
    rows = dimensions[0]
    columns = dimensions[1]

    index = 0
    for x in matrix:
        if (index % rows) == 0:
            print("\n",end="")
        print(f"{x} ",end="")
        index += 1
        
def multiply(matrix1 = [],matrix2 = [],firstDimen = [], secondDimen = []):
    pass
def performOpperation(matrix1 = [],matrix2 = [],opperation = '*'):
    pass
firstMatrix = getContents(firstDimen)
printMatrix(firstMatrix,firstDimen)




