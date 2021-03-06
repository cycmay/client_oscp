# coding:utf-8
# __author__: bicycle

__all__ = ["MAX_CH_NUM", "CONTROLDATA", "RELAYCONTROL", "COLORREF", "BUF_4K_LEN", "CAL_LEVEL_LEN", "CH1", "CH2", "CH3",
           "CH4", "YT_NORMAL", "RISE", "DC", "EDGE", "AUTO" , "AMPCALI_Len"]

#_HT_SCOPE_DEFINE_MACRO_H

 #GDIPLUS
EE_OFFSET = 0x200
D10_100DELAY = 1
AUTOSET_TIME1 = 19
AUTOSET_TIME2  = 18
DRIVERVERLEN = 8 # 必须为偶数
#if DSO_6000_12DIV:
ZERO_START_VOLT = 4
# elif defined D10_100DELAY
ZERO_START_VOLT = 5
# else
ZERO_START_VOLT  = 0
# endif
TRIGGER_VIDEO_POSITIVE = (-900) #mV单位
TRIGGER_VIDEO_NEGATIVE = (900) #mV单位
"""
if DSO_6000_12DIV 
 CALI_2mV 	3#8
 CALI_5mV 	8#8
 CALI_10mV 	15
 CALI_20mV 	30
 CALI_50mV 	70
 CALI_100mV 	30
 CALI_200mV 	60#6.4
 CALI_500mV 	18
 CALI_1V 	35
 CALI_2V 	71
 CALI_5V 	35
 CALI_10V 	70
 CALI_FACTOR  0.6

# elif defined D10_100DELAY
 CALI_2mV 	2#8
 CALI_5mV 	6#8
 CALI_10mV 	12
 CALI_20mV 	30
 CALI_50mV 	60
 CALI_100mV 	120
 CALI_200mV 	30
 CALI_500mV 	60
 CALI_1V 	120
 CALI_2V 	30
 CALI_5V 	60
 CALI_10V 	120
 CALI_FACTOR  0.6

# else 
 CALI_5mV 	4#8
 CALI_10mV 	16
 CALI_20mV 	32
 CALI_50mV 	80
 CALI_100mV 	160
 CALI_200mV 	3.2#6.4
 CALI_500mV 	16
 CALI_1V 	32
 CALI_2V 	64
 CALI_5V 	160
 CALI_FACTOR  0.3
"""



"""
# ifdef DSO3064
# ifdef DSO3074
	DEVICE_NAME = _T("DSO-3074")
 PROGRAM_TITLE = _T("DSO-3074 Ver1.0.8")
 SF_VERSION = _T("1.0.8");
 NO_MENU_AUTOMOTIVE
# elif defined(SEALEY)
	DEVICE_NAME = _T("TA4000")
 PROGRAM_TITLE = _T("Sealey TA4000 Ver1.0.5")
 SF_VERSION = _T("1.0.5");
# elif defined(_8786N)
	DEVICE_NAME = _T("8786N")
 PROGRAM_TITLE = _T("8786N Ver1.0.5")
 SF_VERSION = _T("1.0.5");
# elif defined(_TENMA10175)
	DEVICE_NAME = _T("TENMA72-10175")
 PROGRAM_TITLE = _T("TENMA72-10175 Ver1.0.9") = #在1.0.8基础上解决Autoset操作时时基到1us
 SF_VERSION = _T("1.0.9");
# else
# ifdef DSO3000_NEW
	DEVICE_NAME = _T("DSO-3064_DSO6104") = #
 PROGRAM_TITLE = _T("DSO-3064_DSO6104 Ver2.0.11")
 SF_VERSION = _T("2.0.11");
# else
	DEVICE_NAME = _T("DSO-3064")
 PROGRAM_TITLE = _T("DSO-3064 Ver1.0.10")
 SF_VERSION = _T("1.0.10");
# endif
# endif
"""

# elif defined DSO6000
# 定义垂直8bit精度
VERTICAL_8BIT = 1
MAX_TIMEDIV_NUM = 35	#总时基档位个数 = 
TIMEDIV_OFFSET = 3	#时基偏移量
DEVICE_NAME	= "DSO-6000"
PROGRAM_TITLE	= "DSO-6000"
SF_VERSION = "2.0.9"
FUN_DDS = 1	#定义是否有DDS功能


