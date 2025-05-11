# This Python file uses the following encoding: utf-8
import ctypes
import os

SdkPath = r'C:/VayoPro/DFX_MetaLab/' # DFX MetaLab安装路径

SdkdllPath = os.path.join(SdkPath, "vSDK.dll")
if not os.path.exists(SdkdllPath):
    raise FileNotFoundError(f"vSDK.dll not found at {SdkdllPath}")


with os.add_dll_directory(SdkPath):
    vSDK_dll = ctypes.CDLL(SdkdllPath)


def InitvSDKGUI(SdkPath: bytes):
    if SdkPath == "":
        SdkPath = str(os.getcwd()) + "/"
    return vSDK_dll.InitVSDKDll(SdkPath)


def InitvSDK(SdkPath: bytes):
    if SdkPath == "":
        SdkPath = str(os.getcwd()) + "/"
    return vSDK_dll.vSDK_Init(SdkPath)


def vSDK_Init(exepath: bytes):
    """
    VSDK_EXPORT int vSDK_Init(const char *_exe_path);

    :param exepath:
    :return: vSDK_dll.vSDK_Init(exepath)
    """
    return vSDK_dll.vSDK_Init(exepath)

def vSDK_OpenJob(JobPath: bytes):
    """
    VSDK_EXPORT int vSDK_OpenJob(const char *_JobPath, Job &_Job);

    :param JobPath:
    :return: Job
    """
    Job = ctypes.c_void_p()
    vSDK_dll.vSDK_OpenJob(JobPath, ctypes.byref(Job))
    return Job


def vSDK_SaveJob():
    """
    VSDK_EXPORT int vSDK_SaveJob();

    :return: vSDK_dll.vSDK_SaveJob()
    """
    return vSDK_dll.vSDK_SaveJob()


def vSDK_CloseJob(bSave: bool):
    """
    VSDK_EXPORT int vSDK_CloseJob(const bool _bSave);

    :param bSave:
    :return: vSDK_dll.vSDK_CloseJob(bSave)
    """
    return vSDK_dll.vSDK_CloseJob(bSave)


def vSDK_AddJob():
    """
    VSDK_EXPORT int vSDK_AddJob(Job &_Job);

    :return: Job
    """
    Job = ctypes.c_void_p()
    vSDK_dll.vSDK_AddJob(ctypes.byref(Job))
    return Job


def vSDK_Job_AddPcb(Job, pcbName: bytes):
    """
    VSDK_EXPORT int vSDK_Job_AddPcb(Job _Job, const char *pcbName);

    :param Job:
    :param pcbName:
    :return: vSDK_dll.vSDK_Job_AddPcb(Job, pcbName)
    """
    return vSDK_dll.vSDK_Job_AddPcb(Job, pcbName)


def vSDK_Job_GetPcbListCount(Job):
    """
    VSDK_EXPORT int vSDK_Job_GetPcbListCount(Job _Job, int &_PcbCount);

    :param Job:
    :return: PcbCount
    """
    PcbCount = ctypes.c_int(0)
    vSDK_dll.vSDK_Job_GetPcbListCount(Job, ctypes.byref(PcbCount))
    return PcbCount


def vSDK_SwitchCurrentPcbByIndex(Index: int):
    """
    VSDK_EXPORT int vSDK_SwitchCurrentPcbByIndex(const int _Index);

    :param Index:
    :return: vSDK_dll.vSDK_SwitchCurrentPcbByIndex(Index)
    """
    return vSDK_dll.vSDK_SwitchCurrentPcbByIndex(Index)


def vSDK_Job_GetBOMCount(Job):
    """
    VSDK_EXPORT int vSDK_Job_GetBOMCount(Job _Job, int &_BOMCount);

    :param Job:
    :return: BOMCount
    """
    BOMCount = ctypes.c_int(0)
    vSDK_dll.vSDK_Job_GetBOMCount(Job, ctypes.byref(BOMCount))
    return BOMCount


def vSDK_Job_GetBOMByIndex(Job, BOMIndex: int):
    """
    VSDK_EXPORT int vSDK_Job_GetBOMByIndex(Job _Job, int _BOMIndex, BOM &_BOM);

    :param Job:
    :param BOMIndex:
    :return: BOM
    """
    BOM = ctypes.c_void_p()
    vSDK_dll.vSDK_Job_GetBOMByIndex(Job, BOMIndex, ctypes.byref(BOM))
    return BOM

def vSDK_Job_DeleteBOM(Job):
    """
    VSDK_EXPORT int vSDK_Job_DeleteBOM(Job _Job, BOM &_BOM);

    :param Job:
    :return: BOM
    """
    BOM = ctypes.c_void_p()
    vSDK_dll.vSDK_Job_DeleteBOM(Job, ctypes.byref(BOM))
    return BOM

def vSDK_GetCurrentJob():
    """
    VSDK_EXPORT int vSDK_GetCurrentJob(Job &_Job);

    :return: Job
    """
    Job = ctypes.c_void_p()
    vSDK_dll.vSDK_GetCurrentJob(ctypes.byref(Job))
    return Job

def vSDK_Job_GetCurrentPcb(Job):
    """
    VSDK_EXPORT int vSDK_Job_GetCurrentPcb(Job _Job, Pcb &_Pcb);

    :param Job:
    :return: Pcb
    """
    Pcb = ctypes.c_void_p()
    vSDK_dll.vSDK_Job_GetCurrentPcb(Job, ctypes.byref(Pcb))
    return Pcb

def vSDK_Pcb_GetBoard(Pcb):
    """
    VSDK_EXPORT int vSDK_Pcb_GetBoard(Pcb _Pcb, Board &_Board);

    :param Pcb:
    :return: Board
    """
    Board = ctypes.c_void_p()
    vSDK_dll.vSDK_Pcb_GetBoard(Pcb, ctypes.byref(Board))
    return Board

def vSDK_Pcb_GetBOM(Pcb):
    """
    VSDK_EXPORT int vSDK_Pcb_GetBOM(Pcb _Pcb, BOM &_BOM);

    :param Pcb:
    :return: BOM
    """
    BOM = ctypes.c_void_p()
    vSDK_dll.vSDK_Pcb_GetBOM(Pcb, ctypes.byref(BOM))
    return BOM

def vSDK_Pcb_GetBomCheckStatus(Pcb):
    """
    VSDK_EXPORT int vSDK_Pcb_GetBomCheckStatus(Pcb _Pcb, bool &_bCheck);

    :param Pcb:
    :return: bCheck
    """
    bCheck = ctypes.c_bool()
    vSDK_dll.vSDK_Pcb_GetBomCheckStatus(Pcb, ctypes.byref(bCheck))
    return bCheck

def vSDK_Pcb_SetBomCheckStatus(Pcb, bCheck: bool):
    """
    VSDK_EXPORT int vSDK_Pcb_SetBomCheckStatus(Pcb _Pcb, const bool _bCheck);

    :param Pcb:
    :param bCheck:
    :return: vSDK_dll.vSDK_Pcb_SetBomCheckStatus(Pcb, bCheck)
    """
    return vSDK_dll.vSDK_Pcb_SetBomCheckStatus(Pcb, bCheck)

def vSDK_Pcb_SetBomByName(Pcb, bomFullPathName: bytes):
    """
    VSDK_EXPORT int vSDK_Pcb_SetBomByName(Pcb _Pcb, const char* bomFullPathName);

    :param Pcb:
    :param bomFullPathName:
    :return: vSDK_dll.vSDK_Pcb_SetBomByName(Pcb, bomFullPathName)
    """
    return vSDK_dll.vSDK_Pcb_SetBomByName(Pcb, bomFullPathName)

def vSDK_Pcb_SetBomByBom(Pcb, BOM):
    """
    VSDK_EXPORT int vSDK_Pcb_SetBomByBom(Pcb _Pcb, BOM _BOM);

    :param Pcb:
    :param BOM:
    :return: vSDK_dll.vSDK_Pcb_SetBomByBom(Pcb, BOM)
    """
    return vSDK_dll.vSDK_Pcb_SetBomByBom(Pcb, BOM)

def vSDK_Pcb_GetPanelListCount(Pcb):
    """
    VSDK_EXPORT int vSDK_Pcb_GetPanelListCount(Pcb _Pcb, int &_PanelCount);

    :param Pcb:
    :return: PanelCount
    """
    PanelCount = ctypes.c_int(0)
    vSDK_dll.vSDK_Pcb_GetPanelListCount(Pcb, ctypes.byref(PanelCount))
    return PanelCount

def vSDK_Pcb_GetPanelByIndex(Pcb, PanelIndex: int):
    """
    VSDK_EXPORT int vSDK_Pcb_GetPanelByIndex(Pcb _Pcb, int _PanelIndex, Panel &_Panel);

    :param Pcb:
    :param PanelIndex:
    :return: Panel
    """
    Panel = ctypes.c_void_p()
    vSDK_dll.vSDK_Pcb_GetPanelByIndex(Pcb, PanelIndex, ctypes.byref(Panel))
    return Panel

def vSDK_Pcb_SetPcbThickness(Pcb, dThickness: float):
    """
    VSDK_EXPORT int vSDK_Pcb_SetPcbThickness(Pcb _Pcb, const double _dThickness);

    :param Pcb:
    :param dThickness:
    :return: vSDK_dll.vSDK_Pcb_SetPcbThickness(Pcb, ctypes.c_double(dThickness))
    """
    return vSDK_dll.vSDK_Pcb_SetPcbThickness(Pcb, ctypes.c_double(dThickness))

def vSDK_Pcb_GetPcbThickness(Pcb):
    """
    VSDK_EXPORT int vSDK_Pcb_GetPcbThickness(Pcb _Pcb, double &_dThickness);

    :param Pcb:
    :return: dThickness
    """
    dThickness = ctypes.c_double()
    vSDK_dll.vSDK_Pcb_GetPcbThickness(Pcb, ctypes.byref(dThickness))
    return dThickness

def vSDK_Pcb_SetPcbSize(Pcb, MinX: float, MinY: float, MaxX: float, MaxY: float):
    """
    VSDK_EXPORT int vSDK_Pcb_SetPcbSize(Pcb _Pcb, const double _MinX, const double _MinY, const double _MaxX, const double _MaxY);

    :param Pcb:
    :param MinX:
    :param MinY:
    :param MaxX:
    :param MaxY:
    :return: vSDK_dll.vSDK_Pcb_SetPcbSize(Pcb, ctypes.c_double(MinX), ctypes.c_double(MinY), ctypes.c_double(MaxX), ctypes.c_double(MaxY))
    """
    return vSDK_dll.vSDK_Pcb_SetPcbSize(Pcb, ctypes.c_double(MinX), ctypes.c_double(MinY), ctypes.c_double(MaxX), ctypes.c_double(MaxY))

def vSDK_Pcb_GetPcbSize(Pcb):
    """
    VSDK_EXPORT int vSDK_Pcb_GetPcbSize(Pcb _Pcb, double &_MinX, double &_MinY, double &_MaxX, double &_MaxY);

    :param Pcb:
    :return: MinX, MinY, MaxX, MaxY
    """
    MinX = ctypes.c_double()
    MinY = ctypes.c_double()
    MaxX = ctypes.c_double()
    MaxY = ctypes.c_double()
    vSDK_dll.vSDK_Pcb_GetPcbSize(Pcb, ctypes.byref(MinX), ctypes.byref(MinY), ctypes.byref(MaxX), ctypes.byref(MaxY))
    return MinX, MinY, MaxX, MaxY

def vSDK_Board_AddProperty(Board, ckey: bytes, cvalue: bytes):
    """
    VSDK_EXPORT int vSDK_Board_AddProperty(Board _Board, const char *ckey, const char *cvalue);

    :param Board:
    :param ckey:
    :param cvalue:
    :return: vSDK_dll.vSDK_Board_AddProperty(Board, ckey, cvalue)
    """
    return vSDK_dll.vSDK_Board_AddProperty(Board, ckey, cvalue)

def vSDK_Board_GetPropertyCount(Board):
    """
    VSDK_EXPORT int vSDK_Board_GetPropertyCount(Board _Board, int &_PropertyCount);

    :param Board:
    :return: PropertyCount
    """
    PropertyCount = ctypes.c_int(0)
    vSDK_dll.vSDK_Board_GetPropertyCount(Board, ctypes.byref(PropertyCount))
    return PropertyCount

def vSDK_Board_GetPropertyByIndex(Board, Index: int):
    """
    VSDK_EXPORT int vSDK_Board_GetPropertyByIndex(Board _Board, int Index, char *&ckey, char *&cvalue);

    :param Board:
    :param Index:
    :return: ckey, cvalue
    """
    ckey = ctypes.c_char_p()
    cvalue = ctypes.c_char_p()
    vSDK_dll.vSDK_Board_GetPropertyByIndex(Board, Index, ctypes.byref(ckey), ctypes.byref(cvalue))
    return ckey, cvalue

def vSDK_Board_AddLayer(Board, LayerName: bytes):
    """
    VSDK_EXPORT int vSDK_Board_AddLayer(Board _Board, const char *_LayerName, Layer &_Layer);

    :param Board:
    :param LayerName:
    :return: Layer
    """
    Layer = ctypes.c_void_p()
    vSDK_dll.vSDK_Board_AddLayer(Board, LayerName, ctypes.byref(Layer))
    return Layer

def vSDK_Board_GetLayerListCount(Board):
    """
    VSDK_EXPORT int vSDK_Board_GetLayerListCount(Board _Board, int &_LayerCount);

    :param Board:
    :return: LayerCount
    """
    LayerCount = ctypes.c_int(0)
    vSDK_dll.vSDK_Board_GetLayerListCount(Board, ctypes.byref(LayerCount))
    return LayerCount

def vSDK_Board_GetLayerByIndex(Board, LayerIndex: int):
    """
    VSDK_EXPORT int vSDK_Board_GetLayerByIndex(Board _Board, int _LayerIndex, Layer &_Layer);

    :param Board:
    :param LayerIndex:
    :return: Layer
    """
    Layer = ctypes.c_void_p()
    vSDK_dll.vSDK_Board_GetLayerByIndex(Board, LayerIndex, ctypes.byref(Layer))
    return Layer

def vSDK_Board_GetLayerByID(Board, LayerID: int):
    """
    VSDK_EXPORT int vSDK_Board_GetLayerByID(Board _Board, int _LayerID, Layer &_Layer);

    :param Board:
    :param LayerID:
    :return: Layer
    """
    Layer = ctypes.c_void_p()
    vSDK_dll.vSDK_Board_GetLayerByID(Board, LayerID, ctypes.byref(Layer))
    return Layer

def vSDK_Board_GetLayerByName(Board, LayerName: bytes):
    """
    VSDK_EXPORT int vSDK_Board_GetLayerByName(Board _Board, const char *_LayerName, Layer &_Layer);

    :param Board:
    :param LayerName:
    :return: Layer
    """
    Layer = ctypes.c_void_p()
    vSDK_dll.vSDK_Board_GetLayerByName(Board, LayerName, ctypes.byref(Layer))
    return Layer

def vSDK_Board_DeleteLayer(Board, LayerName: bytes):
    """
    VSDK_EXPORT int vSDK_Board_DeleteLayer(Board _Board, const char *_LayerName);

    :param Board:
    :param LayerName:
    :return: vSDK_dll.vSDK_Board_DeleteLayer(Board, LayerName)
    """
    return vSDK_dll.vSDK_Board_DeleteLayer(Board, LayerName)

def vSDK_Board_ReLoadLayer(Board, LayerID: int, mode: int):
    """
    VSDK_EXPORT int vSDK_Board_ReLoadLayer(Board _Board, const int _LayerID, int mode);

    :param Board:
    :param LayerID:
    :param mode:
    :return: vSDK_dll.vSDK_Board_ReLoadLayer(Board, LayerID, mode)
    """
    return vSDK_dll.vSDK_Board_ReLoadLayer(Board, LayerID, mode)

def vSDK_Board_GetDcodeTableCount(Board):
    """
    VSDK_EXPORT int vSDK_Board_GetDcodeTableCount(Board _Board, int &_DcodeTableCount);

    :param Board:
    :return: DcodeTableCount
    """
    DcodeTableCount = ctypes.c_int(0)
    vSDK_dll.vSDK_Board_GetDcodeTableCount(Board, ctypes.byref(DcodeTableCount))
    return DcodeTableCount

def vSDK_Board_GetDCodeTableByIndex(Board, DCodeTableIndex: int):
    """
    VSDK_EXPORT int vSDK_Board_GetDCodeTableByIndex(Board _Board, const int _DCodeTableIndex, DcodeTable &_DcodeTable);

    :param Board:
    :param DCodeTableIndex:
    :return: DcodeTable
    """
    DcodeTable = ctypes.c_void_p()
    vSDK_dll.vSDK_Board_GetDCodeTableByIndex(Board, DCodeTableIndex, ctypes.byref(DcodeTable))
    return DcodeTable

def vSDK_Board_AddNet(Board, NetID: int, NetName: bytes):
    """
    VSDK_EXPORT int vSDK_Board_AddNet(Board _Board, const int _NetID, const char* _NetName, Net &_Net);

    :param Board:
    :param NetID:
    :param NetName:
    :return: Net
    """
    Net = ctypes.c_void_p()
    vSDK_dll.vSDK_Board_AddNet(Board, NetID, NetName, ctypes.byref(Net))
    return Net

def vSDK_Board_GetNetListCount(Board):
    """
    VSDK_EXPORT int vSDK_Board_GetNetListCount(Board _Board, int &_NetCount);

    :param Board:
    :return: NetCount
    """
    NetCount = ctypes.c_int(0)
    vSDK_dll.vSDK_Board_GetNetListCount(Board, ctypes.byref(NetCount))
    return NetCount

def vSDK_Board_GetNetByIndex(Board, NetIndex: int):
    """
    VSDK_EXPORT int vSDK_Board_GetNetByIndex(Board _Board, int _NetIndex, Net &_Net);

    :param Board:
    :param NetIndex:
    :return: Net
    """
    Net = ctypes.c_void_p()
    vSDK_dll.vSDK_Board_GetNetByIndex(Board, NetIndex, ctypes.byref(Net))
    return Net

def vSDK_Board_GetNetByID(Board, NetID: int):
    """
    VSDK_EXPORT int vSDK_Board_GetNetByID(Board _Board, int _NetID, Net &_Net);

    :param Board:
    :param NetID:
    :return: Net
    """
    Net = ctypes.c_void_p()
    vSDK_dll.vSDK_Board_GetNetByID(Board, NetID, ctypes.byref(Net))
    return Net

def vSDK_Board_GetNetByName(Board, NetName: bytes):
    """
    VSDK_EXPORT int vSDK_Board_GetNetByName(Board _Board, const char *_NetName, Net &_Net);

    :param Board:
    :param NetName:
    :return: Net
    """
    Net = ctypes.c_void_p()
    vSDK_dll.vSDK_Board_GetNetByName(Board, NetName, ctypes.byref(Net))
    return Net

def vSDK_Board_NetExistByNetId(Board, NetID: int):
    """
    VSDK_EXPORT int vSDK_Board_NetExistByNetId(Board _Board, int _NetID, bool &IfExist, Net &_Net);

    :param Board:
    :param NetID:
    :return: IfExist, Net
    """
    IfExist = ctypes.c_bool()
    Net = ctypes.c_void_p()
    vSDK_dll.vSDK_Board_NetExistByNetId(Board, NetID, ctypes.byref(IfExist), ctypes.byref(Net))
    return IfExist, Net

def vSDK_Board_NetExistByNetName(Board, NetName: bytes):
    """
    VSDK_EXPORT int vSDK_Board_NetExistByNetName(Board _Board, const char *_NetName, bool &IfExist, Net &_Net);

    :param Board:
    :param NetName:
    :return: IfExist, Net
    """
    IfExist = ctypes.c_bool()
    Net = ctypes.c_void_p()
    vSDK_dll.vSDK_Board_NetExistByNetName(Board, NetName, ctypes.byref(IfExist), ctypes.byref(Net))
    return IfExist, Net

def vSDK_Board_AddSymbol(Board):
    """
    VSDK_EXPORT int vSDK_Board_AddSymbol(Board _Board, Symbol &_Symbol);

    :param Board:
    :return: Symbol
    """
    Symbol = ctypes.c_void_p()
    vSDK_dll.vSDK_Board_AddSymbol(Board, ctypes.byref(Symbol))
    return Symbol

def vSDK_Board_GetSymbolListCount(Board):
    """
    VSDK_EXPORT int vSDK_Board_GetSymbolListCount(Board _Board, int &_SymbolCount);

    :param Board:
    :return: SymbolCount
    """
    SymbolCount = ctypes.c_int(0)
    vSDK_dll.vSDK_Board_GetSymbolListCount(Board, ctypes.byref(SymbolCount))
    return SymbolCount

def vSDK_Board_GetSymbolByIndex(Board, SymbolIndex: int):
    """
    VSDK_EXPORT int vSDK_Board_GetSymbolByIndex(Board _Board, const int _SymbolIndex, Symbol &_Symbol);

    :param Board:
    :param SymbolIndex:
    :return: Symbol
    """
    Symbol = ctypes.c_void_p()
    vSDK_dll.vSDK_Board_GetSymbolByIndex(Board, SymbolIndex, ctypes.byref(Symbol))
    return Symbol

def vSDK_Board_GetSymbolByID(Board, SymbolID: int):
    """
    VSDK_EXPORT int vSDK_Board_GetSymbolByID(Board _Board, const int _SymbolID, Symbol &_Symbol);

    :param Board:
    :param SymbolID:
    :return: Symbol
    """
    Symbol = ctypes.c_void_p()
    vSDK_dll.vSDK_Board_GetSymbolByID(Board, SymbolID, ctypes.byref(Symbol))
    return Symbol

def vSDK_Board_GetSymbolByName(Board, SymbolName: bytes):
    """
    VSDK_EXPORT int vSDK_Board_GetSymbolByName(Board _Board, const char *_SymbolName, Symbol &_Symbol);

    :param Board:
    :param SymbolName:
    :return: Symbol
    """
    Symbol = ctypes.c_void_p()
    vSDK_dll.vSDK_Board_GetSymbolByName(Board, SymbolName, ctypes.byref(Symbol))
    return Symbol

def vSDK_Board_AddPadGroup(Board):
    """
    VSDK_EXPORT int vSDK_Board_AddPadGroup(Board _Board, PadGroup &_PadGroup);

    :param Board:
    :return: PadGroup
    """
    PadGroup = ctypes.c_void_p()
    vSDK_dll.vSDK_Board_AddPadGroup(Board, ctypes.byref(PadGroup))
    return PadGroup

def vSDK_Board_GetPadGroupListCount(Board):
    """
    VSDK_EXPORT int vSDK_Board_GetPadGroupListCount(Board _Board, int &_PadGroupCount);

    :param Board:
    :return: PadGroupCount
    """
    PadGroupCount = ctypes.c_int(0)
    vSDK_dll.vSDK_Board_GetPadGroupListCount(Board, ctypes.byref(PadGroupCount))
    return PadGroupCount

def vSDK_Board_GetPadGroupByIndex(Board, PadGroupIndex: int):
    """
    VSDK_EXPORT int vSDK_Board_GetPadGroupByIndex(Board _Board, int _PadGroupIndex, PadGroup &_PadGroup);

    :param Board:
    :param PadGroupIndex:
    :return: PadGroup
    """
    PadGroup = ctypes.c_void_p()
    vSDK_dll.vSDK_Board_GetPadGroupByIndex(Board, PadGroupIndex, ctypes.byref(PadGroup))
    return PadGroup

def vSDK_Board_GetPadGroupByID(Board, PadGroupID: int):
    """
    VSDK_EXPORT int vSDK_Board_GetPadGroupByID(Board _Board, int _PadGroupID, PadGroup &_PadGroup);

    :param Board:
    :param PadGroupID:
    :return: PadGroup
    """
    PadGroup = ctypes.c_void_p()
    vSDK_dll.vSDK_Board_GetPadGroupByID(Board, PadGroupID, ctypes.byref(PadGroup))
    return PadGroup

def vSDK_Board_AddPackage(Board):
    """
    VSDK_EXPORT int vSDK_Board_AddPackage(Board _Board, Package &_Package);

    :param Board:
    :return: Package
    """
    Package = ctypes.c_void_p()
    vSDK_dll.vSDK_Board_AddPackage(Board, ctypes.byref(Package))
    return Package

def vSDK_Board_GetPackageListCount(Board):
    """
    VSDK_EXPORT int vSDK_Board_GetPackageListCount(Board _Board, int &_PackageCount);

    :param Board:
    :return: PackageCount
    """
    PackageCount = ctypes.c_int(0)
    vSDK_dll.vSDK_Board_GetPackageListCount(Board, ctypes.byref(PackageCount))
    return PackageCount

def vSDK_Board_GetPackageByIndex(Board, PackageIndex: int):
    """
    VSDK_EXPORT int vSDK_Board_GetPackageByIndex(Board _Board, int _PackageIndex, Package &_Package);

    :param Board:
    :param PackageIndex:
    :return: Package
    """
    Package = ctypes.c_void_p()
    vSDK_dll.vSDK_Board_GetPackageByIndex(Board, PackageIndex, ctypes.byref(Package))
    return Package

def vSDK_Board_GetPackageByID(Board, PackageId: int):
    """
    VSDK_EXPORT int vSDK_Board_GetPackageByID(Board _Board, const int _PackageId, Package &_Package);

    :param Board:
    :param PackageId:
    :return: Package
    """
    Package = ctypes.c_void_p()
    vSDK_dll.vSDK_Board_GetPackageByID(Board, PackageId, ctypes.byref(Package))
    return Package

def vSDK_Board_GetPackageByName(Board, PackageName: bytes):
    """
    VSDK_EXPORT int vSDK_Board_GetPackageByName(Board _Board, const char *_PackageName, Package &_Package);

    :param Board:
    :param PackageName:
    :return: Package
    """
    Package = ctypes.c_void_p()
    vSDK_dll.vSDK_Board_GetPackageByName(Board, PackageName, ctypes.byref(Package))
    return Package

def vSDK_Board_AddPart(Board):
    """
    VSDK_EXPORT int vSDK_Board_AddPart(Board _Board, Part &_Part);

    :param Board:
    :return: Part
    """
    Part = ctypes.c_void_p()
    vSDK_dll.vSDK_Board_AddPart(Board, ctypes.byref(Part))
    return Part

