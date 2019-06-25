# -*- encoding: utf-8 -*-
'''
@File    :   replacexx.py
@Time    :   2019/05/10 22:28:11
@Author  :   guozi
@Version :   1.0
@WebSite    :  github.com/lewoking
'''
import pandas as pd
import sys
from sqlalchemy import create_engine

# here put the import lib


def getdata(operate, username): 
    conn = create_engine(
        'mysql+pymysql://root:usbw@127.0.0.1:3306/jmjkxx?charset=utf8')
    hf = operate  # 操作接口
    str_bh = 'username'  # 查询输入接口
    sql = 'SELECT concat(`站名`,`名称2`) FROM `荆门开关表` WHERE `编号`=\'' + \
        str_bh + '\' limit 1 '  # 查询线路名称
    sqlr = 'SELECT * FROM `操作` limit 0,20'  # 默认结果
    res = conn.execute(sql)
    row = res.fetchone()

    str_zmc = row[0]  # 获取查询结果

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
    # list转pd
    data = pd.DataFrame(list_cz)
    data.rename(columns={0: '操作项目'}, inplace=True)  # 注意这里0和1都不是字符串

    pd.io.sql.to_sql(data, '操作', con=conn, if_exists='append',
                        index=False)  # 写入历史数据库

    df = pd.read_sql(sqlr, conn)
    conn.dispose()
    return df
