
#!/usr/bin/env python
# -*- coding: utf-8 -*-

###############################################################################
# título		: monitor_cpu.py 								              #
# descrição		: monitora a porcentagem de consumo de cpu de cada IDS	      #
# autor			: Geyciane Tavares Jorge <geycianetj@gmail.com> 	          #
# notas			: instalar o pacote python-psutil 					          #
###############################################################################

import os
import sys
import psutil
import time

while True:
    for id in psutil.pids():
        p = psutil.Process(id)
        if (p.name() == 'Nome_Processo'):
            cpu = p.cpu_percent(interval=10)
            arq = open("cpu.txt", "a")
            arq.write(str(cpu) + "\n")