def vSDK_Board_GetPartListCount(Board):
    """
    VSDK_EXPORT int vSDK_Board_GetPartListCount(Board _Board, int &_PartCount);

    :param Board:
    :return: PartCount
    """
    PartCount = ctypes.c_int(0)
    vSDK_dll.vSDK_Board_GetPartListCount(Board, ctypes.byref(PartCount))
    return PartCount

def vSDK_Board_GetPartByIndex(Board, PartIndex: int):
    """
    VSDK_EXPORT int vSDK_Board_GetPartByIndex(Board _Board, int _PartIndex, Part &_Part);

    :param Board:
    :param PartIndex:
    :return: Part
    """
    Part = ctypes.c_void_p()
    vSDK_dll.vSDK_Board_GetPartByIndex(Board, PartIndex, ctypes.byref(Part))
    return Part

def vSDK_Board_GetPartByID(Board, PartID: int):
    """
    VSDK_EXPORT int vSDK_Board_GetPartByID(Board _Board, int _PartID, Part &_Part);

    :param Board:
    :param PartID:
    :return: Part
    """
    Part = ctypes.c_void_p()
    vSDK_dll.vSDK_Board_GetPartByID(Board, PartID, ctypes.byref(Part))
    return Part

def vSDK_Board_GetPartByName(Board, PartName: bytes):
    """
    VSDK_EXPORT int vSDK_Board_GetPartByName(Board _Board, const char *_PartName, Part &_Part);

    :param Board:
    :param PartName:
    :return: Part
    """
    Part = ctypes.c_void_p()
    vSDK_dll.vSDK_Board_GetPartByName(Board, PartName, ctypes.byref(Part))
    return Part

def vSDK_Board_AddVia(Board, NetID: int, PadGroupID: int, PadName: bytes):
    """
    VSDK_EXPORT int vSDK_Board_AddVia(Board _Board, const int NetID, const int _PadGroupID, const char *PadName, Via &_Via);

    :param Board:
    :param NetID:
    :param PadGroupID:
    :param PadName:
    :return: Via
    """
    Via = ctypes.c_void_p()
    vSDK_dll.vSDK_Board_AddVia(Board, NetID, PadGroupID, PadName, ctypes.byref(Via))
    return Via

def vSDK_Board_GetViaListCount(Board):
    """
    VSDK_EXPORT int vSDK_Board_GetViaListCount(Board _Board, int &_ViaCount);

    :param Board:
    :return: ViaCount
    """
    ViaCount = ctypes.c_int(0)
    vSDK_dll.vSDK_Board_GetViaListCount(Board, ctypes.byref(ViaCount))
    return ViaCount

def vSDK_Board_GetViaByIndex(Board, ViaIndex: int):
    """
    VSDK_EXPORT int vSDK_Board_GetViaByIndex(Board _Board, int _ViaIndex, Via &_Via);

    :param Board:
    :param ViaIndex:
    :return: Via
    """
    Via = ctypes.c_void_p()
    vSDK_dll.vSDK_Board_GetViaByIndex(Board, ViaIndex, ctypes.byref(Via))
    return Via

def vSDK_Board_AddMark(Board):
    """
    VSDK_EXPORT int vSDK_Board_AddMark(Board _Board, Mark &_Mark);

    :param Board:
    :return: Mark
    """
    Mark = ctypes.c_void_p()
    vSDK_dll.vSDK_Board_AddMark(Board, ctypes.byref(Mark))
    return Mark

def vSDK_Board_GetMarkListCount(Board):
    """
    VSDK_EXPORT int vSDK_Board_GetMarkListCount(Board _Board, int &_MarkCount);

    :param Board:
    :return: MarkCount
    """
    MarkCount = ctypes.c_int(0)
    vSDK_dll.vSDK_Board_GetMarkListCount(Board, ctypes.byref(MarkCount))
    return MarkCount

def vSDK_Board_GetMarkByIndex(Board, MarkIndex: int):
    """
    VSDK_EXPORT int vSDK_Board_GetMarkByIndex(Board _Board, const int _MarkIndex, Mark &_Mark);

    :param Board:
    :param MarkIndex:
    :return: Mark
    """
    Mark = ctypes.c_void_p()
    vSDK_dll.vSDK_Board_GetMarkByIndex(Board, MarkIndex, ctypes.byref(Mark))
    return Mark

def vSDK_Board_GetMarkByID(Board, MarkID: int):
    """
    VSDK_EXPORT int vSDK_Board_GetMarkByID(Board _Board, const int _MarkID, Mark &_Mark);

    :param Board:
    :param MarkID:
    :return: Mark
    """
    Mark = ctypes.c_void_p()
    vSDK_dll.vSDK_Board_GetMarkByID(Board, MarkID, ctypes.byref(Mark))
    return Mark

def vSDK_Board_GetMarkByName(Board, MarkName: bytes):
    """
    VSDK_EXPORT int vSDK_Board_GetMarkByName(Board _Board, const char *_MarkName, Mark &_Mark);

    :param Board:
    :param MarkName:
    :return: Mark
    """
    Mark = ctypes.c_void_p()
    vSDK_dll.vSDK_Board_GetMarkByName(Board, MarkName, ctypes.byref(Mark))
    return Mark

def vSDK_BOM_GetName(BOM):
    """
    VSDK_EXPORT int vSDK_BOM_GetName(BOM _BOM, char *&_cBOMName);

    :param BOM:
    :return: cBOMName
    """
    cBOMName = ctypes.c_char_p()
    vSDK_dll.vSDK_BOM_GetName(BOM, ctypes.byref(cBOMName))
    return cBOMName

def vSDK_BOM_GetPath(BOM):
    """
    VSDK_EXPORT int vSDK_BOM_GetPath(BOM _BOM, char *&_cBOMPath);

    :param BOM:
    :return: cBOMPath
    """
    cBOMPath = ctypes.c_char_p()
    vSDK_dll.vSDK_BOM_GetPath(BOM, ctypes.byref(cBOMPath))
    return cBOMPath

def vSDK_BOM_GetPNListCount(BOM):
    """
    VSDK_EXPORT int vSDK_BOM_GetPNListCount(BOM _BOM, int &_PNCount);

    :param BOM:
    :return: PNCount
    """
    PNCount = ctypes.c_int(0)
    vSDK_dll.vSDK_BOM_GetPNListCount(BOM, ctypes.byref(PNCount))
    return PNCount

def vSDK_BOM_GetPNByIndex(BOM, Index: int):
    """
    VSDK_EXPORT int vSDK_BOM_GetPNByIndex(BOM _BOM, int _Index, PN &_PN);

    :param BOM:
    :param Index:
    :return: PN
    """
    PN = ctypes.c_void_p()
    vSDK_dll.vSDK_BOM_GetPNByIndex(BOM, Index, ctypes.byref(PN))
    return PN

def vSDK_BOM_PN_SetPNName(PN, PNName: bytes):
    """
    VSDK_EXPORT int vSDK_BOM_PN_SetPNName(PN _PN, const char* _PNName);

    :param PN:
    :param PNName:
    :return: vSDK_dll.vSDK_BOM_PN_SetPNName(PN, PNName)
    """
    return vSDK_dll.vSDK_BOM_PN_SetPNName(PN, PNName)

def vSDK_BOM_PN_GetPNName(PN):
    """
    VSDK_EXPORT int vSDK_BOM_PN_GetPNName(PN _PN, char *&_PNName);

    :param PN:
    :return: PNName
    """
    PNName = ctypes.c_char_p()
    vSDK_dll.vSDK_BOM_PN_GetPNName(PN, ctypes.byref(PNName))
    return PNName

def vSDK_BOM_PN_SetPNFlag(PN, flag: int):
    """
    VSDK_EXPORT int vSDK_BOM_PN_SetPNFlag(PN _PN, int flag);

    :param PN:
    :param flag:
    :return: vSDK_dll.vSDK_BOM_PN_SetPNFlag(PN, flag)
    """
    return vSDK_dll.vSDK_BOM_PN_SetPNFlag(PN, flag)

def vSDK_BOM_PN_GetPNFlag(PN):
    """
    VSDK_EXPORT int vSDK_BOM_PN_GetPNFlag(PN _PN, int &flag);

    :param PN:
    :return: flag
    """
    flag = ctypes.c_int(0)
    vSDK_dll.vSDK_BOM_PN_GetPNFlag(PN, ctypes.byref(flag))
    return flag

def vSDK_BOM_PN_AddAltPN(PN, cAltPN: bytes):
    """
    VSDK_EXPORT int vSDK_BOM_PN_AddAltPN(PN _PN, const char *_cAltPN);

    :param PN:
    :param cAltPN:
    :return: vSDK_dll.vSDK_BOM_PN_AddAltPN(PN, cAltPN)
    """
    return vSDK_dll.vSDK_BOM_PN_AddAltPN(PN, cAltPN)

def vSDK_BOM_PN_GetAltPNsCount(PN):
    """
    VSDK_EXPORT int vSDK_BOM_PN_GetAltPNsCount(PN _PN, int &_AltPNCount);

    :param PN:
    :return: AltPNCount
    """
    AltPNCount = ctypes.c_int(0)
    vSDK_dll.vSDK_BOM_PN_GetAltPNsCount(PN, ctypes.byref(AltPNCount))
    return AltPNCount

def vSDK_BOM_PN_GetAltPNsByIndex(PN, Index: int):
    """
    VSDK_EXPORT int vSDK_BOM_PN_GetAltPNsByIndex(PN _PN, const int _Index, char *&_cAltPN);

    :param PN:
    :param Index:
    :return: cAltPN
    """
    cAltPN = ctypes.c_char_p()
    vSDK_dll.vSDK_BOM_PN_GetAltPNsByIndex(PN, Index, ctypes.byref(cAltPN))
    return cAltPN

def vSDK_BOM_PN_AddPNParam(PN, cKey: bytes, cValue: bytes):
    """
    VSDK_EXPORT int vSDK_BOM_PN_AddPNParam(PN _PN, const char *_cKey, const char *_cValue);

    :param PN:
    :param cKey:
    :param cValue:
    :return: vSDK_dll.vSDK_BOM_PN_AddPNParam(PN, cKey, cValue)
    """
    return vSDK_dll.vSDK_BOM_PN_AddPNParam(PN, cKey, cValue)

def vSDK_BOM_PN_GetPNParamsCount(PN):
    """
    VSDK_EXPORT int vSDK_BOM_PN_GetPNParamsCount(PN _PN, int &_ParamsCount);

    :param PN:
    :return: ParamsCount
    """
    ParamsCount = ctypes.c_int(0)
    vSDK_dll.vSDK_BOM_PN_GetPNParamsCount(PN, ctypes.byref(ParamsCount))
    return ParamsCount

def vSDK_BOM_PN_GetPNParamsByIndex(PN, Index: int):
    """
    VSDK_EXPORT int vSDK_BOM_PN_GetPNParamsByIndex(PN _PN, const int _Index, char *&_cKey, char *&_cValue);

    :param PN:
    :param Index:
    :return: cKey, cValue
    """
    cKey = ctypes.c_char_p()
    cValue = ctypes.c_char_p()
    vSDK_dll.vSDK_BOM_PN_GetPNParamsByIndex(PN, Index, ctypes.byref(cKey), ctypes.byref(cValue))
    return cKey, cValue

def vSDK_BOM_PN_AddPartName(PN, cPartName: bytes):
    """
    VSDK_EXPORT int vSDK_BOM_PN_AddPartName(PN _PN, const char *_cPartName);

    :param PN:
    :param cPartName:
    :return: vSDK_dll.vSDK_BOM_PN_AddPartName(PN, cPartName)
    """
    return vSDK_dll.vSDK_BOM_PN_AddPartName(PN, cPartName)

def vSDK_BOM_PN_GetPartNamesCount(PN):
    """
    VSDK_EXPORT int vSDK_BOM_PN_GetPartNamesCount(PN _PN, int &_PartNameCount);

    :param PN:
    :return: PartNameCount
    """
    PartNameCount = ctypes.c_int(0)
    vSDK_dll.vSDK_BOM_PN_GetPartNamesCount(PN, ctypes.byref(PartNameCount))
    return PartNameCount

def vSDK_BOM_PN_GetPartNamesByIndex(PN, Index: int):
    """
    VSDK_EXPORT int vSDK_BOM_PN_GetPartNamesByIndex(PN _PN, const int _Index, char *&_cPartName);

    :param PN:
    :param Index:
    :return: cPartName
    """
    cPartName = ctypes.c_char_p()
    vSDK_dll.vSDK_BOM_PN_GetPartNamesByIndex(PN, Index, ctypes.byref(cPartName))
    return cPartName

def vSDK_BOM_PN_GetCADLinkPartNameCount(PN):
    """
    VSDK_EXPORT int vSDK_BOM_PN_GetCADLinkPartNameCount(PN _PN, int &_PartNameCount);

    :param PN:
    :return: PartNameCount
    """
    PartNameCount = ctypes.c_int(0)
    vSDK_dll.vSDK_BOM_PN_GetCADLinkPartNameCount(PN, ctypes.byref(PartNameCount))
    return PartNameCount

def vSDK_BOM_PN_GetCADLinkPartName(PN, Index: int):
    """
    VSDK_EXPORT int vSDK_BOM_PN_GetCADLinkPartName(PN _PN, const int _Index, char *&_cPartName);

    :param PN:
    :param Index:
    :return: cPartName
    """
    cPartName = ctypes.c_char_p()
    vSDK_dll.vSDK_BOM_PN_GetCADLinkPartName(PN, Index, ctypes.byref(cPartName))
    return cPartName

def vSDK_BOM_PN_GetNoInCADPartNameCount(PN):
    """
    VSDK_EXPORT int vSDK_BOM_PN_GetNoInCADPartNameCount(PN _PN, int &_PartNameCount);

    :param PN:
    :return: PartNameCount
    """
    PartNameCount = ctypes.c_int(0)
    vSDK_dll.vSDK_BOM_PN_GetNoInCADPartNameCount(PN, ctypes.byref(PartNameCount))
    return PartNameCount

def vSDK_BOM_PN_GetNoInCADPartNameByIndex(PN, Index: int):
    """
    VSDK_EXPORT int vSDK_BOM_PN_GetNoInCADPartNameByIndex(PN _PN, const int _Index, char *&_cPartName);

    :param PN:
    :param Index:
    :return: cPartName
    """
    cPartName = ctypes.c_char_p()
    vSDK_dll.vSDK_BOM_PN_GetNoInCADPartNameByIndex(PN, Index, ctypes.byref(cPartName))
    return cPartName

def vSDK_DcodeTable_GetDcodeCount(DcodeTable):
    """
    VSDK_EXPORT int vSDK_DcodeTable_GetDcodeCount(DcodeTable _DcodeTable, int &_DcodeCount);

    :param DcodeTable:
    :return: DcodeCount
    """
    DcodeCount = ctypes.c_int(0)
    vSDK_dll.vSDK_DcodeTable_GetDcodeCount(DcodeTable, ctypes.byref(DcodeCount))
    return DcodeCount

def vSDK_DcodeTable_GetDcodeShapeCount(DcodeTable, DcodeIndex: int):
    """
    VSDK_EXPORT int vSDK_DcodeTable_GetDcodeShapeCount(DcodeTable _DcodeTable, const int _DcodeIndex, int &_ShapeCount);

    :param DcodeTable:
    :param DcodeIndex:
    :return: ShapeCount
    """
    ShapeCount = ctypes.c_int(0)
    vSDK_dll.vSDK_DcodeTable_GetDcodeShapeCount(DcodeTable, DcodeIndex, ctypes.byref(ShapeCount))
    return ShapeCount

def vSDK_DcodeTable_GetDcodeShapeByIndex(DcodeTable, DcodeIndex: int, iShapeIndex: int):
    """
    VSDK_EXPORT int vSDK_DcodeTable_GetDcodeShapeByIndex(DcodeTable _DcodeTable, const int _DcodeIndex, const int _iShapeIndex, Shape *&_Shape);

    :param DcodeTable:
    :param DcodeIndex:
    :param iShapeIndex:
    :return: Shape
    """
    Shape = ctypes.c_void_p()
    vSDK_dll.vSDK_DcodeTable_GetDcodeShapeByIndex(DcodeTable, DcodeIndex, iShapeIndex, ctypes.byref(Shape))
    return Shape

def vSDK_DcodeTable_FindRoundDcodeIDBySize(DcodeTable, X: float, Y: float, Size: float):
    """
    VSDK_EXPORT int vSDK_DcodeTable_FindRoundDcodeIDBySize(DcodeTable _DcodeTable, double _X, double _Y, double _Size, int &_DcodeID);

    :param DcodeTable:
    :param X:
    :param Y:
    :param Size:
    :return: DcodeID
    """
    DcodeID = ctypes.c_int(0)
    vSDK_dll.vSDK_DcodeTable_FindRoundDcodeIDBySize(DcodeTable, ctypes.c_double(X), ctypes.c_double(Y), ctypes.c_double(Size), ctypes.byref(DcodeID))
    return DcodeID

def vSDK_Dcode_CreateDcode(DcodeTable, DcodeName: bytes, DcodeAliasName: bytes):
    """
    VSDK_EXPORT int vSDK_Dcode_CreateDcode(DcodeTable _DcodeTable, const char *DcodeName, const char *DcodeAliasName, DCode &_DCode);

    :param DcodeTable:
    :param DcodeName:
    :param DcodeAliasName:
    :return: DCode
    """
    DCode = ctypes.c_void_p()
    vSDK_dll.vSDK_Dcode_CreateDcode(DcodeTable, DcodeName, DcodeAliasName, ctypes.byref(DCode))
    return DCode

def vSDK_Dcode_AddDcodeShape(DcodeTable, DCode, Shape):
    """
    VSDK_EXPORT int vSDK_Dcode_AddDcodeShape(DcodeTable _DcodeTable, DCode _DCode, Shape *_Shape);

    :param DcodeTable:
    :param DCode:
    :param Shape:
    :return: vSDK_dll.vSDK_Dcode_AddDcodeShape(DcodeTable, DCode, Shape)
    """
    return vSDK_dll.vSDK_Dcode_AddDcodeShape(DcodeTable, DCode, Shape)

def vSDK_Dcode_AddDcodeEnd(DcodeTable, DCode):
    """
    VSDK_EXPORT int vSDK_Dcode_AddDcodeEnd(DcodeTable _DcodeTable, DCode _DCode, int &_DcodeID);

    :param DcodeTable:
    :param DCode:
    :return: DcodeID
    """
    DcodeID = ctypes.c_int(0)
    vSDK_dll.vSDK_Dcode_AddDcodeEnd(DcodeTable, DCode, ctypes.byref(DcodeID))
    return DcodeID

def vSDK_Layer_SetLayerID(Layer, LayerID: int):
    """
    VSDK_EXPORT int vSDK_Layer_SetLayerID(Layer _Layer, int _LayerID);

    :param Layer:
    :param LayerID:
    :return: vSDK_dll.vSDK_Layer_SetLayerID(Layer, LayerID)
    """
    return vSDK_dll.vSDK_Layer_SetLayerID(Layer, LayerID)

def vSDK_Layer_GetLayerID(Layer):
    """
    VSDK_EXPORT int vSDK_Layer_GetLayerID(Layer _Layer, int &_LayerID);

    :param Layer:
    :return: LayerID
    """
    LayerID = ctypes.c_int(0)
    vSDK_dll.vSDK_Layer_GetLayerID(Layer, ctypes.byref(LayerID))
    return LayerID

def vSDK_Layer_SetLayerName(Layer, LayerName: bytes):
    """
    VSDK_EXPORT int vSDK_Layer_SetLayerName(Layer _Layer, const char *_LayerName);

    :param Layer:
    :param LayerName:
    :return: vSDK_dll.vSDK_Layer_SetLayerName(Layer, LayerName)
    """
    return vSDK_dll.vSDK_Layer_SetLayerName(Layer, LayerName)

def vSDK_Layer_GetLayerName(Layer):
    """
    VSDK_EXPORT int vSDK_Layer_GetLayerName(Layer _Layer, char *&_LayerName);

    :param Layer:
    :return: LayerName
    """
    LayerName = ctypes.c_char_p()
    vSDK_dll.vSDK_Layer_GetLayerName(Layer, ctypes.byref(LayerName))
    return LayerName

def vSDK_Layer_SetLayerSide(Layer, LayerSide: int):
    """
    VSDK_EXPORT int vSDK_Layer_SetLayerSide(Layer _Layer, int _LayerSide);

    :param Layer:
    :param LayerSide:
    :return: vSDK_dll.vSDK_Layer_SetLayerSide(Layer, LayerSide)
    """
    return vSDK_dll.vSDK_Layer_SetLayerSide(Layer, LayerSide)

def vSDK_Layer_GetLayerSide(Layer):
    """
    VSDK_EXPORT int vSDK_Layer_GetLayerSide(Layer _Layer, int &_LayerSide);

    :param Layer:
    :return: LayerSide
    """
    LayerSide = ctypes.c_int(0)
    vSDK_dll.vSDK_Layer_GetLayerSide(Layer, ctypes.byref(LayerSide))
    return LayerSide

def vSDK_Layer_SetLayerType(Layer, LayerType: int):
    """
    VSDK_EXPORT int vSDK_Layer_SetLayerType(Layer _Layer, int _LayerType);

    :param Layer:
    :param LayerType:
    :return: vSDK_dll.vSDK_Layer_SetLayerType(Layer, LayerType)
    """
    return vSDK_dll.vSDK_Layer_SetLayerType(Layer, LayerType)

def vSDK_Layer_GetLayerType(Layer):
    """
    VSDK_EXPORT int vSDK_Layer_GetLayerType(Layer _Layer, int &_LayerType);

    :param Layer:
    :return: LayerType
    """
    LayerType = ctypes.c_int(0)
    vSDK_dll.vSDK_Layer_GetLayerType(Layer, ctypes.byref(LayerType))
    return LayerType

def vSDK_Layer_SetLayerThickness(Layer, LayerThickness: float):
    """
    VSDK_EXPORT int vSDK_Layer_SetLayerThickness(Layer _Layer, double _LayerThickness);

    :param Layer:
    :param LayerThickness:
    :return: vSDK_dll.vSDK_Layer_SetLayerThickness(Layer, ctypes.c_double(LayerThickness))
    """
    return vSDK_dll.vSDK_Layer_SetLayerThickness(Layer, ctypes.c_double(LayerThickness))

def vSDK_Layer_GetLayerThickness(Layer):
    """
    VSDK_EXPORT int vSDK_Layer_GetLayerThickness(Layer _Layer, double &_LayerThickness);

    :param Layer:
    :return: LayerThickness
    """
    LayerThickness = ctypes.c_double()
    vSDK_dll.vSDK_Layer_GetLayerThickness(Layer, ctypes.byref(LayerThickness))
    return LayerThickness

def vSDK_Layer_SetReshThickness(Layer, LayerThickness: float):
    """
    VSDK_EXPORT int vSDK_Layer_SetReshThickness(Layer _Layer, double _LayerThickness);

    :param Layer:
    :param LayerThickness:
    :return: vSDK_dll.vSDK_Layer_SetReshThickness(Layer, ctypes.c_double(LayerThickness))
    """
    return vSDK_dll.vSDK_Layer_SetReshThickness(Layer, ctypes.c_double(LayerThickness))

def vSDK_Layer_GetReshThickness(Layer):
    """
    VSDK_EXPORT int vSDK_Layer_GetReshThickness(Layer _Layer, double &_LayerThickness);

    :param Layer:
    :return: LayerThickness
    """
    LayerThickness = ctypes.c_double()
    vSDK_dll.vSDK_Layer_GetReshThickness(Layer, ctypes.byref(LayerThickness))
    return LayerThickness

def vSDK_Layer_SetPositive(Layer, isPositive: bool):
    """
    VSDK_EXPORT int vSDK_Layer_SetPositive(Layer _Layer, bool _isPositive);

    :param Layer:
    :param isPositive:
    :return: vSDK_dll.vSDK_Layer_SetPositive(Layer, isPositive)
    """
    return vSDK_dll.vSDK_Layer_SetPositive(Layer, isPositive)

def vSDK_Layer_GetPositive(Layer):
    """
    VSDK_EXPORT int vSDK_Layer_GetPositive(Layer _Layer, bool &_isPositive);

    :param Layer:
    :return: isPositive
    """
    isPositive = ctypes.c_bool()
    vSDK_dll.vSDK_Layer_GetPositive(Layer, ctypes.byref(isPositive))
    return isPositive

def vSDK_Layer_GetPropertyCount(Layer):
    """
    VSDK_EXPORT int vSDK_Layer_GetPropertyCount(Layer _Layer, int &_PropertyCount);

    :param Layer:
    :return: PropertyCount
    """
    PropertyCount = ctypes.c_int(0)
    vSDK_dll.vSDK_Layer_GetPropertyCount(Layer, ctypes.byref(PropertyCount))
    return PropertyCount

def vSDK_Layer_GetPropertyByIndex(Layer, iIndex: int):
    """
    VSDK_EXPORT int vSDK_Layer_GetPropertyByIndex(Layer _Layer, int _iIndex, char *&_ckey, char *&_cvalue);

    :param Layer:
    :param iIndex:
    :return: ckey, cvalue
    """
    ckey = ctypes.c_char_p()
    cvalue = ctypes.c_char_p()
    vSDK_dll.vSDK_Layer_GetPropertyByIndex(Layer, iIndex, ctypes.byref(ckey), ctypes.byref(cvalue))
    return ckey, cvalue

def vSDK_Layer_AddProperty(Layer, ckey: bytes, cvalue: bytes):
    """
    VSDK_EXPORT int vSDK_Layer_AddProperty(Layer _Layer, const char *_ckey, const char *_cvalue);

    :param Layer:
    :param ckey:
    :param cvalue:
    :return: vSDK_dll.vSDK_Layer_AddProperty(Layer, ckey, cvalue)
    """
    return vSDK_dll.vSDK_Layer_AddProperty(Layer, ckey, cvalue)

def vSDK_Layer_GetLayerPropertyExist(Board, LayerName: bytes, Key: bytes):
    """
    VSDK_EXPORT int vSDK_Layer_GetLayerPropertyExist(Board _Board, const char *_LayerName, const char *_Key, bool &_IfExist);

    :param Board:
    :param LayerName:
    :param Key:
    :return: IfExist
    """
    IfExist = ctypes.c_bool()
    vSDK_dll.vSDK_Layer_GetLayerPropertyExist(Board, LayerName, Key, ctypes.byref(IfExist))
    return IfExist

