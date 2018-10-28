from robot.lights import Lights
import sentry_sdk
import pytest

def test_get_lights():
    lights = Lights(test_mode=True)
    assert lights.getLights() == (False,False)


def test_set_lights():
    lights = Lights(test_mode=True)
    lights.setLight(1, True)
    assert lights.getLights() == (True, False)
    lights.setLight(1, False)
    lights.setLight(2, True)
    assert lights.getLights() == (False, True)

def test_update():
    lights = Lights(test_mode=True)
    lights.setLight(1, True)
    assert lights._update(1) == "l1+"
    lights.setLight(1, False)
    assert lights._update(1) == "l1-"
    lights.setLight(2, True)
    assert lights._update(2) == "l2+"
    lights.setLight(2, False)
    assert lights._update(2) == "l2-"
