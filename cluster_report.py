#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20  2020

@author: devyne
"""


import yaml
from __future__ import print_function


with open('example-inventory.yaml', 'r') as fh:
  data = yaml.load(fh, Loader=yaml.FullLoader)

  def get_hostname():

    for host in data['all']['children']['compute']['hosts']:
      return host

  def get_gpus('hostname'):
    for mach_class in data['all']['var']['machine_class']:
      if mach_class == data['all']['children']['compute']['hosts'][hostname]['mclass']:
        gpus = data['all']['var']['machine_class'][mach_class]['gres'].split(':')[2]
        gpu_type = data['all']['var']['machine_class'][mach_class]['gres'].split(':')[1]
        ram = data['all']['var']['machine_class'][mach_class]['realmemory']
        cpus = data['all']['var']['machine_class'][mach_class]['cpus']
        cpu_type = data['all']['var']['machine_class'][mach_class]['cpu']
        sockets = data['all']['var']['machine_class'][mach_class]['sockets']

        return [gpus, gpu_type, ram, cpus, cpu_type, sockets]

  print('hostname  #GPUs  gpu_type  RAM  #CPUs  cpu_type  #Sockets')
  print('\n')
  for node in get_hostname():
    res = get_gpus(node)
    print('{} {} {} {} {} {} {}'.format(node, res[0], res[1], res[2], res[3], res[5] ))
