import pandas as pd

test_file="team.xlsx"

df = pd.read_excel(test_file)
#print(df.head())    # 默认显示前5行
#print(df.tail())    # 默认显示后5行
#print(df.columns)    # 列名 Index(['name', 'team', 'Q1', 'Q2', 'Q3', 'Q4'], dtype='object')
#print(df.shape)     # 行数和列数 (10, 6)
#print(df.info())    # 查看索引，数据类型和内存信息
#print(df.describe())    # 快速统计汇总 总数（count）​、平均数（mean）​、标准差（std）​、最小值（min）​、四分位数和最大值（max）​：
#print(df['team'].value_counts())    # 查看某列有多少个不同值，并计算每个不同值有在该列中有多少重复值

# 选择多行
#print(df[2:5])
# 选择多列
#print(df[['name', 'team']])
#print(df.loc[2:5, ['name', 'team']])    # 选择指定行和列