def insertionsort(input):
    key= 1
    length = len(input)
    for i in range(1,length):
        j = i
        while(j>0 and input[j-1] > input[j]):
            if(input[j-1] > input[j]):
                key = input[j]
                input[j] = input[j-1]
                input[j-1] = key
                j-=1

    for i in input:
        print(i)

input = [5, 1, 6, 2, 4, 3]
insertionsort(input)