# -*- coding: utf-8 -*-
"""Video22.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hzYa4ZjBwg_r_E8DdiDq965ilv41ciQK
"""

s = "amirhossein babaeayan"

print(type(s))

s.capitalize()

s

class Shape:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def s(self):
    return self.x * self.y
  
  def p(self):
    return 2*(self.x + self.y)

sh = Shape(2,4)

print(type(sh))

sh.s()

sh.x

sh.y

sh.p()

shape_x = 2
shape_y = 4

def s(x,y):
  return(x*y)

print("s = ", s(shape_x, shape_y))

class Square(Shape):
  
  def __init__(self, x):
    self.x = x
    self.y = x
  
  def xxx(self):
    return self.x

  def s(self):
    return self.x ** 3

sq = Square(5)

sq.s()

sq.p()

sq.xxx()

sp = Shape(4,6)

sp.xxx()

type(Square)

class Circle:
  pi = 3.14
  
  def __init__(self, r):
    self.r = r
  
  def p(self):
    return 2*self.pi*self.r

c1 = Circle(5)

c1.p()

class Circle2:
  pi = 3.14
  r = 1
  def set_r(self, ra):
    self.r = ra
  def p(self):
    return 2*self.pi*self.r

c2 = Circle2()

c2.pi

c2.p()

c2.set_r(5)

c2.p()

c2.p()