#Scan
#模式是否有10K长度限制(也就是说SCAN模式只有在10K长度下才能使用)
BUF_10K_LIMIT = 1

ROLL_STEP_32 = 32	##ROLL/SCAN读取一次数据的步进

# Project
DSO = 0	#示波器
DDS = 1	#信号源
LA = 2	#逻辑分析仪

MAX_USB_DEV_NUMBER = 32 #PC最大设备连接数目
_NO_SN = 1 #不在设备列表和DOC标题栏显示SN
MIN_DEMO_POS = MAX_USB_DEV_NUMBER	#模拟状态在设备列表中最小位置

THREAD_TIMEOUT = 0
PI = 3.14159265358979323846
# Communication
USB = 0
NET = 1
NET_LAN = 2
NET_WIFI = 3
UDP = 0
TCP_IP = 1

# 频率单位定义
FREQUENCY_UNIT_HZ = 0
FREQUENCY_UNIT_KHZ = 1
FREQUENCY_UNIT_MHZ = 2
MAX_FREQUENCY_UNIT = 3

MIN_SWEEPSTEPS_NUM = 2	#最小扫描步骤数
SWEEP_FREQUENCY_LINEAR = 0	#线性扫频
SWEEP_FREQUENCY_LOGARITHM = 1	#对数扫频
MAX_SWEEP_FREQUENCY_TYPE = 2	#最大扫频数目

BUF_4K_LEN = 0x1000
BUF_3K_LEN = 0x0C00#3072
BUF_8K_LEN = 0x2000
BUF_16K_LEN = 0x4000
BUF_32K_LEN = 0x8000
BUF_64K_LEN = 0x10000
BUF_10K_LEN = 10240  
BUF_1M_LEN = 1048576
BUF_2M_LEN = 2097152
BUF_4M_LEN = 4194304
BUF_8M_LEN = 8388608
BUF_12M_LEN = 12582912
BUF_16M_LEN = 16252928
BUF_40K_LEN = 40960 #40960#32768
BUF_INSERT_LEN = BUF_40K_LEN
DEF_READ_DATA_LEN = BUF_4K_LEN
DEF_DRAW_DATA_LEN = BUF_4K_LEN


MAX_INSERT_TIMEDIV = 6	##200nS	最大需要插值的时基  #modified by zhang from 9 to 5  200ns
MAX_DOUBLE_TIMEDIV = MAX_INSERT_TIMEDIV
MAX_SF_T_TIMEDIV = MAX_INSERT_TIMEDIV - 2  #需要软件找触发的时基
MAX_SINE_TIMEDI = 3##2##2  #小于3必须正弦插值
#   INSERT_DATA_LEN = 4*BUF_1K_LEN
INSERT_MODE_SIN = 2
INSERT_MODE_STE = 0
INSERT_MODE_LINEAR = 1
YT = 0
XY = 1
YT_NORMAL = 0
YT_SCAN = 1
YT_ROLL = 2
PEAK_START_TIMEDI = 5#13


MIN_SCAN_TIMEDI = 26 #扫描模式最小时基
MIN_ROLL_TIMEDI = 26 #


SINE_WAVE_LEN = 128 #中间小窗口的波形长度
MAX_ETS_TIMEDIV = 3  #0,1,2,3
ETS_SAMPLING_100M = 0 #ETS 100M

# 基准电平的9点校准 ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
NEW_CAL_LEVEL_LEN = 400 #1*9+9*(4*9)=334 = #首个点为9代表9点校准发


# 垂直 ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
# 定义CH
CH1 = 0
CH2 = 1
CH3 = 2
CH4 = 3

MAX_CH_NUM = 4 #定义最大输入通道数(不包括MATH/REF)



HORIZONTAL = MAX_CH_NUM #CH1/CH2/CH3/CH4/HORIZONTAL/(水平lever)
MATH = MAX_CH_NUM #CH1/CH2/CH3/CH4/MATH/REF (垂直lever)
REF = MAX_CH_NUM+1	#CH1/CH2/CH3/CH4/MATH/REF (垂直lever)
ALL_CH = MAX_CH_NUM+2
MIN_DATA = 0  #
# ifdef VERTICAL_8BIT
MAX_DATA = 255  #
MID_DATA = 128  #

