import pytest


def test_connect_to_api(new_api):
    assert new_api.verify_credentials() != False


def test_get_tweets(sample_tweets):
    assert len(sample_tweets) != 0


def test_get_tweets_is_over_140(sample_tweets):
    # full_text 라는 속성이 있는지 확인
    assert sample_tweets[0].full_text is not None
