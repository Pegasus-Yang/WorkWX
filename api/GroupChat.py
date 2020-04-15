# Author:Pegasus-Yang
# Time:2020/4/13 上午10:03
import logging

import requests

from api.BaseApi import BaseApi
from api.Secret import Secret


class GroupChat(BaseApi):
    """企业微信外部联系人管理-客户群"""
    def __init__(self,corpsecret):
        self.token = Secret.get_token(corpsecret)

    def list(self, offset, limit,**kwargs):
        """获取客户群列表，对应接口/cgi-bin/externalcontact/groupchat/list"""
        url = 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/groupchat/list'
        params={'access_token': self.token}
        json={'offset': offset, 'limit': limit}
        return_response = requests.post(url, params=params, json=json)
        BaseApi.print_json(return_response.json())
        logging.info(return_response.json())
        return return_response.json()

    def get(self,chat_id,**kwargs):
        """获取客户群详情，对应接口/cgi-bin/externalcontact/groupchat/get"""
        url = 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/groupchat/get'
        params={'access_token': self.token}
        json={'chat_id': chat_id}
        return_response = requests.post(url, params=params, json=json)
        BaseApi.print_json(return_response.json())
        logging.info(return_response.json())
        return return_response.json()




