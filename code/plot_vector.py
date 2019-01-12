# _*_ coding: utf-8 _*_
__author__ = 'xbr'
__date__ = '2018/10/31 12:44'

import os

import matplotlib.pyplot as plt

from ospybook.vectorplotter import VectorPlotter

# 数据当前路径
os.chdir(r'D:\osgeopy-data\global')
# 调用VectorPlotter类
vp = VectorPlotter(True)
# 在当前路径下分别画两个矢量数据
vp.plot('ne_50m_admin_0_countries.shp', fill=False)  # 面矢量
vp.plot('ne_50m_populated_places.shp', 'bo')         # 点矢量

# 设置横纵坐标的名称以及对应字体格式
font2 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 15,
        }
plt.xlabel('Longitude', font2)  # X轴标题
plt.ylabel('Latitude', font2)   # Y轴标题
plt.show()   # 少了这句话则图像不显示
