# -*- coding: utf-8 -*-
# 隔离 pyqt5 依赖
import os
pyqt_path = r'C:/Users/Maxwe/.conda/envs/DFXMetaLab/Lib/site-packages/PyQt5/Qt5/bin'
with os.add_dll_directory(pyqt_path):
    from Ui_main import Ui_Main
    from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog, QMessageBox
import sys

app = QApplication(sys.argv)

vsdk_path = b'C:/VayoPro/DFX_MetaLab/'
with os.add_dll_directory(vsdk_path):
    from vSDK import *
    from component_position_marker import ComponentPositionMarker

import logging

class Main(QDialog, Ui_Main):
    def __init__(self, parent=None):
        super().__init__(parent=None)
        self.setupUi(self)
        self.toolButton_sdk_path.clicked.connect(self.get_vsdk_path)
        self.toolButton_job_path.clicked.connect(self.get_job_path)
        self.pushButton_place_mark.clicked.connect(self.place_mark)
        self.pushButton_clear_mark.clicked.connect(self.clear_mark)
        self.cpm = None

    def get_vsdk_path(self):
        sdk_path = QFileDialog.getExistingDirectory(
            self, "Select SDK Path", "", QFileDialog.ShowDirsOnly)
        if sdk_path:
            self.lineEdit_sdk_path.setText(str(sdk_path))

    def get_job_path(self):
        job_path, ok = QFileDialog.getOpenFileName(self, "Select Job File", "", "Job Files (*.job)")
        if ok:
            self.lineEdit_job_path.setText(str(job_path))

    def update_path(self):
        self.sdk_path = self.lineEdit_sdk_path.text()
        self.job_path = self.lineEdit_job_path.text()
        if not self.sdk_path or not self.job_path:
            QMessageBox.warning(self, "Warning", "Please select SDK path and job file.")
            return
        print("sdk_path: ", self.sdk_path)
        print("job_path: ", self.job_path)
        self.sdk_path = bytes(self.sdk_path, encoding='utf-8')
        self.job_path = bytes(self.job_path, encoding='utf-8')

    def place_mark(self):
        # 创建元件位置标记器对象
        # 如果没有 cpm，则创建一个新的
        pass
        # if not self.cpm:
        #     self.cpm = ComponentPositionMarker(self.sdk_path, self.job_path)
        # self.cpm.place_mark()
        # self.cpm.save_job()

        QMessageBox.information(self, "Success", "Marks placed successfully.")

    def clear_mark(self):
        self.cpm.clear_mark()
        self.cpm.save_job()

if __name__ == '__main__':
    sdk_path = b'C:/VayoPro/DFX_MetaLab/'
    job_path = b"E:/DFXMetaLabDev/jobs/DEMO01.vayo/DEMO01.job" # vayo 工程文件
    # cpm = ComponentPositionMarker(sdk_path, job_path)

    # cpm.place_mark()
    # cpm.clear_mark()
    # 获取元件信息
    # part_data_list = cpm.get_part_data()
    # print(part_data_list)

    # 添加新层
    # layer_tcp_id, layer_tcp = cpm.add_layer("Top_Component_Position", True)
    # layer_bcp_id, layer_bcp = cpm.add_layer("Bottom_Component_Position", False)
    # layer_id_list = [layer_tcp_id, layer_bcp_id]
    # print(layer_tcp)
    # print(layer_bcp)

    # for part_data in part_data_list:
    #     cpm.circle(part_data[0], part_data[1], 0.8, layer_id_list[part_data[2] - 1], circleFilled=False)
    #     logging.info("Circle drawn at (%f, %f) on layer %d", part_data[0], part_data[1], part_data[2])
    
    # 保存 job 文件
    # cpm.save_job()
    # app = QApplication(sys.argv)
    w = Main()
    w.show()
    sys.exit(app.exec_())
