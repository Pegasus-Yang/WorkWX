# Author:Pegasus-Yang
# Time:2020/4/13 上午10:03
import logging

import requests

from api.BaseApi import BaseApi


class Secret(BaseApi):
    """定义token相关方法"""
    _token = {}
    _token_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
    _corpid = 'ww814bcc991cacb79b'

    @classmethod
    def get_token(cls, secret):
        """获取token"""
        if secret not in cls._token.keys():
            cls._token[secret] = cls.request_token(secret)
        return cls._token[secret]

    @classmethod
    def request_token(cls, corpsecret):
        """向服务器发送请求获取token"""
        return_response = requests.get(cls._token_url, params={'corpid': cls._corpid, 'corpsecret': corpsecret})
        BaseApi.print_json(return_response.json())
        logging.info(return_response.json())
        assert return_response.json()['errcode'] == 0
        return return_response.json()['access_token']
