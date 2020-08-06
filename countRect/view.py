# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Time   :  2020/7/2 17:56
# Author :  Richard
# File   :  view.py

'''
负责与用户的数据交互
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
                    时（默认为{早上8:00}，输入格式如：8:00或8）：
                结束时间（默认为{今年-今月-今日 20:00}）
                    年（默认为{今年}，输入格式如：2020）：
                    月（默认为{本月}，输入格式如：7）：
                    日（默认为{今天}，输入格式如：7）：
                    时（默认为{晚上20:00}，输入格式如：20:00或20）：
'''
import os
import time


class View(object):
    def __init__(self):
        self.welcome = "***************labelImg矩形框统计器***************"
        print(self.welcome)
        self.input_path = "\n####################################################\n" \
                            "请输入Pascal VOC标注文件所在文件夹路径\n" \
                            "（注：可通过点击标注文件所在窗口的顶部路径窗口复制路径）:\n" \
                            "###################################################\n" \
                          "这里输入："
        self.path_error = "!!!!!!!!!请检查路径是否为包含.xml标注数据的文件夹!!!!!!!"
        self.input_datetime = "\n####################\n" \
                              "请输入需要统计的时间段\n" \
                              "####################\n"
        self.input_start_datetime = "\n####################################\n" \
                                    "开始时间（默认为{今年-今月-今日 08:00}）\n" \
                                    "####################################\n"
        self.input_end_datetime = "\n####################################\n" \
                                    "结束时间（默认为{今年-今月-今日 20:00}）\n" \
                                    "####################################\n"
        self.input_year = "\n年（默认为{今年}，输入格式如：2020）:"
        self.input_month = "\n月（默认为{本月}，输入格式如：7）："
        self.input_day = "\n日（默认为{今天}，输入格式如：7）："
        self.input_hour_minute_start = "\n时（默认为{早上8:00}，输入格式如：8:00或8）："
        self.input_hour_minute_end = "\n时（默认为{晚上20:00}，输入格式如：20:00或20）："
        self.output_count_format = "\n##########################\n" \
                            "该路径下该时间段的框数为：{}\n" \
                            "##########################\n"

    def get_path(self):
        base_dir_path = input(self.input_path)
        try:
            if not os.path.exists(base_dir_path):
                print("路径不正确，请重新输入！")
                return self.get_path()
        except:
            print("路径不正确，请重新输入！")
            return self.get_path()
        return base_dir_path

    def get_year(self):
        localtime = time.localtime(time.time())
        year = input(self.input_year) or str(localtime.tm_year)
        try:
            year = int(year)
            if year < 1980 or year > 2080:
                raise Exception
            return year
        except Exception as e:
            print("年的格式是不正确，请重新输入！")
            return self.get_year()

    def get_month(self, year):
        localtime = time.localtime(time.time())
        month = input(self.input_month) or localtime.tm_mon
        try:
            month = int(month)
            if month>=1 and month<=12:
                return month
            else:
                raise Exception
        except Exception:
            print("月的格式不正确，请重新输入！")
            return self.get_month(year)

    def get_day(self, year, month):
        localtime = time.localtime(time.time())
        day = input(self.input_day) or localtime.tm_mday
        try:
            day = int(day)
            if (0 < month <= 12):
                if ((month in (1, 3, 5, 7, 8, 10, 12)) and (day > 31 or day < 0)):
                    print('输入的日期有误，%d月为大月，最多31天。请重新输入！\n' % month)
                    raise Exception
                if ((month in (4, 6, 9, 11)) and (day > 30 or day < 0)):
                    print('输入的日期有误，%d月为小月，最多30天。请重新输入！\n' % month)
                    raise Exception
                if (month == 2):
                    if (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)):
                        if (day > 29 or day < 0):
                            print('输入的日期有误，该年2月为闰年2月，最多29天。请重新输入！\n')
                            raise Exception
                    else:
                        if (day > 28 or day < 0):
                            print('输入的日期有误，该年2月为平年2月，最多28天。请重新输入！\n')
                            raise Exception
            else:
                print('输入的月份有误，每年只有12个月份。请重新输入！\n')
                raise Exception
        except Exception:
            return self.get_day(year, month)
        return day

    def get_time(self, start_or_end="start"):
        if start_or_end == "start":
            t_time = input(self.input_hour_minute_start) or "8"
        else:
            t_time = input(self.input_hour_minute_end) or "20"
        if len(t_time) > 5:
            print("输入的时间格式错误，请参考输入范例重新输入！")
            return self.get_time()
        start_datetime_split = t_time.split(':')
        try:
            start_hour = int(start_datetime_split[0])
            if start_hour>=0 and start_hour<=24:
                if len(start_datetime_split) == 1:
                    return str(start_hour).zfill(2)+':00:00'
                elif len(start_datetime_split) == 2:
                    start_min = int(start_datetime_split[1].lstrip('0'))
                    if start_min>=0 and start_min<60:
                        return str(start_hour).zfill(2)+":"+str(start_min).zfill(2)+":00"
                else:
                    raise Exception
            else:
                raise Exception
        except Exception:
            print("输入的时间格式错误，请参考输入范例重新输入！")
            return self.get_time(start_or_end)

    def get_datetime(self, start_or_end="start"):
        year = self.get_year()
        month = self.get_month(year)
        day = self.get_day(year, month)
        t_time = self.get_time(start_or_end)
        return "{}-{}-{} {}".format(year, month, day, t_time)

    def output_count(self, count):
        print(self.output_count_format.format(count))