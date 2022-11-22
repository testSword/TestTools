#coding:utf-8
'''
定义响应代码格式
'''

class resp():

    @staticmethod
    def Resp(data,code="000000",message="请求成功"):
        resp={}
        resp["code"] = code
        resp["message"] = message
        resp["data"]=data
        return resp