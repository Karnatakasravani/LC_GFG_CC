class Solution:
    def game_with_number (self, arr,  n) : 
        #Complete the function
        for i in range(0,len(arr)-1):
            if arr[i]|arr[i+1]==arr[i+1]:
        #         print(arr[i],arr[i+1])
                arr[i]=(arr[i+1])
            else:
        #         print(arr[i],arr[i+1])
                arr[i]=(arr[i]|arr[i+1])
        return arr
