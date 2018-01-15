# -*- coding: UTF-8 -*-

# 面向对象简介
# 类Class用来描述具有相同属性和方法的对象的集合,定义了该集合中每个对象所共有的属性和方法,对象是类的实例
# 类变量: 类的变量在整个实例化的对象是公用的
# 数据成员: 类变量或者实例变量用于处理类及其实例对象的相关的数据
# 方法重写: 如果从父类继承的方法不能满足子类的需求,可以对其进行改写,这个过程方法叫方法的覆盖,也称为方法的重写
# 实例变量: 定义在方法中的变量,只作用于当前实例的类
# 继承: 即一个派生类继承基类的字段和方法,继承允许把一个派生类的对象作为一个基类对象对待
# 实例化: 创建一个类的实例,类的具体对象
# 方法: 类中定义的函数
# 对象: 通过类定义的数据结构实例,对象包括两个数据成员(类变量和实例变量)和方法

# 创建类
class Employee:
    '所有员工的基类'
    empCount = 0

    # __init__是一种特殊的方法,被称为类的构造函数或初始化方法;
    # 当创建这个类的实例对象的时候就会调用该方法
    # self代表类的实例,而非类本身,在定义的时候是必须的
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print '员工总数: %d' % Employee.empCount

    def displayEmployee(self):
        print 'Name: ', self.name
        print 'Salary: ', self.salary

    # def __del__(self):
    #     className = self.__class__.__name__
    #     print className, '对象被销毁了'

a = Employee('FFF', '9000')
a.displayEmployee()
a.displayCount()

# 访问属性
# 可以使用'.'来访问对象的属性
# 可以添加,删除,修改类的属性

b = Employee('WWW', '5000')
b.displayEmployee()
b.displayCount()

b.empCount = 100
print b.empCount
print a.empCount
print '###########################'

# getattr(对象, 属性名)访问对象的属性
# hasattr(对象, 属性名)检查是否存在一个属性
# setattr(对象, 属性名, 值)设置一个属性,如果不存在,将会创建一个新属性
# delattr(对象, 属性名)删除属性

# print hasattr(a, 'age')
setattr(a, 'age', 26)
print getattr(a, 'age')
delattr(a, 'age')
print hasattr(a, 'age')

# python内置类属性
# __dict__: 类的属性(包含一个字典, 由类的数据属性组成)
# __doc__: 类的文档字符串
# __name__: 类名
# __module__: 类所定义的模块
# __bases__: 类的所有父类构成元素(包含了一个由所有父类组成的元组)

print 'dict: ', Employee.__dict__
print 'doc: ', Employee.__doc__
print 'name: ', Employee.__name__
print 'module: ', Employee.__module__
print 'bases: ', Employee.__bases__

# python对象销毁(垃圾回收)
# python使用引用计数来跟踪和回收垃圾
# 在python内部记录所有使用中的对象各有多少引用
# 当对象的引用技术为0的时候,它被垃圾回收,由解析器选择适当的时机,将垃圾对象占用的内存空间回收
# 析构函数__del__在对象被销毁的时候调用
print '#######################'
# del a

# 类的继承
# 面向对象的编程带来的主要好处之一是代码的重用,实现这种重用的方法之一是通过继承机制
# 继承的特点
# 1.在继承中基类的构造__init__方法不会被自动调用,它需要在派生类中主动调用
# 2.在调用基类的方法时,需要加上基类的类名前缀,且需要带上self参数,区别在于类中调用普通函数时并不需要带上self参数
# 3.python总是首先查找对应类的方法,如果它不能在派生类中找到对应的方法,它才开始到基类中逐个查找

# Employee的派生类: Designer(设计师类)

class Designer(Employee):
    def __init__(self, part):
        self.part = part

    def displayPart(self):
        print self.part

c = Designer('开发部')
c.name = 'FFF'
c.salary = '4500'

print c.displayEmployee()

# 类属性与方法
# 类的私有属性
# __private_attrs: 声明该属性为私有,不能在类的外部被使用或直接访问,在类的内部使用self.__private_attrs访问
# 类的方法
# 在类的内部,使用def关键字为类定义一个方法,与一般函数定义不同,类方法必须包含参数self,且为第一个参数
# 类的私有方法
# __private_method:声明该方法为私有方法,不能在类的外部调用

# 实例
class JustCounter:
    __secretCount = 0 # 私有属性
    publicCount = 0   # 公有属性

    def count(self):
        self.__serentCount += 1
        self.publicCount += 1
        print self.__serentCount

coun = JustCounter()

print coun.publicCount