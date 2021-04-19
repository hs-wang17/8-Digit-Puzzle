import sys
from mainwindow import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui, QtCore
import main_9gong
import main_xgong
import numpy as np
import pygame
from split_jpeg import *


sys.setrecursionlimit(100000)


class my_window(QtWidgets.QWidget, Ui_MainWindow):
    def __init__(self):
        super(my_window, self).__init__()
        self.setupUi(self)

        pygame.init()

        self.setWindowOpacity(0.95)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)   # 设置窗口背景透明
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)   # 隐藏边框
        self.label_183.setScaledContents(True)
        self.label_183.setPixmap(QtGui.QPixmap("pic/background_gif.gif"))
        # self.gif = QtGui.QMovie("pic/background_gif.gif")
        # self.label_183.setMovie(self.gif)
        # self.gif.start()
        self.pushButton_18.setStyleSheet("QPushButton{border-image: url(pic/close_.png)}"
                                         "QPushButton:hover{border-image: url(pic/close.png)}")
        self.pushButton_18.pressed.connect(self.close_mainwindow)

        pixmap = QtGui.QPixmap('pic/cursor_1.png')
        cursor = QtGui.QCursor(pixmap, 1, 1)
        self.setCursor(cursor)

        self.path_direction = 1
        self.empty = 0
        self.make_state = 1
        self.check_state = []   # zgong
        self.check_state_ = []  # zgong

        self.timer_9gong = QtCore.QTimer()
        self.timer_9gong.setInterval(1000)
        self.timer_zgong = QtCore.QTimer()
        self.timer_zgong.setInterval(1000)
        self.timer_xgong = QtCore.QTimer()
        self.timer_xgong.setInterval(200)
        self.timer_dgong = QtCore.QTimer()
        self.timer_dgong.setInterval(1000)
        self.init_9gong()
        self.init_zgong()
        self.init_dgong()

        self.timer_9gong.timeout.connect(self.next_step_9gong)
        self.timer_zgong.timeout.connect(self.next_step_zgong)
        self.timer_xgong.timeout.connect(self.next_step_xgong)
        self.timer_dgong.timeout.connect(self.show_time_dgong)

        self.comboBox_4.activated.connect(self.change_9gong)
        self.pushButton.pressed.connect(self.begin_9gong)
        self.pushButton_2.pressed.connect(self.pause_9gong)
        self.pushButton_3.pressed.connect(self.next_step_9gong)
        self.pushButton_4.pressed.connect(self.last_step_9gong)
        self.horizontalSlider.valueChanged.connect(self.timer_set_interval_9gong)

        self.comboBox_5.activated.connect(self.init_zgong)
        self.checkBox_1.stateChanged.connect(self.make_zgong)
        self.checkBox_2.stateChanged.connect(self.make_zgong)
        self.checkBox_3.stateChanged.connect(self.make_zgong)
        self.checkBox_4.stateChanged.connect(self.make_zgong)
        self.checkBox_5.stateChanged.connect(self.make_zgong)
        self.checkBox_6.stateChanged.connect(self.make_zgong)
        self.checkBox_7.stateChanged.connect(self.make_zgong)
        self.checkBox_8.stateChanged.connect(self.make_zgong)
        self.checkBox_9.stateChanged.connect(self.make_zgong)
        self.pushButton_7.pressed.connect(self.begin_zgong)
        self.pushButton_8.pressed.connect(self.pause_zgong)
        self.pushButton_13.pressed.connect(self.reset_zgong)
        self.horizontalSlider_2.valueChanged.connect(self.timer_set_interval_zgong)

        self.groupBox_22.hide()
        self.groupBox_23.hide()
        self.groupBox_24.hide()
        self.groupBox_25.hide()
        self.groupBox_34.hide()
        self.groupBox_35.hide()
        self.groupBox_44.hide()
        self.groupBox_45.hide()
        self.groupBox_55.hide()
        self.spinBox_2.setMinimum(self.spinBox.value())
        self.spinBox.valueChanged.connect(self.set_xgong)
        self.spinBox_2.valueChanged.connect(self.set_xgong)
        self.pushButton_14.pressed.connect(self.init_xgong)
        self.pushButton_15.pressed.connect(self.search_xgong_A)
        self.pushButton_16.pressed.connect(self.search_xgong_B)
        self.pushButton_19.pressed.connect(self.search_xgong_D)
        self.pushButton_11.pressed.connect(self.begin_xgong)
        self.pushButton_12.pressed.connect(self.pause_xgong)
        self.pushButton_11.setEnabled(False)
        self.pushButton_12.setEnabled(False)
        self.label_12.setScaledContents(True)
        self.label_12.setPixmap(QtGui.QPixmap("pic/wzxg.jpeg"))

        self.comboBox_6.activated.connect(self.init_dgong)
        self.pushButton_10.pressed.connect(self.up_dgong)
        self.pushButton_5.pressed.connect(self.down_dgong)
        self.pushButton_9.pressed.connect(self.left_dgong)
        self.pushButton_6.pressed.connect(self.right_dgong)
        self.pushButton_17.pressed.connect(self.finish_dgong)

        self.setScaled()

    def keyPressEvent(self, QKeyEvent):
        if QtGui.QKeyEvent.key(QKeyEvent) == QtCore.Qt.Key_W:
            self.up_dgong()
        elif QtGui.QKeyEvent.key(QKeyEvent) == QtCore.Qt.Key_S:
            self.down_dgong()
        elif QtGui.QKeyEvent.key(QKeyEvent) == QtCore.Qt.Key_A:
            self.left_dgong()
        elif QtGui.QKeyEvent.key(QKeyEvent) == QtCore.Qt.Key_D:
            self.right_dgong()
        elif QtGui.QKeyEvent.key(QKeyEvent) == QtCore.Qt.Key_Space:
            self.finish_dgong()

    def close_mainwindow(self):
        my_show.close()

    def setScaled(self):
        self.label_100.setScaledContents(True)
        self.label_101.setScaledContents(True)
        self.label_102.setScaledContents(True)
        self.label_103.setScaledContents(True)
        self.label_104.setScaledContents(True)
        self.label_105.setScaledContents(True)
        self.label_106.setScaledContents(True)
        self.label_107.setScaledContents(True)
        self.label_108.setScaledContents(True)

        self.label_000.setScaledContents(True)
        self.label_001.setScaledContents(True)
        self.label_002.setScaledContents(True)
        self.label_003.setScaledContents(True)
        self.label_004.setScaledContents(True)
        self.label_005.setScaledContents(True)
        self.label_006.setScaledContents(True)
        self.label_007.setScaledContents(True)
        self.label_008.setScaledContents(True)

        self.label.setScaledContents(True)
        self.label_3.setScaledContents(True)
        self.label_21.setScaledContents(True)
        self.label_22.setScaledContents(True)

        self.label_55.setScaledContents(True)
        self.label_56.setScaledContents(True)
        self.label_48.setScaledContents(True)
        self.label_49.setScaledContents(True)
        self.label_50.setScaledContents(True)
        self.label_52.setScaledContents(True)

        self.label_61.setScaledContents(True)
        self.label_62.setScaledContents(True)
        self.label_51.setScaledContents(True)
        self.label_57.setScaledContents(True)
        self.label_53.setScaledContents(True)
        self.label_54.setScaledContents(True)
        self.label_58.setScaledContents(True)
        self.label_59.setScaledContents(True)

        self.label_111.setScaledContents(True)
        self.label_90.setScaledContents(True)
        self.label_95.setScaledContents(True)
        self.label_109.setScaledContents(True)
        self.label_112.setScaledContents(True)
        self.label_94.setScaledContents(True)
        self.label_97.setScaledContents(True)
        self.label_110.setScaledContents(True)
        self.label_96.setScaledContents(True)
        self.label_92.setScaledContents(True)

        self.label_2.setScaledContents(True)
        self.label_23.setScaledContents(True)
        self.label_24.setScaledContents(True)
        self.label_42.setScaledContents(True)
        self.label_43.setScaledContents(True)
        self.label_44.setScaledContents(True)
        self.label_45.setScaledContents(True)
        self.label_46.setScaledContents(True)
        self.label_47.setScaledContents(True)

        self.label_70.setScaledContents(True)
        self.label_71.setScaledContents(True)
        self.label_63.setScaledContents(True)
        self.label_72.setScaledContents(True)
        self.label_64.setScaledContents(True)
        self.label_65.setScaledContents(True)
        self.label_67.setScaledContents(True)
        self.label_73.setScaledContents(True)
        self.label_66.setScaledContents(True)
        self.label_68.setScaledContents(True)
        self.label_69.setScaledContents(True)
        self.label_74.setScaledContents(True)

        self.label_83.setScaledContents(True)
        self.label_86.setScaledContents(True)
        self.label_85.setScaledContents(True)
        self.label_84.setScaledContents(True)
        self.label_87.setScaledContents(True)
        self.label_79.setScaledContents(True)
        self.label_76.setScaledContents(True)
        self.label_82.setScaledContents(True)
        self.label_78.setScaledContents(True)
        self.label_88.setScaledContents(True)
        self.label_75.setScaledContents(True)
        self.label_80.setScaledContents(True)
        self.label_81.setScaledContents(True)
        self.label_77.setScaledContents(True)
        self.label_89.setScaledContents(True)

        self.label_178.setScaledContents(True)
        self.label_174.setScaledContents(True)
        self.label_157.setScaledContents(True)
        self.label_171.setScaledContents(True)
        self.label_162.setScaledContents(True)
        self.label_158.setScaledContents(True)
        self.label_167.setScaledContents(True)
        self.label_166.setScaledContents(True)
        self.label_154.setScaledContents(True)
        self.label_173.setScaledContents(True)
        self.label_160.setScaledContents(True)
        self.label_175.setScaledContents(True)
        self.label_168.setScaledContents(True)
        self.label_156.setScaledContents(True)
        self.label_172.setScaledContents(True)
        self.label_177.setScaledContents(True)

        self.label_121.setScaledContents(True)
        self.label_91.setScaledContents(True)
        self.label_114.setScaledContents(True)
        self.label_119.setScaledContents(True)
        self.label_122.setScaledContents(True)
        self.label_113.setScaledContents(True)
        self.label_116.setScaledContents(True)
        self.label_120.setScaledContents(True)
        self.label_115.setScaledContents(True)
        self.label_98.setScaledContents(True)
        self.label_93.setScaledContents(True)
        self.label_118.setScaledContents(True)
        self.label_99.setScaledContents(True)
        self.label_123.setScaledContents(True)
        self.label_117.setScaledContents(True)
        self.label_124.setScaledContents(True)
        self.label_125.setScaledContents(True)
        self.label_126.setScaledContents(True)
        self.label_127.setScaledContents(True)
        self.label_128.setScaledContents(True)

        self.label_145.setScaledContents(True)
        self.label_139.setScaledContents(True)
        self.label_140.setScaledContents(True)
        self.label_147.setScaledContents(True)
        self.label_130.setScaledContents(True)
        self.label_134.setScaledContents(True)
        self.label_143.setScaledContents(True)
        self.label_146.setScaledContents(True)
        self.label_148.setScaledContents(True)
        self.label_144.setScaledContents(True)
        self.label_141.setScaledContents(True)
        self.label_135.setScaledContents(True)
        self.label_133.setScaledContents(True)
        self.label_136.setScaledContents(True)
        self.label_142.setScaledContents(True)
        self.label_137.setScaledContents(True)
        self.label_131.setScaledContents(True)
        self.label_129.setScaledContents(True)
        self.label_138.setScaledContents(True)
        self.label_132.setScaledContents(True)
        self.label_149.setScaledContents(True)
        self.label_150.setScaledContents(True)
        self.label_151.setScaledContents(True)
        self.label_152.setScaledContents(True)
        self.label_153.setScaledContents(True)

        self.label_199.setScaledContents(True)
        self.label_190.setScaledContents(True)
        self.label_203.setScaledContents(True)
        self.label_189.setScaledContents(True)
        self.label_191.setScaledContents(True)
        self.label_188.setScaledContents(True)
        self.label_184.setScaledContents(True)
        self.label_195.setScaledContents(True)
        self.label_198.setScaledContents(True)

    def move_sound(self):
        sound = pygame.mixer.Sound(r"music/move.wav")
        sound.set_volume(1)
        sound.play()

    def win_sound(self):
        sound = pygame.mixer.Sound(r"music/win.wav")
        sound.set_volume(1)
        sound.play()

    def alarm_sound(self):
        sound = pygame.mixer.Sound(r"music/alarm.wav")
        sound.set_volume(1)
        sound.play()

    # ----------------------------- #

    def timer_set_interval_9gong(self):
        self.timer_9gong.setInterval(1000 - 500 * self.horizontalSlider.value())

    def change_matrix_9gong(self, matrix):
        if matrix[0][0]:
            self.label_100.setPixmap(QtGui.QPixmap(self.pic_9gong[matrix[0][0]]))
        else:
            self.label_100.setPixmap(QtGui.QPixmap(""))

        if matrix[0][1]:
            self.label_101.setPixmap(QtGui.QPixmap(self.pic_9gong[matrix[0][1]]))
        else:
            self.label_101.setPixmap(QtGui.QPixmap(""))

        if matrix[0][2]:
            self.label_102.setPixmap(QtGui.QPixmap(self.pic_9gong[matrix[0][2]]))
        else:
            self.label_102.setPixmap(QtGui.QPixmap(""))

        if matrix[1][0]:
            self.label_103.setPixmap(QtGui.QPixmap(self.pic_9gong[matrix[1][0]]))
        else:
            self.label_103.setPixmap(QtGui.QPixmap(""))

        if matrix[1][1]:
            self.label_104.setPixmap(QtGui.QPixmap(self.pic_9gong[matrix[1][1]]))
        else:
            self.label_104.setPixmap(QtGui.QPixmap(""))

        if matrix[1][2]:
            self.label_105.setPixmap(QtGui.QPixmap(self.pic_9gong[matrix[1][2]]))
        else:
            self.label_105.setPixmap(QtGui.QPixmap(""))

        if matrix[2][0]:
            self.label_106.setPixmap(QtGui.QPixmap(self.pic_9gong[matrix[2][0]]))
        else:
            self.label_106.setPixmap(QtGui.QPixmap(""))

        if matrix[2][1]:
            self.label_107.setPixmap(QtGui.QPixmap(self.pic_9gong[matrix[2][1]]))
        else:
            self.label_107.setPixmap(QtGui.QPixmap(""))

        if matrix[2][2]:
            self.label_108.setPixmap(QtGui.QPixmap(self.pic_9gong[matrix[2][2]]))
        else:
            self.label_108.setPixmap(QtGui.QPixmap(""))

    def fill_matrix_9gong(self, matrix):
        self.label_100.setPixmap(QtGui.QPixmap(self.pic_9gong[matrix[0][0]]))
        self.label_101.setPixmap(QtGui.QPixmap(self.pic_9gong[matrix[0][1]]))
        self.label_102.setPixmap(QtGui.QPixmap(self.pic_9gong[matrix[0][2]]))
        self.label_103.setPixmap(QtGui.QPixmap(self.pic_9gong[matrix[1][0]]))
        self.label_104.setPixmap(QtGui.QPixmap(self.pic_9gong[matrix[1][1]]))
        self.label_105.setPixmap(QtGui.QPixmap(self.pic_9gong[matrix[1][2]]))
        self.label_106.setPixmap(QtGui.QPixmap(self.pic_9gong[matrix[2][0]]))
        self.label_107.setPixmap(QtGui.QPixmap(self.pic_9gong[matrix[2][1]]))
        self.label_108.setPixmap(QtGui.QPixmap(self.pic_9gong[matrix[2][2]]))

    def init_9gong(self):
        self.env_9gong = main_9gong.init_env()
        self.inv_9gong = main_9gong.invert_env(self.env_9gong)
        self.open_list_9gong = []
        self.closed_list_9gong = []
        self.path_9gong = []
        self.path__9gong = []
        self.pic_9gong = []
        print(self.env_9gong, self.inv_9gong)

        role_id_9gong = self.comboBox_4.currentIndex()
        pic_file = "pic/" + str(role_id_9gong) + ".jpg"
        pix = QtGui.QPixmap(pic_file)
        self.label_10.setPixmap(pix)
        self.label_10.setScaledContents(True)
        pic_list = cut_image(Image.open(pic_file), 3, 3)
        save_images(pic_list, [1, 2, 3, 8, 0, 4, 7, 6, 5])
        for i in range(9):
            self.pic_9gong.append(QtGui.QPixmap("temp/" + str(i) + ".jpg"))

        self.change_matrix_9gong(self.env_9gong)
        if self.inv_9gong:
            if self.env_9gong[0][0] != 0 and self.env_9gong[0][1] != 0:
                temp = np.copy(self.env_9gong[0][0])
                self.env_9gong[0][0] = np.copy(self.env_9gong[0][1])
                self.env_9gong[0][1] = temp
            else:
                temp = np.copy(self.env_9gong[1][0])
                self.env_9gong[1][0] = np.copy(self.env_9gong[1][1])
                self.env_9gong[1][1] = temp
            self.inv_9gong = 0
            _, self.path_9gong = main_9gong.A_remake_9gong(self.env_9gong, self.inv_9gong, self.open_list_9gong, self.closed_list_9gong, self.path_9gong)
            self.change_matrix_9gong(self.env_9gong)
        else:
            _, self.path_9gong = main_9gong.A_remake_9gong(self.env_9gong, self.inv_9gong, self.open_list_9gong, self.closed_list_9gong, self.path_9gong)
        self.lcdNumber.display(int(len(self.path_9gong)))
        self.lcdNumber_2.display(0)
        self.lcdNumber_3.display(int(len(self.path_9gong)))
        self.progressBar.setValue(0)

    def change_9gong(self):
        self.env_9gong = main_9gong.init_env()
        self.inv_9gong = main_9gong.invert_env(self.env_9gong)
        self.open_list_9gong = []
        self.closed_list_9gong = []
        self.path_9gong = []
        self.path__9gong = []
        self.pic_9gong = []
        print(self.env_9gong, self.inv_9gong)

        role_id_9gong = self.comboBox_4.currentIndex()
        pic_file = "pic/" + str(role_id_9gong) + ".jpg"
        pix = QtGui.QPixmap(pic_file)
        self.label_10.setPixmap(pix)
        self.label_10.setScaledContents(True)
        pic_list = cut_image(Image.open(pic_file), 3, 3)
        save_images(pic_list, [1, 2, 3, 8, 0, 4, 7, 6, 5])
        for i in range(9):
            self.pic_9gong.append(QtGui.QPixmap("temp/" + str(i) + ".jpg"))

        self.change_matrix_9gong(self.env_9gong)
        if self.inv_9gong:
            if self.env_9gong[0][0] != 0 and self.env_9gong[0][1] != 0:
                temp = np.copy(self.env_9gong[0][0])
                self.env_9gong[0][0] = np.copy(self.env_9gong[0][1])
                self.env_9gong[0][1] = temp
            else:
                temp = np.copy(self.env_9gong[1][0])
                self.env_9gong[1][0] = np.copy(self.env_9gong[1][1])
                self.env_9gong[1][1] = temp
            self.inv_9gong = 0
            _, self.path_9gong = main_9gong.A_remake_9gong(self.env_9gong, self.inv_9gong, self.open_list_9gong, self.closed_list_9gong, self.path_9gong)
            QtWidgets.QMessageBox.information(self, "标题", "找到到达相对状态的一种方法，将相邻两格调换顺序！",
                                              QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                              QtWidgets.QMessageBox.Yes)
            self.change_matrix_9gong(self.env_9gong)
        else:
            _, self.path_9gong = main_9gong.A_remake_9gong(self.env_9gong, self.inv_9gong, self.open_list_9gong, self.closed_list_9gong, self.path_9gong)
            QtWidgets.QMessageBox.information(self, "标题", "找到一种方法！", QtWidgets.QMessageBox.Yes |
                                              QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.Yes)
        self.lcdNumber.display(int(len(self.path_9gong)))
        self.lcdNumber_2.display(0)
        self.lcdNumber_3.display(int(len(self.path_9gong)))
        self.progressBar.setValue(0)

    def next_step_9gong(self):
        if len(self.path_9gong):
            if self.path_direction:
                self.change_matrix_9gong(self.path_9gong[0])
                self.path__9gong.append(self.path_9gong[0])
                del (self.path_9gong[0])
                self.move_sound()
            else:
                self.path__9gong.append(self.path_9gong[0])
                del (self.path_9gong[0])
                self.change_matrix_9gong(self.path_9gong[0])
                self.path__9gong.append(self.path_9gong[0])
                del (self.path_9gong[0])
                self.path_direction = 1
                self.move_sound()
            self.lcdNumber_2.display(int(len(self.path__9gong)))
            self.lcdNumber_3.display(int(len(self.path_9gong)))
            self.progressBar.setValue(len(self.path__9gong) / self.lcdNumber.value() * 100)
        else:
            if len(self.path__9gong) == 0:
                QtWidgets.QMessageBox.information(self, "标题", "本题目已经解决！", QtWidgets.QMessageBox.Yes |
                                                  QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.Yes)
                self.timer_9gong.stop()
            else:
                self.fill_matrix_9gong(self.path__9gong[-1])
                QtWidgets.QMessageBox.information(self, "标题", "九宫格已还原！", QtWidgets.QMessageBox.Yes |
                                                  QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.Yes)
                self.timer_9gong.stop()
            self.win_sound()

    def last_step_9gong(self):
        self.timer_9gong.stop()
        if len(self.path__9gong):
            if self.path_direction == 0:
                self.change_matrix_9gong(self.path__9gong[-1])
                self.path_9gong.insert(0, self.path__9gong[-1])
                del (self.path__9gong[-1])
                self.move_sound()
            else:
                self.path_9gong.insert(0, self.path__9gong[-1])
                del (self.path__9gong[-1])
                self.change_matrix_9gong(self.path__9gong[-1])
                self.path_9gong.insert(0, self.path__9gong[-1])
                del (self.path__9gong[-1])
                self.path_direction = 0
                self.move_sound()
            self.lcdNumber_2.display(int(len(self.path__9gong)))
            self.lcdNumber_3.display(int(len(self.path_9gong)))
            self.progressBar.setValue(len(self.path__9gong) / self.lcdNumber.value() * 100)
        else:
            QtWidgets.QMessageBox.information(self, "标题", "已经到达初始状态！", QtWidgets.QMessageBox.Yes |
                                              QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.Yes)

    def begin_9gong(self):
        self.timer_9gong.start()

    def pause_9gong(self):
        self.timer_9gong.stop()

    # -------------------------------- #

    def timer_set_interval_zgong(self):
        self.timer_zgong.setInterval(1000 - 500 * self.horizontalSlider_2.value())

    def change_matrix_zgong(self, matrix):
        if matrix[0][0]:
            self.label_000.setPixmap(QtGui.QPixmap(self.pic_zgong[matrix[0][0]]))
        else:
            self.label_000.setPixmap(QtGui.QPixmap(""))

        if matrix[0][1]:
            self.label_001.setPixmap(QtGui.QPixmap(self.pic_zgong[matrix[0][1]]))
        else:
            self.label_001.setPixmap(QtGui.QPixmap(""))

        if matrix[0][2]:
            self.label_002.setPixmap(QtGui.QPixmap(self.pic_zgong[matrix[0][2]]))
        else:
            self.label_002.setPixmap(QtGui.QPixmap(""))

        if matrix[1][0]:
            self.label_003.setPixmap(QtGui.QPixmap(self.pic_zgong[matrix[1][0]]))
        else:
            self.label_003.setPixmap(QtGui.QPixmap(""))

        if matrix[1][1]:
            self.label_004.setPixmap(QtGui.QPixmap(self.pic_zgong[matrix[1][1]]))
        else:
            self.label_004.setPixmap(QtGui.QPixmap(""))

        if matrix[1][2]:
            self.label_005.setPixmap(QtGui.QPixmap(self.pic_zgong[matrix[1][2]]))
        else:
            self.label_005.setPixmap(QtGui.QPixmap(""))

        if matrix[2][0]:
            self.label_006.setPixmap(QtGui.QPixmap(self.pic_zgong[matrix[2][0]]))
        else:
            self.label_006.setPixmap(QtGui.QPixmap(""))

        if matrix[2][1]:
            self.label_007.setPixmap(QtGui.QPixmap(self.pic_zgong[matrix[2][1]]))
        else:
            self.label_007.setPixmap(QtGui.QPixmap(""))

        if matrix[2][2]:
            self.label_008.setPixmap(QtGui.QPixmap(self.pic_zgong[matrix[2][2]]))
        else:
            self.label_008.setPixmap(QtGui.QPixmap(""))

    def fill_matrix_zgong(self, matrix):
            self.label_000.setPixmap(QtGui.QPixmap(self.pic_zgong[matrix[0][0]]))
            self.label_001.setPixmap(QtGui.QPixmap(self.pic_zgong[matrix[0][1]]))
            self.label_002.setPixmap(QtGui.QPixmap(self.pic_zgong[matrix[0][2]]))
            self.label_003.setPixmap(QtGui.QPixmap(self.pic_zgong[matrix[1][0]]))
            self.label_004.setPixmap(QtGui.QPixmap(self.pic_zgong[matrix[1][1]]))
            self.label_005.setPixmap(QtGui.QPixmap(self.pic_zgong[matrix[1][2]]))
            self.label_006.setPixmap(QtGui.QPixmap(self.pic_zgong[matrix[2][0]]))
            self.label_007.setPixmap(QtGui.QPixmap(self.pic_zgong[matrix[2][1]]))
            self.label_008.setPixmap(QtGui.QPixmap(self.pic_zgong[matrix[2][2]]))

    def init_zgong(self):
        self.num = 0
        self.env_zgong = np.zeros((3, 3), dtype=int)
        self.pic_zgong = []

        role_id_zgong = self.comboBox_5.currentIndex()
        pic_file = "pic/" + str(role_id_zgong) + ".jpg"
        pix = QtGui.QPixmap(pic_file)
        self.label_11.setPixmap(pix)
        self.label_11.setScaledContents(True)

        pic_list = cut_image(Image.open(pic_file), 3, 3)
        save_images(pic_list, [1, 2, 3, 8, 0, 4, 7, 6, 5])
        for i in range(9):
            self.pic_zgong.append(QtGui.QPixmap("temp/" + str(i) + ".jpg"))

        self.open_list_zgong = []
        self.closed_list_zgong = []
        self.path_zgong = []
        self.path__zgong = []
        self.check_state = []
        self.check_state_ = []

        self.label_000.setPixmap(QtGui.QPixmap(""))
        self.label_001.setPixmap(QtGui.QPixmap(""))
        self.label_002.setPixmap(QtGui.QPixmap(""))
        self.label_003.setPixmap(QtGui.QPixmap(""))
        self.label_004.setPixmap(QtGui.QPixmap(""))
        self.label_005.setPixmap(QtGui.QPixmap(""))
        self.label_006.setPixmap(QtGui.QPixmap(""))
        self.label_007.setPixmap(QtGui.QPixmap(""))
        self.label_008.setPixmap(QtGui.QPixmap(""))

    def check_state_zgong(self):
        self.check_state = []
        if self.checkBox_1.isChecked() and self.make_state:
            self.check_state.append(1)
            self.checkBox_1.hide()
        if self.checkBox_2.isChecked() and self.make_state:
            self.check_state.append(2)
            self.checkBox_2.hide()
        if self.checkBox_3.isChecked() and self.make_state:
            self.check_state.append(3)
            self.checkBox_3.hide()
        if self.checkBox_4.isChecked() and self.make_state:
            self.check_state.append(4)
            self.checkBox_4.hide()
        if self.checkBox_5.isChecked() and self.make_state:
            self.check_state.append(5)
            self.checkBox_5.hide()
        if self.checkBox_6.isChecked() and self.make_state:
            self.check_state.append(6)
            self.checkBox_6.hide()
        if self.checkBox_7.isChecked() and self.make_state:
            self.check_state.append(7)
            self.checkBox_7.hide()
        if self.checkBox_8.isChecked() and self.make_state:
            self.check_state.append(8)
            self.checkBox_8.hide()
        if self.checkBox_9.isChecked() and self.make_state:
            self.check_state.append(0)
            self.checkBox_9.hide()

    def reset_zgong(self):
        self.checkBox_1.setChecked(False)
        self.checkBox_2.setChecked(False)
        self.checkBox_3.setChecked(False)
        self.checkBox_4.setChecked(False)
        self.checkBox_5.setChecked(False)
        self.checkBox_6.setChecked(False)
        self.checkBox_7.setChecked(False)
        self.checkBox_8.setChecked(False)
        self.checkBox_9.setChecked(False)
        self.checkBox_1.show()
        self.checkBox_2.show()
        self.checkBox_3.show()
        self.checkBox_4.show()
        self.checkBox_5.show()
        self.checkBox_6.show()
        self.checkBox_7.show()
        self.checkBox_8.show()
        self.checkBox_9.show()
        self.label_000.setPixmap(QtGui.QPixmap(""))
        self.label_001.setPixmap(QtGui.QPixmap(""))
        self.label_002.setPixmap(QtGui.QPixmap(""))
        self.label_003.setPixmap(QtGui.QPixmap(""))
        self.label_004.setPixmap(QtGui.QPixmap(""))
        self.label_005.setPixmap(QtGui.QPixmap(""))
        self.label_006.setPixmap(QtGui.QPixmap(""))
        self.label_007.setPixmap(QtGui.QPixmap(""))
        self.label_008.setPixmap(QtGui.QPixmap(""))
        self.make_state = 1
        self.init_zgong()

    def make_zgong(self):
        if self.make_state:
            self.num += 1
            self.check_state_zgong()
            cur_num = list(set(self.check_state) ^ set(self.check_state_))[0]
            self.check_state_ = self.check_state
            index = [1, 2, 3, 8, 0, 4, 7, 6, 5].index(self.num)
            self.env_zgong[int(index / 3)][int(index % 3)] = cur_num
            if self.num == 1:
                self.label_000.setPixmap(QtGui.QPixmap(self.pic_zgong[cur_num]))
            elif self.num == 2:
                self.label_001.setPixmap(QtGui.QPixmap(self.pic_zgong[cur_num]))
            elif self.num == 3:
                self.label_002.setPixmap(QtGui.QPixmap(self.pic_zgong[cur_num]))
            elif self.num == 4:
                self.label_005.setPixmap(QtGui.QPixmap(self.pic_zgong[cur_num]))
            elif self.num == 5:
                self.label_008.setPixmap(QtGui.QPixmap(self.pic_zgong[cur_num]))
            elif self.num == 6:
                self.label_007.setPixmap(QtGui.QPixmap(self.pic_zgong[cur_num]))
            elif self.num == 7:
                self.label_006.setPixmap(QtGui.QPixmap(self.pic_zgong[cur_num]))
            elif self.num == 8:
                self.label_003.setPixmap(QtGui.QPixmap(self.pic_zgong[cur_num]))
                list_num = [0, 1, 2, 3, 4, 5, 6, 7, 8]
                env_ = self.env_zgong.flatten().tolist()
                del env_[4]
                print(env_)
                num = list(set(list_num) - set(env_))[0]
                self.env_zgong[1][1] = num
                self.make_state = 0
                self.change_zgong()
            print(self.env_zgong)

    def change_zgong(self):
        self.inv_zgong = main_9gong.invert_env(self.env_zgong)
        self.open_list_zgong = []
        self.closed_list_zgong = []
        self.path_zgong = []
        self.path__zgong = []
        print(self.env_zgong, self.inv_zgong)

        self.change_matrix_zgong(self.env_zgong)
        if self.inv_zgong:
            if self.env_zgong[0][0] != 0 and self.env_zgong[0][1] != 0:
                temp = np.copy(self.env_zgong[0][0])
                self.env_zgong[0][0] = np.copy(self.env_zgong[0][1])
                self.env_zgong[0][1] = temp
            else:
                temp = np.copy(self.env_zgong[1][0])
                self.env_zgong[1][0] = np.copy(self.env_zgong[1][1])
                self.env_zgong[1][1] = temp
            self.inv_zgong = 0
            _, self.path_zgong = main_9gong.A_remake_9gong(self.env_zgong, self.inv_zgong, self.open_list_zgong, self.closed_list_zgong, self.path_zgong)
            QtWidgets.QMessageBox.information(self, "标题", "找到到达相对状态的一种方法，将相邻两格调换顺序！",
                                              QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                              QtWidgets.QMessageBox.Yes)
            self.change_matrix_zgong(self.env_zgong)
        else:
            _, self.path_zgong = main_9gong.A_remake_9gong(self.env_zgong, self.inv_zgong, self.open_list_zgong, self.closed_list_zgong, self.path_zgong)
            QtWidgets.QMessageBox.information(self, "标题", "找到一种方法！", QtWidgets.QMessageBox.Yes |
                                              QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.Yes)
        self.lcdNumber_4.display(int(len(self.path_zgong)))
        self.lcdNumber_5.display(0)
        self.lcdNumber_6.display(int(len(self.path_zgong)))
        self.progressBar_2.setValue(0)

    def next_step_zgong(self):
        if len(self.path_zgong):
            self.change_matrix_zgong(self.path_zgong[0])
            self.path__zgong.append(self.path_zgong[0])
            del (self.path_zgong[0])

            self.lcdNumber_5.display(int(len(self.path__zgong)))
            self.lcdNumber_6.display(int(len(self.path_zgong)))
            self.progressBar_2.setValue(len(self.path__zgong) / self.lcdNumber_4.value() * 100)
            self.move_sound()
        else:
            if len(self.path__zgong) == 0:
                QtWidgets.QMessageBox.information(self, "标题", "本题目已经解决！", QtWidgets.QMessageBox.Yes |
                                                  QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.Yes)
                self.timer_zgong.stop()
            else:
                self.fill_matrix_zgong(self.path__zgong[-1])
                QtWidgets.QMessageBox.information(self, "标题", "九宫格已还原！", QtWidgets.QMessageBox.Yes |
                                                  QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.Yes)
                self.timer_zgong.stop()
            self.win_sound()

    def begin_zgong(self):
        self.timer_zgong.start()

    def pause_zgong(self):
        self.timer_zgong.stop()

    # ------------------------------ #

    def set_xgong(self):
        self.spinBox_2.setMinimum(self.spinBox.value())
        r = self.spinBox.value()
        c = self.spinBox_2.value()
        if r == 2:
            if c == 2:
                self.groupBox_22.show()
                self.groupBox_23.hide()
                self.groupBox_24.hide()
                self.groupBox_25.hide()
                self.groupBox_33.hide()
                self.groupBox_34.hide()
                self.groupBox_35.hide()
                self.groupBox_44.hide()
                self.groupBox_45.hide()
                self.groupBox_55.hide()
            elif c == 3:
                self.groupBox_22.hide()
                self.groupBox_23.show()
                self.groupBox_24.hide()
                self.groupBox_25.hide()
                self.groupBox_33.hide()
                self.groupBox_34.hide()
                self.groupBox_35.hide()
                self.groupBox_44.hide()
                self.groupBox_45.hide()
                self.groupBox_55.hide()
            elif c == 4:
                self.groupBox_22.hide()
                self.groupBox_23.hide()
                self.groupBox_24.show()
                self.groupBox_25.hide()
                self.groupBox_33.hide()
                self.groupBox_34.hide()
                self.groupBox_35.hide()
                self.groupBox_44.hide()
                self.groupBox_45.hide()
                self.groupBox_55.hide()
            else:
                self.groupBox_22.hide()
                self.groupBox_23.hide()
                self.groupBox_24.hide()
                self.groupBox_25.show()
                self.groupBox_33.hide()
                self.groupBox_34.hide()
                self.groupBox_35.hide()
                self.groupBox_44.hide()
                self.groupBox_45.hide()
                self.groupBox_55.hide()
        elif r == 3:
            if c == 3:
                self.groupBox_22.hide()
                self.groupBox_23.hide()
                self.groupBox_24.hide()
                self.groupBox_25.hide()
                self.groupBox_33.show()
                self.groupBox_34.hide()
                self.groupBox_35.hide()
                self.groupBox_44.hide()
                self.groupBox_45.hide()
                self.groupBox_55.hide()
            elif c == 4:
                self.groupBox_22.hide()
                self.groupBox_23.hide()
                self.groupBox_24.hide()
                self.groupBox_25.hide()
                self.groupBox_33.hide()
                self.groupBox_34.show()
                self.groupBox_35.hide()
                self.groupBox_44.hide()
                self.groupBox_45.hide()
                self.groupBox_55.hide()
            else:
                self.groupBox_22.hide()
                self.groupBox_23.hide()
                self.groupBox_24.hide()
                self.groupBox_25.hide()
                self.groupBox_33.hide()
                self.groupBox_34.hide()
                self.groupBox_35.show()
                self.groupBox_44.hide()
                self.groupBox_45.hide()
                self.groupBox_55.hide()
        elif r == 4:
            if c == 4:
                self.groupBox_22.hide()
                self.groupBox_23.hide()
                self.groupBox_24.hide()
                self.groupBox_25.hide()
                self.groupBox_33.hide()
                self.groupBox_34.hide()
                self.groupBox_35.hide()
                self.groupBox_44.show()
                self.groupBox_45.hide()
                self.groupBox_55.hide()
            else:
                self.groupBox_22.hide()
                self.groupBox_23.hide()
                self.groupBox_24.hide()
                self.groupBox_25.hide()
                self.groupBox_33.hide()
                self.groupBox_34.hide()
                self.groupBox_35.hide()
                self.groupBox_44.hide()
                self.groupBox_45.show()
                self.groupBox_55.hide()
        else:
            self.groupBox_22.hide()
            self.groupBox_23.hide()
            self.groupBox_24.hide()
            self.groupBox_25.hide()
            self.groupBox_33.hide()
            self.groupBox_34.hide()
            self.groupBox_35.hide()
            self.groupBox_44.hide()
            self.groupBox_45.hide()
            self.groupBox_55.show()

    def change_matrix_xgong(self, matrix):
        if matrix.shape[0] == 2 and matrix.shape[1] == 2:
            if matrix[0][0]:
                self.label.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][0]]))
            else:
                self.label.setPixmap(QtGui.QPixmap(""))
            if matrix[0][1]:
                self.label_3.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][1]]))
            else:
                self.label_3.setPixmap(QtGui.QPixmap(""))
            if matrix[1][0]:
                self.label_21.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][0]]))
            else:
                self.label_21.setPixmap(QtGui.QPixmap(""))
            if matrix[1][1]:
                self.label_22.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][1]]))
            else:
                self.label_22.setPixmap(QtGui.QPixmap(""))
        if matrix.shape[0] == 2 and matrix.shape[1] == 3:
            if matrix[0][0]:
                self.label_55.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][0]]))
            else:
                self.label_55.setPixmap(QtGui.QPixmap(""))

            if matrix[0][1]:
                self.label_56.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][1]]))
            else:
                self.label_56.setPixmap(QtGui.QPixmap(""))

            if matrix[0][2]:
                self.label_48.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][2]]))
            else:
                self.label_48.setPixmap(QtGui.QPixmap(""))

            if matrix[1][0]:
                self.label_49.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][0]]))
            else:
                self.label_49.setPixmap(QtGui.QPixmap(""))

            if matrix[1][1]:
                self.label_50.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][1]]))
            else:
                self.label_50.setPixmap(QtGui.QPixmap(""))

            if matrix[1][2]:
                self.label_52.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][2]]))
            else:
                self.label_52.setPixmap(QtGui.QPixmap(""))
        if matrix.shape[0] == 2 and matrix.shape[1] == 4:
            if matrix[0][0]:
                self.label_61.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][0]]))
            else:
                self.label_61.setPixmap(QtGui.QPixmap(""))

            if matrix[0][1]:
                self.label_62.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][1]]))
            else:
                self.label_62.setPixmap(QtGui.QPixmap(""))

            if matrix[0][2]:
                self.label_51.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][2]]))
            else:
                self.label_51.setPixmap(QtGui.QPixmap(""))

            if matrix[0][3]:
                self.label_57.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][3]]))
            else:
                self.label_57.setPixmap(QtGui.QPixmap(""))

            if matrix[1][0]:
                self.label_53.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][0]]))
            else:
                self.label_53.setPixmap(QtGui.QPixmap(""))

            if matrix[1][1]:
                self.label_54.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][1]]))
            else:
                self.label_54.setPixmap(QtGui.QPixmap(""))

            if matrix[1][2]:
                self.label_58.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][2]]))
            else:
                self.label_58.setPixmap(QtGui.QPixmap(""))

            if matrix[1][3]:
                self.label_59.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][3]]))
            else:
                self.label_59.setPixmap(QtGui.QPixmap(""))
        if matrix.shape[0] == 2 and matrix.shape[1] == 5:
            if matrix[0][0]:
                self.label_111.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][0]]))
            else:
                self.label_111.setPixmap(QtGui.QPixmap(""))

            if matrix[0][1]:
                self.label_90.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][1]]))
            else:
                self.label_90.setPixmap(QtGui.QPixmap(""))

            if matrix[0][2]:
                self.label_95.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][2]]))
            else:
                self.label_95.setPixmap(QtGui.QPixmap(""))

            if matrix[0][3]:
                self.label_109.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][3]]))
            else:
                self.label_109.setPixmap(QtGui.QPixmap(""))

            if matrix[0][4]:
                self.label_112.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][4]]))
            else:
                self.label_112.setPixmap(QtGui.QPixmap(""))

            if matrix[1][0]:
                self.label_94.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][0]]))
            else:
                self.label_94.setPixmap(QtGui.QPixmap(""))

            if matrix[1][1]:
                self.label_97.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][1]]))
            else:
                self.label_97.setPixmap(QtGui.QPixmap(""))

            if matrix[1][2]:
                self.label_110.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][2]]))
            else:
                self.label_110.setPixmap(QtGui.QPixmap(""))

            if matrix[1][3]:
                self.label_96.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][3]]))
            else:
                self.label_96.setPixmap(QtGui.QPixmap(""))

            if matrix[1][4]:
                self.label_92.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][4]]))
            else:
                self.label_92.setPixmap(QtGui.QPixmap(""))

        if matrix.shape[0] == 3 and matrix.shape[1] == 3:
            if matrix[0][0]:
                self.label_2.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][0]]))
            else:
                self.label_2.setPixmap(QtGui.QPixmap(""))

            if matrix[0][1]:
                self.label_42.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][1]]))
            else:
                self.label_42.setPixmap(QtGui.QPixmap(""))

            if matrix[0][2]:
                self.label_45.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][2]]))
            else:
                self.label_45.setPixmap(QtGui.QPixmap(""))

            if matrix[1][0]:
                self.label_24.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][0]]))
            else:
                self.label_24.setPixmap(QtGui.QPixmap(""))

            if matrix[1][1]:
                self.label_23.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][1]]))
            else:
                self.label_23.setPixmap(QtGui.QPixmap(""))

            if matrix[1][2]:
                self.label_46.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][2]]))
            else:
                self.label_46.setPixmap(QtGui.QPixmap(""))

            if matrix[2][0]:
                self.label_43.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[2][0]]))
            else:
                self.label_43.setPixmap(QtGui.QPixmap(""))

            if matrix[2][1]:
                self.label_44.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[2][1]]))
            else:
                self.label_44.setPixmap(QtGui.QPixmap(""))

            if matrix[2][2]:
                self.label_47.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[2][2]]))
            else:
                self.label_47.setPixmap(QtGui.QPixmap(""))
        if matrix.shape[0] == 3 and matrix.shape[1] == 4:
            if matrix[0][0]:
                self.label_70.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][0]]))
            else:
                self.label_70.setPixmap(QtGui.QPixmap(""))

            if matrix[0][1]:
                self.label_71.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][1]]))
            else:
                self.label_71.setPixmap(QtGui.QPixmap(""))

            if matrix[0][2]:
                self.label_63.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][2]]))
            else:
                self.label_63.setPixmap(QtGui.QPixmap(""))

            if matrix[0][3]:
                self.label_72.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][3]]))
            else:
                self.label_72.setPixmap(QtGui.QPixmap(""))

            if matrix[1][0]:
                self.label_64.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][0]]))
            else:
                self.label_64.setPixmap(QtGui.QPixmap(""))

            if matrix[1][1]:
                self.label_65.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][1]]))
            else:
                self.label_65.setPixmap(QtGui.QPixmap(""))

            if matrix[1][2]:
                self.label_67.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][2]]))
            else:
                self.label_67.setPixmap(QtGui.QPixmap(""))

            if matrix[1][3]:
                self.label_73.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][3]]))
            else:
                self.label_73.setPixmap(QtGui.QPixmap(""))

            if matrix[2][0]:
                self.label_66.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[2][0]]))
            else:
                self.label_66.setPixmap(QtGui.QPixmap(""))

            if matrix[2][1]:
                self.label_68.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[2][1]]))
            else:
                self.label_68.setPixmap(QtGui.QPixmap(""))

            if matrix[2][2]:
                self.label_69.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[2][2]]))
            else:
                self.label_69.setPixmap(QtGui.QPixmap(""))

            if matrix[2][3]:
                self.label_74.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[2][3]]))
            else:
                self.label_74.setPixmap(QtGui.QPixmap(""))
        if matrix.shape[0] == 3 and matrix.shape[1] == 5:
            if matrix[0][0]:
                self.label_83.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][0]]))
            else:
                self.label_83.setPixmap(QtGui.QPixmap(""))

            if matrix[0][1]:
                self.label_86.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][1]]))
            else:
                self.label_86.setPixmap(QtGui.QPixmap(""))

            if matrix[0][2]:
                self.label_85.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][2]]))
            else:
                self.label_85.setPixmap(QtGui.QPixmap(""))

            if matrix[0][3]:
                self.label_84.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][3]]))
            else:
                self.label_84.setPixmap(QtGui.QPixmap(""))

            if matrix[0][4]:
                self.label_87.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][4]]))
            else:
                self.label_87.setPixmap(QtGui.QPixmap(""))

            if matrix[1][0]:
                self.label_79.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][0]]))
            else:
                self.label_79.setPixmap(QtGui.QPixmap(""))

            if matrix[1][1]:
                self.label_76.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][1]]))
            else:
                self.label_76.setPixmap(QtGui.QPixmap(""))

            if matrix[1][2]:
                self.label_82.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][2]]))
            else:
                self.label_82.setPixmap(QtGui.QPixmap(""))

            if matrix[1][3]:
                self.label_78.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][3]]))
            else:
                self.label_78.setPixmap(QtGui.QPixmap(""))

            if matrix[1][4]:
                self.label_88.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][4]]))
            else:
                self.label_88.setPixmap(QtGui.QPixmap(""))

            if matrix[2][0]:
                self.label_75.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[2][0]]))
            else:
                self.label_75.setPixmap(QtGui.QPixmap(""))

            if matrix[2][1]:
                self.label_80.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[2][1]]))
            else:
                self.label_80.setPixmap(QtGui.QPixmap(""))

            if matrix[2][2]:
                self.label_81.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[2][2]]))
            else:
                self.label_81.setPixmap(QtGui.QPixmap(""))

            if matrix[2][3]:
                self.label_77.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[2][3]]))
            else:
                self.label_77.setPixmap(QtGui.QPixmap(""))

            if matrix[2][4]:
                self.label_89.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[2][4]]))
            else:
                self.label_89.setPixmap(QtGui.QPixmap(""))

        if matrix.shape[0] == 4 and matrix.shape[1] == 4:
            if matrix[0][0]:
                self.label_178.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][0]]))
            else:
                self.label_178.setPixmap(QtGui.QPixmap(""))

            if matrix[0][1]:
                self.label_174.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][1]]))
            else:
                self.label_174.setPixmap(QtGui.QPixmap(""))

            if matrix[0][2]:
                self.label_157.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][2]]))
            else:
                self.label_157.setPixmap(QtGui.QPixmap(""))

            if matrix[0][3]:
                self.label_171.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][3]]))
            else:
                self.label_171.setPixmap(QtGui.QPixmap(""))

            if matrix[1][0]:
                self.label_162.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][0]]))
            else:
                self.label_162.setPixmap(QtGui.QPixmap(""))

            if matrix[1][1]:
                self.label_158.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][1]]))
            else:
                self.label_158.setPixmap(QtGui.QPixmap(""))

            if matrix[1][2]:
                self.label_167.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][2]]))
            else:
                self.label_167.setPixmap(QtGui.QPixmap(""))

            if matrix[1][3]:
                self.label_166.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][3]]))
            else:
                self.label_166.setPixmap(QtGui.QPixmap(""))

            if matrix[2][0]:
                self.label_154.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[2][0]]))
            else:
                self.label_154.setPixmap(QtGui.QPixmap(""))

            if matrix[2][1]:
                self.label_173.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[2][1]]))
            else:
                self.label_173.setPixmap(QtGui.QPixmap(""))

            if matrix[2][2]:
                self.label_160.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[2][2]]))
            else:
                self.label_160.setPixmap(QtGui.QPixmap(""))

            if matrix[2][3]:
                self.label_175.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[2][3]]))
            else:
                self.label_175.setPixmap(QtGui.QPixmap(""))

            if matrix[3][0]:
                self.label_168.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[3][0]]))
            else:
                self.label_168.setPixmap(QtGui.QPixmap(""))

            if matrix[3][1]:
                self.label_156.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[3][1]]))
            else:
                self.label_156.setPixmap(QtGui.QPixmap(""))

            if matrix[3][2]:
                self.label_172.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[3][2]]))
            else:
                self.label_172.setPixmap(QtGui.QPixmap(""))

            if matrix[3][3]:
                self.label_177.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[3][3]]))
            else:
                self.label_177.setPixmap(QtGui.QPixmap(""))
        if matrix.shape[0] == 4 and matrix.shape[1] == 5:
            if matrix[0][0]:
                self.label_121.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][0]]))
            else:
                self.label_121.setPixmap(QtGui.QPixmap(""))

            if matrix[0][1]:
                self.label_91.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][1]]))
            else:
                self.label_91.setPixmap(QtGui.QPixmap(""))

            if matrix[0][2]:
                self.label_114.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][2]]))
            else:
                self.label_114.setPixmap(QtGui.QPixmap(""))

            if matrix[0][3]:
                self.label_119.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][3]]))
            else:
                self.label_119.setPixmap(QtGui.QPixmap(""))

            if matrix[0][4]:
                self.label_122.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][4]]))
            else:
                self.label_122.setPixmap(QtGui.QPixmap(""))

            if matrix[1][0]:
                self.label_113.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][0]]))
            else:
                self.label_113.setPixmap(QtGui.QPixmap(""))

            if matrix[1][1]:
                self.label_116.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][1]]))
            else:
                self.label_116.setPixmap(QtGui.QPixmap(""))

            if matrix[1][2]:
                self.label_120.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][2]]))
            else:
                self.label_120.setPixmap(QtGui.QPixmap(""))

            if matrix[1][3]:
                self.label_115.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][3]]))
            else:
                self.label_115.setPixmap(QtGui.QPixmap(""))

            if matrix[1][4]:
                self.label_98.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][4]]))
            else:
                self.label_98.setPixmap(QtGui.QPixmap(""))

            if matrix[2][0]:
                self.label_93.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[2][0]]))
            else:
                self.label_93.setPixmap(QtGui.QPixmap(""))

            if matrix[2][1]:
                self.label_118.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[2][1]]))
            else:
                self.label_118.setPixmap(QtGui.QPixmap(""))

            if matrix[2][2]:
                self.label_99.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[2][2]]))
            else:
                self.label_99.setPixmap(QtGui.QPixmap(""))

            if matrix[2][3]:
                self.label_123.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[2][3]]))
            else:
                self.label_123.setPixmap(QtGui.QPixmap(""))

            if matrix[2][4]:
                self.label_117.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[2][4]]))
            else:
                self.label_117.setPixmap(QtGui.QPixmap(""))

            if matrix[3][0]:
                self.label_124.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[3][0]]))
            else:
                self.label_124.setPixmap(QtGui.QPixmap(""))

            if matrix[3][1]:
                self.label_125.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[3][1]]))
            else:
                self.label_125.setPixmap(QtGui.QPixmap(""))

            if matrix[3][2]:
                self.label_126.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[3][2]]))
            else:
                self.label_126.setPixmap(QtGui.QPixmap(""))

            if matrix[3][3]:
                self.label_127.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[3][3]]))
            else:
                self.label_127.setPixmap(QtGui.QPixmap(""))

            if matrix[3][4]:
                self.label_128.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[3][4]]))
            else:
                self.label_128.setPixmap(QtGui.QPixmap(""))

        if matrix.shape[0] == 5 and matrix.shape[1] == 5:
            if matrix[0][0]:
                self.label_145.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][0]]))
            else:
                self.label_145.setPixmap(QtGui.QPixmap(""))

            if matrix[0][1]:
                self.label_139.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][1]]))
            else:
                self.label_139.setPixmap(QtGui.QPixmap(""))

            if matrix[0][2]:
                self.label_140.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][2]]))
            else:
                self.label_140.setPixmap(QtGui.QPixmap(""))

            if matrix[0][3]:
                self.label_147.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][3]]))
            else:
                self.label_147.setPixmap(QtGui.QPixmap(""))

            if matrix[0][4]:
                self.label_130.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][4]]))
            else:
                self.label_130.setPixmap(QtGui.QPixmap(""))

            if matrix[1][0]:
                self.label_134.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][0]]))
            else:
                self.label_134.setPixmap(QtGui.QPixmap(""))

            if matrix[1][1]:
                self.label_143.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][1]]))
            else:
                self.label_143.setPixmap(QtGui.QPixmap(""))

            if matrix[1][2]:
                self.label_146.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][2]]))
            else:
                self.label_146.setPixmap(QtGui.QPixmap(""))

            if matrix[1][3]:
                self.label_148.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][3]]))
            else:
                self.label_148.setPixmap(QtGui.QPixmap(""))

            if matrix[1][4]:
                self.label_144.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][4]]))
            else:
                self.label_144.setPixmap(QtGui.QPixmap(""))

            if matrix[2][0]:
                self.label_141.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[2][0]]))
            else:
                self.label_141.setPixmap(QtGui.QPixmap(""))

            if matrix[2][1]:
                self.label_135.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[2][1]]))
            else:
                self.label_135.setPixmap(QtGui.QPixmap(""))

            if matrix[2][2]:
                self.label_133.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[2][2]]))
            else:
                self.label_133.setPixmap(QtGui.QPixmap(""))

            if matrix[2][3]:
                self.label_136.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[2][3]]))
            else:
                self.label_136.setPixmap(QtGui.QPixmap(""))

            if matrix[2][4]:
                self.label_142.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[2][4]]))
            else:
                self.label_142.setPixmap(QtGui.QPixmap(""))

            if matrix[3][0]:
                self.label_137.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[3][0]]))
            else:
                self.label_137.setPixmap(QtGui.QPixmap(""))

            if matrix[3][1]:
                self.label_131.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[3][1]]))
            else:
                self.label_131.setPixmap(QtGui.QPixmap(""))

            if matrix[3][2]:
                self.label_129.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[3][2]]))
            else:
                self.label_129.setPixmap(QtGui.QPixmap(""))

            if matrix[3][3]:
                self.label_138.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[3][3]]))
            else:
                self.label_138.setPixmap(QtGui.QPixmap(""))

            if matrix[3][4]:
                self.label_132.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[3][4]]))
            else:
                self.label_132.setPixmap(QtGui.QPixmap(""))

            if matrix[4][0]:
                self.label_149.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[4][0]]))
            else:
                self.label_149.setPixmap(QtGui.QPixmap(""))

            if matrix[4][1]:
                self.label_150.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[4][1]]))
            else:
                self.label_150.setPixmap(QtGui.QPixmap(""))

            if matrix[4][2]:
                self.label_151.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[4][2]]))
            else:
                self.label_151.setPixmap(QtGui.QPixmap(""))

            if matrix[4][3]:
                self.label_152.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[4][3]]))
            else:
                self.label_152.setPixmap(QtGui.QPixmap(""))

            if matrix[4][4]:
                self.label_153.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[4][4]]))
            else:
                self.label_153.setPixmap(QtGui.QPixmap(""))

    def fill_matrix_xgong(self, matrix):
        if matrix.shape[0] == 2 and matrix.shape[1] == 2:
            self.label.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][0]]))
            self.label_3.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][1]]))
            self.label_21.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][0]]))
            self.label_22.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][1]]))
        if matrix.shape[0] == 2 and matrix.shape[1] == 3:
            self.label_55.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][0]]))
            self.label_56.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][1]]))
            self.label_48.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][2]]))
            self.label_49.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][0]]))
            self.label_50.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][1]]))
            self.label_52.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][2]]))
        if matrix.shape[0] == 2 and matrix.shape[1] == 4:
            self.label_61.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][0]]))
            self.label_62.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][1]]))
            self.label_51.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][2]]))
            self.label_57.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][3]]))
            self.label_53.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][0]]))
            self.label_54.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][1]]))
            self.label_58.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][2]]))
            self.label_59.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][3]]))
        if matrix.shape[0] == 2 and matrix.shape[1] == 5:
            self.label_110.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][0]]))
            self.label_90.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][1]]))
            self.label_95.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][2]]))
            self.label_109.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][3]]))
            self.label_112.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][4]]))
            self.label_94.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][0]]))
            self.label_97.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][1]]))
            self.label_110.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][2]]))
            self.label_96.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][3]]))
            self.label_92.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][4]]))
        if matrix.shape[0] == 3 and matrix.shape[1] == 3:
            self.label_2.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][0]]))
            self.label_42.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][1]]))
            self.label_45.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][2]]))
            self.label_24.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][0]]))
            self.label_23.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][1]]))
            self.label_46.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][2]]))
            self.label_43.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[2][0]]))
            self.label_44.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[2][1]]))
            self.label_47.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[2][2]]))
        if matrix.shape[0] == 3 and matrix.shape[1] == 4:
            self.label_70.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][0]]))
            self.label_71.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][1]]))
            self.label_63.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][2]]))
            self.label_72.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][3]]))
            self.label_64.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][0]]))
            self.label_65.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][1]]))
            self.label_67.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][2]]))
            self.label_73.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][3]]))
            self.label_66.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[2][0]]))
            self.label_68.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[2][1]]))
            self.label_69.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[2][2]]))
            self.label_74.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[2][3]]))
        if matrix.shape[0] == 3 and matrix.shape[1] == 5:
            self.label_83.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][0]]))
            self.label_86.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][1]]))
            self.label_85.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][2]]))
            self.label_84.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][3]]))
            self.label_87.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][4]]))
            self.label_79.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][0]]))
            self.label_76.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][1]]))
            self.label_82.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][2]]))
            self.label_78.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][3]]))
            self.label_88.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][4]]))
            self.label_75.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[2][0]]))
            self.label_80.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[2][1]]))
            self.label_81.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[2][2]]))
            self.label_77.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[2][3]]))
            self.label_89.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[2][4]]))
        if matrix.shape[0] == 4 and matrix.shape[1] == 4:
            self.label_178.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][0]]))
            self.label_174.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][1]]))
            self.label_157.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][2]]))
            self.label_171.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][3]]))
            self.label_162.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][0]]))
            self.label_158.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][1]]))
            self.label_167.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][2]]))
            self.label_166.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][3]]))
            self.label_154.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[2][0]]))
            self.label_173.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[2][1]]))
            self.label_160.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[2][2]]))
            self.label_175.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[2][3]]))
            self.label_168.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[3][0]]))
            self.label_156.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[3][1]]))
            self.label_172.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[3][2]]))
            self.label_177.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[3][3]]))
        if matrix.shape[0] == 4 and matrix.shape[1] == 5:
            self.label_121.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][0]]))
            self.label_91.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][1]]))
            self.label_114.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][2]]))
            self.label_119.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][3]]))
            self.label_122.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][4]]))
            self.label_113.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][0]]))
            self.label_116.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][1]]))
            self.label_120.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][2]]))
            self.label_115.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][3]]))
            self.label_98.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][4]]))
            self.label_93.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[2][0]]))
            self.label_118.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[2][1]]))
            self.label_99.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[2][2]]))
            self.label_123.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[2][3]]))
            self.label_117.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[2][4]]))
            self.label_124.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[3][0]]))
            self.label_125.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[3][1]]))
            self.label_126.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[3][2]]))
            self.label_127.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[3][3]]))
            self.label_128.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[3][4]]))
        if matrix.shape[0] == 5 and matrix.shape[1] == 5:
            self.label_145.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][0]]))
            self.label_139.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][1]]))
            self.label_140.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][2]]))
            self.label_147.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][3]]))
            self.label_130.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[0][4]]))
            self.label_134.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][0]]))
            self.label_143.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][1]]))
            self.label_146.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][2]]))
            self.label_148.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][3]]))
            self.label_144.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[1][4]]))
            self.label_141.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[2][0]]))
            self.label_135.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[2][1]]))
            self.label_133.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[2][2]]))
            self.label_136.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[2][3]]))
            self.label_142.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[2][4]]))
            self.label_137.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[3][0]]))
            self.label_131.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[3][1]]))
            self.label_129.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[3][2]]))
            self.label_138.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[3][3]]))
            self.label_132.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[3][4]]))
            self.label_149.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[4][0]]))
            self.label_150.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[4][1]]))
            self.label_151.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[4][2]]))
            self.label_152.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[4][3]]))
            self.label_153.setPixmap(QtGui.QPixmap(self.pic_xgong[matrix[4][4]]))

    def init_xgong(self):
        self.M = self.spinBox.value()
        self.N = self.spinBox_2.value()
        self.env_xgong = main_xgong.init_env(self.M, self.N)
        self.des_env_xgong = main_xgong.des_env(self.M, self.N)
        if main_xgong.invert_env(self.env_xgong) == main_xgong.invert_env(self.des_env_xgong[0]):
            self.inv_xgong = 0
        else:
            self.inv_xgong = 1
        # self.state_xgong = main_xgong.state(self.M, self.N)[self.inv_xgong]
        self.path_xgong = []
        self.pic_xgong = []
        print(self.env_xgong, self.inv_xgong)

        pic_file = "pic/wzxg.jpeg"
        pic_list = cut_image(Image.open(pic_file), self.M, self.N)
        list_ = list(range(1, self.M * self.N)) + [0]
        print(list_, self.M, self.N)
        save_images(pic_list, list_)
        for i in range(self.M * self.N):
            self.pic_xgong.append(QtGui.QPixmap("temp/" + str(i) + ".jpg"))

        self.change_matrix_xgong(self.env_xgong)

    def search_xgong_A(self):
        self.pushButton_11.setEnabled(True)
        self.pushButton_12.setEnabled(True)
        if self.inv_xgong:
            if self.env_xgong[0][0] != 0 and self.env_xgong[0][1] != 0:
                temp = np.copy(self.env_xgong[0][0])
                self.env_xgong[0][0] = np.copy(self.env_xgong[0][1])
                self.env_xgong[0][1] = temp
            else:
                temp = np.copy(self.env_xgong[1][0])
                self.env_xgong[1][0] = np.copy(self.env_xgong[1][1])
                self.env_xgong[1][1] = temp
            self.inv_xgong = 0
            _, self.path_xgong = main_xgong.C_remake_xgong(self.env_xgong, self.inv_xgong, self.des_env_xgong)
            QtWidgets.QMessageBox.information(self, "标题", "找到到达相对状态的一种方法，将相邻两格调换顺序！",
                                              QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                              QtWidgets.QMessageBox.Yes)
            self.change_matrix_xgong(self.env_xgong)
        else:
            _, self.path_xgong = main_xgong.C_remake_xgong(self.env_xgong, self.inv_xgong, self.des_env_xgong)
            QtWidgets.QMessageBox.information(self, "标题", "找到一种方法！",
                                              QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                              QtWidgets.QMessageBox.Yes)
        self.lcdNumber_7.display(int(len(self.path_xgong)))
        self.lcdNumber_8.display(0)
        self.lcdNumber_9.display(int(len(self.path_xgong)))
        self.progressBar_3.setValue(0)

    def search_xgong_B(self):
        self.pushButton_11.setEnabled(True)
        self.pushButton_12.setEnabled(True)
        if self.inv_xgong:
            if self.env_xgong[0][0] != 0 and self.env_xgong[0][1] != 0:
                temp = np.copy(self.env_xgong[0][0])
                self.env_xgong[0][0] = np.copy(self.env_xgong[0][1])
                self.env_xgong[0][1] = temp
            else:
                temp = np.copy(self.env_xgong[1][0])
                self.env_xgong[1][0] = np.copy(self.env_xgong[1][1])
                self.env_xgong[1][1] = temp
            self.inv_xgong = 0
            self.path_xgong = main_xgong.B_remake_xgong(self.env_xgong, self.inv_xgong)
            QtWidgets.QMessageBox.information(self, "标题", "找到到达相对状态的一种方法，将相邻两格调换顺序！",
                                              QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                              QtWidgets.QMessageBox.Yes)
            self.change_matrix_xgong(self.env_xgong)
        else:
            self.path_xgong = main_xgong.B_remake_xgong(self.env_xgong, self.inv_xgong)
            QtWidgets.QMessageBox.information(self, "标题", "找到一种方法！",
                                              QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                              QtWidgets.QMessageBox.Yes)
        self.lcdNumber_7.display(int(len(self.path_xgong)))
        self.lcdNumber_8.display(0)
        self.lcdNumber_9.display(int(len(self.path_xgong)))
        self.progressBar_3.setValue(0)

    def search_xgong_D(self):
        self.pushButton_11.setEnabled(True)
        self.pushButton_12.setEnabled(True)
        if self.inv_xgong:
            if self.env_xgong[0][0] != 0 and self.env_xgong[0][1] != 0:
                temp = np.copy(self.env_xgong[0][0])
                self.env_xgong[0][0] = np.copy(self.env_xgong[0][1])
                self.env_xgong[0][1] = temp
            else:
                temp = np.copy(self.env_xgong[1][0])
                self.env_xgong[1][0] = np.copy(self.env_xgong[1][1])
                self.env_xgong[1][1] = temp
            self.inv_xgong = 0
            self.path_xgong = main_xgong.D_remake_xgong(self.env_xgong, self.inv_xgong)
            QtWidgets.QMessageBox.information(self, "标题", "找到到达相对状态的一种方法，将相邻两格调换顺序！",
                                              QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                              QtWidgets.QMessageBox.Yes)
            self.change_matrix_xgong(self.env_xgong)
        else:
            self.path_xgong = main_xgong.D_remake_xgong(self.env_xgong, self.inv_xgong)
            QtWidgets.QMessageBox.information(self, "标题", "找到一种方法！",
                                              QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                              QtWidgets.QMessageBox.Yes)
        self.lcdNumber_7.display(int(len(self.path_xgong)))
        self.lcdNumber_8.display(0)
        self.lcdNumber_9.display(int(len(self.path_xgong)))
        self.progressBar_3.setValue(0)

    def next_step_xgong(self):
        if len(self.path_xgong):
            self.change_matrix_xgong(self.path_xgong[0])
            self.path_temp = self.path_xgong[0]
            del (self.path_xgong[0])
            self.lcdNumber_8.display(int(self.lcdNumber_7.value() - self.lcdNumber_9.value()) + 1)
            self.lcdNumber_9.display(int(len(self.path_xgong)))
            self.progressBar_3.setValue(int(self.lcdNumber_8.value()) / self.lcdNumber_7.value() * 100)
            self.move_sound()
        else:
            if self.lcdNumber_8.value() == 0:
                QtWidgets.QMessageBox.information(self, "标题", "本题目已经解决！", QtWidgets.QMessageBox.Yes |
                                                  QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.Yes)
                self.timer_xgong.stop()
            else:
                self.fill_matrix_xgong(self.path_temp)
                str_ = str(self.M) + "×" + str(self.N) + "宫格已还原！"
                QtWidgets.QMessageBox.information(self, "标题", str_, QtWidgets.QMessageBox.Yes |
                                                  QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.Yes)
                self.timer_xgong.stop()
            self.win_sound()

    def begin_xgong(self):
        self.timer_xgong.start()

    def pause_xgong(self):
        self.timer_xgong.stop()

    # ------------------------------ #

    def init_dgong(self):
        self.remove_dgong()
        self.env_dgong = main_9gong.init_env()
        # self.env_dgong = np.array([[1, 2, 3],
        #                            [8, 0, 5],
        #                            [7, 4, 6]])
        self.env_vector_dgong = np.copy(self.env_dgong)
        self.null_dgong = np.argwhere(self.env_vector_dgong == 0)[0]
        print(self.null_dgong)
        self.inv_dgong = main_9gong.invert_env(self.env_dgong)
        self.open_list_dgong = []
        self.closed_list_dgong = []
        self.path_dgong = []
        self.path__dgong = []
        self.pic_dgong = []
        self.step_dgong = 0
        self.time_dgong = 0
        self.position_dgong = np.array([[[11,  81], [196,  81], [380,  81]],
                                        [[11, 218], [196, 218], [380, 218]],
                                        [[11, 355], [196, 355], [380, 355]]])
        self.label_set = np.array([[self.label_199, self.label_190, self.label_203],
                                   [self.label_189, self.label_191, self.label_188],
                                   [self.label_184, self.label_195, self.label_198]])
        self.label_set_ = [self.label_199, self.label_190, self.label_203,
                           self.label_189, self.label_191, self.label_188,
                           self.label_184, self.label_195, self.label_198]

        role_id_dgong = self.comboBox_6.currentIndex()
        pic_file = "pic/" + str(role_id_dgong) + ".jpg"
        pix = QtGui.QPixmap(pic_file)
        self.label_196.setPixmap(pix)
        self.label_196.setScaledContents(True)
        pic_list = cut_image(Image.open(pic_file), 3, 3)
        save_images(pic_list, [1, 2, 3, 8, 0, 4, 7, 6, 5])
        for i in range(9):
            self.pic_dgong.append(QtGui.QPixmap("temp/" + str(i) + ".jpg"))

        if self.inv_dgong:
            if self.env_dgong[0][0] != 0 and self.env_dgong[0][1] != 0:
                temp = np.copy(self.env_dgong[0][0])
                self.env_dgong[0][0] = np.copy(self.env_dgong[0][1])
                self.env_dgong[0][1] = temp
            else:
                temp = np.copy(self.env_dgong[1][0])
                self.env_dgong[1][0] = np.copy(self.env_dgong[1][1])
                self.env_dgong[1][1] = temp
            self.inv_dgong = 0
        self.change_matrix_dgong(self.env_dgong)
        _, self.path_dgong = main_9gong.A_remake_9gong(self.env_dgong, self.inv_dgong, self.open_list_dgong, self.closed_list_dgong, self.path_dgong)
        self.lcdNumber_10.display(int(len(self.path_dgong)) + 1)
        self.lcdNumber_11.display(self.step_dgong)
        self.lcdNumber_12.display(self.time_dgong)

    def remove_dgong(self):
        self.label_199.move(11, 81)
        self.label_190.move(196, 81)
        self.label_203.move(380, 81)
        self.label_189.move(11, 218)
        self.label_191.move(196, 218)
        self.label_188.move(380, 218)
        self.label_184.move(11, 355)
        self.label_195.move(196, 355)
        self.label_198.move(380, 355)

    def act_dgong(self, label_1, label_2, pos_1, pos_2):
        label_1.raise_()
        self.animation_1 = QtCore.QPropertyAnimation(label_1, b'pos')
        self.animation_1.setDuration(100)
        self.animation_1.setStartValue(QtCore.QPoint(pos_1[0], pos_1[1]))
        self.animation_1.setEndValue(QtCore.QPoint(pos_2[0], pos_2[1]))
        self.animation_1.setLoopCount(1)

        self.animation_2 = QtCore.QPropertyAnimation(label_2, b'pos')
        self.animation_2.setDuration(100)
        self.animation_2.setStartValue(QtCore.QPoint(pos_2[0], pos_2[1]))
        self.animation_2.setEndValue(QtCore.QPoint(pos_1[0], pos_1[1]))
        self.animation_2.setLoopCount(1)

        self.animation_1.start()
        self.animation_2.start()

    def change_matrix_dgong(self, matrix):
        if matrix[0][0]:
            self.label_199.setPixmap(QtGui.QPixmap(self.pic_dgong[matrix[0][0]]))
        else:
            self.label_199.setPixmap(QtGui.QPixmap(""))

        if matrix[0][1]:
            self.label_190.setPixmap(QtGui.QPixmap(self.pic_dgong[matrix[0][1]]))
        else:
            self.label_190.setPixmap(QtGui.QPixmap(""))

        if matrix[0][2]:
            self.label_203.setPixmap(QtGui.QPixmap(self.pic_dgong[matrix[0][2]]))
        else:
            self.label_203.setPixmap(QtGui.QPixmap(""))

        if matrix[1][0]:
            self.label_189.setPixmap(QtGui.QPixmap(self.pic_dgong[matrix[1][0]]))
        else:
            self.label_189.setPixmap(QtGui.QPixmap(""))

        if matrix[1][1]:
            self.label_191.setPixmap(QtGui.QPixmap(self.pic_dgong[matrix[1][1]]))
        else:
            self.label_191.setPixmap(QtGui.QPixmap(""))

        if matrix[1][2]:
            self.label_188.setPixmap(QtGui.QPixmap(self.pic_dgong[matrix[1][2]]))
        else:
            self.label_188.setPixmap(QtGui.QPixmap(""))

        if matrix[2][0]:
            self.label_184.setPixmap(QtGui.QPixmap(self.pic_dgong[matrix[2][0]]))
        else:
            self.label_184.setPixmap(QtGui.QPixmap(""))

        if matrix[2][1]:
            self.label_195.setPixmap(QtGui.QPixmap(self.pic_dgong[matrix[2][1]]))
        else:
            self.label_195.setPixmap(QtGui.QPixmap(""))

        if matrix[2][2]:
            self.label_198.setPixmap(QtGui.QPixmap(self.pic_dgong[matrix[2][2]]))
        else:
            self.label_198.setPixmap(QtGui.QPixmap(""))

    def up_dgong(self):
        zx, zy = np.argwhere(self.env_dgong == 0)[0][0], np.argwhere(self.env_dgong == 0)[0][1]
        if zx < 2:
            if not self.timer_dgong.isActive():
                self.timer_dgong.start()
            self.env_dgong = main_9gong.change_env(self.env_dgong, [zx, zy], [zx + 1, zy])
            # self.change_matrix_dgong(self.env_dgong)
            self.act_dgong(self.label_set[zx][zy], self.label_set[zx + 1][zy], self.position_dgong[zx][zy], self.position_dgong[zx + 1][zy])
            main_xgong.change_env_(self.label_set, [zx, zy], [zx + 1, zy])
            self.step_dgong += 1
            self.lcdNumber_11.display(self.step_dgong)
        print(self.env_dgong)

    def down_dgong(self):
        zx, zy = np.argwhere(self.env_dgong == 0)[0][0], np.argwhere(self.env_dgong == 0)[0][1]
        if zx > 0:
            if not self.timer_dgong.isActive():
                self.timer_dgong.start()
            self.env_dgong = main_9gong.change_env(self.env_dgong, [zx, zy], [zx - 1, zy])
            # self.change_matrix_dgong(self.env_dgong)
            self.act_dgong(self.label_set[zx][zy], self.label_set[zx - 1][zy], self.position_dgong[zx][zy], self.position_dgong[zx - 1][zy])
            main_xgong.change_env_(self.label_set, [zx, zy], [zx - 1, zy])
            self.step_dgong += 1
            self.lcdNumber_11.display(self.step_dgong)
            self.move_sound()
        print(self.env_dgong)

    def left_dgong(self):
        zx, zy = np.argwhere(self.env_dgong == 0)[0][0], np.argwhere(self.env_dgong == 0)[0][1]
        if zy < 2:
            if not self.timer_dgong.isActive():
                self.timer_dgong.start()
            self.env_dgong = main_9gong.change_env(self.env_dgong, [zx, zy], [zx, zy + 1])
            # self.change_matrix_dgong(self.env_dgong)
            self.act_dgong(self.label_set[zx][zy], self.label_set[zx][zy + 1], self.position_dgong[zx][zy], self.position_dgong[zx][zy + 1])
            main_xgong.change_env_(self.label_set, [zx, zy], [zx, zy + 1])
            self.step_dgong += 1
            self.lcdNumber_11.display(self.step_dgong)
            self.move_sound()
        print(self.env_dgong)

    def right_dgong(self):
        zx, zy = np.argwhere(self.env_dgong == 0)[0][0], np.argwhere(self.env_dgong == 0)[0][1]
        if zy > 0:
            if not self.timer_dgong.isActive():
                self.timer_dgong.start()
            self.env_dgong = main_9gong.change_env(self.env_dgong, [zx, zy], [zx, zy - 1])
            # self.change_matrix_dgong(self.env_dgong)
            self.act_dgong(self.label_set[zx][zy], self.label_set[zx][zy - 1], self.position_dgong[zx][zy], self.position_dgong[zx][zy - 1])
            main_xgong.change_env_(self.label_set, [zx, zy], [zx, zy - 1])
            self.step_dgong += 1
            self.lcdNumber_11.display(self.step_dgong)
            self.move_sound()
        print(self.env_dgong)

    def fill_matrix_dgong(self, matrix):
        self.label_199.setPixmap(QtGui.QPixmap(self.pic_dgong[matrix[0][0]]))
        self.label_190.setPixmap(QtGui.QPixmap(self.pic_dgong[matrix[0][1]]))
        self.label_203.setPixmap(QtGui.QPixmap(self.pic_dgong[matrix[0][2]]))
        self.label_189.setPixmap(QtGui.QPixmap(self.pic_dgong[matrix[1][0]]))
        self.label_191.setPixmap(QtGui.QPixmap(self.pic_dgong[matrix[1][1]]))
        self.label_188.setPixmap(QtGui.QPixmap(self.pic_dgong[matrix[1][2]]))
        self.label_184.setPixmap(QtGui.QPixmap(self.pic_dgong[matrix[2][0]]))
        self.label_195.setPixmap(QtGui.QPixmap(self.pic_dgong[matrix[2][1]]))
        self.label_198.setPixmap(QtGui.QPixmap(self.pic_dgong[matrix[2][2]]))
        # self.step_dgong += 1
        # self.lcdNumber_11.display(self.step_dgong)

    def finish_dgong(self):
        self.des_dgong = np.array([[1, 2, 3],
                                   [8, 0, 4],
                                   [7, 6, 5]])
        if np.all(self.env_dgong == self.des_dgong):
            self.timer_dgong.stop()
            print(self.position_dgong)
            self.fill_matrix_dgong(self.des_dgong)
            self.remove_dgong()
            self.win_sound()
            QtWidgets.QMessageBox.information(self, "标题", "重排九宫成功！",
                                              QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                              QtWidgets.QMessageBox.Yes)
            self.init_dgong()
        else:
            self.alarm_sound()
            QtWidgets.QMessageBox.information(self, "标题", "重排九宫尚未完成！",
                                              QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                              QtWidgets.QMessageBox.Yes)

    def show_time_dgong(self):
        self.time_dgong += 1
        self.lcdNumber_12.display(self.time_dgong)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    my_show = my_window()

    my_show.show()
    sys.exit(app.exec_())
