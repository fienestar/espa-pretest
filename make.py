# -*- coding: utf-8 -*
import os
import time

file_list = [file.split('.') for file in os.listdir('.')]

input_files = []

tc_count = 0
for file in file_list:
    if file[-1] == 'inp' and '1' <= file[0][0] <= '9':
        tc_count = max(tc_count, int(file[0]))

def get_input(text):
    result = []
    result.append(input(text))
    while True:
        t = input('>> ')
        if len(t) == 0:
            break
        result.append(t)
    return '\n'.join(result)

def write(filename,text):
    with open(filename, mode='w') as file:
        file.write(text)

print('이미 저장된 테스트 케이스: '+str(tc_count)+'개')

try:
    while True:
        tc_count+=1
        print('='*15)
        inp = get_input('input[' + str(tc_count) + ']: ')
        out = get_input('output[' + str(tc_count) + ']: ')
        write(str(tc_count)+'.inp',inp)
        write(str(tc_count)+'.out',out)

except KeyboardInterrupt:
    print('\n\n총 테스트 케이스: '+str(tc_count-1)+'개')
