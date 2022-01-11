import numpy
from path import Path
CWD = Path.getcwd()


def make_pie_data():
    zeros = numpy.zeros([300])
    ones = numpy.ones([150])
    twos = numpy.ones([200]) * 2
    threes = numpy.ones([60]) * 3
    x = numpy.hstack([zeros, ones, twos, threes])
    numpy.random.shuffle(x)
    numpy.save(CWD / "pie_data.npy", x)

def make_fish_data():
    ...


if __name__ == '__main__':
    make_pie_data()