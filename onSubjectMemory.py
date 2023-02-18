
class Solution():
    def stage1(nums):
        if nums[4] == 1:
            return 1
        elif nums[4] == 2:
            return 1
        elif nums[4] == 3:
            return 2
        elif nums[4] == 4:
            return 3

    def stage3(nums, stage1_response, stage2_response):
        if nums[4] == 1:
            return stage2_response
        elif nums[4] == 2:
            return stage1_response
        elif nums[4] == 3:
            return 2
        elif nums[4] == 4:
            return nums.index(4)
    
    def stage5(nums, stage1_response, stage2_response, stage3_response, stage4_response):
        if nums[4] == 1:
            return stage1_response
        elif nums[4] == 2:
            return stage2_response
        elif nums[4] == 3:
            return stage3_response
        elif nums[4] == 4:
            return stage4_response

    def stage2(nums,stage1_response):
        if nums[4]==1: return nums.index(4)
        elif nums[4]==2: return stage1_response
        elif nums[4]==3: return 1
        elif nums[4]==4: return stage1_response
    
    def stage4(nums, stage1_response,stage2_response,stage3_response):
        if nums[4]==1: return stage1_response
        elif nums[4]==2: return 1
        elif nums[4]==3: return stage2_response
        elif nums[4]==4: return stage2_response

    
    def __init__(self, nums):
        
