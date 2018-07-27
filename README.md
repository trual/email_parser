# Parser to return subject lines of an email archive

archive_parser.py takes in an archive of email in a tar and returns
the name of file|from address|subject line|date.

This parser assumes that all the email archives are tar files
Which contain all MIME (.msg) formatted emails.

The parser also returns all dates as mm/dd/yyyy format.

# To run the parser
 `python python archive_parser.py`
  to specify the file input_file `-i` or `--input_file` then filename
  if no name is specified it defaults to "sampleEmails4.tar"

  to specify an output_file `-o` or `-output_file` then the dest named
  if no destination is specified it defaults to  "archive_metadata.txt"

# testing
test_parse.py contains a multitude of test cases.

to run the test classes
`python test_parser.py`

These files were all written using python 2.7
