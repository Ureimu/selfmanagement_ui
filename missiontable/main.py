from PyQt5.QtWidgets import QTableWidgetItem
from IOfile import *
from mission import mission
from mainwindow import *
import sys

mission_list = []
mission_number_list = []
searchBtn = []


def update_log_mission(mission_liste):
    print('update log...')
    file = open('historylog.txt', 'a+')
    file.write(str(mission_liste) + '\n')
    file.close()
    print('finish')


def finish_mission():
    print(mission.count - mission.delete_count - 1)
    last_mission_number = mission.count - mission.delete_count - 1
    idity = mission_list[mission.count - mission.delete_count - 1].id
    print(idity)
    ui_main.tableWidget.removeRow(last_mission_number)
    mission_number_list.pop(last_mission_number)
    searchBtn.pop(last_mission_number)
    mission_list.pop(last_mission_number)
    mission.delete_count += 1
    write_archive(mission_list)  # 对mission_list用pop会出问题,所以现在存档有问题
    # mission.count-mission.delete_count-1是指最后一个加入的mission对象的索引值


def set_table_item(row_number):
    ui_main.tableWidget.insertRow(row_number)
    ui_main.tableWidget.setItem(row_number, 0, QTableWidgetItem(mission_list[row_number].name))
    ui_main.tableWidget.setItem(row_number, 1, QTableWidgetItem(mission_list[row_number].description))
    ui_main.tableWidget.setItem(row_number, 2, QTableWidgetItem(mission_list[row_number].date_start.toString()))
    ui_main.tableWidget.setItem(row_number, 3, QTableWidgetItem(mission_list[row_number].date_end.toString()))
    searchBtn.append(QtWidgets.QPushButton('结束任务%d' % mission_list[-1].id))
    searchBtn[row_number].setStyleSheet('QPushButton{margin:3px}')
    ui_main.tableWidget.setCellWidget(row_number, 4, searchBtn[row_number])
    searchBtn[row_number].clicked.connect(finish_mission)
    mission_number_list.append(mission.id)


def read_mission(a_list):
    serial_number = 0
    for mission_detail_list in a_list:
        new_mission = mission(mission_detail_list[0], QtCore.QDateTime.fromString(mission_detail_list[2]),
                              QtCore.QDateTime.fromString(mission_detail_list[2]),
                              QtCore.QDateTime.fromString(mission_detail_list[3]),
                              mission_detail_list[1])
        mission_list.append(new_mission)
        set_table_item(serial_number)
        mission_number_list.append(serial_number)
        serial_number += 1
    mission.id = serial_number - 1
    mission.count = serial_number - 1
    return 0


def push_new_mission():
    mission_list.append(mission(ui_main.name.text(), ui_main.start_time.dateTime(),
                                ui_main.start_time.dateTime(), ui_main.end_time.dateTime(),
                                ui_main.description.toPlainText()))
    last_mission_number = mission.count - mission.delete_count - 1
    print(last_mission_number)
    print(type(mission_list[last_mission_number].date_start))
    set_table_item(last_mission_number)
    return mission.id


def new_mission_click():
    push_new_mission()
    write_archive(mission_list)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui_main = Ui_Mainwindow()
    mainwin = QtWidgets.QMainWindow()
    ui_main.setupUi(mainwin)
    read_mission(pre_read_archive())
    mainwin.show()
    ui_main.push_to_mission.clicked.connect(new_mission_click)
    app.exec_()