def vSDK_Layer_AddLayerProperty(Board, LayerName: bytes, Key: bytes, Value: bytes):
    """
    VSDK_EXPORT int vSDK_Layer_AddLayerProperty(Board _Board, char *_LayerName, char *_Key, char *_Value);

    :param Board:
    :param LayerName:
    :param Key:
    :param Value:
    :return: vSDK_dll.vSDK_Layer_AddLayerProperty(Board, LayerName, Key, Value)
    """
    return vSDK_dll.vSDK_Layer_AddLayerProperty(Board, LayerName, Key, Value)

def vSDK_Layer_DeleteLayerProperty(Board, LayerName: bytes, Key: bytes):
    """
    VSDK_EXPORT int vSDK_Layer_DeleteLayerProperty(Board _Board, char *_LayerName, char *_Key);

    :param Board:
    :param LayerName:
    :param Key:
    :return: vSDK_dll.vSDK_Layer_DeleteLayerProperty(Board, LayerName, Key)
    """
    return vSDK_dll.vSDK_Layer_DeleteLayerProperty(Board, LayerName, Key)

def vSDK_Layer_GetLayerBound(Layer):
    """
    VSDK_EXPORT int vSDK_Layer_GetLayerBound(Layer _Layer, double &_dMinX, double &_dMinY, double &_dMaxX, double &_dMaxY, bool &_bBoundExist);

    :param Layer:
    :return: dMinX, dMinY, dMaxX, dMaxY, bBoundExist
    """
    dMinX = ctypes.c_double()
    dMinY = ctypes.c_double()
    dMaxX = ctypes.c_double()
    dMaxY = ctypes.c_double()
    bBoundExist = ctypes.c_bool()
    vSDK_dll.vSDK_Layer_GetLayerBound(Layer, ctypes.byref(dMinX), ctypes.byref(dMinY), ctypes.byref(dMaxX), ctypes.byref(dMaxY), ctypes.byref(bBoundExist))
    return dMinX, dMinY, dMaxX, dMaxY, bBoundExist

def vSDK_Layer_GetDcodeCountByLayerId(Board, LayerId: int):
    """
    VSDK_EXPORT int vSDK_Layer_GetDcodeCountByLayerId(Board _Board, const int _LayerId, int &_DcodeCount, DcodeTable &_DcodeTable);

    :param Board:
    :param LayerId:
    :return: DcodeCount, DcodeTable
    """
    DcodeCount = ctypes.c_int(0)
    DcodeTable = ctypes.c_void_p()
    vSDK_dll.vSDK_Layer_GetDcodeCountByLayerId(Board, LayerId, ctypes.byref(DcodeCount), ctypes.byref(DcodeTable))
    return DcodeCount, DcodeTable

def vSDK_Layer_ByCircleSize_GetDCodeID(Board, LayerId: int, Size: float):
    """
    VSDK_EXPORT int vSDK_Layer_ByCircleSize_GetDCodeID(Board _Board, const int _LayerId, double _Size, int &_DcodeID);

    :param Board:
    :param LayerId:
    :param Size:
    :return: DcodeID
    """
    DcodeID = ctypes.c_int(0)
    vSDK_dll.vSDK_Layer_ByCircleSize_GetDCodeID(Board, LayerId, ctypes.c_double(Size), ctypes.byref(DcodeID))
    return DcodeID

def vSDK_Layer_LoadLayerByLayerID(Board, LayerID: int):
    """
    VSDK_EXPORT int vSDK_Layer_LoadLayerByLayerID(Board _Board, const int _LayerID);

    :param Board:
    :param LayerID:
    :return: vSDK_dll.vSDK_Layer_LoadLayerByLayerID(Board, LayerID)
    """
    return vSDK_dll.vSDK_Layer_LoadLayerByLayerID(Board, LayerID)

def vSDK_Layer_GetLayerObjectCount(Board, LayerID: int):
    """
    VSDK_EXPORT int vSDK_Layer_GetLayerObjectCount(Board _Board, int _LayerID, int &_iObjectCount);

    :param Board:
    :param LayerID:
    :return: iObjectCount
    """
    iObjectCount = ctypes.c_int(0)
    vSDK_dll.vSDK_Layer_GetLayerObjectCount(Board, LayerID, ctypes.byref(iObjectCount))
    return iObjectCount

def vSDK_Layer_GetLayerObjectPositive(Board, LayerID: int, iObjectIndex: int):
    """
    VSDK_EXPORT int vSDK_Layer_GetLayerObjectPositive(Board _Board, int _LayerID, int _iObjectIndex, bool &_Positive);

    :param Board:
    :param LayerID:
    :param iObjectIndex:
    :return: Positive
    """
    Positive = ctypes.c_bool()
    vSDK_dll.vSDK_Layer_GetLayerObjectPositive(Board, LayerID, iObjectIndex, ctypes.byref(Positive))
    return Positive

def vSDK_Layer_GetLayerObjectType(Board, LayerID: int, iObjectIndex: int):
    """
    VSDK_EXPORT int vSDK_Layer_GetLayerObjectType(Board _Board, int _LayerID, int _iObjectIndex, int &_iShapeType);

    :param Board:
    :param LayerID:
    :param iObjectIndex:
    :return: iShapeType
    """
    iShapeType = ctypes.c_int(0)
    vSDK_dll.vSDK_Layer_GetLayerObjectType(Board, LayerID, iObjectIndex, ctypes.byref(iShapeType))
    return iShapeType

def vSDK_Layer_GetLayerObjectDCodeIndex(Board, LayerID: int, iObjectIndex: int):
    """
    VSDK_EXPORT int vSDK_Layer_GetLayerObjectDCodeIndex(Board _Board, int _LayerID, int _iObjectIndex, int &_DCodeIndex);

    :param Board:
    :param LayerID:
    :param iObjectIndex:
    :return: DCodeIndex
    """
    DCodeIndex = ctypes.c_int(0)
    vSDK_dll.vSDK_Layer_GetLayerObjectDCodeIndex(Board, LayerID, iObjectIndex, ctypes.byref(DCodeIndex))
    return DCodeIndex

def vSDK_Layer_GetLayerObjectShapeCount(Board, LayerID: int, iObjectIndex: int):
    """
    VSDK_EXPORT int vSDK_Layer_GetLayerObjectShapeCount(Board _Board, int _LayerID, int _iObjectIndex, int &_iShapeCount);

    :param Board:
    :param LayerID:
    :param iObjectIndex:
    :return: iShapeCount
    """
    iShapeCount = ctypes.c_int(0)
    vSDK_dll.vSDK_Layer_GetLayerObjectShapeCount(Board, LayerID, iObjectIndex, ctypes.byref(iShapeCount))
    return iShapeCount

def vSDK_Layer_GetLayerObjectShapeByIndex(Board, LayerID: int, iObjectIndex: int, iShapeIndex: int):
    """
    VSDK_EXPORT int vSDK_Layer_GetLayerObjectShapeByIndex(Board _Board, int _LayerID, int _iObjectIndex, int _iShapeIndex, int &_Mirror, double &_Angle, int &_DcodeId, Shape *&_Shape);

    :param Board:
    :param LayerID:
    :param iObjectIndex:
    :param iShapeIndex:
    :return: Mirror, Angle, DcodeId, Shape
    """
    Mirror = ctypes.c_int(0)
    Angle = ctypes.c_double()
    DcodeId = ctypes.c_int(0)
    Shape = ctypes.c_void_p()
    vSDK_dll.vSDK_Layer_GetLayerObjectShapeByIndex(Board, LayerID, iObjectIndex, iShapeIndex, ctypes.byref(Mirror), ctypes.byref(Angle), ctypes.byref(DcodeId), ctypes.byref(Shape))
    return Mirror, Angle, DcodeId, Shape

def vSDK_Layer_AddShapeByDcode(Board, LayerId: int, NetID: int, Mirror: int, Angle: float, DcodeId: int, PositiveNegative: bool, X: float, Y: float):
    """
    VSDK_EXPORT int vSDK_Layer_AddShapeByDcode(Board _Board, int LayerId, int NetID, int Mirror, double Angle, int DcodeId, bool PositiveNegative, double X, double Y, int &LayerObjectId);

    :param Board:
    :param LayerId:
    :param NetID:
    :param Mirror:
    :param Angle:
    :param DcodeId:
    :param PositiveNegative:
    :param X:
    :param Y:
    :return: LayerObjectId
    """
    LayerObjectId = ctypes.c_int(0)
    vSDK_dll.vSDK_Layer_AddShapeByDcode(Board, LayerId, NetID, Mirror, ctypes.c_double(Angle), DcodeId, PositiveNegative, ctypes.c_double(X), ctypes.c_double(Y), ctypes.byref(LayerObjectId))
    return LayerObjectId

def vSDK_Layer_AddShapeByLine(Board, LayerId: int, NetID: int, Shape):
    """
    VSDK_EXPORT int vSDK_Layer_AddShapeByLine(Board _Board, int LayerId, int NetID, Shape *_Shape, int &LayerObjectId);

    :param Board:
    :param LayerId:
    :param NetID:
    :param Shape:
    :return: LayerObjectId
    """
    LayerObjectId = ctypes.c_int(0)
    vSDK_dll.vSDK_Layer_AddShapeByLine(Board, LayerId, NetID, Shape, ctypes.byref(LayerObjectId))
    return LayerObjectId

def vSDK_Layer_AddShapeByArc(Board, LayerId: int, NetID: int, Shape):
    """
    VSDK_EXPORT int vSDK_Layer_AddShapeByArc(Board _Board, int LayerId, int NetID, Shape *_Shape, int &LayerObjectId);

    :param Board:
    :param LayerId:
    :param NetID:
    :param Shape:
    :return: LayerObjectId
    """
    LayerObjectId = ctypes.c_int(0)
    vSDK_dll.vSDK_Layer_AddShapeByArc(Board, LayerId, NetID, Shape, ctypes.byref(LayerObjectId))
    return LayerObjectId

def vSDK_Layer_AddShapeGroupPolygonsStart(Board, LayerId: int, NetID: int, PositiveNegative: bool):
    """
    VSDK_EXPORT int vSDK_Layer_AddShapeGroupPolygonsStart(Board _Board, int LayerId, int NetID, bool PositiveNegative, void *&_GroupPolygons, int &LayerObjectId);

    :param Board:
    :param LayerId:
    :param NetID:
    :param PositiveNegative:
    :return: GroupPolygons, LayerObjectId
    """
    GroupPolygons = ctypes.c_void()
    LayerObjectId = ctypes.c_int(0)
    vSDK_dll.vSDK_Layer_AddShapeGroupPolygonsStart(Board, LayerId, NetID, PositiveNegative, ctypes.byref(GroupPolygons), ctypes.byref(LayerObjectId))
    return GroupPolygons, LayerObjectId

def vSDK_Layer_AddShapeGroupPolygonsEnd(Board, LayerId: int, GroupPolygons: int):
    """
    VSDK_EXPORT int vSDK_Layer_AddShapeGroupPolygonsEnd(Board _Board, int LayerId, void *_GroupPolygons);

    :param Board:
    :param LayerId:
    :param GroupPolygons:
    :return: vSDK_dll.vSDK_Layer_AddShapeGroupPolygonsEnd(Board, LayerId, GroupPolygons)
    """
    return vSDK_dll.vSDK_Layer_AddShapeGroupPolygonsEnd(Board, LayerId, GroupPolygons)

def vSDK_Layer_AddShapeByPolygon(Board, LayerId: int, NetID: int, GroupPolygons: int, Shape):
    """
    VSDK_EXPORT int vSDK_Layer_AddShapeByPolygon(Board _Board, int LayerId, int NetID, void *_GroupPolygons, Shape *_Shape, int &LayerObjectId);

    :param Board:
    :param LayerId:
    :param NetID:
    :param GroupPolygons:
    :param Shape:
    :return: LayerObjectId
    """
    LayerObjectId = ctypes.c_int(0)
    vSDK_dll.vSDK_Layer_AddShapeByPolygon(Board, LayerId, NetID, GroupPolygons, Shape, ctypes.byref(LayerObjectId))
    return LayerObjectId

def vSDK_Layer_AddShapeByContinuousLine(Board, LayerId: int, NetID: int, Shape):
    """
    VSDK_EXPORT int vSDK_Layer_AddShapeByContinuousLine(Board _Board, int LayerId, int NetID, Shape *_Shape, int &LayerObjectId);

    :param Board:
    :param LayerId:
    :param NetID:
    :param Shape:
    :return: LayerObjectId
    """
    LayerObjectId = ctypes.c_int(0)
    vSDK_dll.vSDK_Layer_AddShapeByContinuousLine(Board, LayerId, NetID, Shape, ctypes.byref(LayerObjectId))
    return LayerObjectId

def vSDK_Layer_SetLayerObjectNetID(Board, LayerId: int, LayerObjectId: int, NetID: int):
    """
    VSDK_EXPORT int vSDK_Layer_SetLayerObjectNetID(Board _Board, int LayerId, const int LayerObjectId, const int NetID);

    :param Board:
    :param LayerId:
    :param LayerObjectId:
    :param NetID:
    :return: vSDK_dll.vSDK_Layer_SetLayerObjectNetID(Board, LayerId, LayerObjectId, NetID)
    """
    return vSDK_dll.vSDK_Layer_SetLayerObjectNetID(Board, LayerId, LayerObjectId, NetID)

def vSDK_Layer_GetLayerObjectNetID(Board, LayerId: int, LayerObjectId: int):
    """
    VSDK_EXPORT int vSDK_Layer_GetLayerObjectNetID(Board _Board, int LayerId, const int LayerObjectId, int &NetID);

    :param Board:
    :param LayerId:
    :param LayerObjectId:
    :return: NetID
    """
    NetID = ctypes.c_int(0)
    vSDK_dll.vSDK_Layer_GetLayerObjectNetID(Board, LayerId, LayerObjectId, ctypes.byref(NetID))
    return NetID

def vSDK_Layer_SetLayerPadPartID(Board, LayerId: int, LayerObjectId: int, PartID: int):
    """
    VSDK_EXPORT int vSDK_Layer_SetLayerPadPartID(Board _Board, int LayerId, const int LayerObjectId, const int PartID);

    :param Board:
    :param LayerId:
    :param LayerObjectId:
    :param PartID:
    :return: vSDK_dll.vSDK_Layer_SetLayerPadPartID(Board, LayerId, LayerObjectId, PartID)
    """
    return vSDK_dll.vSDK_Layer_SetLayerPadPartID(Board, LayerId, LayerObjectId, PartID)

def vSDK_Layer_GetLayerPadPartID(Board, LayerId: int, LayerObjectId: int):
    """
    VSDK_EXPORT int vSDK_Layer_GetLayerPadPartID(Board _Board, int LayerId, const int LayerObjectId, int &PartID);

    :param Board:
    :param LayerId:
    :param LayerObjectId:
    :return: PartID
    """
    PartID = ctypes.c_int(0)
    vSDK_dll.vSDK_Layer_GetLayerPadPartID(Board, LayerId, LayerObjectId, ctypes.byref(PartID))
    return PartID

def vSDK_Layer_SetLayerPadPinID(Board, LayerId: int, LayerObjectId: int, PinID: int):
    """
    VSDK_EXPORT int vSDK_Layer_SetLayerPadPinID(Board _Board, int LayerId, const int LayerObjectId, const int PinID);

    :param Board:
    :param LayerId:
    :param LayerObjectId:
    :param PinID:
    :return: vSDK_dll.vSDK_Layer_SetLayerPadPinID(Board, LayerId, LayerObjectId, PinID)
    """
    return vSDK_dll.vSDK_Layer_SetLayerPadPinID(Board, LayerId, LayerObjectId, PinID)

def vSDK_Layer_GetLayerPadPinID(Board, LayerId: int, LayerObjectId: int):
    """
    VSDK_EXPORT int vSDK_Layer_GetLayerPadPinID(Board _Board, int LayerId, const int LayerObjectId, int &PinID);

    :param Board:
    :param LayerId:
    :param LayerObjectId:
    :return: PinID
    """
    PinID = ctypes.c_int(0)
    vSDK_dll.vSDK_Layer_GetLayerPadPinID(Board, LayerId, LayerObjectId, ctypes.byref(PinID))
    return PinID

def vSDK_Layer_SetLayerPadSMD(Board, LayerId: int, LayerObjectId: int, SMD: int):
    """
    VSDK_EXPORT int vSDK_Layer_SetLayerPadSMD(Board _Board, int LayerId, const int LayerObjectId, const int SMD);

    :param Board:
    :param LayerId:
    :param LayerObjectId:
    :param SMD:
    :return: vSDK_dll.vSDK_Layer_SetLayerPadSMD(Board, LayerId, LayerObjectId, SMD)
    """
    return vSDK_dll.vSDK_Layer_SetLayerPadSMD(Board, LayerId, LayerObjectId, SMD)

def vSDK_Layer_GetLayerPadSMD(Board, LayerId: int, LayerObjectId: int):
    """
    VSDK_EXPORT int vSDK_Layer_GetLayerPadSMD(Board _Board, int LayerId, const int LayerObjectId, int &SMD);

    :param Board:
    :param LayerId:
    :param LayerObjectId:
    :return: SMD
    """
    SMD = ctypes.c_int(0)
    vSDK_dll.vSDK_Layer_GetLayerPadSMD(Board, LayerId, LayerObjectId, ctypes.byref(SMD))
    return SMD

def vSDK_Layer_SetLayerPadPlated(Board, LayerId: int, LayerObjectId: int, Plated: int):
    """
    VSDK_EXPORT int vSDK_Layer_SetLayerPadPlated(Board _Board, int LayerId, const int LayerObjectId, const int Plated);

    :param Board:
    :param LayerId:
    :param LayerObjectId:
    :param Plated:
    :return: vSDK_dll.vSDK_Layer_SetLayerPadPlated(Board, LayerId, LayerObjectId, Plated)
    """
    return vSDK_dll.vSDK_Layer_SetLayerPadPlated(Board, LayerId, LayerObjectId, Plated)

def vSDK_Layer_GetLayerPadPlated(Board, LayerId: int, LayerObjectId: int):
    """
    VSDK_EXPORT int vSDK_Layer_GetLayerPadPlated(Board _Board, int LayerId, const int LayerObjectId, int &Plated);

    :param Board:
    :param LayerId:
    :param LayerObjectId:
    :return: Plated
    """
    Plated = ctypes.c_int(0)
    vSDK_dll.vSDK_Layer_GetLayerPadPlated(Board, LayerId, LayerObjectId, ctypes.byref(Plated))
    return Plated

def vSDK_Layer_SetLayerPadUsage(Board, LayerId: int, LayerObjectId: int, Usage: int):
    """
    VSDK_EXPORT int vSDK_Layer_SetLayerPadUsage(Board _Board, int LayerId, const int LayerObjectId, const int Usage);

    :param Board:
    :param LayerId:
    :param LayerObjectId:
    :param Usage:
    :return: vSDK_dll.vSDK_Layer_SetLayerPadUsage(Board, LayerId, LayerObjectId, Usage)
    """
    return vSDK_dll.vSDK_Layer_SetLayerPadUsage(Board, LayerId, LayerObjectId, Usage)

def vSDK_Layer_GetLayerPadUsage(Board, LayerId: int, LayerObjectId: int):
    """
    VSDK_EXPORT int vSDK_Layer_GetLayerPadUsage(Board _Board, int LayerId, const int LayerObjectId, int &Usage);

    :param Board:
    :param LayerId:
    :param LayerObjectId:
    :return: Usage
    """
    Usage = ctypes.c_int(0)
    vSDK_dll.vSDK_Layer_GetLayerPadUsage(Board, LayerId, LayerObjectId, ctypes.byref(Usage))
    return Usage

def vSDK_Layer_SetLayerPadTestpoint(Board, LayerId: int, LayerObjectId: int, Testpoint: int):
    """
    VSDK_EXPORT int vSDK_Layer_SetLayerPadTestpoint(Board _Board, int LayerId, const int LayerObjectId, const int Testpoint);

    :param Board:
    :param LayerId:
    :param LayerObjectId:
    :param Testpoint:
    :return: vSDK_dll.vSDK_Layer_SetLayerPadTestpoint(Board, LayerId, LayerObjectId, Testpoint)
    """
    return vSDK_dll.vSDK_Layer_SetLayerPadTestpoint(Board, LayerId, LayerObjectId, Testpoint)

def vSDK_Layer_GetLayerPadTestpoint(Board, LayerId: int, LayerObjectId: int):
    """
    VSDK_EXPORT int vSDK_Layer_GetLayerPadTestpoint(Board _Board, int LayerId, const int LayerObjectId, int &Testpoint);

    :param Board:
    :param LayerId:
    :param LayerObjectId:
    :return: Testpoint
    """
    Testpoint = ctypes.c_int(0)
    vSDK_dll.vSDK_Layer_GetLayerPadTestpoint(Board, LayerId, LayerObjectId, ctypes.byref(Testpoint))
    return Testpoint

def vSDK_Layer_SetLayerPadFiducial(Board, LayerId: int, LayerObjectId: int, Fiducial: int):
    """
    VSDK_EXPORT int vSDK_Layer_SetLayerPadFiducial(Board _Board, int LayerId, const int LayerObjectId, const int Fiducial);

    :param Board:
    :param LayerId:
    :param LayerObjectId:
    :param Fiducial:
    :return: vSDK_dll.vSDK_Layer_SetLayerPadFiducial(Board, LayerId, LayerObjectId, Fiducial)
    """
    return vSDK_dll.vSDK_Layer_SetLayerPadFiducial(Board, LayerId, LayerObjectId, Fiducial)

def vSDK_Layer_GetLayerPadFiducial(Board, LayerId: int, LayerObjectId: int):
    """
    VSDK_EXPORT int vSDK_Layer_GetLayerPadFiducial(Board _Board, int LayerId, const int LayerObjectId, int &Fiducial);

    :param Board:
    :param LayerId:
    :param LayerObjectId:
    :return: Fiducial
    """
    Fiducial = ctypes.c_int(0)
    vSDK_dll.vSDK_Layer_GetLayerPadFiducial(Board, LayerId, LayerObjectId, ctypes.byref(Fiducial))
    return Fiducial

def vSDK_Layer_SetLayerObjectExtendedParameter(Board, LayerId: int, LayerObjectId: int, cKey: bytes, cValue: bytes):
    """
    VSDK_EXPORT int vSDK_Layer_SetLayerObjectExtendedParameter(Board _Board, int LayerId, const int LayerObjectId, const char *_cKey, const char *_cValue);

    :param Board:
    :param LayerId:
    :param LayerObjectId:
    :param cKey:
    :param cValue:
    :return: vSDK_dll.vSDK_Layer_SetLayerObjectExtendedParameter(Board, LayerId, LayerObjectId, cKey, cValue)
    """
    return vSDK_dll.vSDK_Layer_SetLayerObjectExtendedParameter(Board, LayerId, LayerObjectId, cKey, cValue)

def vSDK_Layer_GetLayerObjectExtendedParameter(Board, LayerId: int, LayerObjectId: int, cKey: bytes):
    """
    VSDK_EXPORT int vSDK_Layer_GetLayerObjectExtendedParameter(Board _Board, int LayerId, const int LayerObjectId, const char *_cKey, char *&_cValue);

    :param Board:
    :param LayerId:
    :param LayerObjectId:
    :param cKey:
    :return: cValue
    """
    cValue = ctypes.c_char_p()
    vSDK_dll.vSDK_Layer_GetLayerObjectExtendedParameter(Board, LayerId, LayerObjectId, cKey, ctypes.byref(cValue))
    return cValue

def vSDK_LayerShape_SetLayerName(LayerShape, LayerName: bytes):
    """
    VSDK_EXPORT int vSDK_LayerShape_SetLayerName(LayerShape _LayerShape, const char *LayerName);

    :param LayerShape:
    :param LayerName:
    :return: vSDK_dll.vSDK_LayerShape_SetLayerName(LayerShape, LayerName)
    """
    return vSDK_dll.vSDK_LayerShape_SetLayerName(LayerShape, LayerName)

def vSDK_LayerShape_GetLayerName(LayerShape):
    """
    VSDK_EXPORT int vSDK_LayerShape_GetLayerName(LayerShape _LayerShape, char *&LayerName);

    :param LayerShape:
    :return: LayerName
    """
    LayerName = ctypes.c_char_p()
    vSDK_dll.vSDK_LayerShape_GetLayerName(LayerShape, ctypes.byref(LayerName))
    return LayerName

def vSDK_LayerShape_AddShape(Shape, XOrigin: float, YOrigin: float, Mirror: int, Angle: float, XOffset: float, YOffset: float):
    """
    VSDK_EXPORT int vSDK_LayerShape_AddShape(Shape *_Shape, const double _XOrigin, const double _YOrigin, const int _Mirror, const double _Angle, const double _XOffset, const double _YOffset, LayerShape &_LayerShape);

    :param Shape:
    :param XOrigin:
    :param YOrigin:
    :param Mirror:
    :param Angle:
    :param XOffset:
    :param YOffset:
    :return: LayerShape
    """
    LayerShape = ctypes.c_void_p()
    vSDK_dll.vSDK_LayerShape_AddShape(Shape, ctypes.c_double(XOrigin), ctypes.c_double(YOrigin), Mirror, ctypes.c_double(Angle), ctypes.c_double(XOffset), ctypes.c_double(YOffset), ctypes.byref(LayerShape))
    return LayerShape

def vSDK_LayerShape_GetShapeExposure(LayerShape):
    """
    VSDK_EXPORT int vSDK_LayerShape_GetShapeExposure(LayerShape _LayerShape, bool &PositiveNegative);

    :param LayerShape:
    :return: PositiveNegative
    """
    PositiveNegative = ctypes.c_bool()
    vSDK_dll.vSDK_LayerShape_GetShapeExposure(LayerShape, ctypes.byref(PositiveNegative))
    return PositiveNegative

def vSDK_LayerShape_GetShapeCount(LayerShape):
    """
    VSDK_EXPORT int vSDK_LayerShape_GetShapeCount(LayerShape _LayerShape, int &_ShapeCount);

    :param LayerShape:
    :return: ShapeCount
    """
    ShapeCount = ctypes.c_int(0)
    vSDK_dll.vSDK_LayerShape_GetShapeCount(LayerShape, ctypes.byref(ShapeCount))
    return ShapeCount

