# Author:Pegasus-Yang
# Time:2020/4/19 上午10:31
from api.CustomTag import CustomTag


class TestCustomTag:
    secret = 'fHWzletmNtiAt_ZUs_FE8gh8f_BfGzwVzp7z97yEky4'

    @classmethod
    def setup_class(cls):
        cls.custom_tag = CustomTag(cls.secret, is_debug=True)

    def test_get_tag(self):
        return_json = self.custom_tag.get_tag()
        self.custom_tag.print_json(return_json)
