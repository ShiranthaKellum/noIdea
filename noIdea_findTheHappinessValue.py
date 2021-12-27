
def happiness (A, B, arr):
    happy = 0
    for i in arr:
        if i in A:
            happy += 1

        elif i in B:
            happy -= 1

    # print (happy)
    return happy

size_arr , sizeB = list (map (int, input ().split ()))
arr = list (map (int, input ().split ()))
A = set (map (int, input ().split ()))
B = set (map (int, input ().split ()))

print (happiness (A, B, arr))