import tweepy

def connect_api():
    """
    connect_api 함수는 tweepy 로 API 를 연결한 'api' 객체를 리턴합니다.

    Hint: api 객체는 tweepy.API 로 만들 수 있습니다.
    """

    api_key = 'vra8JcPUfnNLRVGSGEE1AkCps'
    api_key_secret = 'g3rOfhyqZTTFcT85uAF0wWdFHLV5989ravrd7vYkSpned3NWEL'
    access_token = '1464037537442377730-OornP0t1KbtNHE9kgmqd9DcpcJUn5A'
    access_token_secret = 'oNiKTmeQd7yGyTTWHdQ4Q15VNNk4iBSL9QPJCy6pT5c0M'

    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    return api


def get_tweets(api, username):
    """
    'username' 이 주어지면 해당 유저의 트윗들을 가지고 올 수 있어야 합니다.
    각 트윗은 140 자 이상이어도 모든 내용을 가지고 올 수 있어야 합니다.

    Hint: 'tweet_mode' 에 대해서 알아보세요!
    """

    # status = api.get_status(username, tweet_mode="extended")
    # try:
    #     tweets = status.retweeted_status.full_text
    # except AttributeError:  # Not a Retweet
    #     tweets = status.full_text

    tweets = api.user_timeline(username, tweet_mode='extended')
    
    return tweets
