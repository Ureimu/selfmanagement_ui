import re
from mainwindow import *


def reformat_time(qt_time_str):
    """
    输入一个qt时间字符串,将其转化为QDateTime的一个实例.
    :param qt_time_str:
    :return: QDateTime() or NoType
    """
    re_time = ''
    matched = re.match(
        r'(PyQt5.QtCore.QDateTime\()+(\d{4})+(, )+(\d{1,2})(, )+(\d{1,2})(, )+(\d{1,2})(, )+(\d{1,2})(\))', qt_time_str)
    try:
        for i in range(2, 9, 2):
            re_time += matched.group(i) + '/'
        re_time += matched.group(10)
        print(re_time)
        x = QtCore.QDateTime.fromString(re_time, 'yyyy/M/d/h/m')
        print(x)
        return x
    except AttributeError:
        pass


def write_archive(mission_list):
    file = open('mission_archive.txt', 'w+')
    for mission_loaded in mission_list:
        file.write(mission_loaded.name + '(separator)' + mission_loaded.description +
                   '(separator)' + str(mission_loaded.date_start) +
                   '(separator)' + str(mission_loaded.date_end) + '(separator)' + '\n')
    file.close()


def pre_read_archive():
    mission_read_list, numx = [], -1
    file = open('mission_archive.txt', 'r')
    for strx in file.readlines():
        numx += 1
        mission_read_list.append(strx.split('(separator)'))
        try:
            mission_read_list[numx][2] = reformat_time(mission_read_list[numx][2])
            mission_read_list[numx][3] = reformat_time(mission_read_list[numx][3])
        except IndexError:
            print('no')
            pass
    file.close()
    return mission_read_list
