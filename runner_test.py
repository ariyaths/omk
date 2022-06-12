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
open(r"C:\fuji_test\deleted\A.jpg", "w")
open(r"C:\fuji_test\deleted\B.jpg", "w")
open(r"C:\fuji_test\Family\D.jpg", "w")
open(r"C:\fuji_test\Family\F.jpg", "w")
open(r"C:\fuji_test\23-04-22\jpg\A.jpg", "w")
open(r"C:\fuji_test\23-04-22\jpg\B.jpg", "w")
open(r"C:\fuji_test\23-04-22\jpg\D.jpg", "w")
open(r"C:\fuji_test\23-04-22\jpg\F.jpg", "w")
open(r"C:\fuji_test\23-04-22\raw\A.raw", "w")
open(r"C:\fuji_test\23-04-22\raw\B.raw", "w")
open(r"C:\fuji_test\23-04-22\raw\D.raw", "w")
open(r"C:\fuji_test\23-04-22\raw\E.raw", "w")
open(r"C:\fuji_test\24-04-22\jpg\A.jpg", "w")
open(r"C:\fuji_test\24-04-22\jpg\B.jpg", "w")
open(r"C:\fuji_test\24-04-22\jpg\D.jpg", "w")
open(r"C:\fuji_test\24-04-22\jpg\F.jpg", "w")
open(r"C:\fuji_test\24-04-22\raw\A.raw", "w")
open(r"C:\fuji_test\24-04-22\raw\B.raw", "w")
open(r"C:\fuji_test\24-04-22\raw\D.raw", "w")
open(r"C:\fuji_test\24-04-22\raw\E.raw", "w")

exec(open(r"C:\code\omk\runner.py").read())
 
assert ld(r"C:\fuji_test\23-04-22\raw") == ["E.raw"]
assert ld(r"C:\fuji_test\24-04-22\raw") == ["E.raw"]
assert ld(r"C:\fuji_test\23-04-22\jpg") == ["A.jpg", "B.jpg", "D.jpg", "F.jpg"]
assert ld(r"C:\fuji_test\24-04-22\jpg") == ["A.jpg", "B.jpg", "D.jpg", "F.jpg"]
assert ld(r"C:\fuji_test\deleted") == ["A.jpg", "B.jpg"]
assert ld(r"C:\fuji_test\Family") == ["D.jpg", "F.jpg"]

print("Code correct")
rmtree(r"C:\fuji_test")