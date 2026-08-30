class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        sort = nums[::-1]
        mi = min(nums)
        ma = max(nums)
        m_i = nums.index(mi) + 1 
        ma_i = nums.index(ma) + 1 
        m_ri = sort.index(mi)  + 1
        ma_ri = sort.index(ma) + 1 
        front = max(m_i, ma_i)
        back = max(m_ri, ma_ri)
        option1 = m_i + ma_ri
        option2 = m_ri + ma_i
        value = min(option1, option2)
        return min(front, back, value)
