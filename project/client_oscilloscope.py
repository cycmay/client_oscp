# coding:utf-8
# __author__: bicycle

import time
import ctypes
import os
from ctypes import c_ushort

from ctypes.wintypes import BOOL

# dll 文件路径
DLL_PATH_HTHARD = os.path.join("DLL", "x64", "HTHardDll.dll")
DLL_PATH_HTSoft = os.path.join("DLL", "x64", "HTSoftDll.dll")
HTSoftDLL = ctypes.cdll.LoadLibrary(DLL_PATH_HTSoft)
HTHardDll = ctypes.cdll.LoadLibrary(DLL_PATH_HTHARD)


# 测试是否连接到设备 参数：int型 0-31
def connected_test(device_index: int):
    """

    :param device_index:
    :return: 成功返回1 失败返回0
    """
    DeviceIndex = ctypes.c_ushort(device_index)
    result = HTHardDll.dsoHTDeviceConnect(DeviceIndex)
    return result


# 连接的设备数量
# 遍历端口
def connected_devices_num():
    """
    :return: int. 连接设备的总数量
    """
    # 声明一个数组类型 实例化为长度为2的short型数组
    array = (ctypes.c_short * 32)()
    for i in range(0, 32):
        array[i] = 0
    # 指针传递
    short_point_device_info = ctypes.pointer(array)
    result = HTHardDll.dsoHTSearchDevice(short_point_device_info)
    return result


# 零电平校准读取函数
def read_calibration_data(device_index: int):
    # 神知道这是什么
    DeviceIndex = ctypes.c_ushort(device_index)
    array = (ctypes.c_ushort * 577)()
    for i in range(0, 577):
        array[i] = 0
    # 指针传递
    short_point_level = ctypes.pointer(array)
    n_len = ctypes.c_ushort(577)
    return None
    result = HTHardDll.dsoHTReadCalibrationData(DeviceIndex, short_point_level, n_len)


# 设定通道的垂直位置 范围0-255. 0-> 通道位置设置到屏幕最下端 128-> 屏幕中间 255-> 屏幕最上端
def set_CH_position(device_index: int, volt_DIV: int, position: int, chanel: int, chanel_mode: int):
    """

    :param device_index: 设备索引值
    :param volt_DIV: 当前通道CH电压索引值
    :param position: 当前通道CH垂直范围0-255
    :param chanel: 当前设置的通道 0-3
    :param chanel_mode: 当前通道模式 1，2，4
    :return: 0: 失败， 1: 成功
    """
    DeviceIndex = ctypes.c_ushort(device_index)
    array = (ctypes.c_ushort * 577)()
    for i in range(0, 577):
        array[i] = 0
    # 指针传递
    short_point_level = ctypes.pointer(array)
    volt_DIV = ctypes.c_ushort(volt_DIV)
    position = ctypes.c_ushort(position)
    chanel = ctypes.c_ushort(chanel)
    chanel_mode = ctypes.c_ushort(chanel_mode)

    result = HTHardDll.dsoHTSetCHPos(DeviceIndex, short_point_level, volt_DIV, position, chanel, chanel_mode)
    return result


# 设定触发的垂直位置
def set_V_trigger_level(device_index, position, sensitivity):
    """

    :param device_index:
    :param position:
    :param sensitivity: 触发灵敏度 越大越不会触发
    :return: 0: 失败， 1: 成功
    """
    DeviceIndex = ctypes.c_ushort(device_index)
    position = ctypes.c_ushort(position)
    sensitivity = ctypes.c_ushort(sensitivity)
    result = HTHardDll.dsoHTSetVTriggerLevel(DeviceIndex, position, sensitivity)
    return result


# 结构体在python中的映射
class ControlDataStruct(ctypes.Structure):
    """实现 HTsoftDll中的结构体--_HT_CONTROL_DATA """

    def __init__(self):
        super(ControlDataStruct, self).__init__()

    _fields_: [
        ("CHSet", ctypes.c_ushort),  # CH开关 0：关，1：开
        ("TimeDIV", ctypes.c_ushort),  # 时基
        ("TrggerSource", ctypes.c_ushort),  # 触发源
        ("HTriggerPos", ctypes.c_ushort),  # 水平触发位置
        ("VTriggerPos", ctypes.c_ushort),  # 垂直触发位置
        ("TriggerSlope", ctypes.c_ushort),  # 边沿触发触发沿
        ("BufferLen", ctypes.c_ulong),  # 内存长度
        ("ReadDataLen", ctypes.c_ulong),  # 需要读取数据长度
        ("AlreadyReadLen", ctypes.c_ulong),  # 已经读取的数据长度
        ("ALT", ctypes.c_ushort),  # 是否交替
        ("ETSOpen", ctypes.c_ushort),  # ETS开关
    ]


