# Author:Pegasus-Yang
# Time:2020/4/13 上午10:03
from api.GroupChat import GroupChat


class TestGroup:
    secret = 'fHWzletmNtiAt_ZUs_FE8gh8f_BfGzwVzp7z97yEky4'

    @classmethod
    def setup_class(cls):
        cls.group_chat = GroupChat(cls.secret)

    def test_group_chat_list(self):
        list_json = self.group_chat.list(offset=0,limit=100)
        assert 0 == list_json['errcode']
        return list_json

    def test_group_chat_get(self):
        list_json = self.test_group_chat_list()
        chat_id = list_json['group_chat_list'][0]['chat_id']
        get_json = self.group_chat.get(chat_id)
        assert 0 == get_json['errcode']
