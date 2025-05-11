import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

from vSDK import *
from component_position_marker import ComponentPositionMarker
import time
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Main:
    def __init__(self):
        self.root = tk.Tk()
        self.setup_ui(self.root)

        self.cpm = None  # 初始时不创建 ComponentPositionMarker 对象
        
        self.root.mainloop()

    def setup_ui(self, root):
        '''
        设置窗口与控件

        :param root: 主窗口
        '''
        root.title("DFX MetaLab Component Position Marker")
        # root.iconbitmap("Pictogrammers-Material-Chip.ico")  # 设置窗口图标
        root.geometry("480x400")  # 设置默认窗口大小
        root.minsize(400, 280)  # 设置最小窗口大小
        root.resizable(True, True)  # 允许调整窗口大小

        # 设置全局字体
        default_font = ("微软雅黑", 10)
        root.option_add("*Font", default_font)

        # 主容器
        main_frame = ttk.Frame(root, padding=10)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # 标题
        label_title = ttk.Label(main_frame, text="DFX MetaLab 元件坐标标记工具", anchor="center", font=("微软雅黑", 12))
        label_title.pack(fill=tk.X, pady=(0, 10))

        # vSDK 路径选择
        frame_sdk_path = ttk.Frame(main_frame)
        frame_sdk_path.pack(fill=tk.X, pady=5)

        label_sdk_path = ttk.Label(frame_sdk_path, text="vSDK 路径：", width=9)
        label_sdk_path.pack(side=tk.LEFT)

        self.entry_sdk_path = ttk.Entry(frame_sdk_path, width=30)
        self.entry_sdk_path.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        self.entry_sdk_path.insert(0, "C:/VayoPro/DFX_MetaLab/")

        button_sdk_path = ttk.Button(frame_sdk_path, text="...", width=3, command=self.select_sdk_path)
        button_sdk_path.pack(side=tk.RIGHT)

        # Job 文件选择
        frame_job_path = ttk.Frame(main_frame)
        frame_job_path.pack(fill=tk.X, pady=5)
        label_job_path = ttk.Label(frame_job_path, text="Job 文件：", width=9)
        label_job_path.pack(side=tk.LEFT)
        self.entry_job_path = ttk.Entry(frame_job_path, width=30)
        self.entry_job_path.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        button_job_path = ttk.Button(frame_job_path, text="...", width=3, command=self.select_job_path)
        button_job_path.pack(side=tk.RIGHT)

        # 标记形状选择
        frame_shape = ttk.Frame(main_frame)
        frame_shape.pack(fill=tk.X, pady=5)
        label_shape = ttk.Label(frame_shape, text="标记形状: ")
        label_shape.pack(side=tk.LEFT)
        self.combo_shape = ttk.Combobox(frame_shape, values=["实心圆", "空心圆"], state="readonly", width=10)
        self.combo_shape.current(0)
        self.combo_shape.pack(side=tk.LEFT, padx=5)

        # 标记大小选择
        frame_size = ttk.Frame(main_frame)
        frame_size.pack(fill=tk.X, pady=5)
        label_size = ttk.Label(frame_size, text="标记大小(mm): ")
        label_size.pack(side=tk.LEFT)
        self.spin_size = ttk.Spinbox(frame_size, from_=0.0, to=100.0, increment=0.1, width=10)
        self.spin_size.set(0.8)
        self.spin_size.pack(side=tk.LEFT, padx=5)

        # 垂直填充
        frame_spacer = ttk.Frame(main_frame)
        frame_spacer.pack(fill=tk.BOTH, expand=True)

        # 按钮
        frame_buttons = ttk.Frame(main_frame)
        frame_buttons.pack(fill=tk.X, pady=10)
        button_place_mark = ttk.Button(frame_buttons, text="添加标记", command=self.place_mark)
        button_place_mark.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        button_clear_mark = ttk.Button(frame_buttons, text="清除标记", command=self.clear_mark)
        button_clear_mark.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)

    def select_sdk_path(self):
        '''
        弹出文件夹选择对话框，选择 vSDK 路径
        '''
        path = filedialog.askdirectory(title="选择 vSDK 路径")
        if path:
            self.entry_sdk_path.delete(0, tk.END)
            self.entry_sdk_path.insert(0, path)

    def select_job_path(self):
        '''
        弹出文件选择对话框，选择 Job 文件
        '''
        path = filedialog.askopenfilename(title="选择 Job 文件", filetypes=[("Job 文件", "*.job"), ("所有文件", "*.*")])
        if path:
            self.entry_job_path.delete(0, tk.END)
            self.entry_job_path.insert(0, path)

    def update_params(self):
        '''
        从 entry 获取路径，从 spin 和 combo 获取形状配置
        '''
        self.sdk_path = self.entry_sdk_path.get()
        self.job_path = self.entry_job_path.get()
        if not self.sdk_path or not self.job_path:
            tk.messagebox.showwarning("Warning", "请先选择 vSDK 路径和 Job 文件")
            return
        print("sdk_path: ", self.sdk_path)
        print("job_path: ", self.job_path)
        self.sdk_path = bytes(self.sdk_path, encoding='utf-8')
        self.job_path = bytes(self.job_path, encoding='utf-8')

        # 如果 cpm 已经存在，则重新创建一个
        if self.cpm:
            self.cpm = None
        self.cpm = ComponentPositionMarker(self.sdk_path, self.job_path)
        # 设置标记形状
        self.cpm.set_mark_format(float(self.spin_size.get()), self.combo_shape.current() == 0)

    def place_mark(self):
        '''
        添加元件位置标记
        '''
        time_1 = time.time()
        self.update_params()
        self.cpm.place_mark()
        time_2 = time.time()
        logging.info(f"Time taken for adding marks: {time_2 - time_1:.2f} s.")
        job_folder = self.cpm.export_cp_gerber()
        if job_folder == "":
            tk.messagebox.showerror("Error", "导出 Gerber 文件失败")
            return
        
        tk.messagebox.showinfo("Success", "标记添加成功\nGerber 文件已导出到: " + job_folder)

    def clear_mark(self):
        '''
        清除元件位置标记
        '''
        time_1 = time.time()
        self.update_params()
        self.cpm.clear_mark()
        time_2 = time.time()
        logging.info(f"Time taken for clearing marks: {time_2 - time_1:.2f} s.")
        tk.messagebox.showinfo("Success", "标记清除成功")

if __name__ == "__main__":
    ui = Main()
