#!/usr/bin/python3
import json
import sys
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

liszt = sys.argv[1:]
filename = "add_item.json"
save_to_json_file(liszt, filename)
my_list = load_from_json_file(filename)
