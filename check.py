# -*- coding: utf-8 -*
import os
import shutil
import time

file_list = [file.split('.') for file in os.listdir('.')]

input_files = []
source_file = ""
problem_name = ""
for file in file_list:
    if file[-1] == 'py' and file[0] != 'check'  and file[0] != 'make':
        source_file = '.'.join(file)
        problem_name = file[0]
        print('문제: '+problem_name)
        break

tc_count = 0
for file in file_list:
    if file[-1] == 'inp' and file[0] != problem_name:
        tc_count = max(tc_count, int(file[0]))

print('인풋: '+str(tc_count)+'개')

def read_all(filename):
    file = open(filename, mode='r', encoding='utf-8')
    result = file.read()
    file.close()
    return result.strip()

def compare_file(file1,file2):
    return read_all(file1) == read_all(file2)

max_running_time = 0
max_running_time_file = ""
error_count = 0
for i in range(1,tc_count+1):
    shutil.copy2(str(i)+'.inp',problem_name+'.inp')
    time_start = time.time()
    os.system("python " + source_file)
    running_time = time.time() - time_start

    if max_running_time < running_time:
        max_running_time = running_time
        max_running_time_file = i

    if not compare_file(problem_name+'.out', str(i)+'.out'):
        error_count+=1
        print('='*15)
        print('TC['+str(i)+']')
        print('input:')
        print(' '*4 + ('\n'+' '*4).join(read_all(str(i)+'.inp').split('\n')))
        print('expected:')
        print(' '*4 + ('\n'+' '*4).join(read_all(str(i)+'.out').split('\n')))
        print('output:')
        print(' '*4 + ('\n'+' '*4).join(read_all(problem_name+'.out').split('\n')))

print('='*15)
print('틀린 개수: '+str(error_count))
print('실행 시간: '+str(max_running_time)+'s')
print('느렸던 입력: '+str(max_running_time_file)+'.inp')
