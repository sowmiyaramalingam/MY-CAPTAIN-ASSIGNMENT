# -*- coding: utf-8 -*-
radius =float(input("Enter the radius of the circle"))
area =3.14*radius*radius
print("area of the circle is: ",area)

filename =input("Input filename")
f_extens =filename.split(".")
print("extension of the file is:"+repr(f_extens[-1]))
