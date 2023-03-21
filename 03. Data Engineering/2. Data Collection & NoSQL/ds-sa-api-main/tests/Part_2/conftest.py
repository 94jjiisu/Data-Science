import pytest
from src.Part_2 import connect_api, get_tweets

@pytest.fixture
def new_api():
    return connect_api()


@pytest.fixture
def sample_tweets():
    return get_tweets(connect_api(), 'bts_official')
