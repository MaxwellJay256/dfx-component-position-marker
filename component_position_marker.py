# This Python file uses the following encoding: utf-8
from vSDK import *
import logging

PI = 3.141592653589793

def vSDK_Board_UpdateLayerConfigFile(pcb):
    return vSDK_dll.vSDK_Board_UpdateLayerConfigFile(pcb, True)

class ComponentPositionMarker:
    def __init__(self, sdk_path: bytes, job_path: bytes):
        '''
        :param sdk_path: vsdk.dll 所在文件夹路径
        :param job_path: vayo job 文件绝对路径
        '''
        if not os.path.exists(sdk_path.decode('utf-8')):
            logging.error("SDK path %s does not exist.", sdk_path.decode('utf-8'))
            exit(1)
        vSDK_Init(sdk_path)
        if not os.path.exists(job_path.decode('utf-8')):
            logging.error("Job file %s does not exist.", job_path.decode('utf-8'))
            exit(1)
        self.job = vSDK_OpenJob(job_path)
        self.pcb = vSDK_Job_GetCurrentPcb(self.job)
        self.board = vSDK_Pcb_GetBoard(self.pcb)

        self.part_data_list = []
        self.layer_tcp_id = 0
        self.layer_bcp_id = 0
        self.layer_tcp_name = "Top_Component_Position"
        self.layer_bcp_name = "Bottom_Component_Position"
        self.circle_diameter = 0.8
        self.filled = False

    def save_job(self):
        vSDK_SaveJob()

    def get_part_data(self) -> list:
        '''
        获取元件坐标、层信息

        :return: 包含 part X, Y, LayerSide 的 list
        '''
        iCount = vSDK_Board_GetPartListCount(self.board)
        part_data_list = []
        for id in range(0, iCount.value):
            part = vSDK_Board_GetPartByIndex(self.board, id)
            part_data = vSDK_Part_GetPartData(part)
            # PartPosX, PartPosY, LayerSide
            part_data_list.append((
                part_data[2].value, part_data[3].value, part_data[11].value))
        return part_data_list

    def get_layer_data(self) -> list:
        """
        获取全部层信息

        :return: 包含全部 layer 信息的 list
        """
        layer_count = vSDK_Board_GetLayerListCount(self.board)
        all_layer_data = []
        for index in range(0, layer_count.value):
            layer = vSDK_Board_GetLayerByIndex(self.board, index)
            layer_id = vSDK_Layer_GetLayerID(layer).value
            layer_name = vSDK_Layer_GetLayerName(layer).value
            layer_side = vSDK_Layer_GetLayerSide(layer).value
            layer_type = vSDK_Layer_GetLayerType(layer).value
            layer_thickness = vSDK_Layer_GetLayerThickness(layer).value
            resh_thickness = vSDK_Layer_GetReshThickness(layer).value
            positive = vSDK_Layer_GetPositive(layer).value
            all_layer_data.append((layer_id, layer_name, layer_side, layer_type, layer_thickness, resh_thickness,
                                   positive))
        return all_layer_data

    def add_layer(self, layer_name: str, layer_side: bool):
        """
        添加一个层，如果存在同名层，则覆盖

        :param layer_name: 层名
        :param layer_side: True 为正面, False 为反面
        :return: 层 id, 层对象指针
        """
        layer = None
        layer_name = layer_name.encode()
        layer = vSDK_Board_GetLayerByName(self.board, layer_name)
        # 如果layer已经存在，则覆盖
        if layer.value:
            vSDK_Board_DeleteLayer(self.board, layer_name)
        layer = vSDK_Board_AddLayer(self.board, layer_name)
        layer_id = vSDK_Layer_GetLayerID(layer)
        if layer_side:
            vSDK_Layer_SetLayerSide(layer, 1)
        else:
            vSDK_Layer_SetLayerSide(layer, 3)
        vSDK_Board_UpdateLayerConfigFile(self.pcb)
        return layer_id.value, layer
    
    def arc(self, CenterX: float, CenterY: float, Radius: float, StartAngle: float, AngleRotate: float, layerId: int,
            LineLength: float = 0.01, LineWidth: float = 0.01, isRectangle: bool = True, PositiveNegative: bool = True,
            Filled: bool = True) -> int:
        """
        向图层添加弧线

        :param CenterX: 弧形圆心 X 轴坐标
        :param CenterY: 弧形圆心 Y 轴坐标
        :param Radius: 弧形半径
        :param StartAngle: 起始弧度
        :param AngleRotate: 旋转弧度
        :param layerId: 要添加图形的层的 ID
        :param LineLength: 线长 (矩形线头使用)
        :param LineWidth: 线宽 (矩形线头使用)
        :param isRectangle: 是否为矩形线头 (False 则为圆形线头)
        :param PositiveNegative: 图形为正片还是负片(True 为正片)
        :param Filled: 图形是否填充 (True 为填充)
        :return: 返回新增图形的 ObjectID
        """

        arcShape = vSDK_Shape_CreateShapeByArc(CenterX, CenterY, Radius, StartAngle,
                                               AngleRotate, LineLength, LineWidth, isRectangle,
                                               PositiveNegative, Filled);
        arcLayerObjectID = vSDK_Layer_AddShapeByArc(self.board, layerId, 0, arcShape)
        vSDK_Shape_DestroyShape(arcShape)
        return arcLayerObjectID.value

    def circle(self, circleX: float, circleY: float, circleDiameter: float, layerId: int,
               circlePositiveNegative: bool = True, circleFilled: bool = True
               ) -> int:
        """
        向图层添加圆形

        :param circleX: 圆心 X 坐标
        :param circleY: 圆心 Y 坐标
        :param circleDiameter: 圆形直径
        :param layerId: 要添加图形的层的 ID
        :param circlePositiveNegative: 图形为正片还是负片 (True 表示正片)
        :param circleFilled: 图形是否填充 (True 表示填充)
        :return: 返回新增图形的 ObjectID
        """
        if not circleFilled:
            return self.arc(circleX, circleY, circleDiameter / 2, 0, 2 * PI, layerId)

        DcodeCount, DcodeTable = self.GetDcodeCountByLayerId(layerId)
        circleShape = vSDK_Shape_CreateShapeByCircle(0, 0, circleDiameter,
                                                     circlePositiveNegative, circleFilled)
        if DcodeCount == 0:
            DcodeName = ("Circle" + str(circleDiameter)).encode()
            DCode = vSDK_Dcode_CreateDcode(DcodeTable, DcodeName, DcodeName)
            vSDK_Dcode_AddDcodeShape(DcodeTable, DCode, circleShape)
            DcodeID = vSDK_Dcode_AddDcodeEnd(DcodeTable, DCode)
        else:
            DcodeID = vSDK_DcodeTable_FindRoundDcodeIDBySize(DcodeTable, 0, 0, circleDiameter)
            if DcodeID.value < 0:
                DcodeName = ("Circle" + str(circleDiameter)).encode()
                DCode = vSDK_Dcode_CreateDcode(DcodeTable, DcodeName, "1".encode())
                vSDK_Dcode_AddDcodeShape(DcodeTable, DCode, circleShape)
                DcodeID = vSDK_Dcode_AddDcodeEnd(DcodeTable, DCode)
        layerObjectId = vSDK_Layer_AddShapeByDcode(self.board, layerId, 0, 0,
                                                   0, DcodeID, circlePositiveNegative, circleX,
                                                   circleY)
        vSDK_Shape_DestroyShape(circleShape)
        return layerObjectId.value
    
    def set_mark_format(self, diameter: float, filled: bool):
        self.circle_diameter = diameter
        self.filled = filled

    def place_mark(self):
        self.part_data_list = self.get_part_data()
        layer_tcp_id, layer_tcp = self.add_layer(self.layer_tcp_name, True)
        layer_bcp_id, layer_bcp = self.add_layer(self.layer_bcp_name, False)
        layer_id_list = [layer_tcp_id, layer_bcp_id]
        for part_data in self.part_data_list:
            self.circle(part_data[0], part_data[1], self.circle_diameter, layer_id_list[part_data[2] - 1], circleFilled=self.filled)
            logging.warning("Circle drawn at (%f, %f) on layer %d", part_data[0], part_data[1], part_data[2])

    def clear_mark(self):
        '''
        清除元件位置标记
        
        :return: None
        '''
        # 按名称查询 tcp, bcp 层是否存在，如有则删除
        layer = vSDK_Board_GetLayerByName(self.board, self.layer_tcp_name)
        if layer.value:
            vSDK_Board_DeleteLayer(self.board, self.layer_tcp_name)
        layer = vSDK_Board_GetLayerByName(self.board, self.layer_bcp_name)
        if layer.value:
            vSDK_Board_DeleteLayer(self.board, self.layer_bcp_name)
        logging.warning("Layers %s and %s are deleted.", self.layer_tcp_name, self.layer_bcp_name)

if __name__ == "__main__":
    sdk_path = b'C:/VayoPro/DFX_MetaLab/'
    job_path = b"E:/DFXMetaLabDev/jobs/DEMO01.vayo/DEMO01.job" # vayo 工程文件
    cpm = ComponentPositionMarker(sdk_path, job_path)
