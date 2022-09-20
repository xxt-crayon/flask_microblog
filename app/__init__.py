# 从flask包中导入Flask类
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# 将Flask类的实例赋值名为 app 的变量。这个实例成为app包的成员
app = Flask(__name__)
app.config.from_object(Config)

# print('等会谁（哪个包或模块）在使用我：', __name__)

db = SQLAlchemy(app)#数据库对象
migrate = Migrate(app, db)#迁移引擎对象

login = LoginManager(app)
login.login_view = 'login'

# 从app包中导入模块routes
from app import routes, models
