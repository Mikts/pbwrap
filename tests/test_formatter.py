"""Contains the tests of the formatter module"""
from pbwrap.pbwrap import Pastebin
import pbwrap.formatter as formatter
from pbwrap.models import Paste
import json
import pytest
import re


@pytest.fixture
def create_Paste_list(json_dic):
    json_paste_list = list()
    for i in json_dic['paste']:
        temp_dict = dict()
        for k, v in i.items():
            temp_dict[k] = v

        json_paste_list.append(Paste(temp_dict))
    return json_paste_list


def test_user_from_xml():
    raw_xml = open('tests/dummyData/dummyUser.xml').read()
    xml_dic = formatter.user_from_xml(raw_xml)
    json_dic = json.load(open('tests/dummyData/dummyUser.json'))

    assert xml_dic == json_dic


def test_paste_list_from_xml():
    raw_xml = open('tests/dummyData/dummyPasteList.xml').read()
    xml_paste_list = formatter.paste_list_from_xml(raw_xml)
    json_dic = json.load(open('tests/dummyData/dummyPasteList.json'))
    json_paste_list = create_Paste_list(json_dic)

    assert len(xml_paste_list) == len(json_paste_list)
    for json_paste, xml_paste in zip(json_paste_list, xml_paste_list):
        assert json_paste.__cmp__(xml_paste) is True


def test_archive_url_format():
    pb = Pastebin()
    archive_list = pb.get_archive()

    for link in archive_list:
        assert re.match(r'https://pastebin\.com/[a-zA-Z0-9]{8}', link).group() == link
