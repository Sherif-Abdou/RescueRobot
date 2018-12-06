import pytest
import sentry_sdk
from robot.motors import Motors

def test_getMotors():
    sentry_sdk.init("https://1e9819f95a3d46fdb1ef8c96287c29e8@sentry.io/1310445")
    motors = Motors(200, test_mode=True)
    assert motors.getMotorSpeeds() == (0, 0, 0, 0)

def test_setMotors():
    sentry_sdk.init("https://1e9819f95a3d46fdb1ef8c96287c29e8@sentry.io/1310445")
    motors = Motors(200, test_mode=True)
    motors.setMotorSpeed(1, 1)
    assert motors.getMotorSpeeds() == (1, 0, 0, 0)

def test_updateMotors():
    sentry_sdk.init("https://1e9819f95a3d46fdb1ef8c96287c29e8@sentry.io/1310445")
    motors = Motors(200, test_mode=True)
    for x in range(1, 4):
        motors.setMotorSpeed(x, 1)
        assert motors._update(x) == "m"+str(x)+"+"
        motors.setMotorSpeed(x, 0)
