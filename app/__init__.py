# 从flask包中导入Flask类
from flask import Flask
from config import Config

# 将Flask类的实例赋值名为 app 的变量。这个实例成为app包的成员
app = Flask(__name__)
app.config.from_object(Config)

# print('等会谁（哪个包或模块）在使用我：', __name__)


# 从app包中导入模块routes
from app import routes
