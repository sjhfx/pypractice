# -*- coding: utf-8 -*-
# 作者：数据化分析
# 微信公众号：isjhfx
# 版本：1.0

import matplotlib.pyplot as plt
import seaborn as sns

# 解决seaborn数据集导入报错的问题
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 数据准备
data = sns.load_dataset('car_crashes')
print(data.head(10))

# 用 seaborn 探索成对关系
sns.pairplot(data)

# 用 seaborn 画散点图
sns.jointplot(x='total', y='speeding', data=data, kind='scatter')

# 用 seaborn 画核密度图
sns.jointplot(x='total', y='speeding', data=data, kind='kde')

# 用 seaborn 画 Hexbin 图
sns.jointplot(x='total', y='speeding', data=data, kind='hex')

plt.show()