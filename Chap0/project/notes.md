# append()  与extend()区别：

分别尝试以下方法，结果如下：

mylist=[1,2,[3,4]]       >>>[1,2,[3,4]]

mylist.append(5)    >>>[1, 2, [3, 4], 5]

mylist.append([5])   >>>[1, 2, [3, 4], [5]]

mylist.append([5,6])   >>>[1, 2, [3, 4], [5, 6]]

mylist.extend([5,6])     >>>[1, 2, [3,  4], 5, 6]

mylist.extend([5])    >>> mylist.expand(1, 2, [3,  4], 5)
mylist.extend(5)   >>>TypeError: 'int' object is not iterable

可总结:

list.append(arg1) 可以是任意参数，作用是往已有列表中添加元素，如果添加的是列表，就被当成一个元素存在原列表中，只使list长度增加1.

list.extend(list1)  参数必须是列表类型，左右时将参数中的列表合并到原列表的末尾，使 list长度增加len(list1)。



# from module import 与import 区别

from module import function 后 ，function() 直接可用

import function 后,，要通过module.function()  调用。 
 
