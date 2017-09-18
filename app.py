# -*- coding: utf-8 -*-


""" 
@author: W@I@S@E 
@contact: wisecsj@gmail.com 
@site: http://hfutoyj.cn/ 
@file: app.py 
@time: 2017/9/8 9:01 
"""

from flask import Flask, render_template, jsonify, request
from utils import wise

app = Flask(__name__)


def format(text):
    d = dict()
    r = text.split('\n')
    for t in r:
        if t is not '':
            l = t.split()
            d[l[0]] = l[1:]
    return d


def output(d):
    s = ''
    for k, v in d.items():
        str = k + '->' + '|'.join(v)
        s += str +'\n'
    return s


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/eliminate', methods=['POST'])
def eliminate():
    G = request.json.get('G', None)
    d = format(G)
    print(d)
    result = wise(d)
    finally_result = output(result)
    return jsonify(G_r=finally_result)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
