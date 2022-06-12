# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 07:45:50 2022

@author: nairo
"""

from os import mkdir as mk, listdir as ld
from shutil import rmtree

mk(r"C:\Fuji")
mk(r"C:\Fuji\23-04-22")
mk(r"C:\Fuji\23-04-22\jpg")
mk(r"C:\Fuji\23-04-22\raw")
mk(r"C:\Fuji\24-04-22")
mk(r"C:\Fuji\24-04-22\jpg")
mk(r"C:\Fuji\24-04-22\raw")
mk(r"C:\Fuji\deleted")
mk(r"C:\Fuji\Family")
open(r"C:\Fuji\deleted\A.jpg", "w")
open(r"C:\Fuji\deleted\B.jpg", "w")
open(r"C:\Fuji\Family\D.jpg", "w")
open(r"C:\Fuji\Family\F.jpg", "w")
open(r"C:\Fuji\23-04-22\jpg\A.jpg", "w")
open(r"C:\Fuji\23-04-22\jpg\B.jpg", "w")
open(r"C:\Fuji\23-04-22\jpg\D.jpg", "w")
open(r"C:\Fuji\23-04-22\jpg\F.jpg", "w")
open(r"C:\Fuji\23-04-22\raw\A.raw", "w")
open(r"C:\Fuji\23-04-22\raw\B.raw", "w")
open(r"C:\Fuji\23-04-22\raw\D.raw", "w")
open(r"C:\Fuji\23-04-22\raw\E.raw", "w")
open(r"C:\Fuji\24-04-22\jpg\A.jpg", "w")
open(r"C:\Fuji\24-04-22\jpg\B.jpg", "w")
open(r"C:\Fuji\24-04-22\jpg\D.jpg", "w")
open(r"C:\Fuji\24-04-22\jpg\F.jpg", "w")
open(r"C:\Fuji\24-04-22\raw\A.raw", "w")
open(r"C:\Fuji\24-04-22\raw\B.raw", "w")
open(r"C:\Fuji\24-04-22\raw\D.raw", "w")
open(r"C:\Fuji\24-04-22\raw\E.raw", "w")

execfile(r"C:\code\omk\runner.py")

assert ld(r"C:\Fuji\23-04-22\raw") == ["E.raw"]
assert ld(r"C:\Fuji\24-04-22\raw") == ["E.raw"]
assert ld(r"C:\Fuji\23-04-22\jpg") == ["A.jpg", "B.jpg", "D.jpg", "F.jpg"]
assert ld(r"C:\Fuji\24-04-22\jpg") == ["A.jpg", "B.jpg", "D.jpg", "F.jpg"]
assert ld(r"C:\Fuji\deleted") == ["A.jpg", "B.jpg"]
assert ld(r"C:\Fuji\Family") == ["D.jpg", "F.jpg"]

print("Code correct")
rmtree(r"C:\Fuji")