MAX_VOLTDIV_NUM = 12 #总电压档位个数  #to cope with DSO6104 add by zhang 2015 0914

# Calibration
CAL_VOLTDIV_NUM = 20   #change from 18 to 20 by zhang 6104
# else
CAL_LEVEL_LEN = 64
STEP_NULL = 0
STEP_1 = 1#Zero
STEP_2 = 2#2mV
STEP_3 = 3#10mV
STEP_4 = 4#100mV
STEP_5 = 5#1V
STEP_6 = 6  #1V -7V
STEP_7 = 7 #1V -10V
STEP_8 = 8 #1V -12V
STEP_9 = 9 #1V -15V
STEP_10 =  10#30mV
STEP_11 = 11#100mV
STEP_12 = 12#160mV
STEP_13 = 13#-30mV
STEP_14 = 14#-100mV
STEP_15 = 15#-160mV
STEP_16 = 16#-200mV
STEP_17 = 17#-500mV
STEP_18 = 18#500mV
STEP_19 = 19#800mV
STEP_20 = 20#-800mV

STEP_21 = 21#结束
# endif

MAX_CAL_DATA = 60000 #modified by  zhang from 2200 to 52000 to fit 6104
SIN_FACTOR = 10 #正弦插值因子
DC = 0
AC = 1
GND = 2

X1 = 0
X10 = 1
X100 = 2
X1000 = 3
X10000 = 4
# ifdef AUTOMOTIVE
X20 = 5
X20A = 6
X65A = 7
X60A = 8
X650A = 9
X100A = 10
X1100A = 11
XSIP_INVERTED = 12
XSIP_POS = 13
PROBE_NUM = XSIP_POS+1 #探头的总数
# else
PROBE_NUM = X10000+1 #探头的总数
# endif

# MATH
MATH_ADD = 0
MATH_SUB = 1
MATH_MUL = 2
MATH_DIV = 3
MATH_FFT = 4

RECTANGLE = 0
HANNING = 1
HAMMING = 2
BLACKMAN = 3
VRMS = 0
DBRMS = 1

# ifdef MINISCOPE
FFT_SRC_DATA_LEN = 256
# else
FFT_SRC_DATA_LEN = 2048#8192  
# endif
# 触发 ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
MAX_TRIGGER_SOURCE_NUM = MAX_CH_NUM+2	#CH1/CH2/CH3/CH4/EXT/(EXT/10)
MAX_ALT_TRIGGER_NUM = MAX_CH_NUM #CH1/CH2/CH3/CH4
EXT = MAX_CH_NUM
EXT10 = MAX_CH_NUM + 1	

EDGE = 0
PULSE = 1
VIDEO = 2
FORCE = 0x80

AUTO = 0
NORMAL = 1
SINGLE = 2

RISE = 0
FALL = 1

PLESS = 0
PEQUAL = 1
PMORE = 2
NLESS = 3
NEQUAL = 4
NMORE = 5


EQUAL = 0
UNEQUAL = 1
MORE = 2
LESS = 3


POSITIVE = 1
NEGATIVE = 0

#
ALL_LINES = 0
ALL_FIELD = 4
ODD_FIELD = 2
EVEN_FIELD = 3
LINE_NUM = 1

# 0: Pal / Secam;1: Ntsc
PALSECAM = 0
NTSC = 1
PALSECAM_MAX_LINENUM = 625
NTSC_MAX_LINENUM = 525
#MY_WM_MSG_UPDATA_BUFFERLEN = (WM_USER+105)

# 幅度校正
ZEROCALI_FIX_OFFSET = 16
ZEROCALI_STEP_NUM = 15
ZEROCALI_DISCARD_NUM = 2
ZEROCALI_ALLOWED_OFFSET  = 10
ZEROCALI_MIN_NUM = 500
ZEROCALI_MAX_NUM = 60000
ZEROCALI_MID_NUM = 37000#35400
ZEROCALI_STEP_NUM = 15

DATA_CHECK_HOP =     0x01
DATA_CHECK_AVE =     0x02
CALI_MSG_ERROR =  0
CALI_MSG_PROGRASS = 1
CALI_MSG_FINISHED = 2
CALI_MSG_ABORT = 3
CALI_MSG_INFO = 4
CALI_MSG_CALI_RESULT = 5
DEVICE_ADDRESS = "USB0::0x049F::0x505B::HTG10000522222::0::INSTR"

