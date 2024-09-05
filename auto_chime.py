# -*- coding: utf-8 -*-

############################################################
# file : auto_chime.py
# 制作 ： tatra 2024年9月5日
# 
# 自動チャイム
#
# 対象バージョン : python 3.x 
# 外部モジュール :
#
# メモ :
############################################################

import os
import json
import time
import argparse


#parser = argparse.ArgumentParser(description=u'自動チャイムプログラム') #
dbg_val_tmpDir = os.path.dirname(__file__)
os.makedirs(dbg_val_tmpDir, exist_ok=True)
dbg_var_schedule_json_path = dbg_val_tmpDir + "schedule.json"

def main():
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()