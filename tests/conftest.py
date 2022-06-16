from click.testing import CliRunner
import pytest
from ape._cli import cli as ape_cli


@pytest.fixture
def runner():
    return CliRunner()



@pytest.fixture
def cli():
    return ape_cli
