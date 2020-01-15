import re
from netaddr import *

def combine_ips(ips):
  # convert to binary
  # compare higher bits to see if they can be combined
  # compare lower bits and check to see if they are enough 
  #   contiguous ips to fill the next level out
  # If so, merge them. If not, keep them seperate
  return cidr_merge(ips)

def convert_line(line):
  ips = line.split(',')
  if len(ips) < 2: return ';'.join(ips)
  verified = []
  invalid = []
  for ip in ips:
    if re.match(r"^[1-2]{0,1}[1-9]{1,2}\.[1-2]{0,1}[0-9]{1,2}\.[1-2]{0,1}[0-9]{1,2}\.[1-2]{0,1}[0-9]{1,2}\/?[0-9.]{0,15}$", ip):
      verified.append(ip)
    else:
      invalid.append(ip)
  results = verified
  if len(verified) >= 2:
      results = combine_ips(verified)
  if len(invalid) > 0:
      results.extend(invalid)
  return ';'.join([str(ip) for ip in results])

def convert_file(input_filename, output_filename):
  inputfile = open(input_filename, "r")
  outputfile = open(output_filename, "w+")
  lines = list()

  if inputfile.mode == 'r':
    contents = inputfile.readlines()
    for line in contents:
      lineid, ips = line.split(':')
      outputfile.write(",".join([lineid,convert_line(ips)]))

if __name__ == '__main__':
  convert_file('coalesce_input.csv', 'output.csv')
