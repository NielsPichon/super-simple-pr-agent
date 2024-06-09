import argparse
import pprint
from typing import Optional

from loguru import logger

from sspr import agent
from sspr import config
from sspr import git
from sspr import utils


def run_from_file(diff_file: str, output_path: Optional[str] = None):
    with open(diff_file, encoding='utf-8') as fp:
        diff = fp.read()

    review = agent.get_review(diff)
    if output_path is not None:
        with open(output_path, 'w', encoding='utf-8') as fp:
            fp.write(review)
    else:
        print(review)


def run_from_github():
    diff = git.get_diff_from_github()
    review = agent.get_review(diff)
    git.publish_review(review)


def run(diff_file: Optional[str] = None, output_path: Optional[str] = None):
    global_config = config.get_config()
    utils.set_global_log_level(global_config.log_level)

    logger.info(f"Running Super-Simple-PR")
    logger.info(f"Config:\n{pprint.pformat(global_config.model_dump())}")

    if diff_file is not None:
        run_from_file(diff_file, output_path)
        return
    run_from_github()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Super-Simple-PR')
    parser.add_argument('--diff', type=str, default=None,
                        help='Path to a diff file')
    parser.add_argument('--out', type=str, default=None,
                        help='If specified, write the review to this file')
    args = parser.parse_args()

    run(diff_file=args.diff, output_path=args.out)
