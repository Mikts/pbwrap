"""Contains function that manipulate the API returns for easier data manipulation."""
import xml.etree.ElementTree as et
import re
from pbwrap.models import Paste


def paste_list_from_xml(xml_paste_list):
    """Input an xml list and return a list of paste objects.
        <paste>
        ....
        </paste>
    """
    paste_list = list()

    # xml demands a base root to create xml element from string.
    # So we have to hardcode it.
    root = et.fromstring("<root>" + xml_paste_list + "</root>")

    # Iterate <paste> child elements and create a paste object.
    for paste_root in root:
        paste_dict = dict()

        for paste_element in paste_root:
            key = paste_element.tag.split('_', 1)[-1]
            value = paste_element.text

            paste_dict[key] = value

        paste_list.append(Paste(paste_dict))

    return paste_list


def archive_url_format(archive_html):
    """Return a list with recent pastes urls"""
    pastes_urls = list()

    # Regex Magic
    pastes = re.findall(r'/><a href=\"/(.+?)\">', archive_html)

    for paste_id in pastes:
        pastes_urls.append('https://pastebin.com/' + paste_id)

    return pastes_urls


def user_from_xml(user_xml_string):
    """Return user dictionary from an xml format string."""
    root = et.fromstring(user_xml_string)
    user_dict = dict()

    for user in root:
        key = user.tag.split('user_')[-1]
        value = user.text
        user_dict[key] = value

    return user_dict
