# from scrapy.loader.processors import TakeFirst
# processor = TakeFirst ()
#
#
# print(processor([1,2,3]))


from scrapy. loader. processors import SelectJmes
# proc = SelectJmes ( 'foo' )
# processor = SelectJmes （’ fo口’）
# print(processor({’ foo ':’ bar'}))



# print(abs(-5.6))

from collections import deque

# a = deque([1,2,3,3])


from collections import deque
# 从尾部进入，从头部弹出，保证长度为5
dq1 = deque('abcdefg', maxlen=5)
print(dq1)  # ['c', 'd', 'e', 'f', 'g']
print(dq1.maxlen)  # 5
# 从左端入列
dq1.appendleft('q')
print(dq1)  # ['q', 'c', 'd', 'e', 'f']
# 从左端入列
dq1.extendleft('abc')
print(dq1)  # ['c', 'b', 'a', 'q', 'c']
# 从左端出列并且返回
dq1.popleft()  # c
print(dq1)  # ['b', 'a', 'q', 'c']
# 将队头n个元素进行右旋
dq1.rotate(2)
print(dq1)  # ['q', 'c', 'b', 'a']
# 将队尾两个元素进行左旋
dq1.rotate(-2)
print(dq1)  # ['b', 'a', 'q', 'c']