AMPCALI_DLG = 0
ZEROCALI_DLG = 1
AMPCALI_FLAG = 0xFACF
TIMEDIV_1GSA =  6
TIMEDIV_500MSA = 7
TIMEDIV_250MSA =  8

AMPCALI_NEED_FIRST_FRAME =   1
AMPCALI_FRAME_NUM  =  5
AMPCALI_INPUT_RANGE = 0.875
AMPCALI_PER_VOLT_Len     = 6
AMPCALI_PER_CH_Len  = (AMPCALI_PER_VOLT_Len*MAX_VOLTDIV_NUM)  
AMPCALI_ALLOW_OFFSET     = 0.5
AMPCALI_DEGREE_OFFSET = 180
AMPCALI_DEGREE = 1024
AMPCALI_Len = (AMPCALI_PER_CH_Len*MAX_CH_NUM)
AMPCALI_DATA_Len  =  (AMPCALI_Len*2)
AMPCALI_ALLOWED_OFFSET = 5#(1-AMPCALI_INPUT_RANGE)*(MAX_DATA-MIN_DATA)*0.5*0.5

ZERO_FLAG = 0xFBCF
ZERO_MAN_OFFSET = 0 
#ZEROCALI_LEN = (ZEROCALI_PER_CH_LEN*MAX_CH_NUM)
#ZEROCALI_PER_CH_LEN = (ZEROCALI_PER_VOLT_LEN*MAX_VOLTDIV_NUM)
ZEROCALI_PER_VOLT_LEN = 12
ZEROCALI_FRAM_NUM =  6
ZEROCALI_SLEE = 0#3


DDS_CALI_LEN = 4 #注意这里指WORD
DDS_AMP_OK = 0xEAEA
DDS_CALI_OK = 0xABAB
"""
# 显示 ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** /
TRANSPARENT_COLOR = RGB(236,233,216)	#定义透明色
BLACK_COLOR = RGB(0,0,0) = #黑色
WHITE_COLOR = RGB(255,255,255)	#白色
RED_COLOR = RGB(255,0,0) = #红色
GREEN_COLOR = RGB(0,255,0) = #绿色
BLUE_COLOR = RGB(0,0,200) = #蓝色
SKY_COLOR = RGB(0,255,255) = #天蓝色
YELLOW_COLOR = RGB(255,255,0) = #黄色
PINK_COLOR = RGB(255,0,255) = #粉红色
BROWN_COLOR = RGB(255,128,0) = #棕色
FRENCHGRAY_COLOR = RGB(155,155,155)	#浅灰色
DEEPGRAY_COLOR = RGB(50,50,50) = #深灰色
PURPLE_COLOR = RGB(128,0,255) = #紫色
JADEGREEN_COLOR = RGB(128,255,128)	#浅绿色
ORANGE_COLOR = RGB(255,127,0) = #橙色
AM1_COLOR = RGB(200,200,0) = #AM1 COLOR	较对应的CH1，颜色浅一些
AM2_COLOR = RGB(0,200,200) = #AM2 COLOR	较对应的CH2，颜色浅一些
AM3_COLOR = RGB(200,0,200) = #AM3 COLOR	较对应的CH3，颜色浅一些
AM4_COLOR = RGB(0,200,0) = #AM4 COLOR	较对应的CH4，颜色浅一些
# ifdef MINISCOPE

AM5_COLOR = RGB(0,100,225) = #AM5 COLOR	较对应的CH5，颜色浅一些
AM6_COLOR = RGB(100,100,227) = #AM6 COLOR	较对应的CH6，颜色浅一些
AM7_COLOR = RGB(100,0,227) = #AM7 COLOR	较对应的CH7，颜色浅一些
AM8_COLOR = RGB(227,100,164) = #AM8 COLOR	较对应的CH8，颜色浅一些

# endif
XY_COLOR = RGB(0,218,236)
CH1_COLOR = YELLOW_COLOR	
CH2_COLOR = SKY_COLOR
CH3_COLOR = PINK_COLOR
CH4_COLOR = GREEN_COLOR	
CH5_COLOR = RGB(0,128,255)
CH6_COLOR = RGB(255,208,100)
CH7_COLOR = PURPLE_COLOR
CH8_COLOR = RGB(255,128,192)
MATH_COLOR = RED_COLOR
REF_COLOR = WHITE_COLOR
EXT_COLOR = BROWN_COLOR
HORI_COLOR = BLUE_COLOR
TRIG_COLOR = BROWN_COLOR

GRID_BRIGHT = 200 #网格亮度
MAX_VCH_LEVER_NUM = MAX_CH_NUM+2	#CH1/CH2/CH3/CH4/MATH/REF
MAX_H_LEVER_NUM = MAX_CH_NUM+1	#CH1/CH2/CH3/CH4/HORIZONTAL
VCH_LEVER = 0
VT_LEVER = 1
H_LEVER = 2
AM_LEVER = 3
CUR_NONE = 0
CUR_CROSS = 1
CUR_TRACE = 2
CUR_VERTICAL = 3
CUR_HORIZONTAL = 4
VECTORS = 0
DOTS = 1
V_GRID_NUM = 8#垂直8个大格
H_GRID_NUM = 10#水平10个大格
# Lever
Position
DIRECTION_LEFT = 0
DIRECTION_RIGHT = 1
DIRECTION_TOP = 2
DIRECTION_BOTTOM = 3

"""
# Measure
MAX_MEAS_LEN = 8
# Voltage
MEAS_VP = 0
MEAS_VMAX = 1
MEAS_VMIN = 2
MEAS_VAM = 3
MEAS_VTO = 4
MEAS_VMID = 5
MEAS_VBASE = 6
MEAS_VAVG = 7
MEAS_VCAVG = 8
MEAS_VRMS = 9
MEAS_VCRMS = 10
MEAS_VPRE = 11
MEAS_VOVER = 12
# Time
MEAS_PERIOD = 13
MEAS_FREQ = 14
MEAS_RISE = 15
MEAS_FALL = 16
MEAS_PDUTY = 17
MEAS_NDUTY = 18
MEAS_PWIDTH = 19
MEAS_NWIDTH = 20
MEAS_PDELAY12 = 21
MEAS_NDELAY12 = 22

