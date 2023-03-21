from src import Part_1


def test_get_page():
    _, page = Part_1.get_page('https://google.com/')

    assert page.status_code == 200


def test_get_avg_stars():
    test_data = [
        {
            'review_text': 'Outstanding',
            'review_star': 9
        },
        {
            'review_text': 'Excellent',
            'review_star': 9
        },
        {
            'review_text': 'Not my cup of tea',
            'review_star': 4
        },
        {
            'review_text': 'Okay!',
            'review_star': 5
        },
        {
            'review_text': 'Horrible...',
            'review_star': 1
        },
        {
            'review_text': 'Great Movie!',
            'review_star': 8
        }
    ]

    avg_stars = Part_1.get_avg_stars(test_data)

    assert avg_stars == 6.0


def test_scrape_by_movie_title():
    test_data = [
        ('Kingdom of Heaven', 38908),
        ('엔더스 게임', 89723),
        ('부산행', 130966)
    ]

    for t_d in test_data:
        assert Part_1.get_movie_code(t_d[0]) == t_d[1]


def test_scrape_by_review_num():
    test_title = '부산행'
    test_review_num = 25

    reviews = Part_1.scrape_by_review_num(test_title, test_review_num)

    assert len(reviews) == test_review_num


def test_scrape_by_page_num():
    test_title = '부산행'
    test_page = 2

    reviews = Part_1.scrape_by_page_num(test_title, test_page)

    assert len(reviews) == test_page * 10
