"""
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.
"""

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    if n not in range(2, 11):
        print("n must be inclusively between 2 and 10")
        exit()
        
    for i in range(len(arr)):
        if arr[i] not in range(-100, 101):
            print("Arr must contain values that are inclusively between -100 and 100")
            exit()
            
    print(sorted(set(arr))[-2]) # takes the array and turns it into a collection of unique values. Find the second to last value in the array. 