# 控制
SAMPLE_NORMAL = 0
SAMPLE_PEAK = 1
SAMPLE_ETS = 2
SAMPLE_AVG = 3

NO_ZOOM = -1
ZOOM_OUT = 0
ZOOM_IN = 1
# RunStatus - -0: STOP;1: RUN;2: Tri'D;3:AUTO;4:WAIT;
STATUS_STO = 0
STATUS_RUN = 1
STATUS_TRID = 2
STATUS_AUTO = 3
STATUS_WAIT = 4
STATUS_PLAY = 5
STATUS_ALT = 6
STATUS_REC = 7

AVG_0 = 0
AVG_4 = 4
AVG_16 = 16
AVG_64 = 64
AVG_128 = 128
AVG_MAX = AVG_128

# 频率计模式
FC_F = 100000000  #实际时间：1E8*8nS=0.8S
FC_C = 1000000000	#正常运行  1S  nS单位
FC_OFF = 2
# Save
FILE_TXT = 0	#Text
FILE_DOC = 1	#Word
FILE_XLS = 2	#Excel
FILE_REF = 3	#Ref
FILE_CS = 4	#CSV
FILE_WMS = 5	#waveform setup#数据+配置

# PASSFAIL
FAIL = 0
FAIL_BEEPER = 1
PASS = 2
PASS_BEEPER = 3
# Record
MAX_RECORD_FRAME = 1000

