import os

from flask import Flask, render_template
import pymysql
from flask_sqlalchemy import SQLAlchemy
# 创建flask对象
app = Flask(__name__)
# 配置
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:3306/movie'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config["SECRET_KEY"] = '350da38cba54418aaf31848211912aab'
app.config['UP_DIR'] = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static/uploads/')



# 开启debug模式
app.debug = True
db = SQLAlchemy(app)

from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

# 注册蓝图
app.register_blueprint(home_blueprint)
# url_prefix用来区分路由
app.register_blueprint(admin_blueprint, url_prefix='/admin')


# 定义404页面
@app.errorhandler(404)
def page_not_found(error):
    return render_template('home/404.html'), 404
