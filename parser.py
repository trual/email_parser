#!/usr/bin/python
import tarfile
import re

class Parser():

    def parse_archive(self, input_file, output_file):
        """
        takes in a email archive and outputs the metadata of the archive,
        the metadata includes,
            name of file | from address | subject line | date
            sample.msg|sample@test.com|Citi Alerts|31/03/2011
        :param input_file: tar file to parse
        :param output_file: output filename
        """
        with open(output_file, 'w') as meta_data:
            if not tarfile.is_tarfile(input_file):
                print("please select a tarfile")
                return
            tar = tarfile.open(input_file)

            for member in tar.getmembers():

                name = self.parse_name(member.name)
                if member.isdir():
                    continue
                file_obj=tar.extractfile(member)

                #Method goes here and pass fileobj into
                from_addr = ""
                subject = ""
                date = ""
                boundary = ""
                for line in file_obj:
                    #From: Suncoast Hotel & Casino - Las Vegas <suncoast@boydgaming.net>
                    #todo add starts with instead of in
                    if "From:" in line:
                        from_addr = self.parse_from(line)
                    #Subject: See What's Happening with our Table Games!
                    elif "Subject:" in line:
                        subject = self.parse_subject(line)
                    #Date: Fri, 01 Apr 2011 10:36:26 -0700
                    elif "Date:" in line:
                        date = self.parse_date(line)
                    elif "boundary=" in line:
                        boundary = self.parse_boundary(line)
                    #todo find a better anchor, boundary, use the boundary value to find the endof the header then hit the value of boundary
                    elif (self.check_write_conditions(line, boundary)):
                        #todo pipe out here
                        print("{}|{}|{}|{}".format(name, from_addr, subject, date))
                        #wtf does this do?
                        meta_data.write("{}|{}|{}|{}\n".format(name, from_addr, subject, date))
                        break
            tar.close()

    @staticmethod
    def check_write_conditions(line, boundary):
        """
        check the line to see if it matches any return conditions
        :param line string: line in file
        :param boundary: variable which marks the end of multipart messages
        :return bool: true if write to the file is possible
        """
        if line.startswith('<html'):
            return True
        elif boundary!= "" and line.startswith(boundary):
            return True
        elif line.startswith('<!--HEADER-->'):
            return True
        else:
            return False

    @staticmethod
    def parse_boundary(line):
        """
        The boundary condition is used in MIME format to mark the end of Multipart
        message
        :param line string: line of msg files
        :return the boundary variable
        """
        search = re.search(r'\"(.+)\"', line)
        if search:
            return "--" + search.group(1)
        return ""

    @staticmethod
    def parse_from(line):
        """
        Parse string for from address in a line given the msg Information
        return string: email address or empty if not found
        """
        if '<' in line:
            search = re.search(r'<(.+)>', line)
        else:
            search = re.search(r': (.+)', line)
        if search:
            return search.group(1)
        return ""

    @staticmethod
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

    def parse_date(self, line):
        """
        parses the date line, returns a standard format for all dates
            Date: Fri, 01 Apr 2011 05:52:55 PDT -0000
            - 04/01/2011
            Date: 3/7/90
            - 03/07/1990
        :param line string: line to parse date from
        :return string: date converted to mm/dd/yyyy format
        """
        #if date is numeric format
        if '/' in line:
            date = self._format_numeric_date(line)
        else :
            date = self._format_to_numeric_date(line)
        return date

    @staticmethod
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

    @staticmethod
    def _format_numeric_date(line):
        """
        takes in a date line with numeric values
        :param line string: line with numeric date values
        :return string: date converted to mm/dd/yyyy format
        """
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

    def _format_to_numeric_date(self, line):
        """
        takes in date line in long format and returns numeric dates
        :param line string: date line with long formatted date
        :retirn string: date converted to mm/dd/yyyy format
        """
        search = re.search(r':\D+(\d{1,2}) (\w{3}) (\d{4})', line)
        if search:
            day = search.group(1)
            month = search.group(2)
            year = search.group(3)
            if len(day) < 2:
                day = day.zfill(2)
            month = self.month_dict[month]
            return '{}/{}/{}'.format(month, day, year)

    month_dict = {'Jan': '01',
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
