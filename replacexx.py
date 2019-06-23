# -*- encoding: utf-8 -*-
'''
@File    :   replacexx.py
@Time    :   2019/05/10 22:28:11
@Author  :   guozi
@Version :   1.0
@WebSite    :  github.com/lewoking
'''
import pandas as pd

from sqlalchemy import create_engine

# here put the import lib
def getdata(df)：
    conn = create_engine('mysql+pymysql://root:usbw@172.0.0.1:3307/jmjkxx?charset=utf8')
    hf = operate
    str_bh = username
    sql = 'SELECT obj_dispidx as ' #查询线路名称
    sqlr = ''      #默认结果
    
    df = pd.read_sql(sql, conn)
    pd.io.sql.to_sql(df, 'tzqk', con=conn, if_exists='append', index=False) #写入历史数据库

    str_zmc = '220kV枣山变掇枣线'

    list_bzh = ('合上××变××线××断路器',
                '检查××变××线××断路器监控指示为合位',
                '检查××变××线××断路器电流指示正常',
                '检查××变××线功率正常。')
    list_bzf = ('断开××变××线××断路器',
                '检查××变××线××断路器监控指示为分位',
                '检查××变××线××断路器电流指示为零',
                '检查××变××线功率为零。')
    if hf == '合上':
        list_cz = [c.replace('××变××线', str_zmc) for c in list_bzh]
    elif hf == '断开':
        list_cz = [c.replace('××变××线', str_zmc) for c in list_bzf]
    else:
        print('error')
    list_cz = [c.replace('××', str_bh) for c in list_cz]
    print(list_cz)
    #list转pd
    data=DataFrame(list_cz)
    data=data.T  #转置之后得到想要的结果
    data.rename(columns={0:'a',1:'b'},inplace=True)  #注意这里0和1都不是字符串
    
    df = pd.read_sql(sqlr, conn1)
    conn.dispose()