# Update
UPDATE_FIALE_LEN = 524288	#bytes
#
TYPE_VERSION = 0 #产品类型
NAME_VERSION = 1 #产品名称
PCB_VERSION = 2 #PCB版本
DRIVER_VERSION = 3 #驱动版本号
PRODUCTOR_VERSION = 4 #生产小组
PACKAGER_VERSION = 5 #包装小组
SN_VERSION = 6 #产品编号
PRODUCE_VERSION = 7  #生产日期
TESTTIME_VERSION = 8 #测试日期
TESTSN_VERSION = 9 #测试人员
FPGA_VERSION = 10#FPGA版本号
"""
# 内存分配段
TYPE_LEN = 6 = #产品类型
NAME_LEN = 8 = #产品名称
PCB_LEN = 6 = #PCB版本
DRIVER_LEN = 6 = #驱动版本号
PRODUCTOR_LEN	4 = #生产小组
PACKAGER_LEN	4 = #包装小组
SN_LEN = 8 = #产品编号
PRODUCE_LEN = 8 = #生产日期
TESTTIME_LEN	8 = #测试日期
TESTSN_LEN = 4 = #测试人员
FPGA_LEN = 6 = #FPGA版本号
SUBVERSION_LEN	2 = #子版本
DEV_INFO_LEN	(TYPE_LEN+NAME_LEN+PCB_LEN+DRIVER_LEN+PRODUCTOR_LEN+PACKAGER_LEN+SN_LEN+PRODUCE_LEN+TESTTIME_LEN+TESTSN_LEN+FPGA_LEN+SUBVERSION_LEN) #128#
DDS_CALI_LEN	4 = #注意这里指WORD
MAX_MINIFLASH_LEN = 20

R_STORAGE	0
R_PLAY = 1

STORAGE_MEMORY	0
STORAGE_DISK	1






# 消息
MSG_NULL = 0x00	#空消息
MSG_SET_TIMEDI = 0x01	#设置时基
MSG_SET_CHANNEL = 0x02	#设置CH开和关
MSG_SET_TRIGGER = 0x03	#设置触发(触发模式，上升沿/下降沿，脉冲条件 ，脉宽，视频同步，视频标准，视频行数，同步输出)
MSG_SET_TRIGGER_SOURCE = 0x2C
MSG_SET_CHLEVER_POS = 0x04	#设置通道Lever Pos
MSG_SET_VTLEVER_POS = 0x05	#设置垂直触发Level
MSG_SET_HTLEVER_POS = 0x06	#设置水平触发Pos
MSG_SET_BUFFERLEN = 0x07	#设置内存大小
MSG_WRITE_CAL_LEVEL = 0x08	#写校对电平
MSG_READ_CAL_LEVEL = 0x09	#读校对电平
MSG_ETS_TDC_CAL = 0x0A	#ETS Calibration
MSG_SET_CONNECT_TYPE	0x0B	#设置通信方式，USB或NET
MSG_SET_DEV_I = 0x0C	#设置设备IP等
MSG_GET_DEV_I = 0x0D
MSG_SET_TARGET_IP = 0x0E	#设置连接IP
MSG_WRITE_FLASH = 0x0F	#写FLASH
MSG_READ_FLASH = 0x10	#
MSG_SET_NET_MODE = 0x11	#网络连接模式设置,WIFI/LAN

MSG_SET_TRIGGER_SWEEP	0x20	#设置Sweep
MSG_CALIBRATION = 0x22	#Calibration
MSG_PRE_CALIBRATE = 0x23	#
MSG_END_CALIBRATE = 0x24	#
MSG_START_COLLECT = 0x25	#
MSG_STOP_COLLECT = 0x26
MSG_AUTOSET = 0x27
MSG_AUTOSET_TIMEDIV = 0x28
MSG_RESET_TRIG_LEVEL	0x29
MSG_FACTORY_SETUP = 0x2A
MSG_LOAD_SETUP_OK = 0x2B

MSG_DEV_PULLOUT = 0x30
MSG_DEV_PLUG = 0x31

# ifdef AUTOMOTIVE
MSG_AM_DATA_CHANGE = 0x32
# endif

# ifdef MINISCOPE
MSG_SET_MINISCOPE = 0x33
MSG_RW_FLASH = 0x34#读写FLASH
MSG_SET_GENERATOR_TIME = 0x35
MSG_SET_GENERATOR_OUTPUT	0x36
MSG_SET_IOENABLE = 0x37
MSG_SET_SAVETODEVICE = 0x38
# endif

MSG_SET_H_FORMAT = 0x42
MSG_SET_YT_FORMAT = 0x43
MSG_SET_SAMPLEMODE = 0x44
MSG_SET_INVERT = 0x45
MSG_CENTER_TRIGGER = 0x46
MSG_SET_FCTYPE = 0x47
MSG_RESET_CNTER = 0x48
MSG_CREATE_PFMASK = 0x49
MSG_PASSFAIL_ONOFF = 0x4A
MSG_SET_AVERAGE = 0x4B
MSG_RECORDER_START = 0x4C
MSG_RECORDER_STO = 0x4D

MSG_READ_FPGA_VERSION = 0x4E

# DDS
设置消息
DDS_MSG_DDSONOFF = 0x50#打开关闭DDS
DDS_MSG_DOWNLOAD = 0x51#下载波形
DDS_MSG_SET_FREQUENCY = 0x52#设置频率
DDS_MSG_SET_SYNCOUT = 0x53#设置同步输出
DDS_MSG_SET_CMD = 0x54#设置单次等参数
#   DDS_MSG_SET_POWERON = 0x55#设置上电输出
DDS_MSG_SWEEPONOFF = 0x56#
DDS_MSG_SWEEP_INCFREQ = 0x57#扫频，频率自加
DDS_MSG_INIT_ARB_WARE = 0x58#重新设定任意波形
DDS_MSG_EMIT_SINGLE = 0x59#发射 Single波形  #zhang
MSG_SET_ADCCHMOD_GAIN	0x60
MSG_SET_AMP_CALI = 0x61#下载波形
MSG_SET_CHLEVEL_DIRECT	0x62
#
INFO_ALREADY_HIDE = 0
INFO_NOW_HIDE = 1
INFO_NOW_SHOW = 2
INFO_ALREADY_SHOW = 3

/ ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *DDS ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
WAVE_SINE = 0
WAVE_RAMP = 1
WAVE_SQUARE = 2
WAVE_TRAPE = 3
WAVE_DC = 4
WAVE_EXP = 5
WAVE_AM = 6
WAVE_STORAGE	7
WAVE_GAUSE = 8
WAVE_WHITE = 9
WAVE_ARB = 10	#用户自定义波形

MAX_BUFFER = 2048
MAX_CLOCK = 200000000	#200M(内部时钟频率)
MAX_VOLT = 3.5f = #最大幅度电压
MAX_ARB_FREQUENCY = 25000000	#任意波形最大25M
MAX_FREQUENCY = 75000000	#75M DDS 最大输出频率
MAX_YOFFSET = 7.0 = #最大偏移量
MIN_YOFFSET = -7.0 = #最小偏移量
MAX_PHASE = 1.0 = #最大相位
MIN_PHASE = 0.0 = #最小相位
MAX_DUTY = 1.0 = #最大占空比
MIN_DUTY = 0.0 = #最小占空比
MAX_TAO = 1.0 = #最大TAO
MIN_TAO = 0.0 = #最小TAO
MAX_AMFM_HIGH_FRE = 25000000.0 = #25M
MIN_AMFM_HIGH_FRE = 0.0 = #
MAX_AMFM_DEPTH = 1.0
MIN_AMFM_DEPTH = 0.0
SWEEP_MAXFREQUENCY = 100000.0
SWEEP_MINFREQUENCY = 20.0
SWEEP_MAXSTE = 99980.0
SWEEP_MINSTE = 1.0
SPEED_MAXTIME = 3600*60 = #1h
SPEED_MINTIME = 5 = #50ms


UNSIGNED = 0#无符号，正数
SIGNED = 1#有符号，自然数


/ ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** DDS ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /

typedef
unsigned
char
BOOLEAN;
typedef
unsigned
char
INT8U; / *Unsigned
8
bit
quantity * /
typedef
signed
char
INT8S; / *Signed
8
bit
quantity * /
typedef
unsigned
short
INT16U; / *Unsigned
16
bit
quantity * /
typedef
signed
short
INT16S; / *Signed
16
bit
quantity * /
typedef
unsigned
long
INT32U; / *Unsigned
32
bit
quantity * /
typedef
signed
long
INT32S; / *Signed
32
bit
quantity * /
typedef
float
FP32; / *Single
precision
floating
point * /
typedef
double
FP64; / *Double
precision
floating
point * /

typedef
unsigned
short
HT_DEVICE_ID; # 设备ID
typedef
INT32U
HTSTATUS; # 定义返回信息
HT_OK = 1
HT_ERROR	0

#
MAX_DRIVER_NAME = 64 = #最大设备名称长度
USB_PACK_SIZE = 512 = #USB上传数据包大小

# AUTOMOTIVE
AM_ROOT = 0
# ifdef _ADD_AM_FUNCTIONS
FIRSTLOOK	AM_ROOT+1#1
# else
FIRSTLOOK	AM_ROOT
# endif
IGNITION	FIRSTLOOK+1#2
SENSORS = IGNITION+1#3
CANBUS = SENSORS+1#4
ACTUATORS	CANBUS+1#5
CHANGING	ACTUATORS+1#6
PRIMARY = CHANGING+1#7
SECONDARY	PRIMARY+1#8
AIRFLOW = SECONDARY+1#9
CAMSHAFT	AIRFLOW+1#10
CRANKSHAFT	CAMSHAFT+1#11
DISTRIBUTOR	CRANKSHAFT+1#12
LAMBDA = DISTRIBUTOR+1#13
THROTTLE	LAMBDA+1#14
INJECTOR	THROTTLE+1#15
PETROL = INJECTOR+1#16
DIESEL = PETROL+1#17
CHARGINGCIRCUITS DIESEL+1#18
# ifdef MINISCOPE
GENERATOR	CHARGINGCIRCUITS+1#19
# endif GENERATOR_LEN	1440 #800
"""

