#!C:\Python27\python.exe
# -*- coding: utf-8 -*-
from protocol import *
from sys_env import *
import time
    
#--------------------相机标定主函数-----------------------------
if __name__ == '__main__':
    
    print u'---进入相机标定流程---'
    i=0
    while i==0:
        N=raw_input(unicode('请输入需要标定的相机编号:','utf-8').encode('gbk'))        
     #   wheel_camera_calibration('100327878','100327878','192.168.1.113')
     #   print u'  相机9轮间距 标定完成! '
      #  N='0'
        if N=='12':
            #-----------行走控制标定相机标定-----------
            #wheel_camera_calibration('100263780','100263780','192.168.1.110')
            wheel_camera_calibration('100263780','100399800','192.168.2.110')
            print u'  相机1行走 标定完成! '
        elif N=='34':
            #----------行走航位标定相机标定----------------
            wheel_camera_calibration('100366817','100408370','192.168.3.111')
            print u'  相机2航位 标定完成! '
        elif N=='4':
            #----------行走航位标定相机标定----------------
            wheel_camera_calibration('100408370','100408370','192.168.1.111')
            print u'  相机2航位 标定完成! '
        elif N=='5':
            #----------轮间距标定相机标定----------------
            wheel_camera_calibration('100289713','100289713','192.168.4.112')
            print u'  相机5轮间距 标定完成! '
        elif N=='6':
            #----------轮间距标定相机标定----------------
            wheel_camera_calibration('100270925','100270925','192.168.4.112')
            print u'  相机6轮间距 标定完成! '
        elif N=='7':
            #----------轮间距标定相机标定----------------
            wheel_camera_calibration('100453594','100453594','192.168.5.113')
            print u'  相机7轮间距 标定完成! '
        elif N=='8':
            #----------轮间距标定相机标定----------------
            wheel_camera_calibration('100323320','100323320','192.168.5.113')
            print u'  相机8轮间距 标定完成! '
        elif N=='9':
            #----------轮间距标定相机标定----------------
            wheel_camera_calibration('100327878','100327878','192.168.5.113')
            print u'  相机9轮间距 标定完成! '
        elif N=='10':
            #----------轮间距标定相机标定----------------
            wheel_camera_calibration('100402546','100402546','192.168.5.113')
            print u'  相机10轮间距 标定完成! '
        elif N=='1112':
            #----------轮间距标定相机标定----------------
            wheel_camera_calibration('100361432','100384058','192.168.6.114')
            print u'  相机11轮间距 标定完成! '
        else:
            print u'  输入相机编号错误! 请重新输入!'
        i+=1
    print u'---相机标定结束!--- '
    time.sleep(3)


     

