from flask import Flask, request, render_template, session, redirect
#import numpy as np
import pandas as pd
#from replacexx import getdata


app = Flask(__name__)
df = pd.DataFrame({'A': [0, 1, 2, 3, 4],
                   'B': [5, 6, 7, 8, 9],
                   'C': ['a', 'b', 'c--', 'd', 'e']})
@app.route('/', methods=['GET'])
def html_table():
    
    return render_template('search.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)

@app.route('/',methods=['POST'])
def search():
    name = request.form['username'].strip()#strip去除前后空格
    if name:
        return send_post(name)
    else:
        return render_template('search.html', tips="请输入正确的双编号")
def send_post(name):
    df = pd.DataFrame({'A': [0, 1, 2, 3, 4],
                   'C': ['y', 'e', 's', 'good', 'luck要长长吃吃吃吃吃吃静静静静']})
    return render_template('search.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)
if __name__ == '__main__':
    app.run(host='0.0.0.0')
