#!/usr/bin/python3
# -*- coding:utf-8 -*-

remark = ''''''

#引入相关包
pythonPath = r'D:\TDdownload\Document\Python'
import os,sys,time
sys.path.append(pythonPath)
import configure as cfg


from xml.etree import ElementTree as ET

tree = ET.parse(r'D:\TDdownload\Document\Python\File\XML\data-text.xml')
root = tree.getroot()

data = root.find('Data')

all_data = []

for observation in data:
    record = {}
    for item in observation:
        lookup_key = item.attrib.keys()[0]

        if lookup_key == 'Numeric':
            rec_key = 'NUMERIC'
            rec_value = item.attrib['Numeric']
        else:
            rec_key = item.attrib[lookup_key]
            rec_value = item.attrib['Code']

        record[rec_key] = rec_value

    all_data.append(record)
print(all_data)








if __name__=="__main__":
    pass