#name: trim_sequences.py

#author: your name here

#date: 21/11/2022

#description: script to run parse_dna.py using data_input.txt & cut-off value

​

#import modules

import os

import subprocess

​

#set up variables

program = 'parse_dna.py'

parameter1 = 'data_input.txt'

parameter2 = 20

​

if os.path.exists(parameter1):

      command = 'python' + ' ' + program + ' ' + parameter1 + ' ' + str(parameter2)

      subprocess.call(command, shell= True)

      print ('Script completed')

else:

   print ('File', parameter1,'missing.')
