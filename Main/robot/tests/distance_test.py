import pytest
from robot.distance import DistanceSensor

def test_distance():
    sensor = DistanceSensor()
    assert 1.4 == sensor.getDistance("d1.4")
    assert 25 == sensor.getDistance("d25")