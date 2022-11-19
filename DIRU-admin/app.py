from flask import Flask,Response
from flask import request
from flask_cors import *
from flask import send_file
import os
import io

basedir = os.path.abspath(os.path.dirname(__file__)) + '/static/'
app = Flask(__name__)
CORS(app,supports_credentials=True)


@app.route('/func1',methods=['POST'])
def hello_world():
    # 这里接收图片二进制文件 注意 我这边的逻辑是下载到本地，如果是
    # 你们的模型的话,pic已经是图片的数据，不需要保存到本地
    pic = request.files['file']
    
    img = pic.read()
    pic.save(basedir + pic.filename)
    # 这里的逻辑是直接返回一个图片的二进制
    
    return send_file(io.BytesIO(img), mimetype='image/jpeg')


if __name__ == '__main__':
    app.run()