def vSDK_LayerShape_GetShapeByIndex(LayerShape, Index: int):
    """
    VSDK_EXPORT int vSDK_LayerShape_GetShapeByIndex(LayerShape _LayerShape, int _Index, double &_XOrigin, double &_YOrigin, int &_Mirror, double &_Angle, double &_XOffset, double &_YOffset, Shape *&_Shape);

    :param LayerShape:
    :param Index:
    :return: XOrigin, YOrigin, Mirror, Angle, XOffset, YOffset, Shape
    """
    XOrigin = ctypes.c_double()
    YOrigin = ctypes.c_double()
    Mirror = ctypes.c_int(0)
    Angle = ctypes.c_double()
    XOffset = ctypes.c_double()
    YOffset = ctypes.c_double()
    Shape = ctypes.c_void_p()
    vSDK_dll.vSDK_LayerShape_GetShapeByIndex(LayerShape, Index, ctypes.byref(XOrigin), ctypes.byref(YOrigin), ctypes.byref(Mirror), ctypes.byref(Angle), ctypes.byref(XOffset), ctypes.byref(YOffset), ctypes.byref(Shape))
    return XOrigin, YOrigin, Mirror, Angle, XOffset, YOffset, Shape

def vSDK_Mark_SetMarkName(Mark, MarkName: bytes):
    """
    VSDK_EXPORT int vSDK_Mark_SetMarkName(Mark _Mark, const char* _MarkName);

    :param Mark:
    :param MarkName:
    :return: vSDK_dll.vSDK_Mark_SetMarkName(Mark, MarkName)
    """
    return vSDK_dll.vSDK_Mark_SetMarkName(Mark, MarkName)

def vSDK_Mark_GetMarkName(Mark):
    """
    VSDK_EXPORT int vSDK_Mark_GetMarkName(Mark _Mark, char *&_MarkName);

    :param Mark:
    :return: MarkName
    """
    MarkName = ctypes.c_char_p()
    vSDK_dll.vSDK_Mark_GetMarkName(Mark, ctypes.byref(MarkName))
    return MarkName

def vSDK_Mark_SetMarkID(Mark, MarkID: int):
    """
    VSDK_EXPORT int vSDK_Mark_SetMarkID(Mark _Mark, const int _MarkID);

    :param Mark:
    :param MarkID:
    :return: vSDK_dll.vSDK_Mark_SetMarkID(Mark, MarkID)
    """
    return vSDK_dll.vSDK_Mark_SetMarkID(Mark, MarkID)

def vSDK_Mark_GetMarkID(Mark):
    """
    VSDK_EXPORT int vSDK_Mark_GetMarkID(Mark _Mark, int &_MarkID);

    :param Mark:
    :return: MarkID
    """
    MarkID = ctypes.c_int(0)
    vSDK_dll.vSDK_Mark_GetMarkID(Mark, ctypes.byref(MarkID))
    return MarkID

def vSDK_Mark_SetLayerName(Mark, LayerName: bytes):
    """
    VSDK_EXPORT int vSDK_Mark_SetLayerName(Mark _Mark, const char *LayerName);

    :param Mark:
    :param LayerName:
    :return: vSDK_dll.vSDK_Mark_SetLayerName(Mark, LayerName)
    """
    return vSDK_dll.vSDK_Mark_SetLayerName(Mark, LayerName)

def vSDK_Mark_GetLayerName(Mark):
    """
    VSDK_EXPORT int vSDK_Mark_GetLayerName(Mark _Mark, char *&LayerName);

    :param Mark:
    :return: LayerName
    """
    LayerName = ctypes.c_char_p()
    vSDK_dll.vSDK_Mark_GetLayerName(Mark, ctypes.byref(LayerName))
    return LayerName

def vSDK_Mark_SetMarkPos(Mark, MarkPosX: float, MarkPosY: float):
    """
    VSDK_EXPORT int vSDK_Mark_SetMarkPos(Mark _Mark, const double _MarkPosX, const double _MarkPosY);

    :param Mark:
    :param MarkPosX:
    :param MarkPosY:
    :return: vSDK_dll.vSDK_Mark_SetMarkPos(Mark, ctypes.c_double(MarkPosX), ctypes.c_double(MarkPosY))
    """
    return vSDK_dll.vSDK_Mark_SetMarkPos(Mark, ctypes.c_double(MarkPosX), ctypes.c_double(MarkPosY))

def vSDK_Mark_GetMarkPos(Mark):
    """
    VSDK_EXPORT int vSDK_Mark_GetMarkPos(Mark _Mark, double &_MarkPosX, double &_MarkPosY);

    :param Mark:
    :return: MarkPosX, MarkPosY
    """
    MarkPosX = ctypes.c_double()
    MarkPosY = ctypes.c_double()
    vSDK_dll.vSDK_Mark_GetMarkPos(Mark, ctypes.byref(MarkPosX), ctypes.byref(MarkPosY))
    return MarkPosX, MarkPosY

def vSDK_Mark_SetMarkAngle(Mark, MarkAngle: float):
    """
    VSDK_EXPORT int vSDK_Mark_SetMarkAngle(Mark _Mark, const double _MarkAngle);

    :param Mark:
    :param MarkAngle:
    :return: vSDK_dll.vSDK_Mark_SetMarkAngle(Mark, ctypes.c_double(MarkAngle))
    """
    return vSDK_dll.vSDK_Mark_SetMarkAngle(Mark, ctypes.c_double(MarkAngle))

def vSDK_Mark_GetMarkAngle(Mark):
    """
    VSDK_EXPORT int vSDK_Mark_GetMarkAngle(Mark _Mark, double &_MarkAngle);

    :param Mark:
    :return: MarkAngle
    """
    MarkAngle = ctypes.c_double()
    vSDK_dll.vSDK_Mark_GetMarkAngle(Mark, ctypes.byref(MarkAngle))
    return MarkAngle

def vSDK_Mark_SetMarkSize(Mark, MarkSize: float):
    """
    VSDK_EXPORT int vSDK_Mark_SetMarkSize(Mark _Mark, const double _MarkSize);

    :param Mark:
    :param MarkSize:
    :return: vSDK_dll.vSDK_Mark_SetMarkSize(Mark, ctypes.c_double(MarkSize))
    """
    return vSDK_dll.vSDK_Mark_SetMarkSize(Mark, ctypes.c_double(MarkSize))

def vSDK_Mark_GetMarkSize(Mark):
    """
    VSDK_EXPORT int vSDK_Mark_GetMarkSize(Mark _Mark, double &_MarkSize);

    :param Mark:
    :return: MarkSize
    """
    MarkSize = ctypes.c_double()
    vSDK_dll.vSDK_Mark_GetMarkSize(Mark, ctypes.byref(MarkSize))
    return MarkSize

def vSDK_Mark_AddProperty(Mark, ckey: bytes, cvalue: bytes):
    """
    VSDK_EXPORT int vSDK_Mark_AddProperty(Mark _Mark, const char *ckey, const char *cvalue);

    :param Mark:
    :param ckey:
    :param cvalue:
    :return: vSDK_dll.vSDK_Mark_AddProperty(Mark, ckey, cvalue)
    """
    return vSDK_dll.vSDK_Mark_AddProperty(Mark, ckey, cvalue)

def vSDK_Mark_FindPropertyVal(Mark, ckey: bytes):
    """
    VSDK_EXPORT int vSDK_Mark_FindPropertyVal(Mark _Mark, const char *ckey, char *&cvalue);

    :param Mark:
    :param ckey:
    :return: cvalue
    """
    cvalue = ctypes.c_char_p()
    vSDK_dll.vSDK_Mark_FindPropertyVal(Mark, ckey, ctypes.byref(cvalue))
    return cvalue

def vSDK_Mark_GetPropertyCount(Mark):
    """
    VSDK_EXPORT int vSDK_Mark_GetPropertyCount(Mark _Mark, int &_PropertyCount);

    :param Mark:
    :return: PropertyCount
    """
    PropertyCount = ctypes.c_int(0)
    vSDK_dll.vSDK_Mark_GetPropertyCount(Mark, ctypes.byref(PropertyCount))
    return PropertyCount

def vSDK_Mark_GetPropertyByIndex(Mark, Index: int):
    """
    VSDK_EXPORT int vSDK_Mark_GetPropertyByIndex(Mark _Mark, int Index, char *&ckey, char *&cvalue);

    :param Mark:
    :param Index:
    :return: ckey, cvalue
    """
    ckey = ctypes.c_char_p()
    cvalue = ctypes.c_char_p()
    vSDK_dll.vSDK_Mark_GetPropertyByIndex(Mark, Index, ctypes.byref(ckey), ctypes.byref(cvalue))
    return ckey, cvalue

def vSDK_Mark_GetMarkData(Mark):
    """
    VSDK_EXPORT int vSDK_Mark_GetMarkData(Mark _Mark, int &MarkID, char *&MarkName, char *&LayerName, double &MarkPosX, double &MarkPosY, double &MarkAngle, double &MarkSize);

    :param Mark:
    :return: MarkID, MarkName, LayerName, MarkPosX, MarkPosY, MarkAngle, MarkSize
    """
    MarkID = ctypes.c_int(0)
    MarkName = ctypes.c_char_p()
    LayerName = ctypes.c_char_p()
    MarkPosX = ctypes.c_double()
    MarkPosY = ctypes.c_double()
    MarkAngle = ctypes.c_double()
    MarkSize = ctypes.c_double()
    vSDK_dll.vSDK_Mark_GetMarkData(Mark, ctypes.byref(MarkID), ctypes.byref(MarkName), ctypes.byref(LayerName), ctypes.byref(MarkPosX), ctypes.byref(MarkPosY), ctypes.byref(MarkAngle), ctypes.byref(MarkSize))
    return MarkID, MarkName, LayerName, MarkPosX, MarkPosY, MarkAngle, MarkSize

def vSDK_Net_SetNetName(Net, NetName: bytes):
    """
    VSDK_EXPORT int vSDK_Net_SetNetName(Net _Net, const char *NetName);

    :param Net:
    :param NetName:
    :return: vSDK_dll.vSDK_Net_SetNetName(Net, NetName)
    """
    return vSDK_dll.vSDK_Net_SetNetName(Net, NetName)

def vSDK_Net_GetNetName(Net):
    """
    VSDK_EXPORT int vSDK_Net_GetNetName(Net _Net, char *&NetName);

    :param Net:
    :return: NetName
    """
    NetName = ctypes.c_char_p()
    vSDK_dll.vSDK_Net_GetNetName(Net, ctypes.byref(NetName))
    return NetName

def vSDK_Net_SetNetID(Net, NetId: int):
    """
    VSDK_EXPORT int vSDK_Net_SetNetID(Net _Net, const int NetId);

    :param Net:
    :param NetId:
    :return: vSDK_dll.vSDK_Net_SetNetID(Net, NetId)
    """
    return vSDK_dll.vSDK_Net_SetNetID(Net, NetId)

def vSDK_Net_GetNetID(Net):
    """
    VSDK_EXPORT int vSDK_Net_GetNetID(Net _Net, int &NetId);

    :param Net:
    :return: NetId
    """
    NetId = ctypes.c_int(0)
    vSDK_dll.vSDK_Net_GetNetID(Net, ctypes.byref(NetId))
    return NetId

def vSDK_Net_AddPartPinID(Net, iPartID: int, iPinID: int, iTestpoint: int):
    """
    VSDK_EXPORT int vSDK_Net_AddPartPinID(Net _Net, const int _iPartID, const int _iPinID, const int _iTestpoint);

    :param Net:
    :param iPartID:
    :param iPinID:
    :param iTestpoint:
    :return: vSDK_dll.vSDK_Net_AddPartPinID(Net, iPartID, iPinID, iTestpoint)
    """
    return vSDK_dll.vSDK_Net_AddPartPinID(Net, iPartID, iPinID, iTestpoint)

def vSDK_Net_AddViaID(Net, iViaID: int):
    """
    VSDK_EXPORT int vSDK_Net_AddViaID(Net _Net, const int _iViaID);

    :param Net:
    :param iViaID:
    :return: vSDK_dll.vSDK_Net_AddViaID(Net, iViaID)
    """
    return vSDK_dll.vSDK_Net_AddViaID(Net, iViaID)

def vSDK_Net_AddLayerObjectID(Net, iLayerID: int, iObjectID: int):
    """
    VSDK_EXPORT int vSDK_Net_AddLayerObjectID(Net _Net, const int _iLayerID, const int _iObjectID);

    :param Net:
    :param iLayerID:
    :param iObjectID:
    :return: vSDK_dll.vSDK_Net_AddLayerObjectID(Net, iLayerID, iObjectID)
    """
    return vSDK_dll.vSDK_Net_AddLayerObjectID(Net, iLayerID, iObjectID)

def vSDK_Net_PinDatasCount(Net):
    """
    VSDK_EXPORT int vSDK_Net_PinDatasCount(Net _Net, int &PinDatasCount);

    :param Net:
    :return: PinDatasCount
    """
    PinDatasCount = ctypes.c_int(0)
    vSDK_dll.vSDK_Net_PinDatasCount(Net, ctypes.byref(PinDatasCount))
    return PinDatasCount

def vSDK_Net_ViaDatasCount(Net):
    """
    VSDK_EXPORT int vSDK_Net_ViaDatasCount(Net _Net, int &ViaDatasCount);

    :param Net:
    :return: ViaDatasCount
    """
    ViaDatasCount = ctypes.c_int(0)
    vSDK_dll.vSDK_Net_ViaDatasCount(Net, ctypes.byref(ViaDatasCount))
    return ViaDatasCount

def vSDK_Net_LayerObjectsCount(Net):
    """
    VSDK_EXPORT int vSDK_Net_LayerObjectsCount(Net _Net, int &LayerObjectsCount);

    :param Net:
    :return: LayerObjectsCount
    """
    LayerObjectsCount = ctypes.c_int(0)
    vSDK_dll.vSDK_Net_LayerObjectsCount(Net, ctypes.byref(LayerObjectsCount))
    return LayerObjectsCount

def vSDK_Net_GetPartPinIDByIndex(Net, iIndex: int):
    """
    VSDK_EXPORT int vSDK_Net_GetPartPinIDByIndex(Net _Net, const int _iIndex, int &_iPartID, int &_iPinID, int &_iTestpoint);

    :param Net:
    :param iIndex:
    :return: iPartID, iPinID, iTestpoint
    """
    iPartID = ctypes.c_int(0)
    iPinID = ctypes.c_int(0)
    iTestpoint = ctypes.c_int(0)
    vSDK_dll.vSDK_Net_GetPartPinIDByIndex(Net, iIndex, ctypes.byref(iPartID), ctypes.byref(iPinID), ctypes.byref(iTestpoint))
    return iPartID, iPinID, iTestpoint

def vSDK_Net_GetViaIDByIndex(Net, iIndex: int):
    """
    VSDK_EXPORT int vSDK_Net_GetViaIDByIndex(Net _Net, const int _iIndex, int &_iViaID);

    :param Net:
    :param iIndex:
    :return: iViaID
    """
    iViaID = ctypes.c_int(0)
    vSDK_dll.vSDK_Net_GetViaIDByIndex(Net, iIndex, ctypes.byref(iViaID))
    return iViaID

def vSDK_Net_GetLayerObjectIDByIndex(Net, iIndex: int):
    """
    VSDK_EXPORT int vSDK_Net_GetLayerObjectIDByIndex(Net _Net, const int _iIndex, int &_iLayerID, int &_iObjectID);

    :param Net:
    :param iIndex:
    :return: iLayerID, iObjectID
    """
    iLayerID = ctypes.c_int(0)
    iObjectID = ctypes.c_int(0)
    vSDK_dll.vSDK_Net_GetLayerObjectIDByIndex(Net, iIndex, ctypes.byref(iLayerID), ctypes.byref(iObjectID))
    return iLayerID, iObjectID

def vSDK_Net_AddProperty(Net, ckey: bytes,  cvalue: bytes):
    """
    VSDK_EXPORT int vSDK_Net_AddProperty(Net _Net, const char *ckey, const char * cvalue);

    :param Net:
    :param ckey:
    :param  cvalue:
    :return: vSDK_dll.vSDK_Net_AddProperty(Net, ckey,  cvalue)
    """
    return vSDK_dll.vSDK_Net_AddProperty(Net, ckey,  cvalue)

def vSDK_Net_FindPropertyVal(Net, ckey: bytes):
    """
    VSDK_EXPORT int vSDK_Net_FindPropertyVal(Net _Net, const char *ckey, char *&cvalue);

    :param Net:
    :param ckey:
    :return: cvalue
    """
    cvalue = ctypes.c_char_p()
    vSDK_dll.vSDK_Net_FindPropertyVal(Net, ckey, ctypes.byref(cvalue))
    return cvalue

def vSDK_Net_GetPropertyCount(Net):
    """
    VSDK_EXPORT int vSDK_Net_GetPropertyCount(Net _Net, int &_PropertyCount);

    :param Net:
    :return: PropertyCount
    """
    PropertyCount = ctypes.c_int(0)
    vSDK_dll.vSDK_Net_GetPropertyCount(Net, ctypes.byref(PropertyCount))
    return PropertyCount

def vSDK_Net_GetPropertyByIndex(Net, Index: int):
    """
    VSDK_EXPORT int vSDK_Net_GetPropertyByIndex(Net _Net, int Index, char *&ckey, char *&cvalue);

    :param Net:
    :param Index:
    :return: ckey, cvalue
    """
    ckey = ctypes.c_char_p()
    cvalue = ctypes.c_char_p()
    vSDK_dll.vSDK_Net_GetPropertyByIndex(Net, Index, ctypes.byref(ckey), ctypes.byref(cvalue))
    return ckey, cvalue

def vSDK_Net_GetNetData(Net):
    """
    VSDK_EXPORT int vSDK_Net_GetNetData(Net _Net, int &NetId, char *&NetName, int &PinDatasCount, int &ViaDatasCount, int &LayerObjectsCount);

    :param Net:
    :return: NetId, NetName, PinDatasCount, ViaDatasCount, LayerObjectsCount
    """
    NetId = ctypes.c_int(0)
    NetName = ctypes.c_char_p()
    PinDatasCount = ctypes.c_int(0)
    ViaDatasCount = ctypes.c_int(0)
    LayerObjectsCount = ctypes.c_int(0)
    vSDK_dll.vSDK_Net_GetNetData(Net, ctypes.byref(NetId), ctypes.byref(NetName), ctypes.byref(PinDatasCount), ctypes.byref(ViaDatasCount), ctypes.byref(LayerObjectsCount))
    return NetId, NetName, PinDatasCount, ViaDatasCount, LayerObjectsCount

def vSDK_Package_SetPackageName(Package, PackageName: bytes):
    """
    VSDK_EXPORT int vSDK_Package_SetPackageName(Package _Package, const char *PackageName);

    :param Package:
    :param PackageName:
    :return: vSDK_dll.vSDK_Package_SetPackageName(Package, PackageName)
    """
    return vSDK_dll.vSDK_Package_SetPackageName(Package, PackageName)

def vSDK_Package_GetPackageName(Package):
    """
    VSDK_EXPORT int vSDK_Package_GetPackageName(Package _Package, char *&PackageName);

    :param Package:
    :return: PackageName
    """
    PackageName = ctypes.c_char_p()
    vSDK_dll.vSDK_Package_GetPackageName(Package, ctypes.byref(PackageName))
    return PackageName

def vSDK_Package_SetCadShapeName(Package, PackageName: bytes):
    """
    VSDK_EXPORT int vSDK_Package_SetCadShapeName(Package _Package, const char *PackageName);

    :param Package:
    :param PackageName:
    :return: vSDK_dll.vSDK_Package_SetCadShapeName(Package, PackageName)
    """
    return vSDK_dll.vSDK_Package_SetCadShapeName(Package, PackageName)

def vSDK_Package_GetCadShapeName(Package):
    """
    VSDK_EXPORT int vSDK_Package_GetCadShapeName(Package _Package, char *&PackageName);

    :param Package:
    :return: PackageName
    """
    PackageName = ctypes.c_char_p()
    vSDK_dll.vSDK_Package_GetCadShapeName(Package, ctypes.byref(PackageName))
    return PackageName

def vSDK_Package_SetPackageID(Package, PackageId: int):
    """
    VSDK_EXPORT int vSDK_Package_SetPackageID(Package _Package, const int PackageId);

    :param Package:
    :param PackageId:
    :return: vSDK_dll.vSDK_Package_SetPackageID(Package, PackageId)
    """
    return vSDK_dll.vSDK_Package_SetPackageID(Package, PackageId)

def vSDK_Package_GetPackageID(Package):
    """
    VSDK_EXPORT int vSDK_Package_GetPackageID(Package _Package, int &PackageId);

    :param Package:
    :return: PackageId
    """
    PackageId = ctypes.c_int(0)
    vSDK_dll.vSDK_Package_GetPackageID(Package, ctypes.byref(PackageId))
    return PackageId

def vSDK_Package_SetBound(Package, BoundXMin: float, BoundYMin: float, BoundXMax: float, BoundYMax: float):
    """
    VSDK_EXPORT int vSDK_Package_SetBound(Package _Package, const double BoundXMin, const double BoundYMin, const double BoundXMax, const double BoundYMax);

    :param Package:
    :param BoundXMin:
    :param BoundYMin:
    :param BoundXMax:
    :param BoundYMax:
    :return: vSDK_dll.vSDK_Package_SetBound(Package, ctypes.c_double(BoundXMin), ctypes.c_double(BoundYMin), ctypes.c_double(BoundXMax), ctypes.c_double(BoundYMax))
    """
    return vSDK_dll.vSDK_Package_SetBound(Package, ctypes.c_double(BoundXMin), ctypes.c_double(BoundYMin), ctypes.c_double(BoundXMax), ctypes.c_double(BoundYMax))

def vSDK_Package_GetBound(Package):
    """
    VSDK_EXPORT int vSDK_Package_GetBound(Package _Package, double &BoundXMin, double &BoundYMin, double &BoundXMax, double &BoundYMax);

    :param Package:
    :return: BoundXMin, BoundYMin, BoundXMax, BoundYMax
    """
    BoundXMin = ctypes.c_double()
    BoundYMin = ctypes.c_double()
    BoundXMax = ctypes.c_double()
    BoundYMax = ctypes.c_double()
    vSDK_dll.vSDK_Package_GetBound(Package, ctypes.byref(BoundXMin), ctypes.byref(BoundYMin), ctypes.byref(BoundXMax), ctypes.byref(BoundYMax))
    return BoundXMin, BoundYMin, BoundXMax, BoundYMax

def vSDK_Package_AddProperty(Package, ckey: bytes, cvalue: bytes):
    """
    VSDK_EXPORT int vSDK_Package_AddProperty(Package _Package, const char *ckey, const char *cvalue);

    :param Package:
    :param ckey:
    :param cvalue:
    :return: vSDK_dll.vSDK_Package_AddProperty(Package, ckey, cvalue)
    """
    return vSDK_dll.vSDK_Package_AddProperty(Package, ckey, cvalue)

def vSDK_Package_FindPropertyVal(Package, ckey: bytes):
    """
    VSDK_EXPORT int vSDK_Package_FindPropertyVal(Package _Package, const char *ckey, char *&cvalue);

    :param Package:
    :param ckey:
    :return: cvalue
    """
    cvalue = ctypes.c_char_p()
    vSDK_dll.vSDK_Package_FindPropertyVal(Package, ckey, ctypes.byref(cvalue))
    return cvalue

def vSDK_Package_GetPropertyCount(Package):
    """
    VSDK_EXPORT int vSDK_Package_GetPropertyCount(Package _Package, int &_PropertyCount);

    :param Package:
    :return: PropertyCount
    """
    PropertyCount = ctypes.c_int(0)
    vSDK_dll.vSDK_Package_GetPropertyCount(Package, ctypes.byref(PropertyCount))
    return PropertyCount

def vSDK_Package_GetPropertyByIndex(Package, Index: int):
    """
    VSDK_EXPORT int vSDK_Package_GetPropertyByIndex(Package _Package, int Index, char *&ckey, char *&cvalue);

    :param Package:
    :param Index:
    :return: ckey, cvalue
    """
    ckey = ctypes.c_char_p()
    cvalue = ctypes.c_char_p()
    vSDK_dll.vSDK_Package_GetPropertyByIndex(Package, Index, ctypes.byref(ckey), ctypes.byref(cvalue))
    return ckey, cvalue

def vSDK_Package_AddPackagePin(Package):
    """
    VSDK_EXPORT int vSDK_Package_AddPackagePin(Package _Package, Pin &_Pin);

    :param Package:
    :return: Pin
    """
    Pin = ctypes.c_void_p()
    vSDK_dll.vSDK_Package_AddPackagePin(Package, ctypes.byref(Pin))
    return Pin

def vSDK_Package_AddPackagePin2(Package, PinID: int, PinName: bytes):
    """
    VSDK_EXPORT int vSDK_Package_AddPackagePin2(Package _Package, const int PinID, const char *PinName, Pin &_Pin);

    :param Package:
    :param PinID:
    :param PinName:
    :return: Pin
    """
    Pin = ctypes.c_void_p()
    vSDK_dll.vSDK_Package_AddPackagePin2(Package, PinID, PinName, ctypes.byref(Pin))
    return Pin

def vSDK_Package_GetPackagePinListCount(Package):
    """
    VSDK_EXPORT int vSDK_Package_GetPackagePinListCount(Package _Package, int &_PinCount);

    :param Package:
    :return: PinCount
    """
    PinCount = ctypes.c_int(0)
    vSDK_dll.vSDK_Package_GetPackagePinListCount(Package, ctypes.byref(PinCount))
    return PinCount

def vSDK_Package_GetPackagePinByIndex(Package, PinIndex: int):
    """
    VSDK_EXPORT int vSDK_Package_GetPackagePinByIndex(Package _Package, int _PinIndex, Pin &_Pin);

    :param Package:
    :param PinIndex:
    :return: Pin
    """
    Pin = ctypes.c_void_p()
    vSDK_dll.vSDK_Package_GetPackagePinByIndex(Package, PinIndex, ctypes.byref(Pin))
    return Pin

def vSDK_Package_AddPackageLayerShape(Package, LayerName: bytes):
    """
    VSDK_EXPORT int vSDK_Package_AddPackageLayerShape(Package _Package, const char *LayerName, LayerShape &_LayerShape);

    :param Package:
    :param LayerName:
    :return: LayerShape
    """
    LayerShape = ctypes.c_void_p()
    vSDK_dll.vSDK_Package_AddPackageLayerShape(Package, LayerName, ctypes.byref(LayerShape))
    return LayerShape

