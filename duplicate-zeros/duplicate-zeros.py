class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        i=0
        while (i < len(arr)):
            if arr[i] == 0:
                arr.pop(-1)
                arr.insert(i+1,0) 
                i+=1 
            i+=1
