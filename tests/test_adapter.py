# coding: utf-8
import pytest
from httmock import HTTMock

from .conftest import response_mock, TEST_CONTENT


def test_initial(adapter):
    assert adapter.api_key == '0' * 32
    assert adapter.api_secret == '1' * 40


@pytest.mark.parametrize(
    'data, method_name, expected',
    (
        ('', '', 'd68c5221539cee380100467f088c18fe6ac7c805'),
        ('test', 'ping', '6f0415622374138fef0d8a8c5208917201edeaa4'),
        ('test', 'campaigns_edit', '7c72661cbffb455e7e451367b25c487076231652'),
    )
)
def test_get_sign(adapter, data, method_name, expected):
    assert adapter.get_sign(data, method_name) == expected


def test_make_request(adapter):
    with HTTMock(response_mock):
        response = adapter.ping()
    assert response.status_code == 200
    assert response.json() == TEST_CONTENT


def test_unknown_method(adapter):
    with pytest.raises(AttributeError):
        adapter.unknown_method()
