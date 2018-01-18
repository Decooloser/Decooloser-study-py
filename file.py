import os.path
import string
from matplotlib import pyplot as plt

'''
文件基本操作，open()函数中有两个参数，一个是文件名(文件路径:如果不存在则新建文件)，另一个是读写方式
读写方式主要有：r-->read,w-->write,rb-->read binary,wb-->write binary
a--->append 在文件末尾追加内容
'''
def main():
    #用os.path判断文件是否存在
    if os.path.isfile('xx.txt'):
        print('exist')
    #在当前目录下新建文件xx.txt，如果要操作系统中其他盘的文件，指明文件所在路径即可
    file = open('xx.txt','w')
    file.write('ASADAD\n')
    file.write('sdasdasd\n')
    file.write('sdasdq33123,a\n')
    file.write('a')
    file.close()

def opfile(filename):
    #定义字典用来统计字符出现的次数
    words = {}
    with open(filename, 'r') as f:
        for line in f:
            for i in line.strip(string.whitespace).split():
                for x in i:
                # 统计文件中对应字符出现的次数
                    words[x] = words.get(x, 0) + 1
    return words
#用pylot画图
def show(content):
    con = []
    for key,value in content.items():
        t = (value,key)
        con.append(t)
    for i in con:
        #将元组数组放入坐标轴
        plt.bar((i[1],),(i[0],))
    plt.legend()
    plt.xlabel('字母')
    plt.ylabel('次数')
    plt.title('统计')
    plt.show()

if __name__ ==('__main__'):
   s = opfile('xx.txt')
   show(s)


