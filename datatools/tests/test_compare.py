import os
import pytest
from pathlib import Path

import datatools.main as dtools


@pytest.fixture
def setup():
    data = {'cwd': Path(os.path.realpath(__file__)).parent}
    return data


def test_compare(setup):
    with open(setup['cwd'] / 'data' / 'fileA1.txt') as A, open(
            setup['cwd'] / 'data' / 'fileB1.txt') as B, open(
                setup['cwd'] / 'data' / 'subtract.txt') as expected:
        subtract = sorted([
            x for x in dtools.compare(A, B, 'subtract', ',', None).split('\n')
        ])
        assert subtract == sorted(expected.read().split('\n'))