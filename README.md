# 基于的LableImg的框数统计工具

这个项目修改了labelImg标注工具，让它得到的标注文件易于统计边框数目。同时，以提供了相应的统计工具。


## 直接使用
* 获取项目;
* 安装项目类的labelIng工具（经过改造的）;
* 标注完后使用CountRec里的窗口程序统计输入时间内的框数;

## 更多
* 也可以使用如下命令打包CountRec成exe可执行文件
```
pyinstaller -F countRect/CountRect.py
```

* 也可以基于自己的意愿改造labelImg, 再重新打包。