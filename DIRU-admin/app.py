from flask import Flask,make_response
from flask import request
from flask_cors import *
import os
import io
import base64


basedir = os.path.abspath(os.path.dirname(__file__)) + '/static/'
app = Flask(__name__)
CORS(app,supports_credentials=True)


@app.route('/func1',methods=['POST'])
def func1():
    # 这里接收图片二进制文件 注意 我这边的逻辑是下载到本地，如果是
    # 你们的模型的话,pic已经是图片的数据，不需要保存到本地
    pic = request.files['file']
    
    img = pic.read()
    # 这里就是正常的img，之前怎么弄得，这里就怎么弄
    img = base64.encodebytes(io.BytesIO(img).getvalue()).decode('ascii')
    
    
    # 返回一个图片的base64格式，必须是png格式，如果不是，format一下
    res = {}
    res['file'] = img
    # 这边的数据模型给出来
    res['data'] = ['car','person','bench']
    resp = make_response(res)
    return resp



@app.route('/filter',methods=['POST'])
def filter():
    # 这里带参数请求图片
    pic = request.files['file']
    # 这里是请求的参数
    arg = request.form['filter']
    
    img = pic.read()
    # 这里就是正常的img，之前怎么弄得，这里就怎么弄
    img = base64.encodebytes(io.BytesIO(img).getvalue()).decode('ascii')
    
    # 返回一个图片的base64格式，必须是png格式，如果不是，format一下
    res = {}
    res['file'] = img
    # 这边的数据模型给出来
    resp = make_response(res)
    return resp



if __name__ == '__main__':
    app.run()
