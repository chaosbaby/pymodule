from libext import proc
import pytest
from freezegun import freeze_time
from datetime import datetime


@freeze_time("2020-01-01")
def test_desDateToDate():

    print(datetime.now())
    assert datetime.now() == datetime(2020, 1, 1, 0, 0, 0)
    assert proc.desDateToDate("1 day") == "2019-12-31"
    assert proc.desDateToDate("1 week") == "2019-12-25"
    assert proc.desDateToDate("1 month") == "2019-12-02"
    assert proc.desDateToDate("2 years") == "2018-01-01"
    assert proc.desDateToDate("1 天") == "2019-12-31"
    assert proc.desDateToDate("1 周") == "2019-12-25"
    assert proc.desDateToDate("1 月") == "2019-12-02"
    assert proc.desDateToDate("2 年") == "2018-01-01"


def test_getNumberOutStr():
    assert proc.getNumberOutStr("1 day") == "1"
    assert proc.getNumberOutStr("we1ek") == "1"


def test_volumeToNumber():
    assert proc.volumeToNumber("100g") == 100
    assert proc.volumeToNumber("100m") == 0.1
    assert proc.volumeToNumber("100k") == pytest.approx(10**-4, 10**-6)
    assert proc.volumeToNumber("100G") == 100
    assert proc.volumeToNumber("100M") == 0.1
    assert proc.volumeToNumber("100K") == pytest.approx(10**-4, 10**-6)