def vSDK_Package_GetPackageLayerShapeCount(Package):
    """
    VSDK_EXPORT int vSDK_Package_GetPackageLayerShapeCount(Package _Package, int &_LayerShapeCount);

    :param Package:
    :return: LayerShapeCount
    """
    LayerShapeCount = ctypes.c_int(0)
    vSDK_dll.vSDK_Package_GetPackageLayerShapeCount(Package, ctypes.byref(LayerShapeCount))
    return LayerShapeCount

def vSDK_Package_GetPackageLayerShapeByIndex(Package, Index: int):
    """
    VSDK_EXPORT int vSDK_Package_GetPackageLayerShapeByIndex(Package _Package, int _Index, LayerShape &_LayerShape);

    :param Package:
    :param Index:
    :return: LayerShape
    """
    LayerShape = ctypes.c_void_p()
    vSDK_dll.vSDK_Package_GetPackageLayerShapeByIndex(Package, Index, ctypes.byref(LayerShape))
    return LayerShape

def vSDK_Package_AddPackagePinLayerShape(Package, PinID: int):
    """
    VSDK_EXPORT int vSDK_Package_AddPackagePinLayerShape(Package _Package, const int PinID, PinLayerShape &_PinLayerShape);

    :param Package:
    :param PinID:
    :return: PinLayerShape
    """
    PinLayerShape = ctypes.c_void_p()
    vSDK_dll.vSDK_Package_AddPackagePinLayerShape(Package, PinID, ctypes.byref(PinLayerShape))
    return PinLayerShape

def vSDK_Package_GetPackagePinLayerShapeCount(Package):
    """
    VSDK_EXPORT int vSDK_Package_GetPackagePinLayerShapeCount(Package _Package, int &_PinLayerShapeCount);

    :param Package:
    :return: PinLayerShapeCount
    """
    PinLayerShapeCount = ctypes.c_int(0)
    vSDK_dll.vSDK_Package_GetPackagePinLayerShapeCount(Package, ctypes.byref(PinLayerShapeCount))
    return PinLayerShapeCount

def vSDK_Package_GetPackagePinLayerShapeByIndex(Package, Index: int):
    """
    VSDK_EXPORT int vSDK_Package_GetPackagePinLayerShapeByIndex(Package _Package, int _Index, PinLayerShape &_PinLayerShape);

    :param Package:
    :param Index:
    :return: PinLayerShape
    """
    PinLayerShape = ctypes.c_void_p()
    vSDK_dll.vSDK_Package_GetPackagePinLayerShapeByIndex(Package, Index, ctypes.byref(PinLayerShape))
    return PinLayerShape

def vSDK_Package_PinLayerShape_SetPinID(Package, PinLayerShape, PinID: int):
    """
    VSDK_EXPORT int vSDK_Package_PinLayerShape_SetPinID(Package _Package, PinLayerShape _PinLayerShape, const int PinID);

    :param Package:
    :param PinLayerShape:
    :param PinID:
    :return: vSDK_dll.vSDK_Package_PinLayerShape_SetPinID(Package, PinLayerShape, PinID)
    """
    return vSDK_dll.vSDK_Package_PinLayerShape_SetPinID(Package, PinLayerShape, PinID)

def vSDK_Package_PinLayerShape_GetPinID(Package, PinLayerShape):
    """
    VSDK_EXPORT int vSDK_Package_PinLayerShape_GetPinID(Package _Package, PinLayerShape _PinLayerShape, int &PinID);

    :param Package:
    :param PinLayerShape:
    :return: PinID
    """
    PinID = ctypes.c_int(0)
    vSDK_dll.vSDK_Package_PinLayerShape_GetPinID(Package, PinLayerShape, ctypes.byref(PinID))
    return PinID

def vSDK_Package_PinLayerShape_SetLayerName(Package, PinLayerShape, LayerName: bytes):
    """
    VSDK_EXPORT int vSDK_Package_PinLayerShape_SetLayerName(Package _Package, PinLayerShape _PinLayerShape, const char *LayerName);

    :param Package:
    :param PinLayerShape:
    :param LayerName:
    :return: vSDK_dll.vSDK_Package_PinLayerShape_SetLayerName(Package, PinLayerShape, LayerName)
    """
    return vSDK_dll.vSDK_Package_PinLayerShape_SetLayerName(Package, PinLayerShape, LayerName)

def vSDK_Package_PinLayerShape_GetLayerName(Package, PinLayerShape):
    """
    VSDK_EXPORT int vSDK_Package_PinLayerShape_GetLayerName(Package _Package, PinLayerShape _PinLayerShape, char *&LayerName);

    :param Package:
    :param PinLayerShape:
    :return: LayerName
    """
    LayerName = ctypes.c_char_p()
    vSDK_dll.vSDK_Package_PinLayerShape_GetLayerName(Package, PinLayerShape, ctypes.byref(LayerName))
    return LayerName

def vSDK_Package_PinLayerShape_GetLayerShape(Package, PinLayerShape):
    """
    VSDK_EXPORT int vSDK_Package_PinLayerShape_GetLayerShape(Package _Package, PinLayerShape _PinLayerShape, LayerShape &_LayerShape);

    :param Package:
    :param PinLayerShape:
    :return: LayerShape
    """
    LayerShape = ctypes.c_void_p()
    vSDK_dll.vSDK_Package_PinLayerShape_GetLayerShape(Package, PinLayerShape, ctypes.byref(LayerShape))
    return LayerShape

def vSDK_PadGroup_SetPadGroupName(PadGroup, PadGroupName: bytes):
    """
    VSDK_EXPORT int vSDK_PadGroup_SetPadGroupName(PadGroup _PadGroup, const char *_PadGroupName);

    :param PadGroup:
    :param PadGroupName:
    :return: vSDK_dll.vSDK_PadGroup_SetPadGroupName(PadGroup, PadGroupName)
    """
    return vSDK_dll.vSDK_PadGroup_SetPadGroupName(PadGroup, PadGroupName)

def vSDK_PadGroup_GetPadGroupName(PadGroup):
    """
    VSDK_EXPORT int vSDK_PadGroup_GetPadGroupName(PadGroup _PadGroup, char *&_PadGroupName);

    :param PadGroup:
    :return: PadGroupName
    """
    PadGroupName = ctypes.c_char_p()
    vSDK_dll.vSDK_PadGroup_GetPadGroupName(PadGroup, ctypes.byref(PadGroupName))
    return PadGroupName

def vSDK_PadGroup_SetPadGroupID(PadGroup, PadGroupID: int):
    """
    VSDK_EXPORT int vSDK_PadGroup_SetPadGroupID(PadGroup _PadGroup, const int _PadGroupID);

    :param PadGroup:
    :param PadGroupID:
    :return: vSDK_dll.vSDK_PadGroup_SetPadGroupID(PadGroup, PadGroupID)
    """
    return vSDK_dll.vSDK_PadGroup_SetPadGroupID(PadGroup, PadGroupID)

def vSDK_PadGroup_GetPadGroupID(PadGroup):
    """
    VSDK_EXPORT int vSDK_PadGroup_GetPadGroupID(PadGroup _PadGroup, int &_PadGroupID);

    :param PadGroup:
    :return: PadGroupID
    """
    PadGroupID = ctypes.c_int(0)
    vSDK_dll.vSDK_PadGroup_GetPadGroupID(PadGroup, ctypes.byref(PadGroupID))
    return PadGroupID

def vSDK_PadGroup_AddPadSymbol(PadGroup, LayerName: bytes, SymbolID: int, SymbolName: bytes):
    """
    VSDK_EXPORT int vSDK_PadGroup_AddPadSymbol(PadGroup _PadGroup, const char *_LayerName, const int _SymbolID, const char* _SymbolName, PadSymbol &_PadSymbol);

    :param PadGroup:
    :param LayerName:
    :param SymbolID:
    :param SymbolName:
    :return: PadSymbol
    """
    PadSymbol = ctypes.c_void_p()
    vSDK_dll.vSDK_PadGroup_AddPadSymbol(PadGroup, LayerName, SymbolID, SymbolName, ctypes.byref(PadSymbol))
    return PadSymbol

def vSDK_PadGroup_GetPadSymbolListCount(PadGroup):
    """
    VSDK_EXPORT int vSDK_PadGroup_GetPadSymbolListCount(PadGroup _PadGroup, int &_PadSymbolCount);

    :param PadGroup:
    :return: PadSymbolCount
    """
    PadSymbolCount = ctypes.c_int(0)
    vSDK_dll.vSDK_PadGroup_GetPadSymbolListCount(PadGroup, ctypes.byref(PadSymbolCount))
    return PadSymbolCount

def vSDK_PadGroup_GetPadSymbolByIndex(PadGroup, PadSymbolIndex: int):
    """
    VSDK_EXPORT int vSDK_PadGroup_GetPadSymbolByIndex(PadGroup _PadGroup, int _PadSymbolIndex, PadSymbol &_PadSymbol);

    :param PadGroup:
    :param PadSymbolIndex:
    :return: PadSymbol
    """
    PadSymbol = ctypes.c_void_p()
    vSDK_dll.vSDK_PadGroup_GetPadSymbolByIndex(PadGroup, PadSymbolIndex, ctypes.byref(PadSymbol))
    return PadSymbol

def vSDK_PadGroup_AddProperty(PadGroup, ckey: bytes, cvalue: bytes):
    """
    VSDK_EXPORT int vSDK_PadGroup_AddProperty(PadGroup _PadGroup, const char *ckey, const char *cvalue);

    :param PadGroup:
    :param ckey:
    :param cvalue:
    :return: vSDK_dll.vSDK_PadGroup_AddProperty(PadGroup, ckey, cvalue)
    """
    return vSDK_dll.vSDK_PadGroup_AddProperty(PadGroup, ckey, cvalue)

def vSDK_PadGroup_FindPropertyVal(PadGroup, ckey: bytes):
    """
    VSDK_EXPORT int vSDK_PadGroup_FindPropertyVal(PadGroup _PadGroup, const char *ckey, char *&cvalue);

    :param PadGroup:
    :param ckey:
    :return: cvalue
    """
    cvalue = ctypes.c_char_p()
    vSDK_dll.vSDK_PadGroup_FindPropertyVal(PadGroup, ckey, ctypes.byref(cvalue))
    return cvalue

def vSDK_PadGroup_GetPropertyCount(PadGroup):
    """
    VSDK_EXPORT int vSDK_PadGroup_GetPropertyCount(PadGroup _PadGroup, int &_PropertyCount);

    :param PadGroup:
    :return: PropertyCount
    """
    PropertyCount = ctypes.c_int(0)
    vSDK_dll.vSDK_PadGroup_GetPropertyCount(PadGroup, ctypes.byref(PropertyCount))
    return PropertyCount

def vSDK_PadGroup_GetPropertyByIndex(PadGroup, Index: int):
    """
    VSDK_EXPORT int vSDK_PadGroup_GetPropertyByIndex(PadGroup _PadGroup, int Index, char *&ckey, char *&cvalue);

    :param PadGroup:
    :param Index:
    :return: ckey, cvalue
    """
    ckey = ctypes.c_char_p()
    cvalue = ctypes.c_char_p()
    vSDK_dll.vSDK_PadGroup_GetPropertyByIndex(PadGroup, Index, ctypes.byref(ckey), ctypes.byref(cvalue))
    return ckey, cvalue

def vSDK_PadSymbol_SetLayerName(PadSymbol, LayerName: bytes):
    """
    VSDK_EXPORT int vSDK_PadSymbol_SetLayerName(PadSymbol _PadSymbol, const char *_LayerName);

    :param PadSymbol:
    :param LayerName:
    :return: vSDK_dll.vSDK_PadSymbol_SetLayerName(PadSymbol, LayerName)
    """
    return vSDK_dll.vSDK_PadSymbol_SetLayerName(PadSymbol, LayerName)

def vSDK_PadSymbol_GetLayerName(PadSymbol):
    """
    VSDK_EXPORT int vSDK_PadSymbol_GetLayerName(PadSymbol _PadSymbol, char *&_LayerName);

    :param PadSymbol:
    :return: LayerName
    """
    LayerName = ctypes.c_char_p()
    vSDK_dll.vSDK_PadSymbol_GetLayerName(PadSymbol, ctypes.byref(LayerName))
    return LayerName

def vSDK_PadSymbol_SetSymbolID(PadSymbol, SymbolID: int):
    """
    VSDK_EXPORT int vSDK_PadSymbol_SetSymbolID(PadSymbol _PadSymbol, const int _SymbolID);

    :param PadSymbol:
    :param SymbolID:
    :return: vSDK_dll.vSDK_PadSymbol_SetSymbolID(PadSymbol, SymbolID)
    """
    return vSDK_dll.vSDK_PadSymbol_SetSymbolID(PadSymbol, SymbolID)

def vSDK_PadSymbol_GetSymbolID(PadSymbol):
    """
    VSDK_EXPORT int vSDK_PadSymbol_GetSymbolID(PadSymbol _PadSymbol, int &_SymbolID);

    :param PadSymbol:
    :return: SymbolID
    """
    SymbolID = ctypes.c_int(0)
    vSDK_dll.vSDK_PadSymbol_GetSymbolID(PadSymbol, ctypes.byref(SymbolID))
    return SymbolID

def vSDK_PadSymbol_SetPadSymbolPos(PadSymbol, PadSymbolPosX: float, PadSymbolPosY: float):
    """
    VSDK_EXPORT int vSDK_PadSymbol_SetPadSymbolPos(PadSymbol _PadSymbol, const double _PadSymbolPosX, const double _PadSymbolPosY);

    :param PadSymbol:
    :param PadSymbolPosX:
    :param PadSymbolPosY:
    :return: vSDK_dll.vSDK_PadSymbol_SetPadSymbolPos(PadSymbol, ctypes.c_double(PadSymbolPosX), ctypes.c_double(PadSymbolPosY))
    """
    return vSDK_dll.vSDK_PadSymbol_SetPadSymbolPos(PadSymbol, ctypes.c_double(PadSymbolPosX), ctypes.c_double(PadSymbolPosY))

def vSDK_PadSymbol_GetPadSymbolPos(PadSymbol):
    """
    VSDK_EXPORT int vSDK_PadSymbol_GetPadSymbolPos(PadSymbol _PadSymbol, double &_PadSymbolPosX, double &_PadSymbolPosY);

    :param PadSymbol:
    :return: PadSymbolPosX, PadSymbolPosY
    """
    PadSymbolPosX = ctypes.c_double()
    PadSymbolPosY = ctypes.c_double()
    vSDK_dll.vSDK_PadSymbol_GetPadSymbolPos(PadSymbol, ctypes.byref(PadSymbolPosX), ctypes.byref(PadSymbolPosY))
    return PadSymbolPosX, PadSymbolPosY

def vSDK_PadSymbol_SetPadSymbolMirror(PadSymbol, Mirror: int):
    """
    VSDK_EXPORT int vSDK_PadSymbol_SetPadSymbolMirror(PadSymbol _PadSymbol, const int _Mirror);

    :param PadSymbol:
    :param Mirror:
    :return: vSDK_dll.vSDK_PadSymbol_SetPadSymbolMirror(PadSymbol, Mirror)
    """
    return vSDK_dll.vSDK_PadSymbol_SetPadSymbolMirror(PadSymbol, Mirror)

def vSDK_PadSymbol_GetPadSymbolMirror(PadSymbol):
    """
    VSDK_EXPORT int vSDK_PadSymbol_GetPadSymbolMirror(PadSymbol _PadSymbol, int &_Mirror);

    :param PadSymbol:
    :return: Mirror
    """
    Mirror = ctypes.c_int(0)
    vSDK_dll.vSDK_PadSymbol_GetPadSymbolMirror(PadSymbol, ctypes.byref(Mirror))
    return Mirror

def vSDK_PadSymbol_SetPadSymbolAngle(PadSymbol, PadSymbolAngle: float):
    """
    VSDK_EXPORT int vSDK_PadSymbol_SetPadSymbolAngle(PadSymbol _PadSymbol, const double _PadSymbolAngle);

    :param PadSymbol:
    :param PadSymbolAngle:
    :return: vSDK_dll.vSDK_PadSymbol_SetPadSymbolAngle(PadSymbol, ctypes.c_double(PadSymbolAngle))
    """
    return vSDK_dll.vSDK_PadSymbol_SetPadSymbolAngle(PadSymbol, ctypes.c_double(PadSymbolAngle))

def vSDK_PadSymbol_GetPadSymbolAngle(PadSymbol):
    """
    VSDK_EXPORT int vSDK_PadSymbol_GetPadSymbolAngle(PadSymbol _PadSymbol, double &_PadSymbolAngle);

    :param PadSymbol:
    :return: PadSymbolAngle
    """
    PadSymbolAngle = ctypes.c_double()
    vSDK_dll.vSDK_PadSymbol_GetPadSymbolAngle(PadSymbol, ctypes.byref(PadSymbolAngle))
    return PadSymbolAngle

def vSDK_PadSymbol_GetPadSymbolData(PadSymbol):
    """
    VSDK_EXPORT int vSDK_PadSymbol_GetPadSymbolData(PadSymbol _PadSymbol, char *&_LayerName, int &_SymbolID, double &PadSymbolPosX, double &PadSymbolPosY, double &PadSymbolAngle, int &Mirror);

    :param PadSymbol:
    :return: LayerName, SymbolID, PadSymbolPosX, PadSymbolPosY, PadSymbolAngle, Mirror
    """
    LayerName = ctypes.c_char_p()
    SymbolID = ctypes.c_int(0)
    PadSymbolPosX = ctypes.c_double()
    PadSymbolPosY = ctypes.c_double()
    PadSymbolAngle = ctypes.c_double()
    Mirror = ctypes.c_int(0)
    vSDK_dll.vSDK_PadSymbol_GetPadSymbolData(PadSymbol, ctypes.byref(LayerName), ctypes.byref(SymbolID), ctypes.byref(PadSymbolPosX), ctypes.byref(PadSymbolPosY), ctypes.byref(PadSymbolAngle), ctypes.byref(Mirror))
    return LayerName, SymbolID, PadSymbolPosX, PadSymbolPosY, PadSymbolAngle, Mirror

def vSDK_Panel_SetPcbName(Panel, PcbName: bytes):
    """
    VSDK_EXPORT int vSDK_Panel_SetPcbName(Panel _Panel, const char* PcbName);

    :param Panel:
    :param PcbName:
    :return: vSDK_dll.vSDK_Panel_SetPcbName(Panel, PcbName)
    """
    return vSDK_dll.vSDK_Panel_SetPcbName(Panel, PcbName)

def vSDK_Panel_GetPcbName(Panel):
    """
    VSDK_EXPORT int vSDK_Panel_GetPcbName(Panel _Panel, char *&PcbName);

    :param Panel:
    :return: PcbName
    """
    PcbName = ctypes.c_char_p()
    vSDK_dll.vSDK_Panel_GetPcbName(Panel, ctypes.byref(PcbName))
    return PcbName

def vSDK_Panel_SetStepPos(Panel, X: float, Y: float):
    """
    VSDK_EXPORT int vSDK_Panel_SetStepPos(Panel _Panel, const double X, const double Y);

    :param Panel:
    :param X:
    :param Y:
    :return: vSDK_dll.vSDK_Panel_SetStepPos(Panel, ctypes.c_double(X), ctypes.c_double(Y))
    """
    return vSDK_dll.vSDK_Panel_SetStepPos(Panel, ctypes.c_double(X), ctypes.c_double(Y))

def vSDK_Panel_GetStepPos(Panel):
    """
    VSDK_EXPORT int vSDK_Panel_GetStepPos(Panel _Panel, double &X, double &Y);

    :param Panel:
    :return: X, Y
    """
    X = ctypes.c_double()
    Y = ctypes.c_double()
    vSDK_dll.vSDK_Panel_GetStepPos(Panel, ctypes.byref(X), ctypes.byref(Y))
    return X, Y

def vSDK_Panel_SetStepOffset(Panel, DX: float, DY: float):
    """
    VSDK_EXPORT int vSDK_Panel_SetStepOffset(Panel _Panel, const double DX, const double DY);

    :param Panel:
    :param DX:
    :param DY:
    :return: vSDK_dll.vSDK_Panel_SetStepOffset(Panel, ctypes.c_double(DX), ctypes.c_double(DY))
    """
    return vSDK_dll.vSDK_Panel_SetStepOffset(Panel, ctypes.c_double(DX), ctypes.c_double(DY))

def vSDK_Panel_GetStepOffset(Panel):
    """
    VSDK_EXPORT int vSDK_Panel_GetStepOffset(Panel _Panel, double &DX, double &DY);

    :param Panel:
    :return: DX, DY
    """
    DX = ctypes.c_double()
    DY = ctypes.c_double()
    vSDK_dll.vSDK_Panel_GetStepOffset(Panel, ctypes.byref(DX), ctypes.byref(DY))
    return DX, DY

def vSDK_Panel_SetStepXYCount(Panel, CountX: int, CountY: int):
    """
    VSDK_EXPORT int vSDK_Panel_SetStepXYCount(Panel _Panel, const int CountX, const int CountY);

    :param Panel:
    :param CountX:
    :param CountY:
    :return: vSDK_dll.vSDK_Panel_SetStepXYCount(Panel, CountX, CountY)
    """
    return vSDK_dll.vSDK_Panel_SetStepXYCount(Panel, CountX, CountY)

def vSDK_Panel_GetStepXYCount(Panel):
    """
    VSDK_EXPORT int vSDK_Panel_GetStepXYCount(Panel _Panel, int &CountX, int &CountY);

    :param Panel:
    :return: CountX, CountY
    """
    CountX = ctypes.c_int(0)
    CountY = ctypes.c_int(0)
    vSDK_dll.vSDK_Panel_GetStepXYCount(Panel, ctypes.byref(CountX), ctypes.byref(CountY))
    return CountX, CountY

def vSDK_Panel_SetStepAngle(Panel, Angle: float):
    """
    VSDK_EXPORT int vSDK_Panel_SetStepAngle(Panel _Panel, const double Angle);

    :param Panel:
    :param Angle:
    :return: vSDK_dll.vSDK_Panel_SetStepAngle(Panel, ctypes.c_double(Angle))
    """
    return vSDK_dll.vSDK_Panel_SetStepAngle(Panel, ctypes.c_double(Angle))

def vSDK_Panel_GetStepAngle(Panel):
    """
    VSDK_EXPORT int vSDK_Panel_GetStepAngle(Panel _Panel, double &Angle);

    :param Panel:
    :return: Angle
    """
    Angle = ctypes.c_double()
    vSDK_dll.vSDK_Panel_GetStepAngle(Panel, ctypes.byref(Angle))
    return Angle

def vSDK_Panel_SetStepMirror(Panel, Mirror: int):
    """
    VSDK_EXPORT int vSDK_Panel_SetStepMirror(Panel _Panel, const int Mirror);

    :param Panel:
    :param Mirror:
    :return: vSDK_dll.vSDK_Panel_SetStepMirror(Panel, Mirror)
    """
    return vSDK_dll.vSDK_Panel_SetStepMirror(Panel, Mirror)

def vSDK_Panel_GetStepMirror(Panel):
    """
    VSDK_EXPORT int vSDK_Panel_GetStepMirror(Panel _Panel, int &Mirror);

    :param Panel:
    :return: Mirror
    """
    Mirror = ctypes.c_int(0)
    vSDK_dll.vSDK_Panel_GetStepMirror(Panel, ctypes.byref(Mirror))
    return Mirror

def vSDK_Panel_GetPanelData(Panel):
    """
    VSDK_EXPORT int vSDK_Panel_GetPanelData(Panel PanelData, int &PanelId, double &X, double &Y, double &DX, double &DY, int &CountX, int &CountY, double &Angle, int &Flip, int &Mirror, char *&PcbName);

    :param Panel:
    :return: PanelId, X, Y, DX, DY, CountX, CountY, Angle, Flip, Mirror, PcbName
    """
    PanelId = ctypes.c_int(0)
    X = ctypes.c_double()
    Y = ctypes.c_double()
    DX = ctypes.c_double()
    DY = ctypes.c_double()
    CountX = ctypes.c_int(0)
    CountY = ctypes.c_int(0)
    Angle = ctypes.c_double()
    Flip = ctypes.c_int(0)
    Mirror = ctypes.c_int(0)
    PcbName = ctypes.c_char_p()
    vSDK_dll.vSDK_Panel_GetPanelData(Panel, ctypes.byref(PanelId), ctypes.byref(X), ctypes.byref(Y), ctypes.byref(DX), ctypes.byref(DY), ctypes.byref(CountX), ctypes.byref(CountY), ctypes.byref(Angle), ctypes.byref(Flip), ctypes.byref(Mirror), ctypes.byref(PcbName))
    return PanelId, X, Y, DX, DY, CountX, CountY, Angle, Flip, Mirror, PcbName

def vSDK_Parameter_GetAllMachineCount(Board):
    """
    VSDK_EXPORT int vSDK_Parameter_GetAllMachineCount(Board _Board, int &_iCount);

    :param Board:
    :return: iCount
    """
    iCount = ctypes.c_int(0)
    vSDK_dll.vSDK_Parameter_GetAllMachineCount(Board, ctypes.byref(iCount))
    return iCount

def vSDK_Parameter_GetMachineByIndex(Board, Index: int):
    """
    VSDK_EXPORT int vSDK_Parameter_GetMachineByIndex(Board _Board, const int _Index, char *&_cMachineName);

    :param Board:
    :param Index:
    :return: cMachineName
    """
    cMachineName = ctypes.c_char_p()
    vSDK_dll.vSDK_Parameter_GetMachineByIndex(Board, Index, ctypes.byref(cMachineName))
    return cMachineName

def vSDK_Parameter_GetAllKeyCount(Board):
    """
    VSDK_EXPORT int vSDK_Parameter_GetAllKeyCount(Board _Board, int &_iCount);

    :param Board:
    :return: iCount
    """
    iCount = ctypes.c_int(0)
    vSDK_dll.vSDK_Parameter_GetAllKeyCount(Board, ctypes.byref(iCount))
    return iCount

def vSDK_Parameter_GetKeyByIndex(Board, Index: int):
    """
    VSDK_EXPORT int vSDK_Parameter_GetKeyByIndex(Board _Board, const int _Index, char *&_cKey);

    :param Board:
    :param Index:
    :return: cKey
    """
    cKey = ctypes.c_char_p()
    vSDK_dll.vSDK_Parameter_GetKeyByIndex(Board, Index, ctypes.byref(cKey))
    return cKey

