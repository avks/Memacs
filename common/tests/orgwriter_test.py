#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time-stamp: <2011-10-26 22:13:31 awieser>

import unittest
import os,sys
import codecs
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from common.orgwriter import OrgOutputWriter


class TestOutputWriter(unittest.TestCase):
    def setUp(self):
        # setting tmpfolder to "./tmp"
        self.TMPFOLDER = os.path.normpath(os.path.dirname(os.path.abspath(__file__))
                                           + os.path.sep +"tmp") + os.sep
        if not os.path.exists(self.TMPFOLDER):
            os.makedirs(self.TMPFOLDER)
    
    def test_ouput_to_file(self):
        """
        Simple Test
        """
        test_filename = self.TMPFOLDER+ "testfile.org"
        
        # writing test output
        writer = OrgOutputWriter("short descript","test-tag",test_filename)
        writer.write("## abc\n")
        writer.writeln("## abc")
        writer.write_comment("abc\n")
        writer.write_commentln("abc")
        writer.write_org_item("begin")
        writer.write_org_subitem("sub")
        writer.close()
        
        # read and check the file_handler
        file_handler = codecs.open(test_filename, "r", "utf-8")
        input_handler = file_handler.readlines()
        
        
        self.assertEqual(input_handler[0], u"## -*- coding: utf-8 mode: org -*-\n", "incorrect header")
        self.assertEqual(input_handler[1][:29], u"## this file is generated by ", "incorrect header")
        self.assertEqual(input_handler[3],u"* short descript        :Memacs:test-tag:\n", "short description and tag not present")
        self.assertEqual(input_handler[4], u"## abc\n", "incorrect write()")
        self.assertEqual(input_handler[5], u"## abc\n", "incorrect writeln()")
        self.assertEqual(input_handler[6], u"## abc\n", "incorrect write_comment()")
        self.assertEqual(input_handler[7], u"## abc\n", "incorrect write_commentln()")
        self.assertEqual(input_handler[8], u"* begin\n", "incorrect write_commentln()")
        self.assertEqual(input_handler[9], u"** sub\n", "incorrect write_commentln()")
        #self.assertEqual(input_handler[10][:24], u"* successfully parsed by", "incorrect footer()")

        #cleaning up
        os.remove(self.TMPFOLDER + "testfile.org")
    def test_utf8(self):
        test_filename = self.TMPFOLDER + "testutf8.org"
        
        # writing test output
        writer = OrgOutputWriter("short-des","tag",test_filename)
        writer.write(u"☁☂☃☄★☆☇☈☉☊☋☌☍☎☏☐☑☒☓☔☕☖☗♞♟♠♡♢♣♤♥♦♧♨♩♪♫♬♭♮♯♰♱♲♳♴♵\n")
        writer.close()
        
        # read and check the file_handler
        file_handler = codecs.open(test_filename, "r", "utf-8")
        input_handler = file_handler.readlines()
        self.assertEqual(input_handler[4], u"☁☂☃☄★☆☇☈☉☊☋☌☍☎☏☐☑☒☓☔☕☖☗♞♟♠♡♢♣♤♥♦♧♨♩♪♫♬♭♮♯♰♱♲♳♴♵\n","utf-8 failure")

        #cleaning up
        os.remove(self.TMPFOLDER + "testutf8.org")
        
if __name__ == '__main__':
    unittest.main()
