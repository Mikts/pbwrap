"""Contains the tests of the ppaw_formatter module"""
from ppaw import ppaw_formatter as ppaw_form
import json
import pytest
from datetime import datetime
from ppaw.ppaw_models import Paste


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
    xml_dic = ppaw_form.user_from_xml(raw_xml)
    json_dic = json.load(open('tests/dummyData/dummyUser.json'))

    assert xml_dic == json_dic


def test_paste_list_from_xml():
    raw_xml = open('tests/dummyData/dummyPasteList.xml').read()
    xml_paste_list = ppaw_form.paste_list_from_xml(raw_xml)
    json_dic = json.load(open('tests/dummyData/dummyPasteList.json'))
    json_paste_list = create_Paste_list(json_dic)

    assert len(xml_paste_list) == len(json_paste_list)
    for json_paste, xml_paste in zip(json_paste_list, xml_paste_list):
        assert json_paste.__cmp__(xml_paste) is True
