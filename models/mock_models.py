import datetime

from app import db


class Mock_interfaces(db.Model):
    '''
    mock接口模型
    service：服务名
    interface_name：接口名
    interface_path:接口url
    interface_mock_id:当前的mockid(m默认为0，为0则随机mock)
    is_delete:是否删除
    '''
    __tablename__="mcok_interfaces"
    id=db.Column(db.Integer,primary_key=True,autoincrement=True,comment='接口id')
    service=db.Column(db.String(50),nullable=False,comment='服务名')
    interface_name=db.Column(db.String(50),nullable=False,comment='接口名')
    interface_path=db.Column(db.String(300),nullable=False,comment='接口url')
    interface_mock_id=db.Column(db.String(20),default=0,comment='接口mock数据，为0为随机mock')
    is_delete=db.Column(db.Integer, default=0, comment='是否删除:0-正常；1-删除')
    create_time=db.Column(db.DateTime,default=datetime.datetime.now,comment='创建时间')
    update_time=db.Column(db.DateTime,default=datetime.datetime.now,onupdate=datetime.datetime.now,comment='更新时间')


class Mock_lists(db.Model):
    '''
    mock接口模型
    mock_name：mock名
    interface_id：接口id
    mock_data:mock数据
    is_delete:是否删除
    '''
    __tablename__="mock_lists"
    id=db.Column(db.Integer,primary_key=True,autoincrement=True,comment='mockid')
    mock_interface_id = db.Column(db.String(50), nullable=False, comment='mock接口id')
    mock_name = db.Column(db.String(20), default=0, comment='mock名称')
    mock_data = db.Column(db.String(3000), default=0, comment='mock数据')
    is_delete=db.Column(db.Integer, default=0, comment='是否删除:0-正常；1-删除')
    create_time = db.Column(db.DateTime, default=datetime.datetime.now, comment='创建时间')
    update_time = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now, comment='更新时间')

