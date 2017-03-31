import math

def my_abs(x):

    # 判断x类型
    if not isinstance(x, (int, float)):
        raise TypeError('Bad operand type. Function need int or float.')
    
    if x >= 0:
        print(x)
    else:
        print(-x)
    return

# Do nothing: pass

def quadratic(a, b, c):
    if not isinstance(a, (int, float)):
        raise TypeError("Type Error !  a")
    if not isinstance(b, (int, float)):
        raise TypeError("Type Error !  b")
    if not isinstance(c, (int, float)):
        raise TypeError("Type Error !  c")

    x1 = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
    x2 = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)

    return x1, x2   # return a tuple


# 默认参数
def my_func(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

# 可变参数, 可以将list或tuple加*传入
def my_func2(*param):
    sum = 0
    for n in param:
        sum += n*n
    return sum

# 关键字参数: 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
#           可以传入不受限制的关键字参数
def my_keyf(name, age, **kw):
    print(name, age, "Other: ", kw)

# 命名关键字参数: 限制关键字参数的名字
# 命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数; 否则定义的将是位置参数
# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def my_namekey(name, age, *, city, job):
    print(name, age, city, job)


# 参数组合:

# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，
# 这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
# def f1(a, b, c=0, *args, **kw):

# 递归
def move(n, froma, dep_b, dst_c):
    if n is 1:
        print(froma, '-->', dst_c);
    else:
        move(n - 1, froma,  dst_c, dep_b)        # 先将初始塔的前n-1个盘子借助目的塔移动到借用塔上
        print(froma, '-->', dst_c);              # 将剩下的一个盘子移动到目的塔上
        move(n - 1, dep_b,  froma, dst_c)        # 最后将借用塔上的n-1个盘子移动到目的塔上



    
