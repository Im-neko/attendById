# -*- coding:utf8 -*-
import time
import random
from datetime import datetime
import nfc
from binascii import hexlify

from play import *

dedenflag = True
soundsflag = True

date = datetime.now()
csv_name = 'attend'+date.strftime('%m-%d')
path = 'csvs/'+csv_name+'.csv'

now_time = date.strftime('%m/%d %H:%M:%s')

def on_connect(tag):
    try:
        flag = True
        idm, pmm = tag.polling(system_code=0x85d1)
        tag.idm, tag.pmm, tag.sys = idm, pmm, 0x85d1

        sc = nfc.tag.tt3.ServiceCode(68, 0x0b)
        bc = nfc.tag.tt3.BlockCode(1, service=0)
        data = tag.read_without_encryption([sc], [bc])
        print '>>> ', data[:8]
        try:
            with open(path, 'a') as f:
                f.write(data[:8]+'\n')
            if random.randrange(100) <= 4:
                sugoi()
            else:
                pinpon()
            print('>>> OK')
        except Exception as e:
            bubu()
            print('>>> error')
            print('>>> ', e)
    except Exception as e:
        print('>>> ', e)
        bubu()

def released(tag):
    flag = False
    print("released:")
    if tag.ndef:
        print(tag.ndef.message.pretty())

def main():
    with nfc.ContactlessFrontend('usb') as clf:
        clf.connect(rdwr={
            'on-connect': on_connect,
            # 'on-release': released,
            })


if __name__ == '__main__':
    flag = False

    with open(path, 'w') as f:
        f.write(now_time+'num\n')
    while True:
        input = raw_input('>>> ')
        if input != 'z':
            print('>>> ready')
            if dedenflag:
                deden()
            main()
        else:
            print('>>> exit')
            break

