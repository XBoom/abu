# -*- encoding:utf-8 -*-
#这是 Python 2 中的一个导入语句，
# 用于确保使用绝对导入，避免相对导入可能带来的混淆。
# 在 Python 3 中，绝对导入是默认的
from __future__ import absolute_import

# 从当前包中的不同模块导入所有公共对象，不推荐使用 * 导入，可能导致命名空间污染
from .CoreBu import *
from .CheckBu import *
from .FactorSellBu import *
from .FactorBuyBu import *
from .AlphaBu import *
from .BetaBu import *
from .DLBu import *
from .IndicatorBu import *
from .MLBu import *
from .MetricsBu import *
from .PickStockBu import *
from .SlippageBu import *
from .UtilBu import *
from .TLineBu import *
from .TradeBu import *
from .UmpBu import *
from .MarketBu import *
from .SimilarBu import *
from .WidgetBu import *

'''
在 module1.py 中，使用 from .WidgetBu import * 可以导入 WidgetBu.py 中的 widget_function 函数。
然而，使用 from .WidgetBu import * 这种导入方式有一些缺点：
它可能会导致命名空间污染，因为你导入了 WidgetBu 模块中的所有公共对象，可能会引入一些你并不需要的名称。
它可能会使代码的可读性变差，因为不清楚具体导入了哪些对象
'''

# 定义使用 from module import * 时应该导入的对象列表，控制模块的公共接口
__all__ = ['AlphaBu', 'BetaBu', 'CheckBu', 'UmpBu', 'FactorSellBu', 'FactorSell', 'IndicatorBu', 'MarketBu', 'UtilBu',
           'SimilarBu', 'MetricsBu', 'SlippageBu', 'PickStockBu', 'CoreBu', 'TLineBu',
           'MLBu', 'DLBu', 'TradeBu', 'WidgetBu']

__version__ = '0.4.0'
