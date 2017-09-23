import logging

import sys

logging.basicConfig(
    stream=sys.stdout,
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(module)s : %(lineno)d - %(message)s"
)

logger = logging.getLogger(__name__)


def main():
    """
    Main entry point for GIT-API
    """
    logger.info("hello world...")


if __name__ == "__main__":
    main()
