'''
输入为带()的数学计算表达式，输出()的合法性，不合法为-1 ，合法为()的对数。

(1+2)((((s+1)))))
'''
import re
class Solution(object):
    def isValid(self, s: str) -> bool:
        stack = []
        num = 0
        pattern = '[^()]'
        new_s = re.sub(pattern,'',s)
        if len(new_s) % 2 != 0:
            return 'feioushu'
        for i in range(len(new_s)):
            if not stack and new_s[i] == ')':
                return 'duo)'
            elif new_s[i] == '(':
                stack.append(new_s[i])
            elif stack[-1] == '(' and new_s[i] == ')':
                stack.pop()
                num += 1
            else:
                stack.append(new_s[i])
        print(stack)
        return -1 if stack else num


s = '((()))'

result = Solution()

print(result.isValid(s))