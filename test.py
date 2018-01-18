import random

'''
列表的简单操作
'''

def getMatrix():
    matrix = []
    #eval是将字符转换成整数,另一种判断是unicodedata.numeric()或者isdigit()方法
    row = eval(input('row:'))
    col = eval(input('col:'))
    for i in range(row):
        matrix.append([])
        for j in range(col):
            # value = eval(input('val:'))
            matrix[i].append(random.randint(0, 15))
    return matrix


def getTotal(m):
    val = 0
    for i in m:
        val += sum(i)
    return val

def getSumdui(m):
    s = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if i == j:
                s += m[i][j]
    return s

def getTwoSum(m,n):
    c = []
    if len(m) == len(n):
        for i in range(len(m)):
            c.append([])
            if len(m[i]) == len(n[i]):
                for j in range(len(m[i])):
                    c[i].append([])
                    c[i][j] = m[i][j] + n[i][j]
            else:
                print('不合要求')
    else:
        print('不合要求')
    return c

def getMutple(m,n):
    c = []
    if len(m) == len(n):
        for i in range(len(m)):
            #增加空行
            c.append([])
            if len(m[i]) == len(n[i]):
                for j in range(len(m[i])):
                    c[i].append([])
                    #c[i].append(sum(m[i]) * (sum(n[j])))
                    c[i][j] = sum(m[i])*(sum(n[j]))
            else:
                print('不合要求')
    else:
        print('buheyaoqoi')
    return c


if __name__ ==('__main__'):
    m = getMatrix()
    n = getMatrix()
    print(n)
    print(m)
    print(getTwoSum(m,n))
    print(getMutple(m,n))
    #print(getSumdui(m))
    #print(getTotal(m))
    '''
    matrix = []
    matrix.append([1,2,3])
    matrix.append([4,5])
    matrix.append([6,7,8,9])
    print(matrix)
    
    row = eval(input('row:'))
    col = eval(input('col:'))
    for i in range(row):
        matrix.append([])
        for j in range(col):
            #value = eval(input('val:'))
            matrix[i].append(random.randint(0,15))
    for row in matrix:
        for val in row:
            print(val)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j])
    print(matrix)
    matrix.append(3 * [1])--->matrix[[1,1,1]]
    matrix.append(3 * [1])--->matrix[[1,1,1],[1,1,1]]
    matrix.append(3 * [1])--->matrix[[1,1,1],[1,1,1],[1,1,1]]
    matrix[0] = 3
    #matrix[0][0] = 2
    print(len(matrix))
    #matrix.sort()---->自然顺序排序
    print(matrix)
  
    s = 0
    while True:
        try:
            k = int(input("x:"))
            print(type(k))
            if type(k) == int:
                for i in range(k):
                    s += i
                print(s)
            break
        except:
            print("请输入数字")
            pass

    print("FFFFFFF  U     U  NN    NN")
    print("FF       U     U  NNN   NN")
    print("FFFFF    U     U  NN N  NN")
    print("FF        U   U   NN  N NN")
    print("FF         UUU    NN   NNN")
    '''
