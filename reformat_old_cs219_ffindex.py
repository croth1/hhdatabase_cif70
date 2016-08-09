#!/usr/bin/env python

import ffindex
import sys

def main():
	input_database_basename = sys.argv[1]
	output_database_basename = sys.argv[2]

	input_data = ffindex.read_data(input_database_basename+".ffdata")
	input_index = ffindex.read_index(input_database_basename+".ffindex")

	fh = open(output_database_basename+".cs219", "wb")

	total_length = 0
	nr_sequences = len(input_index)

	for entry in input_index:
		entry_data = ffindex.read_entry_data(entry, input_data)
		entry_data = entry_data[2:]
		total_length += len(entry_data)
		fh.write(bytearray(">"+entry.name+"\n", "utf-8"))
		fh.write(entry_data)
		
	fh.close()

	fh = open(output_database_basename+".cs219.sizes", "w")
	fh.write(str(nr_sequences) + " " + str(total_length))
	fh.close()

main()
