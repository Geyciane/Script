#!/usr/bin/env python
# -*- coding: utf-8 -*-

###############################################################################
# título		: monitor_cpu.py 								              
# descrição		: monitora a porcentagem de consumo de cpu de cada IDS	      
# autor			: Geyciane Tavares Jorge <geycianetj@gmail.com> 	          
# notas			: instalar o pacote python-psutil 					          
###############################################################################


import os
import sys
import psutil
import time

while True:
    for id in psutil.pids():
        p = psutil.Process(id)
        if (p.name() == 'Nome_IDS'):
            time.sleep(10)
            mem = p.memory_percent()
            arq = open("IDS.txt", "a")
            arq.write(str(mem) + "\n")