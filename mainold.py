# HIII



def hello():
    print('Hello, World!')

# c = ColorOpacity(color=Colors.RED, opacity=0.5)
# print(c)
# Prints 
#   ColorOpacity(b=True, opacity=0.5, a=A(a=2), color=(255, 0, 0))
# as expected
# vect1 = Vector(quaternion=Quaternion(1, 0, 0, 0))



# vect = Vector.from_point((1, 0, 0))
# print(vect)
# from dataclasses import dataclass
# # import dataclasses
# import inspect
# from collections import OrderedDict

# @dataclass
# class A():
#     a = 4

# @dataclass
# class TestData():
#     test1 = 1.0
#     test2 = 2.0
#     test3 = A(a=5)

#     def __mul__(self, scalar):
#         return TestData(self.test1 * scalar, self.test2 * scalar, self.test3)

#     @property
#     def sum(self):
#         return self.test1 + self.test2
    
#     @classmethod
#     def from_array(cls, arr):
#         return cls(test1=arr[0], test2=arr[1])

# t1 = TestData(test1=5, test2=6, test3=A(a=7))
# print(t1)

# testdict = TestData.__dict__
# # print(testdict)

# filtered_attrs = OrderedDict((k, v) for k, v in testdict.items() if not k.startswith('_'))

# attrs = OrderedDict((k, v) for k, v in filtered_attrs.items() if not isinstance(v, (property, classmethod)) and not inspect.isfunction(v))

# print(attrs)

# testdict = TestData.__dict__

# filtered_attrs = {k: v for k, v in TestData.__dict__.items() if not k.startswith('_')}
# attrs = OrderedDict(reversed(list(filtered_attrs.items())))

# print(attrs)
# # print(testdict)

# # print(attrs)


# cls_fields = [dataclasses._get_field(TestData, name, type(t)) for name, t in attrs.items()]

# print(cls_fields)

# testdict = dict((k, v) for k, v in inspect.getmembers(d) if k[0] != '_')

# print(testdict)

# t2 = TestData(test1=1, test2=2) * 2
# t3 = TestData.from_array([1, 2])


# print(t2)
# print(t3)

# print(t3.sum)

# class A:
#     pass

# class B(object, A):
#     pass

# print(B.__mro__)





# connectToWifi(ssid='Mujoo', password='Mosshall3115')
# 
# installPackage('functools')

# import re
# import sys
# import copy
# import types
# import inspect
# import keyword
# import builtins
# import functools
# import _thread


# installPackage('inspect')
# installPackage('abc')
# installPackage('os-path')

# Check if all importing works
# import types
# import inspect
# import abc
# from ulab import numpy as np
# import os.path

# print(os.path.exists('main.py'))
# print(inspect.ismodule(np))



# # Test if importing numpy works (it does!)
# from ulab import numpy as np
# a = np.array([1, 2, 3]) # arrays work
# print(a)
# b = np.log(a) # functions work
# print(b)
# c = 1+2j # complex numbers work
# print(c**2)

# c = ColorOpacity(color=Colors.RED, opacity=0.5)

# print(c)

# testdict = ColorOpacity.__dict__
# # print(testdict)


# filtered_attrs = {k: v for k, v in testdict.items() if not k.startswith('_')}

# attrs = {k: v for k, v in filtered_attrs.items() if not isinstance(v, (property, classmethod)) and not inspect.isfunction(v)}

# print(attrs)


# print(c)


# # Create an LED and Button object from pin numbers
# led1 = LED(id=1, pins=(40, 39, 38))
# button1 = Button(id=1, pin=13, pull_up=True)


# # Function to run when the button is pressed
# def whenButtonPressed():
#     try:
#         led1.cycleThroughColorsDemo(5)
#         pause(500)
#         led1.cycleThroughIntensityDemo(5)
#         pause(500)
#         led1.setColor(Colors.RED)
#         pause(500)
#         led1.setColor(Colors.GREEN)
#         pause(500)
#         led1.setColor(Colors.BLUE)
#         pause(500)
#         led1.turnOff()
#     except:
#         led1.resetPwms()


# # Wait until the button is pressed
# while True:
#     button1.afterButtonPressedAndReleased(whenButtonPressed)