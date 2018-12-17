from __future__ import print_function
import os
import re


def printDir(dirpath='', extra_tab=1, ignore=(r'\.', r'/_', r'venv')):
    thickness = len(dirpath.split('/'))
    for root, dirs, files in os.walk(dirpath):
        do_ignore = False

        folders = root.split('/')
        for regex in ignore:
            matchObj = re.search(regex, root)
            if matchObj is not None:
                do_ignore = True
                break

        if do_ignore:
            continue

        print('    '*(len(folders)-thickness+extra_tab) + folders[-1] + '/')
        for filename in files:
            if os.path.splitext(filename)[1] == '.py':
                print('    '*(len(folders)-thickness+1) + filename)


if __name__ == '__main__':
    printDir('/Users/patarapolw/PycharmProjects/4wordPassGen')
