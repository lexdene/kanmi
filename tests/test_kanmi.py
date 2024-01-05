import os
from unittest import TestCase

from kanmi import Kanmi


class TestKanmi(TestCase):
    def test_simple(self):
        s1 = Kanmi.create('elephant').to_str()

        k = Kanmi.from_str(s1)

        self.assertTrue(k.validate('elephant'))
        self.assertFalse(k.validate('rhino'))
