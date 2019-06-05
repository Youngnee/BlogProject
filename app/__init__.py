# 主要工作:初始化配置和实例
# 1. 构建Flask的各种实例以及各种配置
# 2. 创建SQLAlchemy的应用实例

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    """
    创建Flask程序实例
    :return: 返回创建好的程序实例
    """
    app = Flask(__name__)
    # 完成各种配置
    app.config["DEBUG"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@localhost:3306/blog"
    app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = "suibianxie"
    # 关联app与创建好的db实例
    db.init_app(app)

    # 将topic蓝图程序与app关联到一起
    from .topic import topic as topic_blueprint
    app.register_blueprint(topic_blueprint)

    # 将users蓝图程序与app关联到一起
    from .users import users as users_bulueprint
    app.register_blueprint(users_bulueprint)

    # 返回创建好的程序实例
    return app
