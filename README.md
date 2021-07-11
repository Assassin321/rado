# 项目名称

基于导航雷达的海洋环境检测平台

## 版本
1.0

## 目录

- [概述](#概述)
- [内容](#内容)
- [功能](#功能)
- [安装运行](#安装运行)
- [输出结果](#输出结果)

## 内容
 检测平台后端，基于django框架和sqllite数据库

 检测平台前端，基于Vue框架以及Bootstrap框架

## 概述
基于Vue和Bootstrap框架搭建前端海洋环境监测平台，以及基于Django构建后端为前端提供支持。利用边缘检测对图像进行分割后，构建神经网络对海洋物体进行识别。

本项目构建yolo模型，从雷达回波信号图像中提取海藻，垃圾等海洋环境信息，建立海洋环境信息检测平台。

## 功能
**实现功能:** 检测平台的后端数据功能支持，绘制了简单的前端界面，实现了简单的边缘检测与识别算法。

 
**待整合功能:**基于yolo的海洋物体识别算法，前端界面待优化。

## 安装运行

**环境:**
- Python 3.6
- JavaScript
- Vue3.0
- Django2.0
- Bootstrap3.0
- Sqlite

**前端:** 
 ```markdown
  npm install
  ```

 ```markdown
  npm run start
  ```

**后端:**

 ```markdown
  python manage.py runserver 0.0.0.0:8000
  ```


## 输出结果
**前端:** 能够进行海洋雷达图像的展示，以及漂浮物的初步检测

**后端:** 能够为前端提供数据支持


 
