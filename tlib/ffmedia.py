# -*- coding: utf-8 -*-

############################################################
# file : ffmedia.py
# 制作 ： tatra 2024年9月8日
# 
# ffmpeg Wrapper
#
# 対象バージョン : python 3.x 
# 外部モジュール :
#
# 外部ソフト :
#	ffmpeg
# メモ :
#
#
#
#	ffmpeg -stream_loop -1 -i "path" -f alsa hw:card Num,device Num
############################################################

import os
import sys
import platform
import subprocess


import debug_print

debug_print.is_debug_print = True
debug_print.debug_print("debug")
"""
	共通
"""
class ffmedia_base():
	# 共通コマンド
	bace_command = ["ffmpeg", "-stream_loop", "-1", "-i"]
	def __init__(self):
		dummy=0

	#
	def play(self, path, exOption=[]):
		command = self.bace_command
		command.append(path)
		command += exOption
		debug_print.debug_print(" cmmand = " + command)
		# プレイヤーを立ち上げて ffprocess へ パイプ を保存
		self.ffprocess = subprocess.Popen(
			command,
			stdin=subprocess.PIPE,
			stdout=subprocess.PIPE,
			stderr=subprocess.PIPE
		)

	# 再生停止
	def stop(self):
		# 停止コマンド送信
		self.ffprocess.stdin.write("q")

	# 強制停止
	def kill(self):
		self.ffprocess.kill()

"""
	windows用
"""
class windows(ffmedia_base):
	def __init__(self):
		dummy=0
	#再生
	def play(self, path):
		super().play(path,[
			"-f", "matroska",
			"-map", "0:a",
			"-c", "copy", 
			"-",
			"|",
			"ffplay.exe", "-nodisp",
			"-i", "-"
		])

"""
	linux用
"""
class linux(ffmedia_base):
	def __init__(self):
		dummy=0

	#
	def play(self, path):
		super().play(path)

	#
	def select_device(self,
					select_sound_device="",
					high_priority_sound_device="",
					select_GPU="",
					high_priority_GPU=""):
		res = subprocess.run(["aplay", "-l", "|", "grep", "card"], capture_output=True)
		res_list = res.stdout.split('\n')
		
"""
	ffmpegを個人的に使いやすくするためのあれこれ
"""
class ffmedia():
	#
	def __init__(self):
		self.platform = platform.system()
		#
		if(self.platform == "Windows"):
			self.env_wrap = windows()
		#
		elif(self.platform == "Linux"):
			self.env_wrap = linux()
		#
		#elif(self.platform == "Darwin")
		#
		else:
			#
			raise Exception("未対応のOSです")
	#
	def play(self,path):
		self.env_wrap.play(path)
	#
	def stop(self):
		self.env_wrap.stop()
	#
	def select_device(self,
				select_sound_device="",
				high_priority_sound_device="",
				select_GPU="",
				high_priority_GPU=""):
		self.env_wrap.select_device(
				select_sound_device,
				high_priority_sound_device,
				select_GPU,
				high_priority_GPU)

