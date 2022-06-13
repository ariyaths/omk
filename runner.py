# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 09:47:43 2022

@author: nairo
"""

from os import listdir as ld, remove

def replacer(rep_path):
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
    rep_list = ld(rep_path)
    out = []

    for filename in rep_list:
        out += [filename.replace(".JPG", ".RAF")]

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
        print(item)
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
        remove(path + "\\" + file)

FOLDER = "C:\\fuji_test"
to_parse = [item for item in ld(FOLDER) if item[0].isdigit()]
to_del = replacer(FOLDER + "\\deleted") + replacer(FOLDER + "\\Family")

for sub_fold in to_parse:
    raw_path = FOLDER + "\\" + sub_fold + "\\raw"
    delete_all(find_similar(ld(raw_path), to_del), raw_path)
