#!/usr/bin/python
import re


def parse_from(line):
    """
    Parse string for from address in a line given the msg Information
    return string: email address or empty if not found
    """
    search = re.search(r'<(.+)>', line)
    if search:
        return search.group(1)
    return ""

def parse_subject(line):
    """
    empty subject line
    """
    search = re.search(r': (.+$)', line)
    if search:
        return search.group(1)
    return ""

def parse_date(line):
    """
    Date: Fri, 01 Apr 2011 05:52:55 PDT -0000
    Date: Fri, 01 Apr 2011 05:52:55 PDT +0000
    Date: Fri, 01 Apr 2011 05:52:55 PDT +0000
    Date: Fri, 01 Apr 2011 05:52:55 PDT
    Date: 03/14/11
    """
    search = re.search(r':.+(\d{1,2} \w{3} \d{4})', line)
    if search:
        return search.group(1)
    return ""

def parse_name(line):
    if '/' not in line:
        return line
    search = re.search(r'\/(\w+.\w+$)', line)
    if search:
        return search.group(1)
    return ""