''' 结构体 '''
class HT_MEASURE_ITEM(Structure):

    _fields_ = [
        ("Enable", c_int),
        ("nSource", c_short),
        ("nType", c_short)
    ]


class CAN_DECODE(Structure):

    _fields_ = [
        ("nInfo", c_ubyte),
        ("nAck", c_ubyte),
        ("nEOF", c_ubyte),
        # FIXME:结构体中成员数组定义方式是否是这样，存疑。
        ("pData", (c_ubyte*8)),
        ("nReadCRC", c_ushort),
        ("nCalCRC", c_ushort),
        ("nStartIndex", c_ushort),
        ("nEndIndex", c_ushort),
        ("nID", c_ulong)
    ]


class LIN_DECODE(Structure):

    _fields_ = [
        ("nID", c_ubyte),
        ("pData", c_ubyte*8),
        ("nReadCRC", c_ubyte),
        ("nCalCRC", c_ubyte),
        ("nStartIndex", c_ushort),
        ("nEndIndex", c_ushort),
    ]

class IIC_DECODE(Structure):

    _fields_ = [
            ("nData", c_ubyte),
            ("nType", c_ubyte),
            ("nAck", c_ubyte),
            ("nStartIndex", c_ushort),
            ("nEndIndex", c_ushort),
        ]

