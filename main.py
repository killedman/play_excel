#! /usr/bin/env python
# -*- coding: utf-8 -*-

from openpyxl import load_workbook

"""
openpyxl 不支持old .xls file format
"""
excel_file = 'wacai_2019-05-2019-05.xlsx'

data = load_workbook(excel_file)
for sheetname in data.sheetnames:
    print(sheetname)