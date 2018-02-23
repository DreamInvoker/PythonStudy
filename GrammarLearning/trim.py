# -*- coding: utf-8 -*-
def trim2(s):
    left = 0
    right = 0
    for c in s:
        if c == ' ':
            left += 1
        else:
            break
    for i in range(len(s) - 1, left, -1):
        if s[i] == ' ':
            right -= 1
        else:
            break
    res = ''
    if right == 0:
        res = s[left:]
    else:
        res = s[left:right]
    return res


def trim(s):
    if s=='':
        return ''
    elif s[0:1] ==' ' :
        return trim(s[1:])
    elif s[-1] == ' ' :
        return trim(s[0:-1])
    else:
        return s


# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