def vSDK_Parameter_GetParameterValueByCADPN(Board, cPN: bytes, cMachineName: bytes, cKey: bytes):
    """
    VSDK_EXPORT int vSDK_Parameter_GetParameterValueByCADPN(Board _Board, const char *_cPN, const char *_cMachineName, const char *_cKey, char *&_cVaule);

    :param Board:
    :param cPN:
    :param cMachineName:
    :param cKey:
    :return: cVaule
    """
    cVaule = ctypes.c_char_p()
    vSDK_dll.vSDK_Parameter_GetParameterValueByCADPN(Board, cPN, cMachineName, cKey, ctypes.byref(cVaule))
    return cVaule

def vSDK_Parameter_GetParameterValueByBOMPN(Board, cPN: bytes, cMachineName: bytes, cKey: bytes):
    """
    VSDK_EXPORT int vSDK_Parameter_GetParameterValueByBOMPN(Board _Board, const char *_cPN, const char *_cMachineName, const char *_cKey, char *&_cVaule);

    :param Board:
    :param cPN:
    :param cMachineName:
    :param cKey:
    :return: cVaule
    """
    cVaule = ctypes.c_char_p()
    vSDK_dll.vSDK_Parameter_GetParameterValueByBOMPN(Board, cPN, cMachineName, cKey, ctypes.byref(cVaule))
    return cVaule

def vSDK_Parameter_GetParameterValueByCADPackage(Board, cPackageName: bytes, cMachineName: bytes, cKey: bytes):
    """
    VSDK_EXPORT int vSDK_Parameter_GetParameterValueByCADPackage(Board _Board, const char *_cPackageName, const char *_cMachineName, const char *_cKey, char *&_cVaule);

    :param Board:
    :param cPackageName:
    :param cMachineName:
    :param cKey:
    :return: cVaule
    """
    cVaule = ctypes.c_char_p()
    vSDK_dll.vSDK_Parameter_GetParameterValueByCADPackage(Board, cPackageName, cMachineName, cKey, ctypes.byref(cVaule))
    return cVaule

def vSDK_Parameter_GetParameterValueByCADPart(Board, cPartName: bytes, cMachineName: bytes, cKey: bytes):
    """
    VSDK_EXPORT int vSDK_Parameter_GetParameterValueByCADPart(Board _Board, const char *_cPartName, const char *_cMachineName, const char *_cKey, char *&_cVaule);

    :param Board:
    :param cPartName:
    :param cMachineName:
    :param cKey:
    :return: cVaule
    """
    cVaule = ctypes.c_char_p()
    vSDK_dll.vSDK_Parameter_GetParameterValueByCADPart(Board, cPartName, cMachineName, cKey, ctypes.byref(cVaule))
    return cVaule

def vSDK_Parameter_AddParameterValueByCADPN(Board, cPN: bytes, cMachineName: bytes, cKey: bytes, cVaule: bytes):
    """
    VSDK_EXPORT int vSDK_Parameter_AddParameterValueByCADPN(Board _Board, const char *_cPN, const char *_cMachineName, const char *_cKey, const char *_cVaule);

    :param Board:
    :param cPN:
    :param cMachineName:
    :param cKey:
    :param cVaule:
    :return: vSDK_dll.vSDK_Parameter_AddParameterValueByCADPN(Board, cPN, cMachineName, cKey, cVaule)
    """
    return vSDK_dll.vSDK_Parameter_AddParameterValueByCADPN(Board, cPN, cMachineName, cKey, cVaule)

def vSDK_Parameter_AddParameterValueByBOMPN(Board, cPN: bytes, cMachineName: bytes, cKey: bytes, cVaule: bytes):
    """
    VSDK_EXPORT int vSDK_Parameter_AddParameterValueByBOMPN(Board _Board, const char *_cPN, const char *_cMachineName, const char *_cKey, const char *_cVaule);

    :param Board:
    :param cPN:
    :param cMachineName:
    :param cKey:
    :param cVaule:
    :return: vSDK_dll.vSDK_Parameter_AddParameterValueByBOMPN(Board, cPN, cMachineName, cKey, cVaule)
    """
    return vSDK_dll.vSDK_Parameter_AddParameterValueByBOMPN(Board, cPN, cMachineName, cKey, cVaule)

def vSDK_Parameter_AddParameterValueByCADPackage(Board, cPackageName: bytes, cMachineName: bytes, cKey: bytes, cVaule: bytes):
    """
    VSDK_EXPORT int vSDK_Parameter_AddParameterValueByCADPackage(Board _Board, const char *_cPackageName, const char *_cMachineName, const char *_cKey, const char *_cVaule);

    :param Board:
    :param cPackageName:
    :param cMachineName:
    :param cKey:
    :param cVaule:
    :return: vSDK_dll.vSDK_Parameter_AddParameterValueByCADPackage(Board, cPackageName, cMachineName, cKey, cVaule)
    """
    return vSDK_dll.vSDK_Parameter_AddParameterValueByCADPackage(Board, cPackageName, cMachineName, cKey, cVaule)

def vSDK_Parameter_AddParameterValueByCADPart(Board, cPartName: bytes, cMachineName: bytes, cKey: bytes, cVaule: bytes):
    """
    VSDK_EXPORT int vSDK_Parameter_AddParameterValueByCADPart(Board _Board, const char *_cPartName, const char *_cMachineName, const char *_cKey, const char *_cVaule);

    :param Board:
    :param cPartName:
    :param cMachineName:
    :param cKey:
    :param cVaule:
    :return: vSDK_dll.vSDK_Parameter_AddParameterValueByCADPart(Board, cPartName, cMachineName, cKey, cVaule)
    """
    return vSDK_dll.vSDK_Parameter_AddParameterValueByCADPart(Board, cPartName, cMachineName, cKey, cVaule)

def vSDK_Parameter_DeleteParameterByCADPN(Board, cPN: bytes, cMachineName: bytes, cKey: bytes):
    """
    VSDK_EXPORT int vSDK_Parameter_DeleteParameterByCADPN(Board _Board, const char *_cPN, const char *_cMachineName, const char *_cKey);

    :param Board:
    :param cPN:
    :param cMachineName:
    :param cKey:
    :return: vSDK_dll.vSDK_Parameter_DeleteParameterByCADPN(Board, cPN, cMachineName, cKey)
    """
    return vSDK_dll.vSDK_Parameter_DeleteParameterByCADPN(Board, cPN, cMachineName, cKey)

def vSDK_Parameter_DeleteParameterValueByBOMPN(Board, cPN: bytes, cMachineName: bytes, cKey: bytes):
    """
    VSDK_EXPORT int vSDK_Parameter_DeleteParameterValueByBOMPN(Board _Board, const char *_cPN, const char *_cMachineName, const char *_cKey);

    :param Board:
    :param cPN:
    :param cMachineName:
    :param cKey:
    :return: vSDK_dll.vSDK_Parameter_DeleteParameterValueByBOMPN(Board, cPN, cMachineName, cKey)
    """
    return vSDK_dll.vSDK_Parameter_DeleteParameterValueByBOMPN(Board, cPN, cMachineName, cKey)

def vSDK_Parameter_DeleteParameterValueByCADPackage(Board, cPackageName: bytes, cMachineName: bytes, cKey: bytes):
    """
    VSDK_EXPORT int vSDK_Parameter_DeleteParameterValueByCADPackage(Board _Board, const char *_cPackageName, const char *_cMachineName, const char *_cKey);

    :param Board:
    :param cPackageName:
    :param cMachineName:
    :param cKey:
    :return: vSDK_dll.vSDK_Parameter_DeleteParameterValueByCADPackage(Board, cPackageName, cMachineName, cKey)
    """
    return vSDK_dll.vSDK_Parameter_DeleteParameterValueByCADPackage(Board, cPackageName, cMachineName, cKey)

def vSDK_Parameter_DeleteParameterValueByCADPart(Board, cPartName: bytes, cMachineName: bytes, cKey: bytes):
    """
    VSDK_EXPORT int vSDK_Parameter_DeleteParameterValueByCADPart(Board _Board, const char *_cPartName, const char *_cMachineName, const char *_cKey);

    :param Board:
    :param cPartName:
    :param cMachineName:
    :param cKey:
    :return: vSDK_dll.vSDK_Parameter_DeleteParameterValueByCADPart(Board, cPartName, cMachineName, cKey)
    """
    return vSDK_dll.vSDK_Parameter_DeleteParameterValueByCADPart(Board, cPartName, cMachineName, cKey)

def vSDK_Part_SetPartName(Part, PartName: bytes):
    """
    VSDK_EXPORT int vSDK_Part_SetPartName(Part _Part, const char* _PartName);

    :param Part:
    :param PartName:
    :return: vSDK_dll.vSDK_Part_SetPartName(Part, PartName)
    """
    return vSDK_dll.vSDK_Part_SetPartName(Part, PartName)

def vSDK_Part_GetPartName(Part):
    """
    VSDK_EXPORT int vSDK_Part_GetPartName(Part _Part, char *&_PartName);

    :param Part:
    :return: PartName
    """
    PartName = ctypes.c_char_p()
    vSDK_dll.vSDK_Part_GetPartName(Part, ctypes.byref(PartName))
    return PartName

def vSDK_Part_SetPartID(Part, PartID: int):
    """
    VSDK_EXPORT int vSDK_Part_SetPartID(Part _Part, const int _PartID);

    :param Part:
    :param PartID:
    :return: vSDK_dll.vSDK_Part_SetPartID(Part, PartID)
    """
    return vSDK_dll.vSDK_Part_SetPartID(Part, PartID)

def vSDK_Part_GetPartID(Part):
    """
    VSDK_EXPORT int vSDK_Part_GetPartID(Part _Part, int &_PartID);

    :param Part:
    :return: PartID
    """
    PartID = ctypes.c_int(0)
    vSDK_dll.vSDK_Part_GetPartID(Part, ctypes.byref(PartID))
    return PartID

def vSDK_Part_SetPartPos(Part, PartPosX: float, PartPosY: float):
    """
    VSDK_EXPORT int vSDK_Part_SetPartPos(Part _Part, const double _PartPosX, const double _PartPosY);

    :param Part:
    :param PartPosX:
    :param PartPosY:
    :return: vSDK_dll.vSDK_Part_SetPartPos(Part, ctypes.c_double(PartPosX), ctypes.c_double(PartPosY))
    """
    return vSDK_dll.vSDK_Part_SetPartPos(Part, ctypes.c_double(PartPosX), ctypes.c_double(PartPosY))

def vSDK_Part_GetPartPos(Part):
    """
    VSDK_EXPORT int vSDK_Part_GetPartPos(Part _Part, double &_PartPosX, double &_PartPosY);

    :param Part:
    :return: PartPosX, PartPosY
    """
    PartPosX = ctypes.c_double()
    PartPosY = ctypes.c_double()
    vSDK_dll.vSDK_Part_GetPartPos(Part, ctypes.byref(PartPosX), ctypes.byref(PartPosY))
    return PartPosX, PartPosY

def vSDK_Part_SetPartAngle(Part, PartAngle: float):
    """
    VSDK_EXPORT int vSDK_Part_SetPartAngle(Part _Part, const double _PartAngle);

    :param Part:
    :param PartAngle:
    :return: vSDK_dll.vSDK_Part_SetPartAngle(Part, ctypes.c_double(PartAngle))
    """
    return vSDK_dll.vSDK_Part_SetPartAngle(Part, ctypes.c_double(PartAngle))

def vSDK_Part_GetPartAngle(Part):
    """
    VSDK_EXPORT int vSDK_Part_GetPartAngle(Part _Part, double &_PartAngle);

    :param Part:
    :return: PartAngle
    """
    PartAngle = ctypes.c_double()
    vSDK_dll.vSDK_Part_GetPartAngle(Part, ctypes.byref(PartAngle))
    return PartAngle

def vSDK_Part_SetMirror(Part, Mirror: int):
    """
    VSDK_EXPORT int vSDK_Part_SetMirror(Part _Part, const int _Mirror);

    :param Part:
    :param Mirror:
    :return: vSDK_dll.vSDK_Part_SetMirror(Part, Mirror)
    """
    return vSDK_dll.vSDK_Part_SetMirror(Part, Mirror)

def vSDK_Part_GetMirror(Part):
    """
    VSDK_EXPORT int vSDK_Part_GetMirror(Part _Part, int &_Mirror);

    :param Part:
    :return: Mirror
    """
    Mirror = ctypes.c_int(0)
    vSDK_dll.vSDK_Part_GetMirror(Part, ctypes.byref(Mirror))
    return Mirror

def vSDK_Part_SetPinCount(Part, PinCount: int):
    """
    VSDK_EXPORT int vSDK_Part_SetPinCount(Part _Part, const int _PinCount);

    :param Part:
    :param PinCount:
    :return: vSDK_dll.vSDK_Part_SetPinCount(Part, PinCount)
    """
    return vSDK_dll.vSDK_Part_SetPinCount(Part, PinCount)

def vSDK_Part_GetPinCount(Part):
    """
    VSDK_EXPORT int vSDK_Part_GetPinCount(Part _Part, int &_PinCount);

    :param Part:
    :return: PinCount
    """
    PinCount = ctypes.c_int(0)
    vSDK_dll.vSDK_Part_GetPinCount(Part, ctypes.byref(PinCount))
    return PinCount

def vSDK_Part_SetPackageID(Part, PackageID: int):
    """
    VSDK_EXPORT int vSDK_Part_SetPackageID(Part _Part, const int _PackageID);

    :param Part:
    :param PackageID:
    :return: vSDK_dll.vSDK_Part_SetPackageID(Part, PackageID)
    """
    return vSDK_dll.vSDK_Part_SetPackageID(Part, PackageID)

def vSDK_Part_GetPackageID(Part):
    """
    VSDK_EXPORT int vSDK_Part_GetPackageID(Part _Part, int &_PackageID);

    :param Part:
    :return: PackageID
    """
    PackageID = ctypes.c_int(0)
    vSDK_dll.vSDK_Part_GetPackageID(Part, ctypes.byref(PackageID))
    return PackageID

def vSDK_Part_GetPackage(Part):
    """
    VSDK_EXPORT int vSDK_Part_GetPackage(Part _Part, Package &_Package);

    :param Part:
    :return: Package
    """
    Package = ctypes.c_void_p()
    vSDK_dll.vSDK_Part_GetPackage(Part, ctypes.byref(Package))
    return Package

def vSDK_Part_SetPackageName(Part, PackageName: bytes):
    """
    VSDK_EXPORT int vSDK_Part_SetPackageName(Part _Part, const char *_PackageName);

    :param Part:
    :param PackageName:
    :return: vSDK_dll.vSDK_Part_SetPackageName(Part, PackageName)
    """
    return vSDK_dll.vSDK_Part_SetPackageName(Part, PackageName)

def vSDK_Part_GetPackageName(Part):
    """
    VSDK_EXPORT int vSDK_Part_GetPackageName(Part _Part, char *&_PackageName);

    :param Part:
    :return: PackageName
    """
    PackageName = ctypes.c_char_p()
    vSDK_dll.vSDK_Part_GetPackageName(Part, ctypes.byref(PackageName))
    return PackageName

def vSDK_Part_SetPkgType(Part, PkgType: bytes):
    """
    VSDK_EXPORT int vSDK_Part_SetPkgType(Part _Part, const char *_PkgType);

    :param Part:
    :param PkgType:
    :return: vSDK_dll.vSDK_Part_SetPkgType(Part, PkgType)
    """
    return vSDK_dll.vSDK_Part_SetPkgType(Part, PkgType)

def vSDK_Part_GetPkgType(Part):
    """
    VSDK_EXPORT int vSDK_Part_GetPkgType(Part _Part, char *&_PkgType);

    :param Part:
    :return: PkgType
    """
    PkgType = ctypes.c_char_p()
    vSDK_dll.vSDK_Part_GetPkgType(Part, ctypes.byref(PkgType))
    return PkgType

def vSDK_Part_SetLayerName(Part, LayerName: bytes):
    """
    VSDK_EXPORT int vSDK_Part_SetLayerName(Part _Part, const char *_LayerName);

    :param Part:
    :param LayerName:
    :return: vSDK_dll.vSDK_Part_SetLayerName(Part, LayerName)
    """
    return vSDK_dll.vSDK_Part_SetLayerName(Part, LayerName)

def vSDK_Part_GetLayerName(Part):
    """
    VSDK_EXPORT int vSDK_Part_GetLayerName(Part _Part, char *&_LayerName);

    :param Part:
    :return: LayerName
    """
    LayerName = ctypes.c_char_p()
    vSDK_dll.vSDK_Part_GetLayerName(Part, ctypes.byref(LayerName))
    return LayerName

def vSDK_Part_SetLayerSide(Part, LayerSide: int):
    """
    VSDK_EXPORT int vSDK_Part_SetLayerSide(Part _Part, const int _LayerSide);

    :param Part:
    :param LayerSide:
    :return: vSDK_dll.vSDK_Part_SetLayerSide(Part, LayerSide)
    """
    return vSDK_dll.vSDK_Part_SetLayerSide(Part, LayerSide)

def vSDK_Part_GetLayerSide(Part):
    """
    VSDK_EXPORT int vSDK_Part_GetLayerSide(Part _Part, int &_LayerSide);

    :param Part:
    :return: LayerSide
    """
    LayerSide = ctypes.c_int(0)
    vSDK_dll.vSDK_Part_GetLayerSide(Part, ctypes.byref(LayerSide))
    return LayerSide

def vSDK_Part_SetInBomStatus(Part, InBom: int):
    """
    VSDK_EXPORT int vSDK_Part_SetInBomStatus(Part _Part, const int _InBom);

    :param Part:
    :param InBom:
    :return: vSDK_dll.vSDK_Part_SetInBomStatus(Part, InBom)
    """
    return vSDK_dll.vSDK_Part_SetInBomStatus(Part, InBom)

def vSDK_Part_GetInBomStatus(Part):
    """
    VSDK_EXPORT int vSDK_Part_GetInBomStatus(Part _Part, int &_InBom);

    :param Part:
    :return: InBom
    """
    InBom = ctypes.c_int(0)
    vSDK_dll.vSDK_Part_GetInBomStatus(Part, ctypes.byref(InBom))
    return InBom

def vSDK_Part_SetPlaceMode(Part, PlaceMode: int):
    """
    VSDK_EXPORT int vSDK_Part_SetPlaceMode(Part _Part, const int _PlaceMode);

    :param Part:
    :param PlaceMode:
    :return: vSDK_dll.vSDK_Part_SetPlaceMode(Part, PlaceMode)
    """
    return vSDK_dll.vSDK_Part_SetPlaceMode(Part, PlaceMode)

def vSDK_Part_GetPlaceMode(Part):
    """
    VSDK_EXPORT int vSDK_Part_GetPlaceMode(Part _Part, int &_PlaceMode);

    :param Part:
    :return: PlaceMode
    """
    PlaceMode = ctypes.c_int(0)
    vSDK_dll.vSDK_Part_GetPlaceMode(Part, ctypes.byref(PlaceMode))
    return PlaceMode

def vSDK_Part_SetCadShapeName(Part, CadShapeName: bytes):
    """
    VSDK_EXPORT int vSDK_Part_SetCadShapeName(Part _Part, const char* _CadShapeName);

    :param Part:
    :param CadShapeName:
    :return: vSDK_dll.vSDK_Part_SetCadShapeName(Part, CadShapeName)
    """
    return vSDK_dll.vSDK_Part_SetCadShapeName(Part, CadShapeName)

def vSDK_Part_GetCadShapeName(Part):
    """
    VSDK_EXPORT int vSDK_Part_GetCadShapeName(Part _Part, char *&_CadShapeName);

    :param Part:
    :return: CadShapeName
    """
    CadShapeName = ctypes.c_char_p()
    vSDK_dll.vSDK_Part_GetCadShapeName(Part, ctypes.byref(CadShapeName))
    return CadShapeName

def vSDK_Part_SetCadPN(Part, CadPN: bytes):
    """
    VSDK_EXPORT int vSDK_Part_SetCadPN(Part _Part, const char *_CadPN);

    :param Part:
    :param CadPN:
    :return: vSDK_dll.vSDK_Part_SetCadPN(Part, CadPN)
    """
    return vSDK_dll.vSDK_Part_SetCadPN(Part, CadPN)

def vSDK_Part_GetCadPN(Part):
    """
    VSDK_EXPORT int vSDK_Part_GetCadPN(Part _Part, char *&_CadPN);

    :param Part:
    :return: CadPN
    """
    CadPN = ctypes.c_char_p()
    vSDK_dll.vSDK_Part_GetCadPN(Part, ctypes.byref(CadPN))
    return CadPN

def vSDK_Part_SetBomPN(Part, BomPN: bytes):
    """
    VSDK_EXPORT int vSDK_Part_SetBomPN(Part _Part, const char *_BomPN);

    :param Part:
    :param BomPN:
    :return: vSDK_dll.vSDK_Part_SetBomPN(Part, BomPN)
    """
    return vSDK_dll.vSDK_Part_SetBomPN(Part, BomPN)

def vSDK_Part_GetBomPN(Part):
    """
    VSDK_EXPORT int vSDK_Part_GetBomPN(Part _Part, char *&_BomPN);

    :param Part:
    :return: BomPN
    """
    BomPN = ctypes.c_char_p()
    vSDK_dll.vSDK_Part_GetBomPN(Part, ctypes.byref(BomPN))
    return BomPN

def vSDK_Part_SetBomPartName(Part, BomPartName: bytes):
    """
    VSDK_EXPORT int vSDK_Part_SetBomPartName(Part _Part, const char *_BomPartName);

    :param Part:
    :param BomPartName:
    :return: vSDK_dll.vSDK_Part_SetBomPartName(Part, BomPartName)
    """
    return vSDK_dll.vSDK_Part_SetBomPartName(Part, BomPartName)

def vSDK_Part_GetBomPartName(Part):
    """
    VSDK_EXPORT int vSDK_Part_GetBomPartName(Part _Part, char *&_BomPartName);

    :param Part:
    :return: BomPartName
    """
    BomPartName = ctypes.c_char_p()
    vSDK_dll.vSDK_Part_GetBomPartName(Part, ctypes.byref(BomPartName))
    return BomPartName

def vSDK_Part_SetBomCheckType(Part, CheckType: int):
    """
    VSDK_EXPORT int vSDK_Part_SetBomCheckType(Part _Part, const int _CheckType);

    :param Part:
    :param CheckType:
    :return: vSDK_dll.vSDK_Part_SetBomCheckType(Part, CheckType)
    """
    return vSDK_dll.vSDK_Part_SetBomCheckType(Part, CheckType)

def vSDK_Part_GetBomCheckType(Part):
    """
    VSDK_EXPORT int vSDK_Part_GetBomCheckType(Part _Part, int &_CheckType);

    :param Part:
    :return: CheckType
    """
    CheckType = ctypes.c_int(0)
    vSDK_dll.vSDK_Part_GetBomCheckType(Part, ctypes.byref(CheckType))
    return CheckType

def vSDK_Part_SetBomMainPNIndex(Part, MainPNIndex: int):
    """
    VSDK_EXPORT int vSDK_Part_SetBomMainPNIndex(Part _Part, const int _MainPNIndex);

    :param Part:
    :param MainPNIndex:
    :return: vSDK_dll.vSDK_Part_SetBomMainPNIndex(Part, MainPNIndex)
    """
    return vSDK_dll.vSDK_Part_SetBomMainPNIndex(Part, MainPNIndex)

def vSDK_Part_GetBomMainPNIndex(Part):
    """
    VSDK_EXPORT int vSDK_Part_GetBomMainPNIndex(Part _Part, int &_MainPNIndex);

    :param Part:
    :return: MainPNIndex
    """
    MainPNIndex = ctypes.c_int(0)
    vSDK_dll.vSDK_Part_GetBomMainPNIndex(Part, ctypes.byref(MainPNIndex))
    return MainPNIndex

def vSDK_Part_AddProperty(Part, ckey: bytes, cvalue: bytes):
    """
    VSDK_EXPORT int vSDK_Part_AddProperty(Part _Part, const char *ckey, const char *cvalue);

    :param Part:
    :param ckey:
    :param cvalue:
    :return: vSDK_dll.vSDK_Part_AddProperty(Part, ckey, cvalue)
    """
    return vSDK_dll.vSDK_Part_AddProperty(Part, ckey, cvalue)

def vSDK_Part_FindPropertyVal(Part, ckey: bytes):
    """
    VSDK_EXPORT int vSDK_Part_FindPropertyVal(Part _Part, const char *ckey, char *&cvalue);

    :param Part:
    :param ckey:
    :return: cvalue
    """
    cvalue = ctypes.c_char_p()
    vSDK_dll.vSDK_Part_FindPropertyVal(Part, ckey, ctypes.byref(cvalue))
    return cvalue

def vSDK_Part_GetPropertyCount(Part):
    """
    VSDK_EXPORT int vSDK_Part_GetPropertyCount(Part _Part, int &_PropertyCount);

    :param Part:
    :return: PropertyCount
    """
    PropertyCount = ctypes.c_int(0)
    vSDK_dll.vSDK_Part_GetPropertyCount(Part, ctypes.byref(PropertyCount))
    return PropertyCount

def vSDK_Part_GetPropertyByIndex(Part, Index: int):
    """
    VSDK_EXPORT int vSDK_Part_GetPropertyByIndex(Part _Part, int Index, char *&ckey, char *&cvalue);

    :param Part:
    :param Index:
    :return: ckey, cvalue
    """
    ckey = ctypes.c_char_p()
    cvalue = ctypes.c_char_p()
    vSDK_dll.vSDK_Part_GetPropertyByIndex(Part, Index, ctypes.byref(ckey), ctypes.byref(cvalue))
    return ckey, cvalue

