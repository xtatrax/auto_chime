
import os


def check_quotation(path,quotation='"'):
	if path[0] != quotation:
		if path[0] == "'":
			path[0] = quotation 
		if path[-1] == "'":
			path[-1] = quotation 
			


"""
	args 			: path
	is_quotation	: quotation で指定した文字で囲む : default = True
	quotation		: default = '"'
"""
def proofreading(*args,sep="/",is_quotation:bool=True,quotation='"') -> str:
	p_path = sep.join(args)


def get_dir(in_base_path,*args,sep="/") -> str:
	if os.path.exists(in_base_path):
		if os.path.isfile(in_base_path):
			d_path = os.path.dirname(in_base_path)
		elif os.path.isdir(in_base_path):
			d_path = in_base_path

	p_path = sep.join(args)
	j_path = os.path.join(d_path,p_path)
	ret_path = os.path.normpath( j_path )
	return ret_path
