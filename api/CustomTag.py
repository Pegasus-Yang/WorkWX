# Author:Pegasus-Yang
# Time:2020/4/19 上午10:24
import logging

import requests

from Tools import Tools
from api.BaseApi import BaseApi
from api.Secret import Secret


class CustomTag(BaseApi):

    def __init__(self, secret, is_debug=False):
        self.token = Secret.get_token(secret)
        self.is_debug = is_debug

    def get_tag(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list'
        request_json = {'tag_id': []}
        return_response = requests.post(
            url,
            params={'access_token': self.token},
            json=request_json,
        )
        if self.is_debug:
            BaseApi.print_json(return_response.json())
            print(Tools.errcode_translate(return_response.json()['errcode']))
        logging.info(return_response.json())
        return return_response.json()

    def add_tag(self):
        pass

    def update_tag(self):
        pass

    def delete_tag(self):
        pass
