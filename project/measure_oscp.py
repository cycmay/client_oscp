# coding:utf-8
# __author__: bicycle

import ctypes
import os

# dll 文件路径

DLL_PATH_Meas = os.path.join("DLL", "x86", "MeasDll.dll")
DLL_PATH_HTHARD = os.path.join("DLL", "x86", "HTHardDll.dll")
DLL_PATH_HTSoft = os.path.join("DLL", "x86", "HTSoftDll.dll")
HTSoftDLL = ctypes.windll.kernel32.GetModuleHandleA(DLL_PATH_HTSoft)
HTHardDll = ctypes.windll.kernel32.GetModuleHandleA(DLL_PATH_HTHARD)
MeasDll = ctypes.windll.kernel32.GetModuleHandleA(DLL_PATH_Meas)

def main():
	pass

if __name__ == '__main__':
	main()
