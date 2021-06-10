from fixtures import (
    simple
)
from unittest import mock


@mock.patch('time.time', mock.MagicMock(return_value=1577836800))
def build_all():
    simple.build()


build_all()
