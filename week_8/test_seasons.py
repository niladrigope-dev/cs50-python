from seasons import minutes
from datetime import date, timedelta



def test_one_day():
    yesterday = date.today() - timedelta(days=1)
    assert minutes(yesterday) == 1440


def test_one_year():
    one_year_ago = date(date.today().year - 1, date.today().month, date.today().day)
    assert minutes(one_year_ago) in (525600, 527040)