from rplidar import RPLidar

lidar = RPLidar("/dev/ttyUSB0")

for _, _, a, d in lidar.iter_measurments():
    print(a)
    print(d)