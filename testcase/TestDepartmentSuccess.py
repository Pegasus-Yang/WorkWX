# Author:Pegasus-Yang
# Time:2020/4/14 下午9:50
import logging

import pytest
from jsonpath import jsonpath

from Tools import Tools
from api.Department import Department


class TestDepartmentSuccess:
    """部门管理接口测试用例-正案例"""
    secret = 'jKvsJatecQIU2sHrPMFCsqExNWYp3RCLIzuaj6JqyHY'
    create = [
        ('一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二', 'aaaabbbbccccddddaaaabbbbccccdddd', 5, 1000000, 33),
        ('测试排序', 'a', 5, 1000001, 34),
    ]
    update = [
        ('一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二', 'aaaabbbbccccddddaaaabbbbccccdddd', 1, 1000000, 5),
        ('1', 'b', 5, 1000001, 6),
    ]
    update_order = [
        (-1, 'Warning: wrong json format'),
        ('aaa', 'Warning: wrong json format'),
        (4294967296, 'Warning: wrong json format'),
    ]

    @classmethod
    def setup_class(cls):
        cls.department = Department(cls.secret, is_debug=True, is_proxy=False)

    def test_list_department_all(self):
        """获取部门列表接口(/cgi-bin/department/list)获取全部"""
        response_json = self.department.list()
        assert response_json['errcode'] == 0
        assert '测试大组1' in jsonpath(response_json, '$..department[*].name')

    def test_list_department_with_id(self):
        """获取部门列表接口(/cgi-bin/department/list)获取指定id"""
        response_json = self.department.list(id=8)
        assert response_json['errcode'] == 0
        assert '测试小组2' in jsonpath(response_json, '$..department[?(@.id==8)].name')

    def test_delete_department(self):
        """删除部门接口(/cgi-bin/department/delete)"""
        response_json = self.department.delete(id=11)
        assert response_json['errcode'] == 0
        assert 'deleted' in response_json['errmsg']

    def test_create_department_min_input(self):
        """创建部门接口(/cgi-bin/department/create)仅必输项-name最短"""
        response_json = self.department.create(name='1', parentid=5)
        assert response_json['errcode'] == 0
        assert 'created' in response_json['errmsg']

    # todo:order值大的部门排序靠前
    @pytest.mark.parametrize('name,name_en,parentid,order,id', create)
    def test_create_department_max_input(self, name, name_en, parentid, order, id):
        """创建部门接口(/cgi-bin/department/create)全部输入项"""
        response_json = self.department.create(name=name, name_en=name_en, parentid=parentid, order=order, id=id)
        assert response_json['errcode'] == 0
        assert 'created' in response_json['errmsg']
        assert response_json['id'] == id

    def test_update_department(self):
        """更新部门接口(/cgi-bin/department/update)仅必输项"""
        response_json = self.department.update(id=2)
        assert response_json['errcode'] == 0
        assert 'updated' in response_json['errmsg']

    # todo:order值大的部门排序靠前
    @pytest.mark.parametrize('name,name_en,parentid,order,id', update)
    def test_update_department_max_input(self, name, name_en, parentid, order, id):
        """更新部门接口(/cgi-bin/department/update)全部输入项"""
        response_json = self.department.update(name=name, name_en=name_en, parentid=parentid, order=order, id=id)
        assert response_json['errcode'] == 0
        assert 'updated' in response_json['errmsg']


    @pytest.mark.parametrize('order,errmsg', update_order)
    def test_update_department_order(self, order, errmsg):
        """更新部门接口(/cgi-bin/department/update)order非法（有Warning但成功）"""
        response_json = self.department.update(id=2, order=order)
        logging.info(Tools.errcode_translate(response_json['errcode']))
        assert response_json['errcode'] == 0
        assert errmsg in response_json['errmsg']

