"""Contains the tests of the formatter module"""
import json
import re

import pytest

from pbwrap import formatter
from pbwrap import Pastebin
from pbwrap.models import Paste, User


@pytest.fixture
def create_paste_list(json_dic):
    """Return a list of Paste objects from a json dictionary"""
    json_paste_list = list()
    for i in json_dic["paste"]:
        temp_dict = dict()
        for k, v in i.items():
            temp_dict[k] = v

        json_paste_list.append(Paste(temp_dict))
    return json_paste_list


def test_user_from_xml():
    """Test the user_from_xml function"""
    raw_xml = open("tests/dummyData/dummyUser.xml").read()
    xml_user = formatter.user_from_xml(raw_xml)
    json_user = User(json.load(open("tests/dummyData/dummyUser.json")))

    assert xml_user.__cmp__(json_user)


def test_paste_list_from_xml():
    raw_xml = open("tests/dummyData/dummyPasteList.xml").read()
    xml_paste_list = formatter.paste_list_from_xml(raw_xml)
    json_dic = json.load(open("tests/dummyData/dummyPasteList.json"))
    json_paste_list = create_paste_list(json_dic)

    assert len(xml_paste_list) == len(json_paste_list)
    for json_paste, xml_paste in zip(json_paste_list, xml_paste_list):
        assert json_paste.__cmp__(xml_paste) is True


def test_archive_url_format():
    pb = Pastebin()
    archive_list = pb.get_archive()
    print(archive_list)
    for id in archive_list:
        print(id)
        reg = re.match(r"[a-zA-Z0-9]{8}", id)
        assert reg.group() == id
