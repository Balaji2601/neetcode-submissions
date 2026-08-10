class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        def counter_dict(l, d):
            for val in nums:
                if val in d:
                    d[val] += 1
                    continue
                d[val] = 1
            return d
    
        input_dict = defaultdict(int)
        output_dict = counter_dict(nums, input_dict)

        arr = []
        for num, freq in output_dict.items():
            arr.append([freq, num])
        arr = sorted(arr)[::-1]
        ans = []
        for i in range(k):
            ans.append(arr[i][1])
        return ans