def vSDK_Part_GetPartData(Part):
    """
    VSDK_EXPORT int vSDK_Part_GetPartData(Part _Part, int &_PartID, char *&_PartName, double &_PartPosX, double &_PartPosY, double &_PartAngle, int &_Mirror, int &_PinCount, int &_PackageID, char *&_PackageName, char *&_PkgType, char *&_LayerName, int &_LayerSide, char *&_CadPN, char *&_BomPN, int &_InBom, int &_PlaceMode, char *&_CadShapeName, char *&_BomPartName, int &_BomCheckType, int &_BomMainPnIndex);

    :param Part:
    :return: PartID, PartName, PartPosX, PartPosY, PartAngle, Mirror, PinCount, PackageID, PackageName, PkgType, LayerName, LayerSide, CadPN, BomPN, InBom, PlaceMode, CadShapeName, BomPartName, BomCheckType, BomMainPnIndex
    """
    PartID = ctypes.c_int(0)
    PartName = ctypes.c_char_p()
    PartPosX = ctypes.c_double()
    PartPosY = ctypes.c_double()
    PartAngle = ctypes.c_double()
    Mirror = ctypes.c_int(0)
    PinCount = ctypes.c_int(0)
    PackageID = ctypes.c_int(0)
    PackageName = ctypes.c_char_p()
    PkgType = ctypes.c_char_p()
    LayerName = ctypes.c_char_p()
    LayerSide = ctypes.c_int(0)
    CadPN = ctypes.c_char_p()
    BomPN = ctypes.c_char_p()
    InBom = ctypes.c_int(0)
    PlaceMode = ctypes.c_int(0)
    CadShapeName = ctypes.c_char_p()
    BomPartName = ctypes.c_char_p()
    BomCheckType = ctypes.c_int(0)
    BomMainPnIndex = ctypes.c_int(0)
    vSDK_dll.vSDK_Part_GetPartData(Part, ctypes.byref(PartID), ctypes.byref(PartName), ctypes.byref(PartPosX), ctypes.byref(PartPosY), ctypes.byref(PartAngle), ctypes.byref(Mirror), ctypes.byref(PinCount), ctypes.byref(PackageID), ctypes.byref(PackageName), ctypes.byref(PkgType), ctypes.byref(LayerName), ctypes.byref(LayerSide), ctypes.byref(CadPN), ctypes.byref(BomPN), ctypes.byref(InBom), ctypes.byref(PlaceMode), ctypes.byref(CadShapeName), ctypes.byref(BomPartName), ctypes.byref(BomCheckType), ctypes.byref(BomMainPnIndex))
    return PartID, PartName, PartPosX, PartPosY, PartAngle, Mirror, PinCount, PackageID, PackageName, PkgType, LayerName, LayerSide, CadPN, BomPN, InBom, PlaceMode, CadShapeName, BomPartName, BomCheckType, BomMainPnIndex

def vSDK_Pin_SetPinName(Pin, PinName: bytes):
    """
    VSDK_EXPORT int vSDK_Pin_SetPinName(Pin _Pin, const char *_PinName);

    :param Pin:
    :param PinName:
    :return: vSDK_dll.vSDK_Pin_SetPinName(Pin, PinName)
    """
    return vSDK_dll.vSDK_Pin_SetPinName(Pin, PinName)

def vSDK_Pin_GetPinName(Pin):
    """
    VSDK_EXPORT int vSDK_Pin_GetPinName(Pin _Pin, char *&_PinName);

    :param Pin:
    :return: PinName
    """
    PinName = ctypes.c_char_p()
    vSDK_dll.vSDK_Pin_GetPinName(Pin, ctypes.byref(PinName))
    return PinName

def vSDK_Pin_SetPinNumber(Pin, PinNumber: bytes):
    """
    VSDK_EXPORT int vSDK_Pin_SetPinNumber(Pin _Pin, const char *_PinNumber);

    :param Pin:
    :param PinNumber:
    :return: vSDK_dll.vSDK_Pin_SetPinNumber(Pin, PinNumber)
    """
    return vSDK_dll.vSDK_Pin_SetPinNumber(Pin, PinNumber)

def vSDK_Pin_GetPinNumber(Pin):
    """
    VSDK_EXPORT int vSDK_Pin_GetPinNumber(Pin _Pin, char *&_PinNumber);

    :param Pin:
    :return: PinNumber
    """
    PinNumber = ctypes.c_char_p()
    vSDK_dll.vSDK_Pin_GetPinNumber(Pin, ctypes.byref(PinNumber))
    return PinNumber

def vSDK_Pin_SetPinID(Pin, PinID: int):
    """
    VSDK_EXPORT int vSDK_Pin_SetPinID(Pin _Pin, const int _PinID);

    :param Pin:
    :param PinID:
    :return: vSDK_dll.vSDK_Pin_SetPinID(Pin, PinID)
    """
    return vSDK_dll.vSDK_Pin_SetPinID(Pin, PinID)

def vSDK_Pin_GetPinID(Pin):
    """
    VSDK_EXPORT int vSDK_Pin_GetPinID(Pin _Pin, int &_PinID);

    :param Pin:
    :return: PinID
    """
    PinID = ctypes.c_int(0)
    vSDK_dll.vSDK_Pin_GetPinID(Pin, ctypes.byref(PinID))
    return PinID

def vSDK_Pin_SetPinPos(Pin, PinPosX: float, PinPosY: float):
    """
    VSDK_EXPORT int vSDK_Pin_SetPinPos(Pin _Pin, const double _PinPosX, const double _PinPosY);

    :param Pin:
    :param PinPosX:
    :param PinPosY:
    :return: vSDK_dll.vSDK_Pin_SetPinPos(Pin, ctypes.c_double(PinPosX), ctypes.c_double(PinPosY))
    """
    return vSDK_dll.vSDK_Pin_SetPinPos(Pin, ctypes.c_double(PinPosX), ctypes.c_double(PinPosY))

def vSDK_Pin_GetPinPos(Pin):
    """
    VSDK_EXPORT int vSDK_Pin_GetPinPos(Pin _Pin, double &_PinPosX, double &_PinPosY);

    :param Pin:
    :return: PinPosX, PinPosY
    """
    PinPosX = ctypes.c_double()
    PinPosY = ctypes.c_double()
    vSDK_dll.vSDK_Pin_GetPinPos(Pin, ctypes.byref(PinPosX), ctypes.byref(PinPosY))
    return PinPosX, PinPosY

def vSDK_Pin_SetPinSide(Pin, PinSide: int):
    """
    VSDK_EXPORT int vSDK_Pin_SetPinSide(Pin _Pin, const int _PinSide);

    :param Pin:
    :param PinSide:
    :return: vSDK_dll.vSDK_Pin_SetPinSide(Pin, PinSide)
    """
    return vSDK_dll.vSDK_Pin_SetPinSide(Pin, PinSide)

def vSDK_Pin_GetPinSide(Pin):
    """
    VSDK_EXPORT int vSDK_Pin_GetPinSide(Pin _Pin, int &_PinSide);

    :param Pin:
    :return: PinSide
    """
    PinSide = ctypes.c_int(0)
    vSDK_dll.vSDK_Pin_GetPinSide(Pin, ctypes.byref(PinSide))
    return PinSide

def vSDK_Pin_SetPinAngle(Pin, PinAngle: float):
    """
    VSDK_EXPORT int vSDK_Pin_SetPinAngle(Pin _Pin, const double _PinAngle);

    :param Pin:
    :param PinAngle:
    :return: vSDK_dll.vSDK_Pin_SetPinAngle(Pin, ctypes.c_double(PinAngle))
    """
    return vSDK_dll.vSDK_Pin_SetPinAngle(Pin, ctypes.c_double(PinAngle))

def vSDK_Pin_GetPinAngle(Pin):
    """
    VSDK_EXPORT int vSDK_Pin_GetPinAngle(Pin _Pin, double &_PinAngle);

    :param Pin:
    :return: PinAngle
    """
    PinAngle = ctypes.c_double()
    vSDK_dll.vSDK_Pin_GetPinAngle(Pin, ctypes.byref(PinAngle))
    return PinAngle

def vSDK_Pin_SetPadName(Pin, PadName: bytes):
    """
    VSDK_EXPORT int vSDK_Pin_SetPadName(Pin _Pin, const char *PadName);

    :param Pin:
    :param PadName:
    :return: vSDK_dll.vSDK_Pin_SetPadName(Pin, PadName)
    """
    return vSDK_dll.vSDK_Pin_SetPadName(Pin, PadName)

def vSDK_Pin_GetPadName(Pin):
    """
    VSDK_EXPORT int vSDK_Pin_GetPadName(Pin _Pin, char *&PadName);

    :param Pin:
    :return: PadName
    """
    PadName = ctypes.c_char_p()
    vSDK_dll.vSDK_Pin_GetPadName(Pin, ctypes.byref(PadName))
    return PadName

def vSDK_Pin_SetPadGroupID(Pin, PadGroupID: int):
    """
    VSDK_EXPORT int vSDK_Pin_SetPadGroupID(Pin _Pin, const int PadGroupID);

    :param Pin:
    :param PadGroupID:
    :return: vSDK_dll.vSDK_Pin_SetPadGroupID(Pin, PadGroupID)
    """
    return vSDK_dll.vSDK_Pin_SetPadGroupID(Pin, PadGroupID)

def vSDK_Pin_GetPadGroupID(Pin):
    """
    VSDK_EXPORT int vSDK_Pin_GetPadGroupID(Pin _Pin, int &PadGroupID);

    :param Pin:
    :return: PadGroupID
    """
    PadGroupID = ctypes.c_int(0)
    vSDK_dll.vSDK_Pin_GetPadGroupID(Pin, ctypes.byref(PadGroupID))
    return PadGroupID

def vSDK_Pin_AddProperty(Pin, ckey: bytes, cvalue: bytes):
    """
    VSDK_EXPORT int vSDK_Pin_AddProperty(Pin _Pin, const char *ckey, const char *cvalue);

    :param Pin:
    :param ckey:
    :param cvalue:
    :return: vSDK_dll.vSDK_Pin_AddProperty(Pin, ckey, cvalue)
    """
    return vSDK_dll.vSDK_Pin_AddProperty(Pin, ckey, cvalue)

def vSDK_Pin_FindPropertyVal(Pin, ckey: bytes):
    """
    VSDK_EXPORT int vSDK_Pin_FindPropertyVal(Pin _Pin, const char *ckey, char *&cvalue);

    :param Pin:
    :param ckey:
    :return: cvalue
    """
    cvalue = ctypes.c_char_p()
    vSDK_dll.vSDK_Pin_FindPropertyVal(Pin, ckey, ctypes.byref(cvalue))
    return cvalue

def vSDK_Pin_GetPropertyCount(Pin):
    """
    VSDK_EXPORT int vSDK_Pin_GetPropertyCount(Pin _Pin, int &_PropertyCount);

    :param Pin:
    :return: PropertyCount
    """
    PropertyCount = ctypes.c_int(0)
    vSDK_dll.vSDK_Pin_GetPropertyCount(Pin, ctypes.byref(PropertyCount))
    return PropertyCount

def vSDK_Pin_GetPropertyByIndex(Pin, Index: int):
    """
    VSDK_EXPORT int vSDK_Pin_GetPropertyByIndex(Pin _Pin, int Index, char *&ckey, char *&cvalue);

    :param Pin:
    :param Index:
    :return: ckey, cvalue
    """
    ckey = ctypes.c_char_p()
    cvalue = ctypes.c_char_p()
    vSDK_dll.vSDK_Pin_GetPropertyByIndex(Pin, Index, ctypes.byref(ckey), ctypes.byref(cvalue))
    return ckey, cvalue

def vSDK_Pin_GetPinData(Pin):
    """
    VSDK_EXPORT int vSDK_Pin_GetPinData(Pin _Pin, int &PinID, int &PinSide, int &SymbMaxId, int &PadGroupId, char *&PinNumber, char *&PinName, double &PinPosX, double &PinPosY, double &PinAngle, char *&PadName);

    :param Pin:
    :return: PinID, PinSide, SymbMaxId, PadGroupId, PinNumber, PinName, PinPosX, PinPosY, PinAngle, PadName
    """
    PinID = ctypes.c_int(0)
    PinSide = ctypes.c_int(0)
    SymbMaxId = ctypes.c_int(0)
    PadGroupId = ctypes.c_int(0)
    PinNumber = ctypes.c_char_p()
    PinName = ctypes.c_char_p()
    PinPosX = ctypes.c_double()
    PinPosY = ctypes.c_double()
    PinAngle = ctypes.c_double()
    PadName = ctypes.c_char_p()
    vSDK_dll.vSDK_Pin_GetPinData(Pin, ctypes.byref(PinID), ctypes.byref(PinSide), ctypes.byref(SymbMaxId), ctypes.byref(PadGroupId), ctypes.byref(PinNumber), ctypes.byref(PinName), ctypes.byref(PinPosX), ctypes.byref(PinPosY), ctypes.byref(PinAngle), ctypes.byref(PadName))
    return PinID, PinSide, SymbMaxId, PadGroupId, PinNumber, PinName, PinPosX, PinPosY, PinAngle, PadName

def vSDK_PinLayerShape_SetPinID(PinLayerShape, PinID: int):
    """
    VSDK_EXPORT int vSDK_PinLayerShape_SetPinID(PinLayerShape _PinLayerShape, const int PinID);

    :param PinLayerShape:
    :param PinID:
    :return: vSDK_dll.vSDK_PinLayerShape_SetPinID(PinLayerShape, PinID)
    """
    return vSDK_dll.vSDK_PinLayerShape_SetPinID(PinLayerShape, PinID)

def vSDK_PinLayerShape_GetPinID(PinLayerShape):
    """
    VSDK_EXPORT int vSDK_PinLayerShape_GetPinID(PinLayerShape _PinLayerShape, int &PinID);

    :param PinLayerShape:
    :return: PinID
    """
    PinID = ctypes.c_int(0)
    vSDK_dll.vSDK_PinLayerShape_GetPinID(PinLayerShape, ctypes.byref(PinID))
    return PinID

def vSDK_PinLayerShape_SetLayerName(PinLayerShape, LayerName: bytes):
    """
    VSDK_EXPORT int vSDK_PinLayerShape_SetLayerName(PinLayerShape _PinLayerShape, const char *LayerName);

    :param PinLayerShape:
    :param LayerName:
    :return: vSDK_dll.vSDK_PinLayerShape_SetLayerName(PinLayerShape, LayerName)
    """
    return vSDK_dll.vSDK_PinLayerShape_SetLayerName(PinLayerShape, LayerName)

def vSDK_PinLayerShape_GetLayerName(PinLayerShape):
    """
    VSDK_EXPORT int vSDK_PinLayerShape_GetLayerName(PinLayerShape _PinLayerShape, char *&LayerName);

    :param PinLayerShape:
    :return: LayerName
    """
    LayerName = ctypes.c_char_p()
    vSDK_dll.vSDK_PinLayerShape_GetLayerName(PinLayerShape, ctypes.byref(LayerName))
    return LayerName

def vSDK_PinLayerShape_GetLayerShape(PinLayerShape):
    """
    VSDK_EXPORT int vSDK_PinLayerShape_GetLayerShape(PinLayerShape _PinLayerShape, LayerShape &_LayerShape);

    :param PinLayerShape:
    :return: LayerShape
    """
    LayerShape = ctypes.c_void_p()
    vSDK_dll.vSDK_PinLayerShape_GetLayerShape(PinLayerShape, ctypes.byref(LayerShape))
    return LayerShape

def vSDK_PinLayerShape_GetPinLayerShapeData(PinLayerShape):
    """
    VSDK_EXPORT int vSDK_PinLayerShape_GetPinLayerShapeData(PinLayerShape _PinLayerShape, int &PinID, char *&LayerName, int &OffsetX, int &OffsetY, LayerShape &_LayerShape);

    :param PinLayerShape:
    :return: PinID, LayerName, OffsetX, OffsetY, LayerShape
    """
    PinID = ctypes.c_int(0)
    LayerName = ctypes.c_char_p()
    OffsetX = ctypes.c_int(0)
    OffsetY = ctypes.c_int(0)
    LayerShape = ctypes.c_void_p()
    vSDK_dll.vSDK_PinLayerShape_GetPinLayerShapeData(PinLayerShape, ctypes.byref(PinID), ctypes.byref(LayerName), ctypes.byref(OffsetX), ctypes.byref(OffsetY), ctypes.byref(LayerShape))
    return PinID, LayerName, OffsetX, OffsetY, LayerShape

def vSDK_Symbol_SetSymbolName(Symbol, SymbolName: bytes):
    """
    VSDK_EXPORT int vSDK_Symbol_SetSymbolName(Symbol _Symbol, const char *_SymbolName);

    :param Symbol:
    :param SymbolName:
    :return: vSDK_dll.vSDK_Symbol_SetSymbolName(Symbol, SymbolName)
    """
    return vSDK_dll.vSDK_Symbol_SetSymbolName(Symbol, SymbolName)

def vSDK_Symbol_GetSymbolName(Symbol):
    """
    VSDK_EXPORT int vSDK_Symbol_GetSymbolName(Symbol _Symbol, char *&_SymbolName);

    :param Symbol:
    :return: SymbolName
    """
    SymbolName = ctypes.c_char_p()
    vSDK_dll.vSDK_Symbol_GetSymbolName(Symbol, ctypes.byref(SymbolName))
    return SymbolName

def vSDK_Symbol_SetSymbolID(Symbol, SymbolID: int):
    """
    VSDK_EXPORT int vSDK_Symbol_SetSymbolID(Symbol _Symbol, const int _SymbolID);

    :param Symbol:
    :param SymbolID:
    :return: vSDK_dll.vSDK_Symbol_SetSymbolID(Symbol, SymbolID)
    """
    return vSDK_dll.vSDK_Symbol_SetSymbolID(Symbol, SymbolID)

def vSDK_Symbol_GetSymbolID(Symbol):
    """
    VSDK_EXPORT int vSDK_Symbol_GetSymbolID(Symbol _Symbol, int &_SymbolID);

    :param Symbol:
    :return: SymbolID
    """
    SymbolID = ctypes.c_int(0)
    vSDK_dll.vSDK_Symbol_GetSymbolID(Symbol, ctypes.byref(SymbolID))
    return SymbolID

def vSDK_Symbol_AddProperty(Symbol, ckey: bytes, cvalue: bytes):
    """
    VSDK_EXPORT int vSDK_Symbol_AddProperty(Symbol _Symbol, const char *ckey, const char *cvalue);

    :param Symbol:
    :param ckey:
    :param cvalue:
    :return: vSDK_dll.vSDK_Symbol_AddProperty(Symbol, ckey, cvalue)
    """
    return vSDK_dll.vSDK_Symbol_AddProperty(Symbol, ckey, cvalue)

def vSDK_Symbol_FindPropertyVal(Symbol, ckey: bytes):
    """
    VSDK_EXPORT int vSDK_Symbol_FindPropertyVal(Symbol _Symbol, const char *ckey, char *&cvalue);

    :param Symbol:
    :param ckey:
    :return: cvalue
    """
    cvalue = ctypes.c_char_p()
    vSDK_dll.vSDK_Symbol_FindPropertyVal(Symbol, ckey, ctypes.byref(cvalue))
    return cvalue

def vSDK_Symbol_AddShape(Shape, XOrigin: float, YOrigin: float, Mirror: int, Angle: float, XOffset: float, YOffset: float):
    """
    VSDK_EXPORT int vSDK_Symbol_AddShape(Shape *_Shape, const double _XOrigin, const double _YOrigin, const int _Mirror, const double _Angle, const double _XOffset, const double _YOffset, Symbol &_Symbol);

    :param Shape:
    :param XOrigin:
    :param YOrigin:
    :param Mirror:
    :param Angle:
    :param XOffset:
    :param YOffset:
    :return: Symbol
    """
    Symbol = ctypes.c_void_p()
    vSDK_dll.vSDK_Symbol_AddShape(Shape, ctypes.c_double(XOrigin), ctypes.c_double(YOrigin), Mirror, ctypes.c_double(Angle), ctypes.c_double(XOffset), ctypes.c_double(YOffset), ctypes.byref(Symbol))
    return Symbol

def vSDK_Symbol_GetShapeCount(Symbol):
    """
    VSDK_EXPORT int vSDK_Symbol_GetShapeCount(Symbol _Symbol, int &_ShapeCount);

    :param Symbol:
    :return: ShapeCount
    """
    ShapeCount = ctypes.c_int(0)
    vSDK_dll.vSDK_Symbol_GetShapeCount(Symbol, ctypes.byref(ShapeCount))
    return ShapeCount

def vSDK_Symbol_GetShapeByIndex(Symbol, Index: int):
    """
    VSDK_EXPORT int vSDK_Symbol_GetShapeByIndex(Symbol _Symbol, const int _Index, double &_XOrigin, double &_YOrigin, int &_Mirror, double &_Angle, double &_XOffset, double &_YOffset, Shape *&_Shape);

    :param Symbol:
    :param Index:
    :return: XOrigin, YOrigin, Mirror, Angle, XOffset, YOffset, Shape
    """
    XOrigin = ctypes.c_double()
    YOrigin = ctypes.c_double()
    Mirror = ctypes.c_int(0)
    Angle = ctypes.c_double()
    XOffset = ctypes.c_double()
    YOffset = ctypes.c_double()
    Shape = ctypes.c_void_p()
    vSDK_dll.vSDK_Symbol_GetShapeByIndex(Symbol, Index, ctypes.byref(XOrigin), ctypes.byref(YOrigin), ctypes.byref(Mirror), ctypes.byref(Angle), ctypes.byref(XOffset), ctypes.byref(YOffset), ctypes.byref(Shape))
    return XOrigin, YOrigin, Mirror, Angle, XOffset, YOffset, Shape

def vSDK_Via_SetNetID(Via, NetID: int):
    """
    VSDK_EXPORT int vSDK_Via_SetNetID(Via _Via, const int _NetID);

    :param Via:
    :param NetID:
    :return: vSDK_dll.vSDK_Via_SetNetID(Via, NetID)
    """
    return vSDK_dll.vSDK_Via_SetNetID(Via, NetID)

def vSDK_Via_GetNetID(Via):
    """
    VSDK_EXPORT int vSDK_Via_GetNetID(Via _Via, int &_NetID);

    :param Via:
    :return: NetID
    """
    NetID = ctypes.c_int(0)
    vSDK_dll.vSDK_Via_GetNetID(Via, ctypes.byref(NetID))
    return NetID

def vSDK_Via_SetViaPos(Via, ViaPosX: float, ViaPosY: float):
    """
    VSDK_EXPORT int vSDK_Via_SetViaPos(Via _Via, const double _ViaPosX, const double _ViaPosY);

    :param Via:
    :param ViaPosX:
    :param ViaPosY:
    :return: vSDK_dll.vSDK_Via_SetViaPos(Via, ctypes.c_double(ViaPosX), ctypes.c_double(ViaPosY))
    """
    return vSDK_dll.vSDK_Via_SetViaPos(Via, ctypes.c_double(ViaPosX), ctypes.c_double(ViaPosY))

def vSDK_Via_GetViaPos(Via):
    """
    VSDK_EXPORT int vSDK_Via_GetViaPos(Via _Via, double &_ViaPosX, double &_ViaPosY);

    :param Via:
    :return: ViaPosX, ViaPosY
    """
    ViaPosX = ctypes.c_double()
    ViaPosY = ctypes.c_double()
    vSDK_dll.vSDK_Via_GetViaPos(Via, ctypes.byref(ViaPosX), ctypes.byref(ViaPosY))
    return ViaPosX, ViaPosY

def vSDK_Via_SetViaMirror(Via, Mirror: int):
    """
    VSDK_EXPORT int vSDK_Via_SetViaMirror(Via _Via, const int _Mirror);

    :param Via:
    :param Mirror:
    :return: vSDK_dll.vSDK_Via_SetViaMirror(Via, Mirror)
    """
    return vSDK_dll.vSDK_Via_SetViaMirror(Via, Mirror)

def vSDK_Via_GetViaMirror(Via):
    """
    VSDK_EXPORT int vSDK_Via_GetViaMirror(Via _Via, int &_Mirror);

    :param Via:
    :return: Mirror
    """
    Mirror = ctypes.c_int(0)
    vSDK_dll.vSDK_Via_GetViaMirror(Via, ctypes.byref(Mirror))
    return Mirror

def vSDK_Via_SetViaSide(Via, ViaSide: int):
    """
    VSDK_EXPORT int vSDK_Via_SetViaSide(Via _Via, const int _ViaSide);

    :param Via:
    :param ViaSide:
    :return: vSDK_dll.vSDK_Via_SetViaSide(Via, ViaSide)
    """
    return vSDK_dll.vSDK_Via_SetViaSide(Via, ViaSide)

def vSDK_Via_GetViaSide(Via):
    """
    VSDK_EXPORT int vSDK_Via_GetViaSide(Via _Via, int &_ViaSide);

    :param Via:
    :return: ViaSide
    """
    ViaSide = ctypes.c_int(0)
    vSDK_dll.vSDK_Via_GetViaSide(Via, ctypes.byref(ViaSide))
    return ViaSide

def vSDK_Via_SetViaAngle(Via, ViaAngle: float):
    """
    VSDK_EXPORT int vSDK_Via_SetViaAngle(Via _Via, const double _ViaAngle);

    :param Via:
    :param ViaAngle:
    :return: vSDK_dll.vSDK_Via_SetViaAngle(Via, ctypes.c_double(ViaAngle))
    """
    return vSDK_dll.vSDK_Via_SetViaAngle(Via, ctypes.c_double(ViaAngle))

def vSDK_Via_GetViaAngle(Via):
    """
    VSDK_EXPORT int vSDK_Via_GetViaAngle(Via _Via, double &_ViaAngle);

    :param Via:
    :return: ViaAngle
    """
    ViaAngle = ctypes.c_double()
    vSDK_dll.vSDK_Via_GetViaAngle(Via, ctypes.byref(ViaAngle))
    return ViaAngle

def vSDK_Via_SetTestPointSide(Via, TestPointSide: int):
    """
    VSDK_EXPORT int vSDK_Via_SetTestPointSide(Via _Via, const int _TestPointSide);

    :param Via:
    :param TestPointSide:
    :return: vSDK_dll.vSDK_Via_SetTestPointSide(Via, TestPointSide)
    """
    return vSDK_dll.vSDK_Via_SetTestPointSide(Via, TestPointSide)

def vSDK_Via_GetTestPointSide(Via):
    """
    VSDK_EXPORT int vSDK_Via_GetTestPointSide(Via _Via, int &_TestPointSide);

    :param Via:
    :return: TestPointSide
    """
    TestPointSide = ctypes.c_int(0)
    vSDK_dll.vSDK_Via_GetTestPointSide(Via, ctypes.byref(TestPointSide))
    return TestPointSide

def vSDK_Via_SetPadName(Via, PadName: bytes):
    """
    VSDK_EXPORT int vSDK_Via_SetPadName(Via _Via, const char *PadName);

    :param Via:
    :param PadName:
    :return: vSDK_dll.vSDK_Via_SetPadName(Via, PadName)
    """
    return vSDK_dll.vSDK_Via_SetPadName(Via, PadName)

def vSDK_Via_GetPadName(Via):
    """
    VSDK_EXPORT int vSDK_Via_GetPadName(Via _Via, char *&PadName);

    :param Via:
    :return: PadName
    """
    PadName = ctypes.c_char_p()
    vSDK_dll.vSDK_Via_GetPadName(Via, ctypes.byref(PadName))
    return PadName

