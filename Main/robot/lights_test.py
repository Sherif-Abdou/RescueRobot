from robot.lights import Lights

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