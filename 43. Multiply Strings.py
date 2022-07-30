class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        zero = []
        for i in range(len(num2)):
            z = ""
            for i in range(i):
                z += "0"
            zero.append(z)

        def findMul(e, num):
            res = ''
            c = 0
            for r in num[::-1]:
                r = int(r)
                res = str(((r*e) + c) %10) + res
                c = ((r*e) + c)//10
                
            return str(c) + res if c else res
        
        for i, e in enumerate(num2[::-1]):
            zero[i] = int(findMul(int(e), num1) + zero[i])
        
        return str(sum(zero))