# 设定水平触发位置 采集深度
def set_H_trigger_length(device_index, H_trigger_pos, data_depth, chanel_mode):
    """
    :param device_index:
    :param H_trigger_pos:
    :param data_depth:
    :param chanel_mode:
    :return:
    """
    DeviceIndex = ctypes.c_ushort(device_index)
    control_data = ControlDataStruct()
    control_data.HTriggerPos = H_trigger_pos
    control_data.ReadDataLen = data_depth
    chanel_mode = ctypes.c_ushort(chanel_mode)
    # 传递指针
    control_data_point = ctypes.byref(control_data)
    result = HTHardDll.dsoHTSetHTriggerLength(DeviceIndex, control_data_point, chanel_mode)
    return result


# 结构体在python中的映射
class RelayControlStruct(ctypes.Structure):
    """实现 结构体--RELAYCONTROL """

    def __init__(self):
        super(RelayControlStruct, self).__init__()

    _fields_: [
        ("CHEnble", ctypes.c_int),  # 大小为MAX_CH_NUM(CH总数)的数组 开关 0/1
        ("CHVoltDIV", ctypes.c_ushort),  # 数组 电压挡位0-
        ("CHCoupling", ctypes.c_ushort),  # CH的耦合 DC: 0, AC:1
        ("CHBWlimit", ctypes.c_int),  # 带宽限制 0/1
        ("TrigSource", ctypes.c_ushort),  # 触发源 1-6
        ("TrigFilt", ctypes.c_int),  # 高频抑制
        ("ALT", ctypes.c_ushort),  # 0/1
    ]


def list_to_ctype_array(my_list: list):
    len_myList = len(my_list)
    array = (ctypes.c_long * len_myList)()
    for i in range(0, len_myList):
        array[i] = my_list[i]
    pointer_array = ctypes.pointer(array)
    return pointer_array


def set_CH_And_trigger(device_index, ch_enable_list: list, DIV_list: list, coupling_list: list, BWlimits_list: list,
                       trigger_source: int, trigger_flit: int, ALT: int, time_DIV: int):
    """

    :param device_index:
    :param ch_enable_list:
    :param DIV_list:
    :param coupling_list:
    :param BWlimits_list:
    :param trigger_source:
    :param trigger_flit:
    :param ALT:
    :param time_DIV:
    :return:
    """
    DeviceIndex: c_ushort = ctypes.c_ushort(device_index)
    # CHEnble = list_to_ctype_array(ch_enable_list)
    # CHVoltDIV = list_to_ctype_array(DIV_list)
    # CHCoupling = list_to_ctype_array(coupling_list)
    # CHBWlimit = list_to_ctype_array(BWlimits_list)
    # TrigSource = ctypes.c_ushort(trigger_source)
    # ALT = ctypes.c_ushort(ALT)
    # TrigFilt = ctypes.c_ushort(trigger_flit)
    RelayControl = RelayControlStruct()
    RelayControl.CHEnble = ch_enable_list
    RelayControl.CHVoltDIV = DIV_list
    RelayControl.CHCoupling = coupling_list
    RelayControl.CHBWlimit = BWlimits_list
    RelayControl.TrigSource = trigger_source
    RelayControl.ALT = ALT
    RelayControl.TrigFilt = trigger_flit
    # 传递指针
    RelayControl_point = ctypes.byref(RelayControl)
    TimeDIV = ctypes.c_ushort(time_DIV)
    result = HTHardDll.dsoHTSetCHAndTrigger(DeviceIndex, RelayControl_point, TimeDIV)
    return result


