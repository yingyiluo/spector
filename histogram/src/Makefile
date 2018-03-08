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


TARGET := hist256

CC = g++

#fpga: OBJECTS = $(patsubst %.cpp, %.o, histogram.cpp main.cpp)
fpga: CFILES = main.cpp histogram.cpp $(HOME)/spector/common/src/monitor.cpp
gpu: CFILES = main.cpp histogram_gpu.cpp
HEADERS = $(wildcard *.h)


CPP_FLAGS=-std=gnu++11

ifeq ($(debug), 1)
	CPP_FLAGS=-g -O0 -fno-inline
endif


LIBS = 

fpga: INCLUDE = -I.\
                -I/usr/include/eigen3\
                -I$(HOME)/spector

gpu: INCLUDE = -I.\
               -I/usr/include/eigen3



.PHONY: all clean cpu gpu fpga


fpga: CL_INCLUDE = $(shell aocl compile-config) -I$(ALTERAOCLSDKROOT)/board/nalla_pcie/software/include
#fpga: CL_LIBS    = $(shell aocl link-config | sed 's/lterasic/laltera/g')
fpga: CL_LIBS    = $(shell aocl link-config) -lhook -lnalla_pcie_mmd

fpga: $(TARGET)

gpu: CL_INCLUDE = -I/usr/local/cuda/include
gpu: CL_LIBS    = -L/usr/local/cuda/lib64 -lOpenCL
gpu: $(TARGET)

cpu: gpu

all: fpga

#%.o: %.cpp $(HEADERS)
#	$(CC) -c $< -o $@ $(CPP_FLAGS) $(INCLUDE) $(CL_INCLUDE)

#$(TARGET): $(OBJECTS)
#	$(CC) $(CPP_FLAGS) $(OBJECTS) -Wall $(LIBS) $(CL_LIBS) -o $@
$(TARGET):
	$(CC) $(CPP_FLAGS) $(CFILES) $(CL_INCLUDE) $(INCLUDE) $(LIBS) $(CL_LIBS) -o $@


clean:
	-rm -f *.o
	-rm -f $(TARGET)

