#coding=utf-8
import os, sys, platform

os.system('rm -rf TALKL.so TALKL32.so')

try:
    if sys.argv[1]=='update':
        os.system('rm -rf TALKL.so TALKL32.so')
except:
    pass


bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('TALKL.so'):
        os.system('curl -L https://github.com/mohaghhjj/TALKL.git TALKL.so') 
        import TALKL
    else:
        import TALKL

elif bit == '32bit':
    if not os.path.isfile('TALKL32.so'):
        os.system('curl -L https://github.com/mohaghhjj/TALKL.git TALKL32.so') 
        import TALKL32
    else:
        import TALKL32
