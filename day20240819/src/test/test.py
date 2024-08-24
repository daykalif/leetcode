# import tensorflow
# import numpy
# import pandas
# import sklearn
# from sklearn.datasets import load_breast_cancer
# cancer = load_breast_cancer()
# print(cancer)


def f(s):
    if s:
        print('当前传入函数的值s--->', s)
        print('截掉第一个字母后的值s[1:]=============>', s[1:])
        return f(s[1:]) + 1
    else:
        return 3


n = input()
print(f(n))



# n = 'hello world';
# print(f(n))；
#
# f('hello world') = f('ello world') + 1
# f('ello world') = f('llo world') + 1
# f('llo world') = f('lo world') + 1
# f('lo world') = f('o world') + 1
# f('o world') = f(' world') + 1
# f(' world') = f('world') + 1
# f('world') = f('orld') + 1
# f('orld') = f('rld') + 1
# f('rld') = f('ld') + 1
# f('ld') = f('d') + 1
# f('d') = f('') + 1
# f('') = 3
#
# 最终：打印f('python') = 14





# f('hello ') = f('ello ') + 1
# f('ello ') = f('llo ') + 1
# f('llo ') = f('lo ') + 1
# f('lo ') = f('o ') + 1
# f('o ') = f(' ') + 1
# f(' ') = f('') + 1
# f('') = 3

# 最终：打印f('python') = 9




