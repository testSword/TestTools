# 数据库配置
HOSTNAME="127.0.0.1"
DATABASE='testApp'
USERNAME='root'
PASSWORD="12345678"
DB_URI="mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}/{db}?charset=utf8".format(USERNAME=USERNAME,PASSWORD=PASSWORD,
                                                                                       HOSTNAME=HOSTNAME,db=DATABASE)
#统一资源标示符
SQLALCHEMY_DATABASE_URI=DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS=False
SQLALCHEMY_ECHO = True
# mysql+pymysql://root:12345678@127.0.0.1:3306/testApp?charset=utf8