def closest(L, n):
    closest_num = None
    for num in L:
        if num <= n:
            if closest_num is None or num > closest_num:
                closest_num = num
    return closest_num

L = [1, 6, 3, 9, 11]
n = int(input('enter your desired number:'))
result = closest(L, n)
print("The closest number to", n, "that is not larger is:", result)