def vSDK_Via_SetPadGroupID(Via, PadGroupID: int):
    """
    VSDK_EXPORT int vSDK_Via_SetPadGroupID(Via _Via, const int PadGroupID);

    :param Via:
    :param PadGroupID:
    :return: vSDK_dll.vSDK_Via_SetPadGroupID(Via, PadGroupID)
    """
    return vSDK_dll.vSDK_Via_SetPadGroupID(Via, PadGroupID)

def vSDK_Via_GetPadGroupID(Via):
    """
    VSDK_EXPORT int vSDK_Via_GetPadGroupID(Via _Via, int &PadGroupID);

    :param Via:
    :return: PadGroupID
    """
    PadGroupID = ctypes.c_int(0)
    vSDK_dll.vSDK_Via_GetPadGroupID(Via, ctypes.byref(PadGroupID))
    return PadGroupID

def vSDK_Via_AddProperty(Via, ckey: bytes, cvalue: bytes):
    """
    VSDK_EXPORT int vSDK_Via_AddProperty(Via _Via, const char *ckey, const char *cvalue);

    :param Via:
    :param ckey:
    :param cvalue:
    :return: vSDK_dll.vSDK_Via_AddProperty(Via, ckey, cvalue)
    """
    return vSDK_dll.vSDK_Via_AddProperty(Via, ckey, cvalue)

def vSDK_Via_FindPropertyVal(Via, ckey: bytes):
    """
    VSDK_EXPORT int vSDK_Via_FindPropertyVal(Via _Via, const char *ckey, char *&cvalue);

    :param Via:
    :param ckey:
    :return: cvalue
    """
    cvalue = ctypes.c_char_p()
    vSDK_dll.vSDK_Via_FindPropertyVal(Via, ckey, ctypes.byref(cvalue))
    return cvalue

def vSDK_Via_GetPropertyCount(Via):
    """
    VSDK_EXPORT int vSDK_Via_GetPropertyCount(Via _Via, int &_PropertyCount);

    :param Via:
    :return: PropertyCount
    """
    PropertyCount = ctypes.c_int(0)
    vSDK_dll.vSDK_Via_GetPropertyCount(Via, ctypes.byref(PropertyCount))
    return PropertyCount

def vSDK_Via_GetPropertyByIndex(Via, Index: int):
    """
    VSDK_EXPORT int vSDK_Via_GetPropertyByIndex(Via _Via, int Index, char *&ckey, char *&cvalue);

    :param Via:
    :param Index:
    :return: ckey, cvalue
    """
    ckey = ctypes.c_char_p()
    cvalue = ctypes.c_char_p()
    vSDK_dll.vSDK_Via_GetPropertyByIndex(Via, Index, ctypes.byref(ckey), ctypes.byref(cvalue))
    return ckey, cvalue

def vSDK_Via_GetViaData(Via):
    """
    VSDK_EXPORT int vSDK_Via_GetViaData(Via _Via, int &NetID, int &PadGroupID, char *&PadName, double &ViaPosX, double &ViaPosY, double &ViaAngle, int &Mirror, int &ViaSide, int &TestPointSide);

    :param Via:
    :return: NetID, PadGroupID, PadName, ViaPosX, ViaPosY, ViaAngle, Mirror, ViaSide, TestPointSide
    """
    NetID = ctypes.c_int(0)
    PadGroupID = ctypes.c_int(0)
    PadName = ctypes.c_char_p()
    ViaPosX = ctypes.c_double()
    ViaPosY = ctypes.c_double()
    ViaAngle = ctypes.c_double()
    Mirror = ctypes.c_int(0)
    ViaSide = ctypes.c_int(0)
    TestPointSide = ctypes.c_int(0)
    vSDK_dll.vSDK_Via_GetViaData(Via, ctypes.byref(NetID), ctypes.byref(PadGroupID), ctypes.byref(PadName), ctypes.byref(ViaPosX), ctypes.byref(ViaPosY), ctypes.byref(ViaAngle), ctypes.byref(Mirror), ctypes.byref(ViaSide), ctypes.byref(TestPointSide))
    return NetID, PadGroupID, PadName, ViaPosX, ViaPosY, ViaAngle, Mirror, ViaSide, TestPointSide

def vSDK_Shape_CreateShapeByCircle(X: float, Y: float, Diameter: float, PositiveNegative: bool, Filled: bool):
    """
    VSDK_EXPORT int vSDK_Shape_CreateShapeByCircle(double X, double Y, double Diameter, bool PositiveNegative, bool Filled, Shape *&_Shape);

    :param X:
    :param Y:
    :param Diameter:
    :param PositiveNegative:
    :param Filled:
    :return: Shape
    """
    Shape = ctypes.c_void_p()
    vSDK_dll.vSDK_Shape_CreateShapeByCircle(ctypes.c_double(X), ctypes.c_double(Y), ctypes.c_double(Diameter), PositiveNegative, Filled, ctypes.byref(Shape))
    return Shape

def vSDK_Shape_CreateShapeByRectangle(CenterX: float, CenterY: float, Length: float, Width: float, PositiveNegative: bool, Filled: bool):
    """
    VSDK_EXPORT int vSDK_Shape_CreateShapeByRectangle(double CenterX, double CenterY, double Length, double Width, bool PositiveNegative, bool Filled, Shape *&_Shape);

    :param CenterX:
    :param CenterY:
    :param Length:
    :param Width:
    :param PositiveNegative:
    :param Filled:
    :return: Shape
    """
    Shape = ctypes.c_void_p()
    vSDK_dll.vSDK_Shape_CreateShapeByRectangle(ctypes.c_double(CenterX), ctypes.c_double(CenterY), ctypes.c_double(Length), ctypes.c_double(Width), PositiveNegative, Filled, ctypes.byref(Shape))
    return Shape

def vSDK_Shape_CreateShapeByLine(StartX: float, StartY: float, EndX: float, EndY: float, LineLength: float, LineWidth: float, isRectangle: bool, PositiveNegative: bool, Filled: bool):
    """
    VSDK_EXPORT int vSDK_Shape_CreateShapeByLine(double StartX, double StartY, double EndX, double EndY, double LineLength, double LineWidth, bool isRectangle, bool PositiveNegative, bool Filled, Shape *&_Shape);

    :param StartX:
    :param StartY:
    :param EndX:
    :param EndY:
    :param LineLength:
    :param LineWidth:
    :param isRectangle:
    :param PositiveNegative:
    :param Filled:
    :return: Shape
    """
    Shape = ctypes.c_void_p()
    vSDK_dll.vSDK_Shape_CreateShapeByLine(ctypes.c_double(StartX), ctypes.c_double(StartY), ctypes.c_double(EndX), ctypes.c_double(EndY), ctypes.c_double(LineLength), ctypes.c_double(LineWidth), isRectangle, PositiveNegative, Filled, ctypes.byref(Shape))
    return Shape

def vSDK_Shape_CreateShapeByArc(CenterX: float, CenterY: float, Radius: float, StartAngle: float, AngleRotate: float, LineLength: float, LineWidth: float, isRectangle: bool, PositiveNegative: bool, Filled: bool):
    """
    VSDK_EXPORT int vSDK_Shape_CreateShapeByArc(double CenterX, double CenterY, double Radius, double StartAngle, double AngleRotate, double LineLength, double LineWidth, bool isRectangle, bool PositiveNegative, bool Filled, Shape *&_Shape);

    :param CenterX:
    :param CenterY:
    :param Radius:
    :param StartAngle:
    :param AngleRotate:
    :param LineLength:
    :param LineWidth:
    :param isRectangle:
    :param PositiveNegative:
    :param Filled:
    :return: Shape
    """
    Shape = ctypes.c_void_p()
    vSDK_dll.vSDK_Shape_CreateShapeByArc(ctypes.c_double(CenterX), ctypes.c_double(CenterY), ctypes.c_double(Radius), ctypes.c_double(StartAngle), ctypes.c_double(AngleRotate), ctypes.c_double(LineLength), ctypes.c_double(LineWidth), isRectangle, PositiveNegative, Filled, ctypes.byref(Shape))
    return Shape

def vSDK_Shape_CreateShapeByArcThreeDrop(StartX: float, StartY: float, ArcPointX: float, ArcPointY: float, EndX: float, EndY: float, LineLength: float, LineWidth: float, isRectangle: bool, PositiveNegative: bool, Filled: bool):
    """
    VSDK_EXPORT int vSDK_Shape_CreateShapeByArcThreeDrop(double StartX, double StartY, double ArcPointX, double ArcPointY, double EndX, double EndY, double LineLength, double LineWidth, bool isRectangle, bool PositiveNegative, bool Filled, Shape *&_Shape);

    :param StartX:
    :param StartY:
    :param ArcPointX:
    :param ArcPointY:
    :param EndX:
    :param EndY:
    :param LineLength:
    :param LineWidth:
    :param isRectangle:
    :param PositiveNegative:
    :param Filled:
    :return: Shape
    """
    Shape = ctypes.c_void_p()
    vSDK_dll.vSDK_Shape_CreateShapeByArcThreeDrop(ctypes.c_double(StartX), ctypes.c_double(StartY), ctypes.c_double(ArcPointX), ctypes.c_double(ArcPointY), ctypes.c_double(EndX), ctypes.c_double(EndY), ctypes.c_double(LineLength), ctypes.c_double(LineWidth), isRectangle, PositiveNegative, Filled, ctypes.byref(Shape))
    return Shape

def vSDK_Shape_CreateArcOrPoint():
    """
    VSDK_EXPORT int vSDK_Shape_CreateArcOrPoint(ArcOrPoints *&_ArcOrPoints);

    :return: ArcOrPoints
    """
    ArcOrPoints = ctypes.c_void_p()
    vSDK_dll.vSDK_Shape_CreateArcOrPoint(ctypes.byref(ArcOrPoints))
    return ArcOrPoints

def vSDK_Shape_DestroyArcOrPoint(ArcOrPoints):
    """
    VSDK_EXPORT int vSDK_Shape_DestroyArcOrPoint(ArcOrPoints *_ArcOrPoints);

    :param ArcOrPoints:
    :return: vSDK_dll.vSDK_Shape_DestroyArcOrPoint(ArcOrPoints)
    """
    return vSDK_dll.vSDK_Shape_DestroyArcOrPoint(ArcOrPoints)

def vSDK_Shape_AddArcOrPointByArc(ArcOrPoints, CenterX: float, CenterY: float, Radius: float, StartAngle: float, AngleRotate: float):
    """
    VSDK_EXPORT int vSDK_Shape_AddArcOrPointByArc(ArcOrPoints *_ArcOrPoints, double CenterX, double CenterY, double Radius, double StartAngle, double AngleRotate, int &Count);

    :param ArcOrPoints:
    :param CenterX:
    :param CenterY:
    :param Radius:
    :param StartAngle:
    :param AngleRotate:
    :return: Count
    """
    Count = ctypes.c_int(0)
    vSDK_dll.vSDK_Shape_AddArcOrPointByArc(ArcOrPoints, ctypes.c_double(CenterX), ctypes.c_double(CenterY), ctypes.c_double(Radius), ctypes.c_double(StartAngle), ctypes.c_double(AngleRotate), ctypes.byref(Count))
    return Count

def vSDK_Shape_AddArcOrPointByArcThreeDrop(ArcOrPoints, StartX: float, StartY: float, ArcPointX: float, ArcPointY: float, EndX: float, EndY: float):
    """
    VSDK_EXPORT int vSDK_Shape_AddArcOrPointByArcThreeDrop(ArcOrPoints *_ArcOrPoints, double StartX, double StartY, double ArcPointX, double ArcPointY, double EndX, double EndY, int &Count);

    :param ArcOrPoints:
    :param StartX:
    :param StartY:
    :param ArcPointX:
    :param ArcPointY:
    :param EndX:
    :param EndY:
    :return: Count
    """
    Count = ctypes.c_int(0)
    vSDK_dll.vSDK_Shape_AddArcOrPointByArcThreeDrop(ArcOrPoints, ctypes.c_double(StartX), ctypes.c_double(StartY), ctypes.c_double(ArcPointX), ctypes.c_double(ArcPointY), ctypes.c_double(EndX), ctypes.c_double(EndY), ctypes.byref(Count))
    return Count

def vSDK_Shape_AddArcOrPoint(ArcOrPoints, ArcOrPointX: float, ArcOrPointY: float, ArcRadius: float, ArcStartAngle: float, ArcAngleRotate: float):
    """
    VSDK_EXPORT int vSDK_Shape_AddArcOrPoint(ArcOrPoints *_ArcOrPoints, double ArcOrPointX, double ArcOrPointY, double ArcRadius, double ArcStartAngle, double ArcAngleRotate, int &Count);

    :param ArcOrPoints:
    :param ArcOrPointX:
    :param ArcOrPointY:
    :param ArcRadius:
    :param ArcStartAngle:
    :param ArcAngleRotate:
    :return: Count
    """
    Count = ctypes.c_int(0)
    vSDK_dll.vSDK_Shape_AddArcOrPoint(ArcOrPoints, ctypes.c_double(ArcOrPointX), ctypes.c_double(ArcOrPointY), ctypes.c_double(ArcRadius), ctypes.c_double(ArcStartAngle), ctypes.c_double(ArcAngleRotate), ctypes.byref(Count))
    return Count

def vSDK_Shape_GetArcOrPointCount(ArcOrPoints):
    """
    VSDK_EXPORT int vSDK_Shape_GetArcOrPointCount(ArcOrPoints *_ArcOrPoints, int &Count);

    :param ArcOrPoints:
    :return: Count
    """
    Count = ctypes.c_int(0)
    vSDK_dll.vSDK_Shape_GetArcOrPointCount(ArcOrPoints, ctypes.byref(Count))
    return Count

def vSDK_Shape_GetArcOrPointByIndex(ArcOrPoints, Index: int):
    """
    VSDK_EXPORT int vSDK_Shape_GetArcOrPointByIndex(ArcOrPoints *_ArcOrPoints, int Index, ArcOrPoint &_ArcOrPoint);

    :param ArcOrPoints:
    :param Index:
    :return: ArcOrPoint
    """
    ArcOrPoint = ctypes.c_void_p()
    vSDK_dll.vSDK_Shape_GetArcOrPointByIndex(ArcOrPoints, Index, ctypes.byref(ArcOrPoint))
    return ArcOrPoint

def vSDK_Shape_CreateShapeByPolygon(ArcOrPoints, Count: int, PositiveNegative: bool, Filled: bool):
    """
    VSDK_EXPORT int vSDK_Shape_CreateShapeByPolygon(ArcOrPoints *_ArcOrPoints, int Count, bool PositiveNegative, bool Filled, Shape *&_Shape);

    :param ArcOrPoints:
    :param Count:
    :param PositiveNegative:
    :param Filled:
    :return: Shape
    """
    Shape = ctypes.c_void_p()
    vSDK_dll.vSDK_Shape_CreateShapeByPolygon(ArcOrPoints, Count, PositiveNegative, Filled, ctypes.byref(Shape))
    return Shape

def vSDK_Shape_CreateShapeByContinuousLine(ArcOrPoints, Count: int, PositiveNegative: bool, Filled: bool):
    """
    VSDK_EXPORT int vSDK_Shape_CreateShapeByContinuousLine(ArcOrPoints *_ArcOrPoints, int Count, bool PositiveNegative, bool Filled, Shape *&_Shape);

    :param ArcOrPoints:
    :param Count:
    :param PositiveNegative:
    :param Filled:
    :return: Shape
    """
    Shape = ctypes.c_void_p()
    vSDK_dll.vSDK_Shape_CreateShapeByContinuousLine(ArcOrPoints, Count, PositiveNegative, Filled, ctypes.byref(Shape))
    return Shape

def vSDK_Shape_DestroyShape(Shape):
    """
    VSDK_EXPORT int vSDK_Shape_DestroyShape(Shape *_Shape);

    :param Shape:
    :return: vSDK_dll.vSDK_Shape_DestroyShape(Shape)
    """
    return vSDK_dll.vSDK_Shape_DestroyShape(Shape)

def vSDK_Shape_GetShapeType(Shape):
    """
    VSDK_EXPORT int vSDK_Shape_GetShapeType(Shape *_Shape, char *&_ShapeType);

    :param Shape:
    :return: ShapeType
    """
    ShapeType = ctypes.c_char_p()
    vSDK_dll.vSDK_Shape_GetShapeType(Shape, ctypes.byref(ShapeType))
    return ShapeType

def vSDK_Shape_GetShapeDataByCircle(Shape):
    """
    VSDK_EXPORT int vSDK_Shape_GetShapeDataByCircle(Shape *_Shape, double &X, double &Y, double &Diameter, bool &PositiveNegative, bool &Filled);

    :param Shape:
    :return: X, Y, Diameter, PositiveNegative, Filled
    """
    X = ctypes.c_double()
    Y = ctypes.c_double()
    Diameter = ctypes.c_double()
    PositiveNegative = ctypes.c_bool()
    Filled = ctypes.c_bool()
    vSDK_dll.vSDK_Shape_GetShapeDataByCircle(Shape, ctypes.byref(X), ctypes.byref(Y), ctypes.byref(Diameter), ctypes.byref(PositiveNegative), ctypes.byref(Filled))
    return X, Y, Diameter, PositiveNegative, Filled

def vSDK_Shape_GetShapeDataByRectangle(Shape):
    """
    VSDK_EXPORT int vSDK_Shape_GetShapeDataByRectangle(Shape *_Shape, double &CenterX, double &CenterY, double &Length, double &Width, bool &PositiveNegative, bool &Filled);

    :param Shape:
    :return: CenterX, CenterY, Length, Width, PositiveNegative, Filled
    """
    CenterX = ctypes.c_double()
    CenterY = ctypes.c_double()
    Length = ctypes.c_double()
    Width = ctypes.c_double()
    PositiveNegative = ctypes.c_bool()
    Filled = ctypes.c_bool()
    vSDK_dll.vSDK_Shape_GetShapeDataByRectangle(Shape, ctypes.byref(CenterX), ctypes.byref(CenterY), ctypes.byref(Length), ctypes.byref(Width), ctypes.byref(PositiveNegative), ctypes.byref(Filled))
    return CenterX, CenterY, Length, Width, PositiveNegative, Filled

def vSDK_Shape_GetShapeDataByLine(Shape):
    """
    VSDK_EXPORT int vSDK_Shape_GetShapeDataByLine(Shape *_Shape, double &StartX, double &StartY, double &EndX, double &EndY, double &LineLength, double &LineWidth, bool &isRectangle, bool &PositiveNegative, bool &Filled);

    :param Shape:
    :return: StartX, StartY, EndX, EndY, LineLength, LineWidth, isRectangle, PositiveNegative, Filled
    """
    StartX = ctypes.c_double()
    StartY = ctypes.c_double()
    EndX = ctypes.c_double()
    EndY = ctypes.c_double()
    LineLength = ctypes.c_double()
    LineWidth = ctypes.c_double()
    isRectangle = ctypes.c_bool()
    PositiveNegative = ctypes.c_bool()
    Filled = ctypes.c_bool()
    vSDK_dll.vSDK_Shape_GetShapeDataByLine(Shape, ctypes.byref(StartX), ctypes.byref(StartY), ctypes.byref(EndX), ctypes.byref(EndY), ctypes.byref(LineLength), ctypes.byref(LineWidth), ctypes.byref(isRectangle), ctypes.byref(PositiveNegative), ctypes.byref(Filled))
    return StartX, StartY, EndX, EndY, LineLength, LineWidth, isRectangle, PositiveNegative, Filled

def vSDK_Shape_GetShapeDataByContinuousLine(Shape):
    """
    VSDK_EXPORT int vSDK_Shape_GetShapeDataByContinuousLine(Shape *_Shape, ArcOrPoint &_ArcOrPoint, int &Count, double &LineLength, double &LineWidth, bool &isRectangle, bool &PositiveNegative, bool &Filled);

    :param Shape:
    :return: ArcOrPoint, Count, LineLength, LineWidth, isRectangle, PositiveNegative, Filled
    """
    ArcOrPoint = ctypes.c_void_p()
    Count = ctypes.c_int(0)
    LineLength = ctypes.c_double()
    LineWidth = ctypes.c_double()
    isRectangle = ctypes.c_bool()
    PositiveNegative = ctypes.c_bool()
    Filled = ctypes.c_bool()
    vSDK_dll.vSDK_Shape_GetShapeDataByContinuousLine(Shape, ctypes.byref(ArcOrPoint), ctypes.byref(Count), ctypes.byref(LineLength), ctypes.byref(LineWidth), ctypes.byref(isRectangle), ctypes.byref(PositiveNegative), ctypes.byref(Filled))
    return ArcOrPoint, Count, LineLength, LineWidth, isRectangle, PositiveNegative, Filled

def vSDK_Shape_GetShapeDataByArc(Shape):
    """
    VSDK_EXPORT int vSDK_Shape_GetShapeDataByArc(Shape *_Shape, double &CenterX, double &CenterY, double &Radius, double &StartAngle, double &AngleRotate, double &LineLength, double &LineWidth, bool &isRectangle, bool &PositiveNegative, bool &Filled);

    :param Shape:
    :return: CenterX, CenterY, Radius, StartAngle, AngleRotate, LineLength, LineWidth, isRectangle, PositiveNegative, Filled
    """
    CenterX = ctypes.c_double()
    CenterY = ctypes.c_double()
    Radius = ctypes.c_double()
    StartAngle = ctypes.c_double()
    AngleRotate = ctypes.c_double()
    LineLength = ctypes.c_double()
    LineWidth = ctypes.c_double()
    isRectangle = ctypes.c_bool()
    PositiveNegative = ctypes.c_bool()
    Filled = ctypes.c_bool()
    vSDK_dll.vSDK_Shape_GetShapeDataByArc(Shape, ctypes.byref(CenterX), ctypes.byref(CenterY), ctypes.byref(Radius), ctypes.byref(StartAngle), ctypes.byref(AngleRotate), ctypes.byref(LineLength), ctypes.byref(LineWidth), ctypes.byref(isRectangle), ctypes.byref(PositiveNegative), ctypes.byref(Filled))
    return CenterX, CenterY, Radius, StartAngle, AngleRotate, LineLength, LineWidth, isRectangle, PositiveNegative, Filled

def vSDK_Shape_GetShapeDataByArcThreeDrop(Shape):
    """
    VSDK_EXPORT int vSDK_Shape_GetShapeDataByArcThreeDrop(Shape *_Shape, double &StartX, double &StartY, double &ArcPointX, double &ArcPointY, double &EndX, double &EndY, double &LineLength, double &LineWidth, bool &isRectangle, bool &PositiveNegative, bool &Filled);

    :param Shape:
    :return: StartX, StartY, ArcPointX, ArcPointY, EndX, EndY, LineLength, LineWidth, isRectangle, PositiveNegative, Filled
    """
    StartX = ctypes.c_double()
    StartY = ctypes.c_double()
    ArcPointX = ctypes.c_double()
    ArcPointY = ctypes.c_double()
    EndX = ctypes.c_double()
    EndY = ctypes.c_double()
    LineLength = ctypes.c_double()
    LineWidth = ctypes.c_double()
    isRectangle = ctypes.c_bool()
    PositiveNegative = ctypes.c_bool()
    Filled = ctypes.c_bool()
    vSDK_dll.vSDK_Shape_GetShapeDataByArcThreeDrop(Shape, ctypes.byref(StartX), ctypes.byref(StartY), ctypes.byref(ArcPointX), ctypes.byref(ArcPointY), ctypes.byref(EndX), ctypes.byref(EndY), ctypes.byref(LineLength), ctypes.byref(LineWidth), ctypes.byref(isRectangle), ctypes.byref(PositiveNegative), ctypes.byref(Filled))
    return StartX, StartY, ArcPointX, ArcPointY, EndX, EndY, LineLength, LineWidth, isRectangle, PositiveNegative, Filled

def vSDK_Shape_GetShapeDataByPolygon(Shape):
    """
    VSDK_EXPORT int vSDK_Shape_GetShapeDataByPolygon(Shape *_Shape, ArcOrPoint &_ArcOrPoint, int &Count, bool &PositiveNegative, bool &Filled);

    :param Shape:
    :return: ArcOrPoint, Count, PositiveNegative, Filled
    """
    ArcOrPoint = ctypes.c_void_p()
    Count = ctypes.c_int(0)
    PositiveNegative = ctypes.c_bool()
    Filled = ctypes.c_bool()
    vSDK_dll.vSDK_Shape_GetShapeDataByPolygon(Shape, ctypes.byref(ArcOrPoint), ctypes.byref(Count), ctypes.byref(PositiveNegative), ctypes.byref(Filled))
    return ArcOrPoint, Count, PositiveNegative, Filled

def vSDK_Shape_GetArcOrPoint(ArcOrPoint, PointIndex: int):
    """
    VSDK_EXPORT int vSDK_Shape_GetArcOrPoint(ArcOrPoint _ArcOrPoint, const int PointIndex, double &ArcOrPointX, double &ArcOrPointY, double &ArcOrPointRadius, double &ArcOrPointStartAngle, double &ArcOrPointAngleRotate, int &ArcOrPointType);

    :param ArcOrPoint:
    :param PointIndex:
    :return: ArcOrPointX, ArcOrPointY, ArcOrPointRadius, ArcOrPointStartAngle, ArcOrPointAngleRotate, ArcOrPointType
    """
    ArcOrPointX = ctypes.c_double()
    ArcOrPointY = ctypes.c_double()
    ArcOrPointRadius = ctypes.c_double()
    ArcOrPointStartAngle = ctypes.c_double()
    ArcOrPointAngleRotate = ctypes.c_double()
    ArcOrPointType = ctypes.c_int(0)
    vSDK_dll.vSDK_Shape_GetArcOrPoint(ArcOrPoint, PointIndex, ctypes.byref(ArcOrPointX), ctypes.byref(ArcOrPointY), ctypes.byref(ArcOrPointRadius), ctypes.byref(ArcOrPointStartAngle), ctypes.byref(ArcOrPointAngleRotate), ctypes.byref(ArcOrPointType))
    return ArcOrPointX, ArcOrPointY, ArcOrPointRadius, ArcOrPointStartAngle, ArcOrPointAngleRotate, ArcOrPointType

def vSDK_Layer_ExportGerber(Pcb, LayerID: int, CExportGerberFileName: str, Mode: int):
    vSDK_dll.vSDK_Layer_ExportGerber(Pcb, LayerID, CExportGerberFileName, Mode)
