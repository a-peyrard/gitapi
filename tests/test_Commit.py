#!/usr/bin/env python
# coding=utf-8
from datetime import datetime
from unittest import TestCase

from gitapi.Commit import extract_commit, Commit


class TestExtractCommit(TestCase):
    def test_it_should_extract_commit_from_line(self):
        # GIVEN
        line = "788c27ecb5d6e4b9a56092579491b634fce35b55 'Augustin Peyrard' "\
               "1505154358 adds a job to launch surveys (every 60s)\n "

        # WHEN
        commit = extract_commit(line)

        # THEN
        self.assertEqual(
            commit,
            Commit(
                hash="788c27ecb5d6e4b9a56092579491b634fce35b55",
                author="Augustin Peyrard",
                date=datetime(2017, 9, 11, 18, 25, 58),
                title="adds a job to launch surveys (every 60s)"
            )
        )
