#! /usr/bin/env python

from datetime import date
from unittest import TestCase, main

from s3stash.util import make_date_prefix

class TestStash(TestCase):
    def test_date_prefix(self):
        self.assertEqual(make_date_prefix(date(year=1988, month=2, day=19)),
                         '1988/02-February/19/')


if __name__ == '__main__':
    main()
