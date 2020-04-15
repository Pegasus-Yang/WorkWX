# Author:Pegasus-Yang
# Time:2020/4/13 上午10:03
import json

from Tools import Tools


class BaseApi:
    """基类，定义通用方法"""
    Tools.set_log()

    @classmethod
    def print_json(cls, response_json, indent=2):
        """将返回数据json格式化后打印到控制台方便查看"""
        print(json.dumps(response_json, indent=indent, ensure_ascii=False))


