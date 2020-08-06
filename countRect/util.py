# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Time   :  2020/7/3 9:49
# Author :  Richard
# File   :  util.py
import glob
import os
import time

'''
解析xml
'''
from xml.dom.minidom import parse


def xml_parser(xml_file):
    '''
    Parse an xml file and return the annotation info in the file

    :param xml_file: the xml file name to be parsed
    :return: file_name,BboxCount,saveDateTime
    '''
    DOMTree = parse(xml_file)
    collection = DOMTree.documentElement  # 得到xml文件的根节点
    file_name = collection.getElementsByTagName('filename')[0].childNodes[0].data
    saveDateTime = collection.getElementsByTagName('saveDateTime')[0].childNodes[0].data
    BboxCount = int(collection.getElementsByTagName('BboxCount')[0].childNodes[0].data)
    return file_name, BboxCount, saveDateTime


def date_to_timestamp(datetime):
    # 转换成时间数组
    timeArray = time.strptime(datetime, "%Y-%m-%d %H:%M:%S")
    # 转换成时间戳
    timestamp = time.mktime(timeArray)
    return timestamp


'''
根据时间段统计xml中的bbox
'''
def count_rec(dir_path, start_datetime, end_datetime):
    start_time = date_to_timestamp(start_datetime)
    end_time = date_to_timestamp(end_datetime)
    if not os.path.exists(dir_path):
        print("路径不存在！")
        return 0
    dir_path = os.path.join(dir_path, '*.xml')
    xmls = glob.glob(dir_path)
    if len(xmls) == 0:
        print("没有发现xml, 请检查路径否正确！")
        return 0
    count = 0
    for xml in xmls:
        try:
            file_name, bbox_count, datetime = xml_parser(xml)
            cur_timestamp = date_to_timestamp(datetime)
            # print(bbox_count)
            if cur_timestamp > start_time and cur_timestamp < end_time:
                count += bbox_count
        except Exception:
            count += 0
    return count
