import unittest
from parser import *


class parser_function_test(unittest.TestCase):

    def test_parse_date_with_timezone(self):
        """
        Date: Fri, 01 Apr 2011 05:52:55 PDT -0000
        Date: Fri, 01 Apr 2011 05:52:55 PDT +0000
        Date: Fri, 01 Apr 2011 05:52:55 PDT +0000
        Date: Fri, 01 Apr 2011 05:52:55 PDT
        Date: Fri, 01 Apr 2011 05:52:55 PDT +0000 (UTC)
        Date: Fri, 31 Apr 2011 05:52:55 PDT +0000
        """
        exp_date = "04/01/2011"
        to_parse = "Date: Fri, 01 Apr 2011 05:52:55 PDT -1000"
        self.assertEqual(exp_date, parse_date(to_parse),
                'exp {} | found {}'.format(exp_date, parse_date(to_parse)))

        to_parse = "Date: Fri, 01 Apr 2011 05:52:55 PDT +2000"
        self.assertEqual(exp_date, parse_date(to_parse),
                'exp {} | found {}'.format(exp_date, parse_date(to_parse)))

        to_parse = "Date: Fri, 01 Apr 2011 05:52:55 PDT -4000 "
        self.assertEqual(exp_date, parse_date(to_parse),
                'exp {} | found {}'.format(exp_date, parse_date(to_parse)))

        to_parse = "Date: Fri, 01 Apr 2011 05:52:55 PDT"
        self.assertEqual(exp_date, parse_date(to_parse),
                'exp {} | found {}'.format(exp_date, parse_date(to_parse)))

    def test_parse_date_numeric_dates(self):
        """
        Date: 03/10/1990
        Date: 03/10/1990 UTC
        Date: 03/10/90
        Date: 3/10/1990
        Date: 03/14/11
        Date: 03/7/2011
        """
        exp_date = "03/10/1990"
        to_parse = "Date: 03/10/1990"
        self.assertEqual(exp_date, parse_date(to_parse),
                'exp {} | found {}'.format(exp_date, parse_date(to_parse)))
        to_parse = "Date: 03/10/1990 UTC"
        self.assertEqual(exp_date, parse_date(to_parse),
                'exp {} | found {}'.format(exp_date, parse_date(to_parse)))
        to_parse = "Date: 03/10/90"
        self.assertEqual(exp_date, parse_date(to_parse),
                'exp {} | found {}'.format(exp_date, parse_date(to_parse)))
        to_parse = "Date: 3/10/1990"
        self.assertEqual(exp_date, parse_date(to_parse),
                'exp {} | found {}'.format(exp_date, parse_date(to_parse)))
        exp_date = "03/14/2011"
        to_parse = "Date: 03/14/11"
        self.assertEqual(exp_date, parse_date(to_parse),
                'exp {} | found {}'.format(exp_date, parse_date(to_parse)))
        exp_date = "03/07/2011"
        to_parse = "Date: 03/7/2011"
        self.assertEqual(exp_date, parse_date(to_parse),
                'exp {} | found {}'.format(exp_date, parse_date(to_parse)))

    def test_parse_name(self):
        exp_name = "20110401_corel_14460139_html.msg"
        to_parse = "smallset/20110401_corel_14460139_html.msg"
        self.assertEqual(exp_name, parse_name(to_parse),
                'exp {} | found {}'.format(exp_name, parse_name(to_parse)))
        to_parse = "20110401_corel_14460139_html.msg"
        self.assertEqual(exp_name, parse_name(to_parse),
                'exp {} | found {}'.format(exp_name, parse_name(to_parse)))
        to_parse = "setsofsets/smallset/20110401_corel_14460139_html.msg"
        self.assertEqual(exp_name, parse_name(to_parse),
                'exp {} | found {}'.format(exp_name, parse_name(to_parse)))

    def test_parse_subject(self):
        exp_subject = "PREVIEW:   Save $170 and get special gift with CorelDraw Premium Suite X5"
        to_parse = "Subject: PREVIEW:   Save $170 and get special gift with CorelDraw Premium Suite X5"
        self.assertEqual(exp_subject, parse_subject(to_parse),
                'exp {} | found {}'.format(exp_subject, parse_subject(to_parse)))

    def test_parse_empty_subject(self):
        exp_subject = ""
        to_parse = "Subject: "
        self.assertEqual(exp_subject, parse_subject(to_parse),
                'exp {} | found {}'.format(exp_subject, parse_subject(to_parse)))


    def test_parse_from(self):
        exp_adr = "from@test.carmamail.com"
        to_parse = "From: {CARMA TEST} Test <from@test.carmamail.com>"
        self.assertEqual(exp_adr, parse_from(to_parse),
                'exp {} | found {}'.format(exp_adr, parse_from(to_parse)))

    def test_parse_empty_from(self):
        exp_adr = ""
        to_parse = "From: "
        self.assertEqual(exp_adr, parse_from(to_parse),
                'exp {} | found {}'.format(exp_adr, parse_from(to_parse)))


if __name__ == '__main__':
    unittest.main()
