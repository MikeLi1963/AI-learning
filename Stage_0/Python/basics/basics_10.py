###   嵌套循环

###   任务 1：打印九九乘法表
# n = 9
# print(type(n))
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f'{j} * {i} = {i * j}',end=' ')
#     print()

# ### 好看版本：
# n = 9
# print(type(n))
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f'{j} * {i} = {i * j : 2}',end='  ')
#     print()
# ##  {i*j:2} 表示乘积占 2 个字符宽度，右对齐，看起来更整齐。

###  任务 2：打印直角三角形

# n = int(input())
# for i in range(1,n + 1):
#     for j in range(1, i + 1):
#         print('*', end='')
#     print()




# ###  这里补充for循环中的一些用法
# ##  Python 的 for 循环本身不规定顺序，顺序由你遍历的可迭代对象决定，所以逆序输入有很多种写法。

# 1. range() 用负数步长（最常用）
# for i in range(9, 0, -1):
#     print(i)
# # 输出 9 8 7 6 5 4 3 2 1
# #  range(start, stop, step)： start=9 从 9 开始    stop=0 到 0 之前停（不包含 0）    step=-1 每次减 1

# 2. reversed() 反转序列
# for i in reversed(range(1, 10)):
#     print(i)
# # 9 8 7 ... 1
# 对列表、字符串、元组也能用：
# for ch in reversed("abc"):
#     print(ch)      # c b a

# 3. sorted(..., reverse=True)
# for x in sorted([3, 1, 2], reverse=True):
#     print(x)       # 3 2 1



# 4. 逆序打印 99 乘法表
# 把上文的循环改成从 9 到 1：
# for i in range(9, 0, -1):
#     for j in range(1, i + 1):
#         print(f"{j}×{i}={i*j:2}", end="  ")
#     print()

# range(9, 0, -1) 是从 9 到 1；如果写成 range(1, 10, -1) 会得到空序列，因为起点 1 加上负步长永远到不了 10。
# range() 的 stop 永远不包含，所以逆序到 1 要写 0 作为 stop。


###  任务 3（进阶挑战）：倒直角三角形


# n = int(input())
# for i in range(n , 0, -1):
#     print('*' * i)



### 变式扩展（第 2 步）
### 变式 1：打印金字塔（等边三角形）

# n = int(input())
# for i in range(1, n + 1):
#     print(' ' * (n - i) + '*' * (2 * i - 1))

###  变式 2：FizzBuzz 嵌套版（可选）

# n = int(input())
# for i in range(0, n):
#     for j in range(0, n):
#         if i * j / 2 == 0:
#             print('#',end = '')
#         else:
#             print('*',end = '')
#     print()

###   问题 1：除号 / 和取模 % 用反了。
###   你写的是 / 2 == 0（除以 2 等于 0）。除了 0/2 等于 0 之外，2/2=1、4/2=2，所以程序只在 i=0, j=0 的时候打印了一个 #，其他全打印了 *。判断奇偶数，应该用取模运算符 %（即 i * j % 2 == 0）。



###   问题 2：起点漏了 1。
###   题目要求 1 到 5 行、1 到 5 列，但你写的是 range(0, n)，也就是 0 到 4。乘积为 0 也是偶数，会导致第一行第一列逻辑出错。应该写 range(1, n + 1)。




n = int(input())
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i * j % 2 == 0:
            print('#',end = '')
        else:
            print('*',end = '')
    print()