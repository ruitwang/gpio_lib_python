from setuptools import setup, Extension, find_packages
import os

# 定义通用的 C 源文件
common_sources = [
    'source/c_gpio.c', 
    'source/cpuinfo.c', 
    'source/event_gpio.c', 
    'source/soft_pwm.c', 
    'source/py_pwm.c', 
    'source/common.c', 
    'source/constants.c', 
    'source/wiringTB.c'
]

setup(
    name='TinkerBoard-GPIO',
    version='0.1.1',
    author='ASUS',
    description='A module to control ASUS GPIO channels',
    # 核心修复：同时定义两个扩展模块
    ext_modules=[
        Extension('ASUS.GPIO', ['source/py_gpio.c'] + common_sources),
        Extension('RPi.GPIO', ['source/py_gpio_RPi.c'] + common_sources),
    ],
    # 自动查找包含 __init__.py 的文件夹
    packages=find_packages(),
    # 强制包含这些包名，防止 find_packages 漏掉
    py_modules=[],
    install_requires=[],
)
