def is_palindrome(n):
    s = str(n)
    a = len(s)
    for i in range(0,a//2):
        if s[i] != s[a-i-1]:
            return False
    return True


if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

