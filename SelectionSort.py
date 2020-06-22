
def selectionsort(input):
    length= len(input)
    for i in range(0,length):
        min= i
        for j in range(i+1, length):
            if(input[min] > input[j]):
                swap = input[min]
                input[min] = input[j]
                input[j] = swap
    for k in input:
        print(k)




#=================================================
input = [3, 6, 1, 8, 4, 5]

selectionsort(input)