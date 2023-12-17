from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_ckeditor import CKEditor
from flask_socketio import SocketIO
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from app.config import Config
from flask_admin import Admin
from flask import Flask


db                                   = SQLAlchemy()
# login_manager                        = LoginManager()
# login_manager.login_view             = 'authenticateBp.login'
# login_manager.login_message_category = 'info'
migrate                              = Migrate(db, render_as_batch=False)
bcrypt                               = Bcrypt()
ckeditor                             = CKEditor()
ADMIN                                = Admin()


def createApp(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    # from app.admin.routes import MyAdminIndexView

    db.init_app(app)
    # login_manager.init_app(app)
    bcrypt.init_app(app)
    # ckeditor.init_app(app)
    migrate.init_app(app, db)
    # ADMIN.init_app(app, index_view=MyAdminIndexView())

    from app.URL.routes import urlBp
    from app.errors.routes import errors
    from app.Web.routes import mainBp
    # app.context_processor(lambda: {'cartPrice': showCartPrice})
    # app.context_processor(lambda: {'Sum': sum})

    app.register_blueprint(urlBp)
    app.register_blueprint(errors)
    app.register_blueprint(mainBp)
    

    return app
