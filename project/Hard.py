# coding:utf-8
# __author__: bicycle

from ctypes import *
from project.DefMacro import *
from project.utils.LoggerInit import LoggerInit

import logging
import os

LoggerInit("DSO").rotating_init()
logger = logging.getLogger("main")

# dll 文件路径
DLL_PATH_HTHARD = os.path.join("DLL", "x64", "HTHardDll.dll")
DLL_PATH_HTSoft = os.path.join("DLL", "x64", "HTSoftDll.dll")
HTSoftDLL = cdll.LoadLibrary(DLL_PATH_HTSoft)
HTHardDll = cdll.LoadLibrary(DLL_PATH_HTHARD)


class CHard(object):
    """ 设备类"""

    # m_bDraw = c_bool(False)
    # m_bStartC = c_bool(True)
    # m_clrRGB = (COLORREF * MAX_CH_NUM)()
    """
    m_clrRGB[CH1] = RGB(255,255,0);
    m_clrRGB[CH2] = RGB(0,255,255);
    m_clrRGB[CH3] = RGB(255,0,255);
    m_clrRGB[CH4] = RGB(0,255,0);
    """
    DeviceIndex = c_ushort(0)  # 设备索引
    DeviceNum = c_ushort(0)  # 连接设备数

    # 控制位置
    LeverPos = (c_ushort * MAX_CH_NUM)()
    LeverPos[CH1] = 80
    LeverPos[CH2] = 112
    LeverPos[CH3] = 144
    LeverPos[CH4] = 176

    # 读取的数据减去零电平的位置(-255 ~ 255) #存储读取数据的指针
    PSrcData = (c_short * MAX_CH_NUM * BUF_4K_LEN)()

    CalLevel = (c_ushort * CAL_LEVEL_LEN)()  # Cal Level

    TimeDIV = c_ushort(9)
    YTFormat = c_ushort(YT_NORMAL)

    ControlData = CONTROLDATA()
    ControlData.nCHSet = 0x0F  # 所有通道打开
    ControlData.nTimeDIV = TimeDIV  # Factory Setup
    ControlData.nTriggerSource = CH1  # 通道1为触发通道
    ControlData.nHTriggerPos = 50  # 水平触发位置（0-100）
    ControlData.nVTriggerPos = 64  # 垂直触发位置和通道1相同
    ControlData.nTriggerSlope = RISE  # 边沿触发的触发方式：上升沿
    ControlData.nBufferLen = BUF_4K_LEN  # 采集深度
    ControlData.nReadDataLen = BUF_4K_LEN  # 读取长度<=采集深度
    ControlData.nAlreadyReadLen = BUF_4K_LEN  # 只在扫描滚动情况下有效，用来记录已经读取的长度
    ControlData.nALT = 0  # Factory Setup
    ControlData.nFPGAVersion = 0xa000  # Factory Setup

    RelayControl = RELAYCONTROL()
    for i in range(MAX_CH_NUM):
        RelayControl.bCHEnable[i] = 1
        RelayControl.nCHVoltDIV[i] = 8
        RelayControl.nCHCoupling[i] = DC
        RelayControl.bCHBWLimit[i] = 0
    RelayControl.nTrigSource = CH1
    RelayControl.bTrigFilt = 0
    RelayControl.nALT = 0

    Collect = c_bool(True)

    TriggerMode = c_ushort(EDGE)
    TriggerSweep = c_ushort(RISE)
    TriggerSlope = c_ushort(AUTO)

    AmpLevel = (c_ushort * AMPCALI_Len)()
    for i in range(AMPCALI_Len):
        # 所有幅度修正设置为1024/1024=1.0
        AmpLevel[i] = 1024

    # 本次读数据是否正确,0,不正确；非0不正确。
    ReadOK = c_ushort(0)

    AmpLevel = (c_ushort * AMPCALI_Len)()
    for i in range(AMPCALI_Len):
        # 所有幅度修正设置为1024/1024=1.0
        AmpLevel[i] = 1024

    def __init__(self):

        pass

    def Init(self):
        DeviceIndex = 0
        # dsoSetUSBBus(index) 此方法说明文档指明无效
        self.init_Hard()
        self.ADC_CH_ModGain(4)
        

    # 设备初始化
    def init_Hard(self):
        DeviceIndex = c_ushort(self.DeviceIndex)
        result = HTHardDll.dsoInitHard(DeviceIndex)
        if result:
            logger.info(f"设备-->{self.DeviceIndex}<--初始化成功!")
        else:
            raise Exception(f"设备-->{self.DeviceIndex}<--初始化失败!")
        return result

    # 通道模式变化时使用
    def ADC_CH_ModGain(self, chanel_mode):
        DeviceIndex = c_ushort(self.DeviceIndex)
        CH_Mod = c_ushort(chanel_mode)
        result = HTHardDll.dsoHTADCCHModGain(DeviceIndex, CH_Mod)
        if result:
            logger.info(f"设备-->{self.DeviceIndex}<--通道模式改变 =>{chanel_mode}!")
        else:
            raise Exception(f"设备-->{self.DeviceIndex}<--通道模式改变!")
        return result

    def ReadData(self):
        pass

    def startAStatus(self):
        pass
