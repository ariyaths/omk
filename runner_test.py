# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 07:45:50 2022

@author: nairo
"""

from os import mkdir as mk, listdir as ld
from shutil import rmtree

mk(r"C:\fuji_test")
mk(r"C:\fuji_test\23-04-22")
mk(r"C:\fuji_test\23-04-22\jpg")
mk(r"C:\fuji_test\23-04-22\raw")
mk(r"C:\fuji_test\24-04-22")
mk(r"C:\fuji_test\24-04-22\jpg")
mk(r"C:\fuji_test\24-04-22\raw")
mk(r"C:\fuji_test\deleted")
mk(r"C:\fuji_test\Family")
open(r"C:\fuji_test\deleted\A.JPG", "w")
open(r"C:\fuji_test\deleted\B.JPG", "w")
open(r"C:\fuji_test\Family\D.JPG", "w")
open(r"C:\fuji_test\Family\F.JPG", "w")
open(r"C:\fuji_test\23-04-22\jpg\A.JPG", "w")
open(r"C:\fuji_test\23-04-22\jpg\B.JPG", "w")
open(r"C:\fuji_test\23-04-22\jpg\D.JPG", "w")
open(r"C:\fuji_test\23-04-22\jpg\F.JPG", "w")
open(r"C:\fuji_test\23-04-22\raw\A.RAF", "w")
open(r"C:\fuji_test\23-04-22\raw\B.RAF", "w")
open(r"C:\fuji_test\23-04-22\raw\D.RAF", "w")
open(r"C:\fuji_test\23-04-22\raw\E.RAF", "w")
open(r"C:\fuji_test\24-04-22\jpg\A.JPG", "w")
open(r"C:\fuji_test\24-04-22\jpg\B.JPG", "w")
open(r"C:\fuji_test\24-04-22\jpg\D.JPG", "w")
open(r"C:\fuji_test\24-04-22\jpg\F.JPG", "w")
open(r"C:\fuji_test\24-04-22\raw\A.RAF", "w")
open(r"C:\fuji_test\24-04-22\raw\B.RAF", "w")
open(r"C:\fuji_test\24-04-22\raw\D.RAF", "w")
open(r"C:\fuji_test\24-04-22\raw\E.RAF", "w")

exec(open(r"C:\code\omk\del_raw_by_jpg.py").read())
# exec(open(r"C:\code\omk\runner.py").read())

assert ld(r"C:\fuji_test\23-04-22\raw") == ["E.RAF"]
assert ld(r"C:\fuji_test\24-04-22\raw") == ["E.RAF"]
assert ld(r"C:\fuji_test\23-04-22\jpg") == ["A.JPG", "B.JPG", "D.JPG", "F.JPG"]
assert ld(r"C:\fuji_test\24-04-22\jpg") == ["A.JPG", "B.JPG", "D.JPG", "F.JPG"]
assert ld(r"C:\fuji_test\deleted") == ["A.JPG", "B.JPG"]
assert ld(r"C:\fuji_test\Family") == ["D.JPG", "F.JPG"]

print("Code correct")
rmtree(r"C:\fuji_test")
