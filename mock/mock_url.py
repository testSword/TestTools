from flask import Blueprint

from mock.mock_interface import select_mock_interface

mock_blue = Blueprint('mock', __name__)
# 定义蓝图路径及请求方法和请求返回逻辑

mock_blue.add_url_rule("/select_interface",view_func=select_mock_interface,methods=['POST'])
mock_blue.add_url_rule("/add_interface", view_func=select_mock_interface, methods=['POST'])
mock_blue.add_url_rule("/update_interface", view_func=select_mock_interface, methods=['POST'])
mock_blue.add_url_rule("/delete_interface", view_func=select_mock_interface, methods=['POST'])
mock_blue.add_url_rule("/add_mockdata", view_func=select_mock_interface, methods=['POST'])
mock_blue.add_url_rule("/edit_mockdata", view_func=select_mock_interface, methods=['POST'])
mock_blue.add_url_rule("/delete_mockdata", view_func=select_mock_interface, methods=['POST'])
mock_blue.add_url_rule("/shuffle_mockdata", view_func=select_mock_interface, methods=['POST'])
mock_blue.add_url_rule("/confirm_mockdata", view_func=select_mock_interface, methods=['POST'])

@mock_blue.route('/get', methods=['get', 'post'])
def getproduct():
    return 'product'

@mock_blue.route('/search', methods=['get', 'post'])
def searchproduct():
    return 'search'