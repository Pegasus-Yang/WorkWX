# Author:Pegasus-Yang
# Time:2020/4/13 上午11:49
import logging

import pytest

from Tools import Tools
from api.Department import Department


# todo:不传token的案例
class TestDepartmentFail:
    """部门管理接口测试用例-反案例"""
    secret = 'jKvsJatecQIU2sHrPMFCsqExNWYp3RCLIzuaj6JqyHY'
    token_fail = [
        ('', 41001, 'access_token missing'),
        ('wrong token', 40014, 'invalid access_token'),
    ]
    del_id_fail = [
        (999, 60123, 'invalid party id'),
        (10, 60005, 'department contains user'),
        (7, 60006, 'department contains sub-department'),
        ('', 40058, 'invalid Request Parameter')
    ]
    name_fail = [
        ('', 40058, 'invalid Request Parameter'),
        ('测试创建1', 60008, 'department existed'),
        ('一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三', 60001, 'department invalid length'),
        ('?', 60009, 'include invalid char'),
        ('\\', 60009, 'include invalid char'),
        (':', 60009, 'include invalid char'),
        # ('"', 60009, 'include invalid char'), # 成功？？
        ('<', 60009, 'include invalid char'),
        ('>', 60009, 'include invalid char'),
        # ('/', 60009, 'include invalid char'), # 成功？？
    ]
    name_en_fail = [
        ('', 60001, 'department invalid length'),
        ('测试创建1', 60008, 'department existed'),
        ('aabbccddaabbccddaabbccddaabbccdda', 40058, 'invalid Request Parameter'),
        ('?', 60009, 'include invalid char'),
        ('\\', 60009, 'include invalid char'),
        (':', 60009, 'include invalid char'),
        # ('"', 60009, 'include invalid char'), # 成功？？
        ('<', 60009, 'include invalid char'),
        ('>', 60009, 'include invalid char'),
        # ('/', 60009, 'include invalid char'), # 成功？？
    ]
    create_parentid_fail = [
        ('', 60009, 'invalid char'),
        (999, 60004, 'parent department not found'),
    ]
    order_fail = [
        (-1, 60009, 'invalid char'),
        ('aaa', 60009, 'invalid char'),
        (4294967296, 60009, 'invalid char'),
    ]
    create_id_fail = [
        (0, 60123, 'invalid party id'),
        ('', 60009, 'include invalid char'),
        (111122223333444455556666777788889, 60009, 'include invalid char'),
    ]
    update_parentid_fail = [
        ('', 60124, 'invalid parent party id'),
        (999, 60124, 'invalid parent party id'),
        (2,60008,'department existed'),
    ]

    @classmethod
    def setup_class(cls):
        cls.department = Department(cls.secret, is_debug=True, is_proxy=False)

    @pytest.mark.parametrize('token,errcode,errmsg', token_fail)
    def test_list_department_token_fail(self, token, errcode, errmsg):
        """获取部门列表接口(/cgi-bin/department/list)token错误"""
        response_json = self.department.list(access_token=token)
        logging.info(Tools.errcode_translate(response_json['errcode']))
        assert response_json['errcode'] == errcode
        assert errmsg in response_json['errmsg']

    def test_list_department_id_fail(self):
        """获取部门列表接口(/cgi-bin/department/list)id错误"""
        response_json = self.department.list(id=999)
        logging.info(Tools.errcode_translate(response_json['errcode']))
        assert response_json['errcode'] == 60123
        assert 'invalid party id' in response_json['errmsg']

    @pytest.mark.parametrize('token,errcode,errmsg', token_fail)
    def test_delete_department_token_fail(self, token, errcode, errmsg):
        """删除部门接口(/cgi-bin/department/delete)token错误"""
        response_json = self.department.delete(id=11, access_token=token)
        logging.info(Tools.errcode_translate(response_json['errcode']))
        assert response_json['errcode'] == errcode
        assert errmsg in response_json['errmsg']

    @pytest.mark.parametrize('id,errcode,errmsg', del_id_fail)
    def test_delete_department_id_fail(self, id, errcode, errmsg):
        """删除部门接口(/cgi-bin/department/delete)id错误"""
        response_json = self.department.delete(id=id)
        logging.info(Tools.errcode_translate(response_json['errcode']))
        assert response_json['errcode'] == errcode
        assert errmsg in response_json['errmsg']

    def test_delete_department_without_id_fail(self):
        """删除部门接口(/cgi-bin/department/delete)不传id"""
        response_json = self.department.delete()
        logging.info(Tools.errcode_translate(response_json['errcode']))
        assert response_json['errcode'] == 40058
        assert 'invalid Request Parameter' in response_json['errmsg']

    @pytest.mark.parametrize('token,errcode,errmsg', token_fail)
    def test_create_department_token_fail(self, token, errcode, errmsg):
        """创建部门接口(/cgi-bin/department/create)token错误"""
        response_json = self.department.create(name='测试创建1', parentid=2, access_token=token)
        logging.info(Tools.errcode_translate(response_json['errcode']))
        assert response_json['errcode'] == errcode
        assert errmsg in response_json['errmsg']

    @pytest.mark.parametrize('name,errcode,errmsg', name_fail)
    def test_create_department_name_fail(self, name, errcode, errmsg):
        """创建部门接口(/cgi-bin/department/create)name错误"""
        response_json = self.department.create(name=name, parentid=2)
        logging.info(Tools.errcode_translate(response_json['errcode']))
        assert response_json['errcode'] == errcode
        assert errmsg in response_json['errmsg']

    def test_create_department_without_name_fail(self):
        """创建部门接口(/cgi-bin/department/create)不传name"""
        response_json = self.department.create(parentid=2)
        logging.info(Tools.errcode_translate(response_json['errcode']))
        assert response_json['errcode'] == 60001
        assert 'department invalid length' in response_json['errmsg']

    @pytest.mark.parametrize('name_en,errcode,errmsg', name_en_fail)
    def test_create_department_name_en_fail(self, name_en, errcode, errmsg):
        """创建部门接口(/cgi-bin/department/create)name_en错误"""
        response_json = self.department.create(name='测试创建002', name_en=name_en, parentid=2)
        logging.info(Tools.errcode_translate(response_json['errcode']))
        assert response_json['errcode'] == errcode
        assert errmsg in response_json['errmsg']

    @pytest.mark.parametrize('parentid,errcode,errmsg', create_parentid_fail)
    def test_create_department_parentid_fail(self, parentid, errcode, errmsg):
        """创建部门接口(/cgi-bin/department/create)parentid错误"""
        response_json = self.department.create(name='测试创建002', parentid=parentid)
        logging.info(Tools.errcode_translate(response_json['errcode']))
        assert response_json['errcode'] == errcode
        assert errmsg in response_json['errmsg']

    def test_create_department_without_parentid_fail(self):
        """创建部门接口(/cgi-bin/department/create)不传parentid"""
        response_json = self.department.create(name='测试创建002')
        logging.info(Tools.errcode_translate(response_json['errcode']))
        assert response_json['errcode'] == 60004
        assert 'parent department not found' in response_json['errmsg']

    @pytest.mark.parametrize('order,errcode,errmsg', order_fail)
    def test_create_department_order_fail(self, order, errcode, errmsg):
        """创建部门接口(/cgi-bin/department/create)order错误"""
        response_json = self.department.create(name='测试创建004', parentid=2, order=order)
        logging.info(Tools.errcode_translate(response_json['errcode']))
        assert response_json['errcode'] == errcode
        assert errmsg in response_json['errmsg']

    @pytest.mark.parametrize('id,errcode,errmsg', create_id_fail)
    def test_create_department_id_fail(self, id, errcode, errmsg):
        """创建部门接口(/cgi-bin/department/create)id错误"""
        response_json = self.department.create(name='测试创建004', parentid=2, id=id)
        logging.info(Tools.errcode_translate(response_json['errcode']))
        assert response_json['errcode'] == errcode
        assert errmsg in response_json['errmsg']

    @pytest.mark.parametrize('token,errcode,errmsg', token_fail)
    def test_update_department_token_fail(self, token, errcode, errmsg):
        """更新部门接口(/cgi-bin/department/update)token错误"""
        response_json = self.department.update(id=1, access_token=token)
        logging.info(Tools.errcode_translate(response_json['errcode']))
        assert response_json['errcode'] == errcode
        assert errmsg in response_json['errmsg']

    def test_update_department_without_id_fail(self):
        """更新部门接口(/cgi-bin/department/update)不传id"""
        response_json = self.department.update()
        logging.info(Tools.errcode_translate(response_json['errcode']))
        assert response_json['errcode'] == 60003
        assert 'department not found' in response_json['errmsg']

    def test_update_department_id_fail(self):
        """更新部门接口(/cgi-bin/department/update)id错误"""
        response_json = self.department.update(id=999)
        logging.info(Tools.errcode_translate(response_json['errcode']))
        assert response_json['errcode'] == 60003
        assert 'department not found' in response_json['errmsg']

    @pytest.mark.parametrize('name,errcode,errmsg', name_fail)
    def test_update_department_name_fail(self, name, errcode, errmsg):
        """更新部门接口(/cgi-bin/department/update)name错误"""
        response_json = self.department.update(name=name, id=2)
        logging.info(Tools.errcode_translate(response_json['errcode']))
        assert response_json['errcode'] == errcode
        assert errmsg in response_json['errmsg']

    @pytest.mark.parametrize('name_en,errcode,errmsg', name_en_fail)
    def test_update_department_name_en_fail(self, name_en, errcode, errmsg):
        """更新部门接口(/cgi-bin/department/update)name_en错误"""
        response_json = self.department.update(name_en=name_en, id=2)
        logging.info(Tools.errcode_translate(response_json['errcode']))
        assert response_json['errcode'] == errcode
        assert errmsg in response_json['errmsg']

    @pytest.mark.parametrize('parentid,errcode,errmsg', update_parentid_fail)
    def test_update_department_parentid_fail(self, parentid, errcode, errmsg):
        """更新部门接口(/cgi-bin/department/update)parentid错误"""
        response_json = self.department.update(id=15, parentid=parentid)
        logging.info(Tools.errcode_translate(response_json['errcode']))
        assert response_json['errcode'] == errcode
        assert errmsg in response_json['errmsg']



