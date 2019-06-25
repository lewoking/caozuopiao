from flask import Flask, request, render_template
import pandas as pd
from sqlalchemy import create_engine


app = Flask(__name__)
conn = create_engine(
        'mysql+pymysql://root:usbw@127.0.0.1:3306/jmjkxx?charset=utf8')
sqlr = 'SELECT * FROM `操作` where id > (SELECT MAX(id) FROM `操作`) - 20'  # 默认结果
df = pd.read_sql(sqlr, conn)
conn.dispose()

@app.route('/', methods=['GET'])
def html_table():
    return render_template('search.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)

@app.route('/',methods=['POST'])
def search():
    name = request.form['username'].strip()#strip去除前后空格
    operate = request.form['operate']
    if name:
        return send_post(operate,name)
    else:
        return render_template('search.html', tips="请输入正确的双编号")
def send_post(operate,name):
    df = getdata(operate,name)
    return render_template('search.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)

def getdata(operate, username): 
    hf = operate  # 操作接口
    str_bh = username  # 查询输入接口
    sql = 'SELECT concat(`站名`,`名称2`) FROM `荆门开关表` WHERE `编号`=\'' + \
        str_bh + '\' limit 1 '  # 查询线路名称
    res = conn.execute(sql)
    row = res.fetchone()
    if row is None:
        error = (str_bh +'not in db',)
        df = pd.DataFrame(error)
    else:
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
        data = pd.DataFrame(list_cz) # list转pd
        data.rename(columns={0: '操作项目'}, inplace=True)  # 注意这里0和1都不是字符串
        pd.io.sql.to_sql(data, '操作', con=conn, if_exists='append',
                            index=False)  # 写入历史数据库
        df = pd.read_sql(sqlr, conn)
    conn.dispose()
    return df

if __name__ == '__main__':
    app.run(host='0.0.0.0')
