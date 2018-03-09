#!/usr/bin/env python

# ----------------------------------------------------------------------
# Copyright (c) 2016-2017, The Regents of the University of California All
# rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
# 
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
# 
#     * Redistributions in binary form must reproduce the above
#       copyright notice, this list of conditions and the following
#       disclaimer in the documentation and/or other materials provided
#       with the distribution.
# 
#     * Neither the name of The Regents of the University of California
#       nor the names of its contributors may be used to endorse or
#       promote products derived from this software without specific
#       prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL REGENTS OF THE
# UNIVERSITY OF CALIFORNIA BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS
# OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
# TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE
# USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH
# DAMAGE.
# ----------------------------------------------------------------------
# Filename: 7_run.py
# Version: 1.0
# Description: Python script to run the designs on CPU or GPU.
# Author: Quentin Gautier



import os
import re
import sys
import argparse


sys.path.append("../../common/scripts")
from runDesigns import runDesigns



def main():

    parser = argparse.ArgumentParser(description='''
    This script runs designs on CPU or GPU.
    ''',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('device', help='cpu or gpu')
    parser.add_argument('-i', '--input', help='Path to the input file to use: ', default='../graphs/large_0.01.txt')
    parser.add_argument('-a', '--process-all', help='Process all designs', default='True', action='store_true')
    parser.add_argument('-n', '--num-runs', help='Number of iterations to run')
    args = parser.parse_args()


    progInputFile = args.input
    if progInputFile:
        progInputFile = os.path.abspath(progInputFile)

    process_all = args.process_all
   
    device = args.device

    num_runs = args.num_runs    

    clBasename  = "bfs_fpga" # Basename for the OpenCL file
    exeFilename = "bfs_host" # Program filename

    paramsfilename = "small.txt" if os.path.isfile("small.txt") else "params.log"

    runDesigns(
            clBasename,
            exeFilename,
            progInputFile,
            paramsfilename   = paramsfilename,
            compiledfilename = paramsfilename,
            process_all = process_all,
            num_runs = num_runs,
            device = device)





if __name__=="__main__":
	main()


