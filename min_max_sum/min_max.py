def miniMaxSum(arr):

    min_val = min(arr)
    max_val = max(arr)
    soma_all = sum(arr)
    
    min_sum = soma_all - max_val
    max_sum = soma_all - min_val

    print(min_sum, max_sum)
