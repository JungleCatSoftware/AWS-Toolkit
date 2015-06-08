import outputFormatters
import StringIO
import sys

class Test_OutputFormatters(object):

    def test_printBigHeader(self, capsys):
        outputFormatters.printBigHeader()
        # capsys is a built-in for py.test that we're making use of here.
        # see https://pytest.org/latest/capture.html#accessing-captured-output-from-a-test-function
        out, err = capsys.readouterr()
        assert out == """*************************************
* Jungle Cat Software | AWS-Toolkit *
*         Output Formatter          *
*************************************
"""

    def test_printSmallHeader(self, capsys):
        outputFormatters.printSmallHeader()
        out, err = capsys.readouterr()
        assert out == "\n==Output Formatter==\n"

    def test_printStartDateStamp(self, capsys):
        # testing with regex.  ... I know... I know... :/
        outputFormatters.printStartDateStamp()
        import re
        out, err = capsys.readouterr()
        mObj = re.search('Begin at \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d*', out)
        assert mObj, "Couldn't match {}".format(out)