class UART_DECODE(Structure):

    _fields_ = [
            ("nData", c_ubyte),
            ("nStartIndex", c_ushort),
            ("nEndIndex", c_ushort),
        ]

class SPI_DECODE(Structure):

    _fields_ = [
            ("nData", c_ubyte*4),
            ("nStartIndex", c_ushort),
            ("nEndIndex", c_ushort),
        ]

class HTMSG(Structure):

    _fields_ = [
            ("nType", c_ushort),
            ("nValue", c_longlong),
            ("dbValue", c_double),
        ]


class DATAMATCH(Structure):

    _fields_ = [
            ("nTimeDIV", c_ushort),
            ("nVoltDIV", c_ushort),
            ("nLeverPos", c_ushort),
            ("nHTriggerPos", c_long),
            ("nReadDataLen", c_ulong),
            ("nAlreadyReadLen", c_ulong),
        ]

'''
#ifdef MINISCOPE

class MINICH(Structure):
    ("bEnable", c_int*MAX_CH_NUM),
    ("nVoltDIV", c_ushort*MAX_CH_NUM),
    ("nTimeDIV", c_ushort),
    ("nDisLever", c_ushort*MAX_CH_NUM),
    ("nSrcDataLen", c_ulong),

	# ("nDisDataLen", c_ulong*MAX_CH_NUM),
	# ("clrRGB", COLORREF*MAX_CH_NUM),
	# ("nHTriggerPos", c_ushort),
	("nOpenCHNum", c_ushort),
    ("pData", c_ushort*MAX_CH_NUM),
    # 已经读取的数据长度,ROLL/SCAN下有效
	("nAlreadyReadLen", c_ulong), 

#endif
'''
