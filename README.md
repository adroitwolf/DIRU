# 使用方法

## 后端


```bash
# 进入后端文件夹后，安装后端相关依赖
cd ./diru-admin
pip install requirements.txt
```

配置完成环境之后，可以点击app.py文件的启动命令，或者在终端输入下面的命令
```bash
flask run --host 0.0.0.0
```


## 前端

### 配置环境

首先在电脑上安装npm yarn环境
```bash
# 安装完yarn之后进入diru-web文件夹,执行install命令，等待命令执行完成
cd ./diru-web
yarn install 
```

启动前端

```bash
yarn serve 
```