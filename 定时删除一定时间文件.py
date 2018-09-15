#coding:gbk
import os
import time
import datetime
from threading import Timer

#��ȡ��ǰʱ���
def date():
    date = time.strftime("%Y-%m-%d %H:%M:%S")
    return date

#��ȡ�ļ��޸�ʱ���
def TimeStampToTime(timestamp):
    timeStruct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S',timeStruct)

#��ȡ3��ǰ������
def get_three_date():
    today = datetime.date.today()
    three_day_ago = today - datetime.timedelta(days=3)
    return three_day_ago

#�жϵ�ǰ�ļ��Ƿ�Ϊ3��ǰ�ļ�������ǣ���ɾ��
def del_files(file_path):
    log_file_path = 'F:\����ѧϰ'
    log_file = open(os.path.join(log_file_path , date()[:10] + ".txt"),"a")
    for root,dirs,files in os.walk(file_path):
        for name in files:
            if name[-6:] == "001.gz":
                modify_time = TimeStampToTime(os.path.getmtime(os.path.join(root,name)))
                if modify_time[:10] < str(get_three_date()):
                    os.remove(os.path.join(root,name))
                    print date() + "ɾ�����ļ���:" + os.path.join(root,name)
                    log_file.write(date() + "ɾ�����ļ���:" + os.path.join(root,name) + '\n')
                else:
                    log_file.write(date() + os.path.join(root,name) +"���ļ�������ɾ�������ļ�����޸�ʱ��Ϊ��"+ modify_time + "������ɾ��ʱ�����" + '\n')
    log_file.close()
#��ʱɾ��
def loop_del_file():
    print "��ʼɾ������ǰ����..."
    del_files(del_file_path)
    loop_time = Timer(86400,loop_del_file) #86400��λΪ��
    loop_time.start()
    print "ɾ����ɣ�"

if __name__ == "__main__":
    del_file_path = "E:\���ݲ���"
    loop_del_file()
