
class Solution():
    def stage1(self, nums):
        if nums[-1] == 1:
            return 1
        elif nums[-1] == 2:
            return 1
        elif nums[-1] == 3:
            return 2
        elif nums[-1] == 4:
            return 3
    
    def stage2(self, nums,stage1_response):
        if nums[-1] == 1:
             return nums.index(4)
        elif nums[-1] == 2:
             return stage1_response
        elif nums[-1] == 3:
             return 0
        elif nums[-1] == 4:
             return stage1_response

    def stage3(self, nums, stage1_response, stage2_response):
        if nums[-1] == 1:
            return stage2_response
        elif nums[-1] == 2:
            return stage1_response
        elif nums[-1] == 3:
            return 2
        elif nums[-1] == 4:
            return nums.index(4)
    
       
    def stage4(self, nums, stage1_response,stage2_response, stage3_response):
        if nums[-1] == 1:
            return stage1_response
        elif nums[-1]==2:
            return 0 # this was wrong...
        elif nums[-1]==3:
            return stage2_response
        elif nums[-1] == 4: 
            return stage2_response
    
    def stage5(self, nums, stage1_response, stage2_response, stage3_response, stage4_response):
        if nums[-1] == 1:
            return stage1_response
        elif nums[-1] == 2:
            return stage2_response
        elif nums[-1] == 3:
            return stage3_response
        elif nums[-1] == 4:
            return stage4_response

    
  

    
    def __init__(self, nums):
        
        output = ""

        stage1_response = self.stage1(nums[0])
        output += str(nums[0][stage1_response])

        stage2_response = self.stage2(nums[1], stage1_response)
        output += str(nums[1][stage2_response])

        stage3_response = self.stage3(nums[2], stage1_response, stage2_response)
        output += str(nums[2][stage3_response])

        stage4_response = self.stage4(nums[3], stage1_response, stage2_response, stage3_response)
        output += str(nums[3][stage4_response])

        stage5_response = self.stage5(nums[4], stage1_response, stage2_response, stage3_response, stage4_response)
        output += str(nums[4][stage5_response])

        print(output)

        

if __name__ == "__main__":

    nums =  [[1,3,2,4,1],
                [3,1,2,4,3],
                [2,3,4,1,2],
                [2,1,4,3,1],
                [4,1,2,3,4]]
    s = Solution(nums)