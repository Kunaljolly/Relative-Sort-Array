class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1 = sorted(arr1)
        t = []
        for x in arr2:
            while(x in arr1):
                t.append(x)
                arr1.remove(x)
        return t + arr1
            

                



