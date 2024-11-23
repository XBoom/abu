# 支持 SQL
# 需要安装 sqlalchemy 库
from sqlalchemy import create_engine
import pandas as pd
# 创建数据库对象，SQLite 内存模式
engine = create_engine('sqlite:///memory:')
# 取出表名为 data 的表数据
with engine.connect() as conn:
    data = pd.read_sql_table('data', conn)

# 将数据写入
data.to_sql('data', engine, index=False)
data.to_sql('data_chunked', engine, index=False, chunksize=1000)
pd.read_sql_query('SELECT * FROM data', engine)
