def ekualisasi(arr):
    sumV = 0
    for i in range(len(arr)):
        sumV += arr[i]
        arr[i] = round(sumV * (len(arr)-1))
    return arr

arr = [1.2, 2.6, 3.8, 4.4, 5.8, 6.9, 7.4, 8.2, 9.6]
a = sum(arr[0:1])
print(a)
print(ekualisasi(arr))
