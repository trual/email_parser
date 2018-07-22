#!/usr/bin/python
import tarfile
import sys

from parser import *


def main():
    with open('archive_metadata.txt', 'w') as meta_data:
        print(tarfile.is_tarfile("sampleEmails4.tar"))
        tar = tarfile.open("sampleEmails4.tar")

        ## this below needs to be a in a function
        for member in tar.getmembers():
            #print(member.type)
            #print(member.name)
            name = parse_name(member.name)
            if member.isdir():
                continue
            file_obj=tar.extractfile(member)
            from_addr = ""
            subject = ""
            date = ""
            for line in file_obj:
                #From: Suncoast Hotel & Casino - Las Vegas <suncoast@boydgaming.net>
                if "From:" in line:
                    #print (line)
                    from_addr = parse_from(line)
                #Subject: See What's Happening with our Table Games!
                elif "Subject:" in line:
                    #print(line)
                    subject = parse_subject(line)
                #Date: Fri, 01 Apr 2011 10:36:26 -0700
                elif "Date:" in line:
                    #print(line)
                    date = parse_date(line)
                #MIME-Version: 1.0
                #todo find a better anchor
                elif "Content-Type:" in line:
                    #todo pipe out here
                    print("{}|{}|{}|{}".format(name, from_addr, subject, date))
                    meta_data.write("{}|{}|{}|{}\n".format(name, from_addr, subject, date))
                    break




            # content=f.read()
            # print "%s has %d newlines" %(member, content.count("\n"))
            # print "%s has %d spaces" % (member,content.count(" "))
            # print "%s has %d characters" % (member, len(content))

        tar.close()



if __name__ == '__main__':
    main()