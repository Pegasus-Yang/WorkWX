# Author:Pegasus-Yang
# Time:2020/4/13 下午5:26

import requests


def test_get_hook():
    def modify_response(r, *args, **kwargs):
        r.demo = 'demo content'
        return r

    r = requests.get('https://httpbin.testing-studio.com/get', params={'a': 1, 'b': 2, 'c': 'cccc'},
                     hooks={'response': [modify_response]})
    print(r.demo)


def errcode_translate(errcode):
    with open('../data/errcode') as errcode_file:
        for line in errcode_file:
            errcode_text = line.split('|')
            if errcode_text[1].strip() == str(errcode):
                print('错误码：{},错误说明：{}，排查方法：{}'.format(errcode_text[1].strip(), errcode_text[2].strip(),
                                                         errcode_text[3].strip()))


# errcode_translate('40017')

