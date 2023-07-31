import tushare as ts
import pandas as pd

pro = ts.pro_api('1db5469693ee4df4da5e095d90b3834a3c62526ee14b05a1d8fd5087')

# 沪深股票-基础数据-股票列表
StockList = pro.query('stock_basic', exchange='', list_status='L',
                 fields='ts_code,symbol,name,area,industry,market,list_date')
data2=pd.DataFrame(StockList,columns=['ts_code','name'])
print(data2['name'])

# 沪深股票-行情数据-每日指标
DailyIndex = pro.daily_basic(**{
    "ts_code": "",
    "trade_date": "",
    "start_date": "",
    "end_date": "",
    "limit": "",
    "offset": ""
}, fields=[
    "ts_code",
    "trade_date",
    "close",
    "turnover_rate",
    "turnover_rate_f",
    "volume_ratio",
    "pe",
    "pe_ttm",
    "pb",
    "ps",
    "ps_ttm",
    "dv_ratio",
    "dv_ttm",
    "total_share",
    "float_share",
    "free_share",
    "total_mv",
    "circ_mv"
])
print(DailyIndex)