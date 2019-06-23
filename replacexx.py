# -*- encoding: utf-8 -*-
'''
@File    :   replacexx.py
@Time    :   2019/05/10 22:28:11
@Author  :   guozi
@Version :   1.0
@WebSite    :  github.com/lewoking
'''
import pandas
# here put the import lib
def getdata(df)：
    hf = operate
    str_bh = username
    


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
