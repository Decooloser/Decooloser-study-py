'''
关于处理数字问题的一个递归函数：就是给定一个数，求得每个位上数字的和
'''

#第一个递归函数，就是正常逻辑我们平常处理这个问题的方法,感觉这个不是递归，是循环，递归应该是n和 n-1或者其他与n相关的项
def digui1(n):
    if n < 10:
        return n
    else:
        s = n % 10
        return s + digui1(n//10)
#第二个递归方法，这是正宗的递归，跟数学一样
def digui2(n):
    if n < 10:
        return n
    #这部分不能少，因为这是递归中的终止条件
    elif n == 10:
        return 1
    else:
        return 1 + digui2(digui2(n-1))# 1=digui2(10)

print(digui1(123))
print(digui2(123))
