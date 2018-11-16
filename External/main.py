import grapher
from threading import Lock

data = []
lock = Lock()
grapher.genFigure(data, lock)