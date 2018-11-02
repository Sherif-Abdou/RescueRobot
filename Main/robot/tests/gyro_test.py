from robot.gyro import Acceleration, Rotation, Gyro

def test_gyro():
    sensor = Gyro()
    output = sensor.getGyroData("0 5 2:0 90 45")
    expected_acc = Acceleration(0, 5, 2)
    expected_rotation = Rotation(0, 90, 45)
    assert output[0].x == expected_acc.x
    assert output[0].y == expected_acc.y
    assert output[0].z == expected_acc.z
    assert output[1].x == expected_rotation.x
    assert output[1].y == expected_rotation.y
    assert output[1].z == expected_rotation.z
