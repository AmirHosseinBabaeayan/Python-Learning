# -*- coding: utf-8 -*-
"""Video16.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vfQK75L-I09ueCv5aUI-O1qfLMUUwowW
"""

d = {
     1:"do",
     2:"se",
     3:"chahar"
}

type(d)

d[3]

#d["3"] # Key Error
d.get("3","vojod nadarad")

d.keys()

d.values()

d.items()

d = {
     1:"do",
     2:"se",
     3:"chahar"
}

for Key in d.keys():
  print(Key, "=====>", d[Key])

for Key in d.keys():
  print(Key, "=====>", d.get(Key))
  d[Key]= "ahb"
d

for k,v in d.items():
  print(k, "=====>", v)
  k = "ahb"
d