# 设定FPGA的采样率
def set_sample_rate(device_index, YT_format,):
    DeviceIndex = ctypes.c_ushort(device_index)
    YTFormat = ctypes.c_ushort(YT_format)
    array = (ctypes.c_ushort * 259)()
    for i in range(0, 259):
        array[i] = 0
    short_point_amp_level = ctypes.pointer(array)
    control_data = ControlDataStruct()
    #control_data.
    RelayControl = RelayControlStruct()
    result = HTHardDll.dsoHTSetSampleRate(DeviceIndex, short_point_amp_level, YT_format, control_data, RelayControl)
    return result


# 开始数据采集
def start_collect_data(device_index, start_control):
    """

    :param device_index:
    :param start_control: 十六进制int型 like:0x21
    :return:
    """
    DeviceIndex = ctypes.c_ushort(device_index)
    start_control = ctypes.c_ushort(start_control)

    result = HTHardDll.dsoHTStartCollectData(DeviceIndex, start_control)
    return result


# 获取采集状态
def get_state(device_index):
    """

    :param device_index:
    :return:
    """
    DeviceIndex = ctypes.c_ushort(device_index)
    result = HTHardDll.dsoHTGetState(DeviceIndex)
    print(result)
    result = hex(result)
    return result


# 神知道这是什么
def get_hard_FC(device_index):
    DeviceIndex = ctypes.c_ushort(device_index)
    result = HTHardDll.dsoHTGetHardFC(DeviceIndex)
    return result

# version
def get_FPGA_version(device_index):
    DeviceIndex = ctypes.c_ushort(device_index)
    result = HTHardDll.dsoGetFPGAVersion(DeviceIndex)
    return result


# 设备初始化
def init_Hard(device_index):
    DeviceIndex = ctypes.c_ushort(device_index)
    result = HTHardDll.dsoInitHard(DeviceIndex)
    return result


# 通道模式变化时使用
def ADC_CH_ModGain(device_index, chanel_mode):
    DeviceIndex = ctypes.c_ushort(device_index)
    CH_Mod = ctypes.c_ushort(chanel_mode)
    result = HTHardDll.dsoHTADCCHModGain(DeviceIndex, CH_Mod)
    return result


# 设置触发源
def set_Ram_And_trigger_control(device_index,time_DIV, CH_set, trigger_source, peak):
    DeviceIndex = ctypes.c_ushort(device_index)
    TimeDiv = ctypes.c_ushort(time_DIV)
    CHSet = ControlDataStruct()
    TrigerSource = ctypes.c_ushort(trigger_source)
    Peak = ctypes.c_ushort(peak)
    result = HTHardDll.dsoHTSetRamAndTrigerControl(DeviceIndex, TimeDiv, CHSet, TrigerSource, Peak)
    return result

# 采集数据
def get_data(device_index):
    DeviceIndex = ctypes.c_ushort(device_index)
    # 申请空间每个通道4096个数据
    array = ctypes.c_ushort * 4096
    array = (array * 4)()
    CH_1 = ctypes.byref(array[0])
    CH_2 = ctypes.byref(array[1])
    CH_3 = ctypes.byref(array[2])
    CH_4 = ctypes.byref(array[3])
    control_data = ControlDataStruct()
    control_data.BufferLen = 4096
    control_data.ReadDataLen = 4096
    # 传递指针
    control_data_point = ctypes.byref(control_data)
    result = HTHardDll.dsoHTGetData(DeviceIndex, CH_1, CH_2, CH_3, CH_4, control_data_point)
    return result







def main():
    print(connected_test(0))
    print(connected_devices_num())
    # print(read_calibration_data(0))
    # print(set_CH_position(0, 2, 128, 0, 1))
    # print(set_V_trigger_level(0, 128, 10))
    # print(set_H_trigger_length(0, 128, 4096*2, 1))
    # print(set_CH_And_trigger(0, [1, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0], 1, 1, 1, 1))
    # print(start_collect_data(0, 0x21))
    # print(get_state(0))
    # print(get_hard_FC(0))
    # print(get_FPGA_version(0))  # ->53249
    # print(init_Hard(0))
    # print(ADC_CH_ModGain(0, 1))
    # print(set_sample_rate(0, 0))
    # print(set_Ram_And_trigger_control(0, 2, 0, 1, 1))
    print(get_data(0))

if __name__ == '__main__':
    main()
