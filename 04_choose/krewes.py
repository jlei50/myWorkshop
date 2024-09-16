# Jady Lei
# 45
# SoftDev
# K04 -- Python Dictionaries
# 2024-09-16
# time spent:
# DISCO: random has a bunch of functions that can be used to generate random stuff
# QCC: Saw code using "from random import random" which does not work. Whats the difference?
# OPS SUMMARY: random.randint() can return a random integer from a range, inclusive

import random

krewes = {
           4: [ 
		'DUA','TAWAB','EVA','JACK','VICTOR','EVAN','JASON','COLYI','IVAN','TANZEEM',
		'TAHMIM','STANLEY','LEON','NAOMI','NIA','ANASTASIA','JADY','BRIAN','JACOB',
		'ALEX','CHONGTIAN','DANNY','MARCO','ABIDUR','ANKITA','ANDY','ETHAN','AMANDA',
		'AIDAN','LINDA','QIANJUN','JIAYING','KISHI'
		],
           5: [ 
                'ADITYA','MARGIE','RACHEL','ALEXANDER','ZIYAD','DANNY','ENDRIT','CADEN',
                'VEDANT','SUHANA','KYLE','KEVIN','RAYMOND','CHRISTOPHER','JONATHAN','SASHA',
                'NAFIYU','TIM','WILL','DANIEL','BENJAMIN','CLAIRE','CHLOE','STELLA','TRACY',
                'JESSICA','JACKIE','WEN YUAN','YINWEI','TIFFANY','JAYDEN DANIEL','PRINCEDEN' 
              ]
         }

def randomStudent():
    key = random.randint(4,5)
    return krewes[key][random.randint(0, len(krewes[key]) -1)]

print(randomStudent())
