from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import config
from mock.mock_url import mock_blue



app = Flask(__name__)
# 增加配置，支持中文显示
app.config['JSON_AS_ASCII'] = False

#蓝图
app.register_blueprint(mock_blue, url_prefix='/mock')

# 注册config文件里的配置到flask中---数据库配置
app.config.from_object(config)
db=SQLAlchemy(app)



@app.route('/')
def hello_world():
    return 'Hello World!'


# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=6869, debug=True)
