heros=['灭霸','钢铁侠','雷神','钢铁侠','绿巨人']
# heros[1]='黑寡妇'
# print(heros)
# heros[1:3]=['武松','林冲']
# print(heros)

nums=[2,3,6,2,3,5,9,6]
nums.sort()
print(nums)
nums.reverse()
print(nums)
nums=[2,3,6,2,3,5,9,6]
nums.sort(reverse=True)
print(nums)
a=nums.count(3)
print(a)
b=heros.index('雷神')
print(b)
heros[heros.index('绿巨人')]='神奇女侠'
print(heros)
nums=[2,3,6,2,3,5,9,6]
print(nums.index(3))
c=nums.index(3,2,5)
print(c)
nums_copy1=nums.copy()
nums_copy2=nums[1:4]
print(nums_copy1)
print(nums_copy2)