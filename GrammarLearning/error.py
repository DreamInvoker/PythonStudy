# 定义函数
def temp_convert(var):
    try:
        return int(var)
    except ValueError as Argument:
        print("参数没有包含数字\n", Argument)


# 调用函数
temp_convert("xyz");
