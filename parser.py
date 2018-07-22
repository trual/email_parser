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
    parse string for removing returning everything after the first ': '
    :param line string: string to be parse_date
    :return string: everything after the : or empty string
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
    #if date is numeric format
    if '/' in line:
        date = _format_numeric_date(line)
    else :
        date = _format_to_numeric_date(line)
    return date

def parse_name(line):
    """
    Parses string returning only the name of the file without directory paths
    :param line string: line to be parsed
    :return string: name of file
    """
    if '/' not in line:
        return line
    search = re.search(r'\/(\w+.\w+$)', line)
    if search:
        return search.group(1)
    return ""

def _format_numeric_date(line):
    search = re.search(r': (\d{1,2})\/(\d{1,2})\/(\d{2,4})', line)
    month = search.group(1)
    day = search.group(2)
    year = search.group(3)
    if len(month) < 2:
        # add leading zero
        month = month.zfill(2)
    if len(day) < 2:
        day = day.zfill(2)
    if len(year) < 4:
        #check time off current time
        if int(year) > 85:
            #add 19
            year = '19' + year
        elif int(year) <= 85:
            #add 20
            year = '20' + year
    return '{}/{}/{}'.format(month, day, year)

def _format_to_numeric_date(line):
    search = re.search(r':\D+(\d{1,2}) (\w{3}) (\d{4})', line)
    if search:
        day = search.group(1)
        month = search.group(2)
        year = search.group(3)
        if len(day) < 2:
            day = day.zfill(2)
        month = month_day_dict[month]
        return '{}/{}/{}'.format(month, day, year)

month_day_dict = {'Jan': '01',
                  'Feb': '02',
                  'Mar': '03',
                  'Apr': '04',
                  'May': '05',
                  'June': '06',
                  'July': '07',
                  'Aug': '08',
                  'Sept': '09',
                  'Oct': '10',
                  'Nov': '11',
                  'Dec': '12'}
