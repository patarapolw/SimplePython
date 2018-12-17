from __future__ import print_function
import collections
import xmltodict
import lxml.etree as etree
import re


def flatten(d, parent_key='', sep='-'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, collections.MutableMapping):
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def xml2flatDict(xml, sep='-'):
    i = 0
    result = {}
    allKeys = flatten(xmltodict.parse(xml), sep=sep).keys()
    for key in allKeys:
        key = re.sub('{}?[@#][^/]*{}?'.format(sep, sep), '', key)
        xpath = '/{}'.format('/'.join(key.split(sep)))
        if '#' in xpath:
            print(xpath)
            i += 1
            continue
        if '@' in xpath:
            print(xpath)
            i += 1
            continue
        tree = etree.fromstring(xml)
        values = tree.xpath(xpath)
        try:
            if key not in result.keys():
                result[key] = [x.text.strip() for x in values]
            else:
                result[key] += [x.text.strip() for x in values]
        except AttributeError:
            pass

    if i != 0:
        print("Missed {} paths".format(i))
    return result
