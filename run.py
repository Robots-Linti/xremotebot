#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from os.path import exists, join, dirname, realpath
import os
import time
import xremotebot.configuration as conf
from util import run, runbg

PWD=realpath(dirname(__file__))
os.chdir(PWD)

venvpy = join(PWD, 'bin', 'python')


def kill_old_daemons():
    for pidfile in ('node.pid', 'avconv.pid'):
        if exists(pidfile):
            with open(pidfile) as f:
                try:
                    os.kill(int(f.read()), 9)
                except OSError:
                    pass
            os.unlink(pidfile)

kill_old_daemons()

if not exists('test.db'):
    print('Creando la base de datos')
    run(venvpy, 'deploy_db.py')

print('Creando dispositivos rfcomm para los robots scribbler')
print('Se requiere la contraseña de root para continuar')
run('su', '-c', ' '.join((venvpy, 'reconnect_myro.py')), stdout=None, stderr=None)

print('Iniciando streaming de video')
node = runbg('node', 'streaming/stream-server.js', 'jiji')
with open('node.pid', 'w') as f:
    f.write(str(node.pid))

print('Esperando a que el servicio de streaming aranque')
time.sleep(1)
avconv = runbg('avconv', '-s', '640x480', '-f', 'video4linux2', '-i', 
               '/dev/video0', '-f', 'mpeg1video', '-b', '800k', '-r',
               '30', 'http://localhost:8082/jiji/640/480/', '-v', 'quiet')
with open('avconv.pid', 'w') as f:
    f.write(str(avconv.pid))

try:
    run(venvpy, 'app.py', stdout=None, stderr=None)
except KeyboardInterrupt:
    pass
finally:
    kill_old_daemons()