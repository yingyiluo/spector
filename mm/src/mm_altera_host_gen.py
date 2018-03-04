#!/usr/bin/python

# ----------------------------------------------------------------------
# Copyright (c) 2016, The Regents of the University of California All
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
# Filename: mm_altera_host_gen.py
# Version: 1.0
# Description: Python script to generate host programs that run the OpenCL designs.
# Author: Pingfan Meng

import numpy as np
import sys

device = "fpga"

if len(sys.argv) >= 2:
    device = sys.argv[1]
print("Using " + device + " device.")
print("( Usage: " + sys.argv[0] + " <fpga|gpu|gpu_all|cpu|cpu_all> )\n")

if device == "fpga":
    base_file_name='mm_base.cpp'
else:
    base_file_name='mm_gpu_base.cpp'   

M=1024

param_setting=[]

params = np.array(np.genfromtxt('params.csv', delimiter=','))

num_kernels = params.shape[0]
num_params = params.shape[1]
print("Total number of kernels: " + str(num_kernels))

for i in range(num_kernels):
    temp = params[i]
    blockdim = int(temp[0])
    subdim_x = int(temp[1])
    subdim_y = int(temp[2])
    simd_x = int(temp[3])
    simd_y = int(temp[4])
    simd_wi = int(temp[5])
    comp_u = int(temp[6])
    unroll_sel = int(temp[7]) + 1
    unroll_f = int(temp[8])
    #subdim_y simd_x
    if simd_y == 1 and subdim_x == 1:

        flag1=M%(blockdim*subdim_x*simd_x)
        flag2=M%(blockdim*subdim_y*simd_y)
        flag3=blockdim%simd_wi

        if unroll_sel ==1:
            flag4=blockdim%unroll_f
        else:
            flag4=subdim_y%unroll_f

        flag5=1 if unroll_f*subdim_x*subdim_y*simd_x*simd_y*simd_wi*comp_u>256 else 0
        flag6=1 if blockdim*blockdim*subdim_y*subdim_x*simd_x*simd_y>1024 else 0

        if flag1==0 and flag2==0 and flag3==0 and flag4==0 and flag5==0 and flag6==0:
            rep_flag=0
            for tmp_setting in param_setting:
                if tmp_setting==[blockdim, unroll_sel, unroll_f, subdim_x, subdim_y, simd_x, simd_y, simd_wi, comp_u]:
                    rep_flag=1

            if rep_flag==0:
                param_setting.append([blockdim, unroll_sel, unroll_f, subdim_x, subdim_y, simd_x, simd_y, simd_wi, comp_u])

                if unroll_sel==1:
                    source_file_name='mm_'+'b'+str(blockdim)+'_'+'subx'+str(subdim_x)+'_'+'suby'+str(subdim_y)+'_'+'simdx'+str(simd_x)+'_'+'simdy'+str(simd_y)+'_'+'simdwi'+str(simd_wi)+'_'+'compu'+str(comp_u)+'_'+'unrollb'+str(unroll_f)+'.cpp'

                else:
                    source_file_name='mm_'+'b'+str(blockdim)+'_'+'subx'+str(subdim_x)+'_'+'suby'+str(subdim_y)+'_'+'simdx'+str(simd_x)+'_'+'simdy'+str(simd_y)+'_'+'simdwi'+str(simd_wi)+'_'+'compu'+str(comp_u)+'_'+'unrollp'+str(unroll_f)+'.cpp'

                #base_file_name='mm_base.cpp'

                input_base_file=open(base_file_name,'r')
                output_source_file=open(source_file_name,'w') 

                source_string='#define M '+str(M)+'\n\n'

                source_string=source_string+'#define BLOCKDIM '+str(blockdim)+'\n'
                source_string=source_string+'#define SUBDIM_X '+str(subdim_x)+'\n'
                source_string=source_string+'#define SUBDIM_Y '+str(subdim_y)+'\n\n'
                source_string=source_string+'#define SIMD_X '+str(simd_x)+'\n'
                source_string=source_string+'#define SIMD_Y '+str(simd_y)+'\n\n'

                if unroll_sel==1:
                    filename_base='"mm_'+'b'+str(blockdim)+'_'+ \
                            'subx'+str(subdim_x)+'_'+'suby'+str(subdim_y)+'_'+'simdx'+str(simd_x)+'_'+ \
                            'simdy'+str(simd_y)+'_'+'simdwi'+str(simd_wi)+'_'+'compu'+str(comp_u)+'_'+'unrollb'+str(unroll_f)
                    filename_base=filename_base.strip()

                    source_string=source_string+'#define AOCX_FILE_NAME '+ filename_base + '.aocx"\n\n'

                    source_string=source_string+'#define CL_FILE_NAME '+ filename_base + '.cl"\n\n'

                    source_string=source_string+'#define print_rsl printf("dse result:\\n %d, %d, %d, %d, %d, %d, %d, %d,  %d, %f\\n",'+ \
                            str(blockdim)+','+ str(subdim_x)+','+str(subdim_y)+','+ str(simd_x)+','+ str(simd_y)+','+ str(simd_wi)+','+str(comp_u)+ \
                            ','+str(0)+','+str(unroll_f)+', ELAPSED_TIME_MS(1, 0)/NUM_ITER)\n\n'


                else:
                    filename_base='"mm_'+'b'+str(blockdim)+'_'+'subx'+str(subdim_x)+'_'+'suby'+str(subdim_y)+ \
                            '_'+'simdx'+str(simd_x)+'_'+'simdy'+str(simd_y)+'_'+'simdwi'+str(simd_wi)+'_'+'compu'+str(comp_u)+'_'+'unrollp'+str(unroll_f)
                    filename_base=filename_base.strip()

                    source_string=source_string+'#define AOCX_FILE_NAME '+filename_base+'.aocx"\n\n'
                    source_string=source_string+'#define CL_FILE_NAME '+filename_base+'.cl"\n\n'

                    source_string=source_string+'#define print_rsl printf("dse result:\\n %d, %d, %d, %d, %d, %d, %d, %d, %d, %f\\n",'+str(blockdim)+','+ \
                            str(subdim_x)+','+str(subdim_y)+','+ str(simd_x)+','+ str(simd_y)+','+ str(simd_wi)+','+str(comp_u)+','+str(1)+','+str(unroll_f)+ \
                            ', ELAPSED_TIME_MS(1, 0)/NUM_ITER)\n\n'

                tmp_string=input_base_file.readline()

                while (tmp_string!=''):
                    source_string=source_string+tmp_string
                    tmp_string=input_base_file.readline()

                input_base_file.close()
                output_source_file.write(source_string)
                output_source_file.close()


    #subdim_x simd_y
    if simd_x == 1 and subdim_y == 1:
        flag1=M%(blockdim*subdim_x*simd_x)
        flag2=M%(blockdim*subdim_y*simd_y)
        flag3=blockdim%simd_wi

        if unroll_sel ==1:
            flag4=blockdim%unroll_f
        else:
            flag4=subdim_x%unroll_f

        flag5=1 if unroll_f*subdim_x*subdim_y*simd_x*simd_y*simd_wi*comp_u>256 else 0
        flag6=1 if blockdim*blockdim*subdim_y*subdim_x*simd_x*simd_y>1024 else 0

        if flag1==0 and flag2==0 and flag3==0 and flag4==0 and flag5==0 and flag6==0:
            rep_flag=0
            for tmp_setting in param_setting:
                if tmp_setting==[blockdim, unroll_sel, unroll_f, subdim_x, subdim_y, simd_x, simd_y, simd_wi, comp_u]:
                    rep_flag=1

            if rep_flag==0:
                param_setting.append([blockdim, unroll_sel, unroll_f, subdim_x, subdim_y, simd_x, simd_y, simd_wi, comp_u])

                if unroll_sel==1:
                    source_file_name='mm_'+'b'+str(blockdim)+'_'+'subx'+str(subdim_x)+'_'+'suby'+str(subdim_y)+'_'+'simdx'+str(simd_x)+'_'+'simdy'+str(simd_y)+'_'+'simdwi'+str(simd_wi)+'_'+'compu'+str(comp_u)+'_'+'unrollb'+str(unroll_f)+'.cpp'
                else:
                    source_file_name='mm_'+'b'+str(blockdim)+'_'+'subx'+str(subdim_x)+'_'+'suby'+str(subdim_y)+'_'+'simdx'+str(simd_x)+'_'+'simdy'+str(simd_y)+'_'+'simdwi'+str(simd_wi)+'_'+'compu'+str(comp_u)+'_'+'unrollp'+str(unroll_f)+'.cpp'

                #base_file_name='mm_base.cpp'

                input_base_file=open(base_file_name,'r')
                output_source_file=open(source_file_name,'w') 

                source_string='#define M '+str(M)+'\n\n'

                source_string=source_string+'#define BLOCKDIM '+str(blockdim)+'\n'
                source_string=source_string+'#define SUBDIM_X '+str(subdim_x)+'\n'
                source_string=source_string+'#define SUBDIM_Y '+str(subdim_y)+'\n\n'
                source_string=source_string+'#define SIMD_X '+str(simd_x)+'\n'
                source_string=source_string+'#define SIMD_Y '+str(simd_y)+'\n\n'

                if unroll_sel==1:
                    source_string=source_string+'#define AOCX_FILE_NAME '+'"mm_'+'b'+str(blockdim)+'_'+'subx'+str(subdim_x)+'_'+'suby'+str(subdim_y)+'_'+'simdx'+str(simd_x)+'_'+'simdy'+str(simd_y)+'_'+'simdwi'+str(simd_wi)+'_'+'compu'+str(comp_u)+'_'+'unrollb'+str(unroll_f)+'.aocx"\n\n'
                    source_string=source_string+'#define CL_FILE_NAME '+'"mm_'+'b'+str(blockdim)+'_'+'subx'+str(subdim_x)+'_'+'suby'+str(subdim_y)+'_'+'simdx'+str(simd_x)+'_'+'simdy'+str(simd_y)+'_'+'simdwi'+str(simd_wi)+'_'+'compu'+str(comp_u)+'_'+'unrollb'+str(unroll_f)+'.cl"\n\n'                    
                    source_string=source_string+'#define print_rsl printf("dse result:\\n %d, %d, %d, %d, %d, %d, %d, %d, %d, %f\\n",'+str(blockdim)+','+ str(subdim_x)+','+str(subdim_y)+','+ str(simd_x)+','+ str(simd_y)+','+ str(simd_wi)+','+str(comp_u)+','+str(0)+','+str(unroll_f)+', ELAPSED_TIME_MS(1, 0)/NUM_ITER)\n\n'

                else:
                    source_string=source_string+'#define AOCX_FILE_NAME '+'"mm_'+'b'+str(blockdim)+'_'+'subx'+str(subdim_x)+'_'+'suby'+str(subdim_y)+'_'+'simdx'+str(simd_x)+'_'+'simdy'+str(simd_y)+'_'+'simdwi'+str(simd_wi)+'_'+'compu'+str(comp_u)+'_'+'unrollp'+str(unroll_f)+'.aocx"\n\n'
                    source_string=source_string+'#define CL_FILE_NAME '+'"mm_'+'b'+str(blockdim)+'_'+'subx'+str(subdim_x)+'_'+'suby'+str(subdim_y)+'_'+'simdx'+str(simd_x)+'_'+'simdy'+str(simd_y)+'_'+'simdwi'+str(simd_wi)+'_'+'compu'+str(comp_u)+'_'+'unrollp'+str(unroll_f)+'.cl"\n\n'
                    source_string=source_string+'#define print_rsl printf("dse result:\\n %d, %d, %d, %d, %d, %d, %d, %d, %d, %f\\n",'+str(blockdim)+','+ str(subdim_x)+','+str(subdim_y)+','+ str(simd_x)+','+ str(simd_y)+','+ str(simd_wi)+','+str(comp_u)+','+str(1)+','+str(unroll_f)+', ELAPSED_TIME_MS(1, 0)/NUM_ITER)\n\n'


                tmp_string=input_base_file.readline()

                while (tmp_string!=''):
                    source_string=source_string+tmp_string
                    tmp_string=input_base_file.readline()

                input_base_file.close()
                output_source_file.write(source_string)
                output_source_file.close()
