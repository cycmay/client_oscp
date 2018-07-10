# coding:utf-8
# __author__: bicycle

import ctypes
import os

# dll 文件路径
DLL_PATH_HTHARD = os.path.join("DLL", "x64", "HTHardDll.dll")
DLL_PATH_HTSoft = os.path.join("DLL", "x64", "HTSoftDll.dll")
HTSoftDLL = ctypes.cdll.LoadLibrary(DLL_PATH_HTSoft)
HTHardDll = ctypes.cdll.LoadLibrary(DLL_PATH_HTHARD)

# 测试是否连接到设备 参数：int型 0-31
def connected_test(device_index: int):
	DeviceIndex = ctypes.c_ushort(device_index)
	result = HTHardDll.dsoHTDeviceConnect(DeviceIndex)
	return result

# 连接的设备数量
# 遍历端口
def connected_devices_num():
	"""
	return: int. 
	"""
	# 声明一个数组类型 实例化为长度为2的short型数组
	array = (ctypes.c_short * 32)()
	for i in range(0, 31):
		array[i] = 0
	# 指针传递
	short_point = ctypes.pointer(array)
	result = HTHardDll.dsoHTSearchDevice(short_point)
	return result
def main():
	print(connected_test(0))
	#print(connected_devices_num())
	pass

if __name__ == '__main__':
	main()

