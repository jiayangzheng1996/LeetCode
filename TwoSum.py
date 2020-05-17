from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        cur_idx = None
        tgt_idx = None
        for idx, num in enumerate(nums):
            if dict:
                tgt_idx = dict.get(num)
                if tgt_idx is not None:
                    cur_idx = idx
                    break

            diff = target - num
            dict.update({diff: idx})
        return [tgt_idx, cur_idx]


def main():
    nums = [1, 3, 6, 11, 15, 17]
    target = 9
    solution = Solution()
    print(solution.twoSum(nums=nums, target=target))

if __name__ == '__main__':
    main()