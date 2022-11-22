#coding:utf-8
'''
1、提供接口查询能力
2、提供mock接口添加能力
3、提供mock接口更新能力
4、提供mock接口删除能力
5、提供mock数据添加能力
6、提供mock数据编辑能力
7、提供mock数据删除能力
8、提供mock数据打散（随机能力）
9.批量导入接口

'''
import logging

from flask import request, jsonify

from common.http_resp import resp


def select_mock_interface():
    reqdata=request.json
    #参数：查询域里的查询字段；
    #入参：查询字段，分页条数。如果不传，默认查10条，排序为按创建时间倒叙
    interface_lists=[]
    '''
    {
        "service_name":"",
        "interface_name":"",
        "interface_path":"",
        "page":"",
        "page_num":"",
    }
    '''
    if "page" in reqdata.keys() and "page_num" in reqdata.keys():
        page=reqdata["page"]
        page_num=reqdata["page_num"]
    else:
        page = 1
        page_num = 10
    try:
        # 如果传过来的字段包含"service_name"
        if "service_name" in reqdata.keys():
            from models import Mock_interfaces
            interface_list=Mock_interfaces.query.filter(Mock_interfaces.service == reqdata["service_name"]).offset(
                (page-1)*page_num).limit(page_num)

        # 如果传过来的字段包含"interface_name"
        if "interface_name" in reqdata.keys():
            print("====")
            print("interface_name")
            interface_list = Mock_interfaces.query.filter(Mock_interfaces.interface_name == reqdata["interface_name"]).offset(
                (page-1)*page_num).limit(page_num)

        # 如果传过来的字段包含"interface_path"
        if "interface_path" in reqdata.keys():
            print("interface_path")
            interface_list = Mock_interfaces.query.filter(Mock_interfaces.interface_path == reqdata["interface_path"]).offset(
                (page-1)*page_num).limit(page_num)

        for item in interface_list:
            service_name=item.service
            interface_name= item.interface_name
            interface_path=item.interface_path
            interface={
                "service_name":service_name,
                "interface_name": interface_name,
                "interface_path": interface_path,
            }
            interface_lists.append(interface)

        res=resp.Resp(data=interface_lists)
        logging.INFO(res)
        return res

    except Exception as e:
        return jsonify({"message":"系统异常","code":500})


# 1、提供mock接口添加能力,注册接口
def add_mock_interface():
    reqdata=request.json

    return "reqdata"


# 1、提供mock接口更新能力
def update_mock_interface():
    reqdata=request.json
    return "reqdata"


# 1、、提供mock接口删除能力

def delete_mock_interface():
    reqdata=request.json

    return "reqdata"


# 5、提供mock数据添加能力

def add_mock_data():
    reqdata=request.json

    return "reqdata"


# # # 6、提供mock数据编辑能力

def edit_mock_data():
    reqdata=request.json

    return "reqdata"


# # # 7、提供mock数据删除能力
def delete_mock_data():
    reqdata=request.json

    return "reqdata"

# # # 8、提供mock数据打散（随机能力）
def shuffle_mock_data():
    reqdata=request.json
    return "reqdata"


# # # 8、确认mock数据数据（指定mock数据）
def shuffle_mock_data():
    '''
    params:接口path、mockdata编号（yaml文件里的data的index）；
    :return:
    '''
    reqdata=request.json
    return "reqdata"

