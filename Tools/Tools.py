# Author:Pegasus-Yang
# Time:2020/4/14 上午9:26
import logging


def errcode_translate(errcode) -> str:
    """将返回信息中的errcode进行翻译，方便查找或者对照"""
    # todo 如果以后查询次数多了可以将文件存入变量处理以免每次查询都要进行文件读取
    with open('../data/errcode') as errcode_file:
        for line in errcode_file:
            errcode_text = line.split('|')
            if errcode_text[1].strip() == str(errcode):
                return '错误码：{},错误说明：{}，排查方法：{}'.format(errcode_text[1].strip(), errcode_text[2].strip(),
                                                       errcode_text[3].strip())


def set_log():
    log_file = '../logs/WxWork.log'
    log_format_string = '%(asctime)s %(levelname)s %(filename)s/%(funcName)s %(message)s '
    log_date_string = '%Y-%m-%d %H:%M:%S'
    logging.basicConfig(level=logging.INFO, filename=log_file, format=log_format_string, datefmt=log_date_string)

