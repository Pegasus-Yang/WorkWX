# Author:Pegasus-Yang
# Time:2020/4/13 上午11:29
import logging

import requests

from Tools import Tools
from api.BaseApi import BaseApi
from api.Secret import Secret


class Department(BaseApi):
    """企业微信通讯录管理-部门管理"""
    #todo 请求中不带token参数的发送
    def __init__(self, secret, is_debug=False, is_proxy=False):
        def encoding_change(response: requests.Response, *args, **kwargs):
            """hook方法修改返回数据的编码格式，解决返回数据中文乱码问题"""
            response.encoding = 'utf-8'
            return response

        self.is_debug = is_debug
        # 设定调试开关，打开的话会有返回数据格式化打印到控制台
        self.token = Secret.get_token(secret)
        # 获取token并保存到实例变量中，方便实例方法调用接口时使用
        session = requests.Session()
        # 预定义session并进行一些通用操作(比如添加token参数和hook方法)
        session.params = {'access_token': self.token}
        session.hooks = {'response': [encoding_change]}
        if is_proxy:  # 设定代理地址，如果打开代理开关就使用该代理地址，为了解决代理安全验证，同时关闭verify
            proxies = {
                'http': '127.0.0.1:8888',
                'https': '127.0.0.1:8888'
            }
            session.proxies = proxies
            session.verify = False
        self.session = session

    def create(self, access_token=None, **kwargs):
        """创建部门，对应接口/cgi-bin/department/create"""
        url = 'https://qyapi.weixin.qq.com/cgi-bin/department/create'
        if access_token is not None:
            return_response = self.session.post(url, json=kwargs, params={'access_token': access_token})
        else:
            return_response = self.session.post(url, json=kwargs)
        if self.is_debug:
            BaseApi.print_json(return_response.json())
            print(Tools.errcode_translate(return_response.json()['errcode']))
        logging.info(return_response.json())
        return return_response.json()

    def update(self, access_token=None, **kwargs):
        """更新部门，对应接口/cgi-bin/department/update"""
        url = 'https://qyapi.weixin.qq.com/cgi-bin/department/update'
        if access_token is not None:
            return_response = self.session.post(url, json=kwargs, params={'access_token': access_token})
        else:
            return_response = self.session.post(url, json=kwargs)
        if self.is_debug:
            BaseApi.print_json(return_response.json())
            print(Tools.errcode_translate(return_response.json()['errcode']))
        logging.info(return_response.json())
        return return_response.json()

    def delete(self, **kwargs):
        """删除部门，对应接口/cgi-bin/department/delete"""
        url = 'https://qyapi.weixin.qq.com/cgi-bin/department/delete'
        return_response = self.session.get(url, params=kwargs)
        if self.is_debug:
            BaseApi.print_json(return_response.json())
            print(Tools.errcode_translate(return_response.json()['errcode']))
        logging.info(return_response.json())
        return return_response.json()

    def list(self, **kwargs):
        """获取部门列表，对应接口/cgi-bin/department/list"""
        url = 'https://qyapi.weixin.qq.com/cgi-bin/department/list'
        return_response = self.session.get(url, params=kwargs)
        if self.is_debug:
            BaseApi.print_json(return_response.json())
            print(Tools.errcode_translate(return_response.json()['errcode']))
        logging.info(return_response.json())
        return return_response.json()
