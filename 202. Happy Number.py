class Solution:
    def isHappy(self, n: int) -> bool:
        hash_ = set({n})
        while n != 1:
            sum_num = 0
            for i in str(n):
                sum_num += int(i)**2
            
            if sum_num in hash_:
                break
            hash_.add(sum_num)
            n = sum_num
        
        return n == 1