import pathlib
import tempfile

from sspr import run_agent


def test_run_agent_local():
    with tempfile.TemporaryDirectory() as tmpdirname:
        tmpdirname = pathlib.Path(tmpdirname)
        run_agent.run(diff_file='diff.txt',
                      output_path=tmpdirname / 'review.md')
        assert (tmpdirname / 'review.md').exists()
