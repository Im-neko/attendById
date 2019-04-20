# -*- coding:utf8 -*-
import random
import os
from datetime import datetime

import nfc

import play

dedenflag = True
soundsflag = True

date = datetime.now()
csv_name = 'attend-'+date.strftime('%m%d%H%M')
path = 'csvs/'+csv_name+'.csv'


def on_connect(tag):
    try:
        idm, pmm = tag.polling(system_code=0x85d1)
        tag.idm, tag.pmm, tag.sys = idm, pmm, 0x85d1

        sc = nfc.tag.tt3.ServiceCode(68, 0x0b)
        bc = nfc.tag.tt3.BlockCode(1, service=0)
        data = tag.read_without_encryption([sc], [bc])
        print '>>> ', data[:8]
        try:
            touch_time = datetime.now().strftime('%H:%M:%S')
            with open(path, 'a') as f:
                f.write(touch_time+', '+data[:8]+'\n')
            if random.randrange(100) <= 4:
                play.sugoi()
            else:
                play.pinpon()
            print('>>> OK')
        except Exception as e:
            play.bubu()
            print('>>> error')
            print('>>> ', e)
    except Exception as e:
        print('>>> ', e)
        play.bubu()


def released(tag):
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
    if not os.path.exists('csvs'):
        print('create csv folder')
        os.makedirs('csvs')
    if not os.path.exists(path):
        print('make new csv file')
        with open(path, 'w') as f:
            f.write('touch_time, num\n')

    while True:
        input = raw_input('>>> ')
        if input != 'exit':
            print('>>> ready')
            if dedenflag:
                play.deden()
            main()
        else:
            print('>>> exit')
            break
