def mergesort(input, min, max):
    mid= 0
    if( min < max):
        mid = (int)((max + min) / 2)
        mergesort(input, min, mid)
        mergesort(input, min+1, max)
        final = merge(input,min, max, mid)

    #for i in final:
     #   print(i)


def merge(arr, mn, mx, md):
    b = [None] * len(arr)
    for i in range(mn, mx):
        if(mn+1 == mx):
            if(arr[mn]>arr[mx]):
                b[mn] = arr[mx]
                b[mx] = arr[mn]
            else:
                b[mn] = arr[mn]
                b[mx] = arr[mx]
        else:
            if(mn != i):
                if(arr[mn] > arr[i]):
                    b[mn] = arr[i]
                    b[i] = arr[mn]
                else:
                    b[mn] = arr[mn]
                    b[i] = arr[i]
    if(len(b) > 0):
        for j in range(0,len(b)):
            if(b[j] is not None):
                arr[j] = b[j]
    return b

input= [32, 45, 67, 2, 7]
min = 0
max = len(input) - 1

mergesort(input, min , max)
