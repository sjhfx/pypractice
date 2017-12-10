# -*- coding: utf-8 -*-
# 作者：数据化分析
# 版本：1.0

# 导入pyecharts中的饼图
from pyecharts import Pie

# 定义饼图的标题、副标题和位置
pie = Pie(
    '数据化分析目前对主要技术的关注度',
    '作者：Jimmy',
    title_pos='center',
)
# 定义名称、属性和值
da = {
    'name': '',
    'attr': ['数据分析', ''],
    'value': [90, 10],
    'redius': [30, 22],
    'center': [30, 30],
    'rosetype': None,
    'label_pos': 'center',
    'is_label_show': True,
    'label_text_color': None,
    'legend_top': 'bottom'
}
dm = {
    'name': '',
    'attr': ['数据挖掘', ''],
    'value': [30, 70],
    'redius': [30, 22],
    'center': [50, 30],
    'rosetype': None,
    'label_pos': 'center',
    'is_label_show': True,
    'label_text_color': None,
    'legend_top': 'bottom'
}
excel = {
    'name': '',
    'attr': ['Excel', ''],
    'value': [70, 30],
    'redius': [30, 22],
    'center': [70, 30],
    'rosetype': None,
    'label_pos': 'center',
    'is_label_show': True,
    'label_text_color': None,
    'legend_top': 'bottom'
}
python = {
    'name': '',
    'attr': ['Python编程', ''],
    'value': [95, 5],
    'redius': [36, 28],
    'center': [40, 70],
    'rosetype': None,
    'label_pos': 'center',
    'is_label_show': True,
    'label_text_color': None,
    'legend_top': 'bottom'
}
r = {
    'name': '',
    'attr': ['R语言', ''],
    'value': [10, 90],
    'redius': [36, 28],
    'center': [60, 70],
    'rosetype': None,
    'label_pos': 'center',
    'is_label_show': True,
    'label_text_color': None,
    'legend_top': 'bottom'
}
# 技术列表
technologies = [da, dm, excel, python, r]
# 循环添加饼图
for technology in technologies:
    pie.add(
        technology['name'],
        technology['attr'],
        technology['value'],
        technology['redius'],
        technology['center'],
        technology['rosetype'],
        label_pos=technology['label_pos'],
        is_label_show=technology['is_label_show'],
        label_text_color=technology['label_text_color'],
        legend_top=technology['legend_top'],
    )
pie.render()
