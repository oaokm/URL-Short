import os
class Config:
    SECRET_KEY                      = 'a05789b2f4bd64ba5d2e6f6e60c08504ec69565edfe645440ac3be9de86b7808'
    SQLALCHEMY_DATABASE_URI         = 'sqlite:///url-short.db'
    SQLALCHEMY_TRACK_MODIFICATIONS  = True
    CKEDITOR_SERVE_LOCAL            = True
    # app.config['CKEDITOR_FILE_UPLOADER']           = 'main.upload'
