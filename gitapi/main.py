"""
Main entry point for the gitapi server.
"""
import logging
import pprint

import sys

from subprocess import Popen, PIPE

from gitapi.Commit import extract_commit

logging.basicConfig(
    stream=sys.stdout,
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(module)s : "
           "%(lineno)d - %(message)s"
)

LOG = logging.getLogger(__name__)


def main():
    """
    Main entry point for GIT-API
    """
    with Popen(args=("git",
                     "--git-dir=/tmp/repo/hyphen-api/.git",
                     "--no-pager",
                     "log",
                     "--grep=410355926645448",
                     "--format=%H '%aN' %at %s"),
               stdout=PIPE,
               bufsize=1,
               universal_newlines=True) as proc:
        commits = [
            extract_commit(line)
            for line in proc.stdout
        ]

        print(pprint.pformat(commits))


if __name__ == "__main__":
    main()
