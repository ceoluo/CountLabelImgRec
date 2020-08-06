# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Time   :  2020/7/2 14:20
# Author :  Richard
# File   :  countRect.py

'''
input:
    请输入Pascal VOC标注文件所在文件夹路径（可通过点击标注文件所在窗口的顶部路径窗口复制路径）；
    parse: 路径是否存在？
        不存在则提示：请检测输入路径是否正确。重新提示输入；
        存在则提示：
            请输入需要统计的时间段：
                开始时间（默认为{今年-今月-今日 08:00}）：
                    年（默认为{今年}，输入格式如：2020）：
                    月（默认为{本月}，输入格式如：7）：
                    日（默认为{今天}，输入格式如：7）：
                    时（默认为{早上8:00}）：
                结束时间（默认为{今年-今月-今日 20:00}）
                    年（默认为{今年}，输入格式如：2020）：
                    月（默认为{本月}，输入格式如：7）：
                    日（默认为{今天}，输入格式如：7）：
                    时（默认为{晚上20:00}）：
        将开始时间和结束时间转化为时间戳；

count:
    1、获取所有xml绝对路径
    2、遍历xml解析出BboxCount和saveDatetime
    3、比较saveDatetime的时间戳是否在开始时间和结束时间之内，若是则计数BboxCount
    4、返回计数

output：
    请记录！！！该目录下共有矩形框的个数为：{count}
'''
import sys

from view import View
from util import count_rec


def main():
    view = View()
    # 获取文件目录
    base_dir_path = view.get_path()
    # 获取开始时间
    print(view.input_start_datetime)
    start_datetime = view.get_datetime(start_or_end="start")
    # 获取结束时间
    print(view.input_end_datetime)
    end_datetime = view.get_datetime(start_or_end="end")
    # 根据时间段统计框数
    all_count = count_rec(base_dir_path, start_datetime, end_datetime)
    view.output_count(all_count)
    return 0

if __name__ == '__main__':
    while True:
        main()
        print("\n\n----------------------------------------------------")
