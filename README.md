介绍
数据挖掘实战代码仓库

问题说明
每天早晨立会, 同步开发进度, 晚上提交日报
每个人都要做, 特征工程相关思路可以一起讨论
每人在自己的分支上开发, 每天提交代码
最后一天下午3点开始汇报,各组准备PPT或者文档（格式，模板不限）, 时间控制在10分钟左右, 有3分钟左右提问环节
目录说明
code python代码最终都放到这个文件夹里
notebook 存notebook文件
src 存放python源文件
data 存放数据 !! 注意数据不要提交到仓库!!
PD 项目文档, 开发计划, 特征工程相关的思路, 日报都放到里面
memo bug记录 开发中遇到的问题
只需要提交项目文档, ipynb文件 , py文件, 其它文件不要提交
建议的项目目录结构
my_project/
│
├── data/
│   ├── raw/    存放原始数据
│   └── processed/处理过的数据
│
├── notebooks/
│
├── src/
│   ├── data/
│   │   ├── __init__.py
│   │   └── data_preparation.py 数据处理
│   ├── features/
│   │   ├── __init__.py
│   │   └── feature_engineering.py  特征工程
│   ├── models/
│   │   ├── __init__.py
│   │   └── train_model.py    模型训练
│   │   
│   └── visualization/ 
│       ├── __init__.py
│       └── visualize.py    可视化(如果有)
│
├── tests/   测试文件
│
├── models/  保存模型的文件夹
│
└── reports/   模型报告 (如果有)
    └── figures/
