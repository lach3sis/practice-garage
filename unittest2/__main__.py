"""Main entry point"""

import sys

from unittest2.main import main_


if sys.argv[0].endswith("__main__.py"):
    sys.argv[0] = "unittest2"

__unittest = True

main_()
