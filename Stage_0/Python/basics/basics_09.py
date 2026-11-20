###  任务 1：密码重试



# nums = 0
# while True:
#     print('请输入密码：')
#     n = input()
#     if nums == 2:
#         break
#     if n == 'abc123':
#         print('登录成功')
#         break
#     else:
#         print('密码错误')
#         nums += 1
# if nums == 2:
#     print('wrong password login forbidden')

# 问题：请你想象这个场景——你前两次都输错了，此时 nums 变成了 2。第三次，你终于输入了正确的密码 'abc123'。
# 根据你的代码，程序先执行 if nums == 2:，发现成立，于是直接 break 跳出循环。程序根本来不及走到 if n == 'abc123': 去判断密码对不对，就直接锁定了！

# 这就导致你的程序只有前两次机会能登录成功。想想看，要把 if nums == 2（或者 if nums == 3）的判断放在哪里，才能既保证次数用完能退出，又不影响本次密码的校验？


### 任务 2：猜数字骨架

# import random
# number = random.randint(1,100)
# count = 0
# print('start guessing the number')
# while True:
#     n = int(input())
#     count += 1
#     if n == number:
#         print('you are right')
#         print(f'This is the {count}th time guessing the number')
#         break
#     elif 0 < n < 100 and n > number:
#         print('Guessed too big')
#     elif 0 < n < 100 and n < number:
#         print('Guessed too small')
#     else:
#         print('Please enter the correct letter-guessing range')

###  问题：0 < n < 100 这个条件，严格排除了 0 和 100。但我们的随机数范围是 1 到 100，如果正确答案恰好是 100，并且用户输入了 100：
###  修改建议：把范围判断改成 1 <= n <= 100，或者干脆把范围判断单独拎出来，这样逻辑更清晰

# if n < 1 or n > 100:
#     print('请输入1-100之间的数字')
#     # 注意：要不要把这种情况也算作一次猜测？（如果不算，要记得减去 count）
#     continue


# random
# 1.需要先导入：
# import random
# 2.a 和 b 都必须是整数，且通常要求 a <= b。如果 a > b，会抛出 ValueError。
# random.randint(100, 1)  # ValueError
# 3.与 random.randrange() 不同：
# random.randint(1, 100)   # 包含 100
# random.randrange(1, 100) # 不包含 100，范围是 1~99
# 4.它是伪随机数，不是真正密码学安全的随机数。如果需要安全随机数，应使用 secrets 模块。
# random.randint(1, 100)
# 总结： 
# random.randint(1, 100)  生成的是 1 到 100 之间的随机整数，包含 1 和 100。


# randrange 支持步长，randint 不支持
# random.randrange(0, 10, 2)
# 从下面这些数中随机选一个：
# 0, 2, 4, 6, 8


# randint(a, b)       -> [a, b]  包含两端
# randrange(a, b)     -> [a, b)  包含左端，不包含右端
# randrange(a, b, s)  -> 按步长 s 取

###  任务 2：猜数字骨架（重写版）

import random
number = random.randint(1,100)

nums = 0
while True:
    n = int(input())
    if 1 <= n <= 100:
        nums += 1
        if n == number:
            print('You guessed it !!!')
            break
        elif n > number:
            print('too big')
        else:
            print('too small')
    else:
        print('Please enter a valid range')
print(f'Guessed a total of {nums} times')


###  任务 3：密码重试    Revision

# nums = 0
# while nums < 3:
#     print('Please enter your password')
#     password = input()

#     if password == 'abc123':
#         print('Login successful')
#         break
#     else:
#         nums += 1
        
# else:
#     print('You\'ve already failed to log in more than 3 times')
    

    
