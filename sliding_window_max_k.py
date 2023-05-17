# https://www.geeksforgeeks.org/window-sliding-technique/
# naive approach
def find_max_sum(array, k):
    max_sum = 0
    for i in range(len(array)-k+1):
        summation = 0
        for j in range(k):
            summation += array[i+j]

        if max_sum < summation:
            max_sum = summation

    return max_sum

def find_max_sum2(array, k):
    if k >= len(array):
        return sum(array)
    
    summation = sum(array[0:k])
    max_summation = summation
    for i in range(k, len(array)):
        summation += array[i] - array[i-k]
        max_summation = max(max_summation, summation)

    return max_summation

print(find_max_sum([1, 4, 2, 10, 23, 3, 1, 0, 20], 4))
print(find_max_sum2([1, 4, 2, 10, 23, 3, 1, 0, 20], 4))
print(find_max_sum([100, 200, 300, 400],2))
print(find_max_sum2([100, 200, 300, 400],2))