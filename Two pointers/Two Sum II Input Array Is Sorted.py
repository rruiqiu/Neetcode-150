class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #search at 2 steps

        left, right = 0, len(numbers) - 1

        while numbers[left] + numbers[right] != target:
            if numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
        
        return [left + 1, right + 1]