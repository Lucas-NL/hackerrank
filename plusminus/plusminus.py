def plusMinus(arr):
    positives = (sum( x > 0 for x in arr)) / len(arr)
    negatives = (sum( x < 0 for x in arr)) / len(arr)
    zeros = (arr.count(0)) / len(arr)
     
    print("{:.6f} \n{:.6f} \n{:.6f}".format(positives, negatives, zeros))
