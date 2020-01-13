import re
from netaddr import *

def combine_ips(ips):
  # convert to binary
  # compare to get the lowest amount of subnets
  merged_ips = cidr_merge(ips)
  return ';'.join([str(ip) for ip in merged_ips])

def convert_line(line):
  ips = line.split(',')
  if len(ips) == 1 or len(ips) == 0: return ';'.join(ips)
  verified = []
  invalid = []
  for ip in ips:
    if re.match(r"^[1-2]{0,1}[1-9]{1,2}\.[1-2]{0,1}[0-9]{1,2}\.[1-2]{0,1}[0-9]{1,2}\.[1-2]{0,1}[0-9]{1,2}\/?[0-9.]{0,15}$", ip):
      verified.append(ip)
    else:
      invalid.append(ip)
  return combine_ips(verified) + ';'.join(invalid)

def convert_file(input_filename, output_filename):
  inputfile = open(input_filename, "r")
  outputfile = open(output_filename, "w+")

  if inputfile.mode == 'r':
    contents = inputfile.readlines()
    for line in contents:
      lineid, ips = line.split(':')
      outputfile.write(",".join([lineid,convert_line(ips)]))

if __name__ == '__main__':
  convert_file('coalesce_input.csv', 'output.csv')
