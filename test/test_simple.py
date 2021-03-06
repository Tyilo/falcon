#!/usr/bin/env python

import unittest
import math

from timed_test import TimedTest, simple_test

@simple_test
def print_item():
  print 'hello'

def add(a, b):
  return a + b

def add1(a):
  return add(a, 1)

@simple_test
def add_loop():
  for i in xrange(1000):
    temp = add1(i)
  return temp

def compare(a, b):
  if a < b:
    return 10
  else:
    return -10

def loop(count):
  x = 0
  for i in xrange(count):
    x = x * 0
  return x

def infinite_loop():
  while 1: pass
  
def count_threshold(limit, threshold):
  count = 0
  for item in xrange(limit):
    if item > threshold: count += 1
  return count

def count_threshold_generator(limit, threshold):
  return sum(item > threshold for item in xrange(limit))

def global_math(count):
  for i in xrange(count):
    math.floor(i)

def unpack_first(x):
    a,b,c = x
    return a

def nested(x):
  def f(y):
    return y+y
  return f(x)

def nested_closure(x):
  def f(y):
    return x + y
  return f(x)

def nested_closure_repeat():
  for i in xrange(50):
    temp = nested_closure(i)
  return temp 

def inplace_add():
  x = 0
  x += 10
  
class Simple(TimedTest):
  def test_add1(self): self.time_compare(add, 1, 2)
  def test_add2(self): self.time_compare(add, 100, 200)
  def test_add3(self): self.time_compare(add, 10 * 50, 2)
  
  def test_compare1(self): self.time_compare(compare, 10, 100)
    
  def test_loop1(self):
    self.time_compare(loop, 100)
    
  def test_count_threshold(self):
    self.time_compare(count_threshold, 100, 40, repeat=5)
    
  def test_count_threshold_generator(self):
    self.time_compare(count_threshold_generator, 100, 40, repeat=5)

  def test_global_load(self): 
    self.time_compare(global_math, 10, repeat=5)
  
  def test_unpack_first(self):
    self.time_compare(unpack_first, (1,2,3), repeat = 1)

  def test_nested(self):
    self.time_compare(nested, 1, repeat=1)
  
  def test_nested_closure(self):
    self.time_compare(nested_closure, 1, repeat=1)
    
  def test_nested_closure_repeat(self):
    self.time_compare(nested_closure_repeat, repeat=1)
    
  def test_inplace_add(self):
    self.time_compare(inplace_add, repeat=1)

if __name__ == '__main__':
  unittest.main()
