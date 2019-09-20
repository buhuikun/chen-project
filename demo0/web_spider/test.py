# li = ['1', 'as', 'ads', 'ds']
# s = ''
# for i in range(len(li)):
#     if i<len(li)-1:
#         a = li[i]+'&&'+li[i+1]
#         s+= a
# print(s)
# class Singleton():
#     def __new__(cls, *args, **kw):
#         if not hasattr(cls, '_instance'):
#             orig = super(Singleton, cls)
#             cls._instance = orig.__new__(cls, *args, **kw)
#             # cls._instance = orig.__new__(cls, *args, **kw)
#         return cls._instance
#
# s = Singleton()


# class Sing():
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, '_instance'):
#             orig = super(Sing,cls)
#             cls._instance = orig.__new__(cls, *args, **kwargs)
#         return cls._instance

# class Sing():
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, '_instance'):
#             a = super(Sing, cls)
#             cls._instance = a.__new__(cls, *args, **kwargs)
#         return cls._instance
#
# class S():
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, '_instance'):
#             a = super(S, cls)
#             cls._instance = a.__new__(cls, *args, **kwargs)
#         return cls._instance
#
# class S():
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, '_instance'):
#             a = super(S, cls)
#             cls._instance = a.__new__(cls, *args, **kwargs)
#         return cls._instance
#
#
# class S():
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, '_instance'):
#             a = super(S, cls)
#             cls._instance = a.__new__(cls, *args, **kwargs)
#         return cls._instance
#

# class S():
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, '_instance'):
#             a = super(S, cls)
#             cls._instance = a.__new__(cls, *args, **kwargs)
#         return cls._instance

# 共享属性
# class Borg():
#     _state = {}
#     def __new__(cls, *args, **kwargs):
#         ob = super(Borg, cls).__new__(cls, *args, **kwargs)
#         ob.__dict__ = cls._state
#         return ob

# class Borg():
#     _state = {}
#     def __new__(cls, *args, **kwargs):
#         ob = super(Borg, cls).__new__(cls, *args, **kwargs)
#         ob.__dict__ = cls._state
# #         return ob
#
# class Borg():
#     _state = {}
#     def __new__(cls, *args, **kwargs):
#         ob = super(Borg, cls).__new__(cls, *args, **kwargs)
#         ob.__dict__ = cls._state
#         return ob
#
# class Borg():
#     _state = {}
#     def __new__(cls, *args, **kwargs):
#         ob = super(Borg, cls).__new__(cls, *args, **kwargs)
#         ob.__dict__ = ob._state
#         return ob
#
#
# class Borg():
#     _state = {}
#     def __new__(cls, *args, **kwargs):
#         ob = super(Borg, cls).__new__(cls , *args, **kwargs)
#         ob.__dict__ = cls._state
#         return ob


# def print_directory(sPath):
#     import os
#     for sChild in os.listdir(sPath):
#         sChildPath=os.path.join(sPath, sChild)
#         if os.path.isdir(sChildPath):
#             print_directory(sChildPath)
#         else:
#             print(sChildPath)

import os

# def directory(sPath):
#     for sChild in os.listdir(sPath):
#         sChildPath = os.path.join(sPath, sChild)
#         if os.path.isdir(sChildPath):
#             directory(sChildPath)
#         else:
#             print(sChildPath)

# def directory(sPath):
#     for sChild in os.listdir(sPath):
#         sChildPath = os.path.join(sPath, sChild)
#         if os.path.isdir(sChildPath):
#             directory(sChildPath)
#         else:
#             print(sChildPath)

# def directory(sPath):
#     for sChild in os.listdir(sPath):
#         sChildPath = os.path.join(sPath, sChild)
#         if os.path.isdir(sChildPath):
#             directory(sChildPath)
#         else:
#             print(sChildPath)

# def directory(sPath):
#     for sChild in os.listdir(sPath):
#         sChildPath = os.path.join(sPath, sChild)
#         if os.path.isdir(sChildPath):
#             directory(sChildPath)
#         else:
#             print(sChildPath)
#
#
# import time
#
# def metric(fun):
#     def wrapper(*args, **kwargs):
#         stat  =time.time()
#         res = fun()
#         print(time.time()-stat)
#     return wrapper
#
#
# @metric
# def main():
#     for i in range(10):
#         for j in range(1000):
#             print(j)
#
# main()
#









