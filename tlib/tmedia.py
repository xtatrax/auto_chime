
import shutil
import subprocess


if shutil.which("ffmpeg") is None:
	COM_EX_FFMPEG = False
else:
	COM_EX_FFMPEG = True
	from . import ffmedia

class tMediaPlayer():
	"""
	個人的にマルチメディアを使いやすくする感じのやつ
	"""
	def __init__(self,
			data,
			is_loop:bool=False,
			is_pick_one:bool=False,
			is_random:bool=False,

			):
		"""
		data		-> 扱いたいデータ
		loop		-> ( bool型 デフォルト値=False data がリストの場合のみ有効 ) ループ
		pick_one	-> ( bool型 デフォルト値=False data がリストの場合のみ有効 ) リストから一つだけデータをピックアプ random=True と組み合わせすると良き
		random		-> ( bool型 デフォルト値=False data がリストの場合のみ有効 ) ランダム
		"""
		self.data=data
		self.is_loop=is_loop
		self.is_pick_one=is_pick_one
		self.is_random=is_random
	
