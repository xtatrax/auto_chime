
import os


def lib_test():
	print(__file__)
	abs_file=os.path.abspath(__file__)
	print(abs_file)
	this_file_dir = os.path.dirname(abs_file)
	print(this_file_dir)
	join_path = os.path.join(this_file_dir,"./close")
	print(join_path)
	nm_path = os.path.normpath(join_path)
	print(nm_path)