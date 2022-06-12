# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 09:47:43 2022

@author: nairo
"""

from os import listdir as ld, remove

def slicer(slice_path):
    """

    Parameters
    ----------
    slice_path : string
        file path

    Returns
    -------
    out
        a copy of all items in slice_list
        with extensions removed.

    """
    slice_list = ld(slice_path)
    out = []

    for filename in slice_list:
        idx = filename.rfind(".")
        out += [filename[:idx]]

    return out

def find_similar(first_l, second_l):
    """

    Parameters
    ----------
    first_l : list
        list to parse.
    second_l : list
        list to find similarities.

    Yields
    ------
    item : string
        similar value found in both lists.

    """
    for item in first_l:
        if item in second_l:
            yield item

def delete_all(generator_object, path):
    """

    Parameters
    ----------
    generator_object : generator
        container of multiple strings that are file names.
    path : string
        file path.

    Returns
    -------
    None.

    """
    for file in generator_object:
        remove(path + "\\" + file + ".raw")

FOLDER = "C:\\Fuji"
to_parse = [item for item in ld(FOLDER) if item[0].isdigit()]
to_del = slicer(FOLDER + "\\deleted") + slicer(FOLDER + "\\Family")

for sub_fold in to_parse:
    raw_path = FOLDER + "\\" + sub_fold + "\\raw"
    sim = find_similar(slicer(raw_path), to_del)
    delete_all(sim, raw_path)
