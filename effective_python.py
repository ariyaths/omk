# -*- coding: utf-8 -*-
"""
Created on Tue May 31 10:59:24 2022

@author: nairo
"""
##1
def safe_division(number, divisor, *,
                  ignore_overflow=False,
                  ignore_zero_division=False):

    try:
        return number / divisor

    except OverflowError:

        if ignore_overflow:
            return 0

        else:
            raise

    except ZeroDivisionError:

        if ignore_zero_division:
            return float('inf')

        else:
            raise
##2
class CountMissing(object):
    def __init__(self):
        self.added = 0

    def __call__(self):
        self.added += 1
        return 0

# counter = CountMissing()
# counter()
# assert callable(counter)

##3
class Field(object):
    def __init__(self, name):
        self.name = name
        self.internal_name = '_' + self.name
    
    def __get__(self, instance, instance_type):
        if instance is None: return self
        return getattr(instance, self.internal_name, ' ')
    
    def __set__(self, instance, value):
        setattr(instance, self.internal_name, value)

class Customer(object):
    # Class attributes
    first_name = Field('first_name')
    last_name = Field('last_name')
    prefix = Field('prefix')
    suffix = Field('suffix')

# foo = Customer()
# print('Before:', repr(foo.first_name), foo.__dict__)
# foo.first_name = 'Euclid'
# print('After:', repr(foo.first_name), foo.__dict__)

##4
from queue import Queue
from time import sleep
from threading import Thread

queue = Queue(1)

def consumer():
    sleep(0.1)
    queue.get()
    print('Consumer got 1')
    queue.get()
    print('Consumer got 2')

# thread = Thread(target=consumer)
# thread.start()

# queue.put(object())
# print('Producer put 1')
# queue.put(object())
# print('Producer put 2')
# thread.join()
# print('Producer done')

##5
def my_coroutine():
    while True:
        recieved = yield
        print('Recieved:', recieved)

# it = my_coroutine()
# next(it)
# it.send('First')
# it.send('Second')

