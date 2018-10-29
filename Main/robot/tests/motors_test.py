import pytest
import sentry_sdk
from robot.motors import Motors

@pytest.fixture(scope="session", autouse=True)
def do_something():
    sentry_sdk.init("https://1e9819f95a3d46fdb1ef8c96287c29e8@sentry.io/1310445")
    print("sentry")

def test_getMotors():
    motors = Motors(200, test_mode=True)
    assert motors.getMotorSpeeds() == (0, 0, 0, 0)

def test_setMotors():
    motors = Motors(200, test_mode=True)
    motors.setMotorSpeed(1, 1)
    assert motors.getMotorSpeeds() == (1, 0, 0, 0)

def test_updateMotors():
    motors = Motors(200, test_mode=True)
    for x in range(1, 4):
        motors.setMotorSpeed(x, 1)
        assert motors._update(x) == "m"+str(x)+"1"
        motors.setMotorSpeed(x, 0)
