#! /usr/bin/env python

# pylint: disable=missing-docstring

from datetime import date
from unittest import TestCase, main

from s3stash import Stash
from s3stash.util import make_date_prefix

class TestStash(TestCase):
    def test_date_prefix(self):
        self.assertEqual(make_date_prefix(date(year=1988, month=2, day=19)),
                         '1988/02-February/19/')

    def test_stash_string(self):
        class MockS3(object):
            def __init__(self):
                self.received = []

            def upload_fileobj(self, rfile, bucket, key):
                self.received.append((rfile.read(), bucket, key))

        s3_client = MockS3()
        credentials = None

        stash = Stash(credentials, 'mycoolbucket', s3_client=s3_client)
        stash.make_key = lambda content: 'somekey'
        stash.stash_string('abc')

        self.assertEqual(s3_client.received, [('abc', 'mycoolbucket', 'somekey')])

if __name__ == '__main__':
    main()
