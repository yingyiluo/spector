#!/bin/bash

ts=$(date +%F-%H-%M)
echo $ts

design_name=dct_bx32_by32_simdType0_simdLoc1_blockSizeF1_blockU0_DCTU0_simdwi1_compu1
source_file_name="$design_name"".cl"
folder_rpt_name="$design_name""_rpt_name"
if [ ! -f ./$folder_rpt_name/quartus_sh_compile.log ]
then
	time aoc --board p385a_sch_ax115 $source_file_name
	mkdir $folder_rpt_name
	cp $design_name/*.txt $folder_rpt_name
	cp $design_name/*.log $folder_rpt_name
	rm -r $design_name
fi

design_name=dct_bx32_by32_simdType0_simdLoc1_blockSizeF1_blockU0_DCTU0_simdwi4_compu2
source_file_name="$design_name"".cl"
folder_rpt_name="$design_name""_rpt_name"
if [ ! -f ./$folder_rpt_name/quartus_sh_compile.log ]
then
	time aoc --board p385a_sch_ax115 $source_file_name
	mkdir $folder_rpt_name
	cp $design_name/*.txt $folder_rpt_name
	cp $design_name/*.log $folder_rpt_name
	rm -r $design_name
fi

design_name=dct_bx32_by32_simdType1_simdLoc2_blockSizeF1_blockU0_DCTU0_simdwi2_compu1
source_file_name="$design_name"".cl"
folder_rpt_name="$design_name""_rpt_name"
if [ ! -f ./$folder_rpt_name/quartus_sh_compile.log ]
then
	time aoc --board p385a_sch_ax115 $source_file_name
	mkdir $folder_rpt_name
	cp $design_name/*.txt $folder_rpt_name
	cp $design_name/*.log $folder_rpt_name
	rm -r $design_name
fi

design_name=dct_bx32_by32_simdType1_simdLoc2_blockSizeF1_blockU0_DCTU1_simdwi1_compu1
source_file_name="$design_name"".cl"
folder_rpt_name="$design_name""_rpt_name"
if [ ! -f ./$folder_rpt_name/quartus_sh_compile.log ]
then
	time aoc --board p385a_sch_ax115 $source_file_name
	mkdir $folder_rpt_name
	cp $design_name/*.txt $folder_rpt_name
	cp $design_name/*.log $folder_rpt_name
	rm -r $design_name
fi

design_name=dct_bx32_by64_simdType0_simdLoc1_blockSizeF1_blockU0_DCTU0_simdwi2_compu2
source_file_name="$design_name"".cl"
folder_rpt_name="$design_name""_rpt_name"
if [ ! -f ./$folder_rpt_name/quartus_sh_compile.log ]
then
	time aoc --board p385a_sch_ax115 $source_file_name
	mkdir $folder_rpt_name
	cp $design_name/*.txt $folder_rpt_name
	cp $design_name/*.log $folder_rpt_name
	rm -r $design_name
fi

design_name=dct_bx32_by64_simdType0_simdLoc1_blockSizeF2_blockU0_DCTU0_simdwi2_compu2
source_file_name="$design_name"".cl"
folder_rpt_name="$design_name""_rpt_name"
if [ ! -f ./$folder_rpt_name/quartus_sh_compile.log ]
then
	time aoc --board p385a_sch_ax115 $source_file_name
	mkdir $folder_rpt_name
	cp $design_name/*.txt $folder_rpt_name
	cp $design_name/*.log $folder_rpt_name
	rm -r $design_name
fi

design_name=dct_bx64_by16_simdType0_simdLoc1_blockSizeF1_blockU0_DCTU1_simdwi1_compu1
source_file_name="$design_name"".cl"
folder_rpt_name="$design_name""_rpt_name"
if [ ! -f ./$folder_rpt_name/quartus_sh_compile.log ]
then
	time aoc --board p385a_sch_ax115 $source_file_name
	mkdir $folder_rpt_name
	cp $design_name/*.txt $folder_rpt_name
	cp $design_name/*.log $folder_rpt_name
	rm -r $design_name
fi

ts=$(date +%F-%H-%M)
echo $ts
exit 0

design_name=dct_bx64_by16_simdType0_simdLoc1_blockSizeF2_blockU0_DCTU0_simdwi1_compu1
design_name=dct_bx64_by32_simdType0_simdLoc2_blockSizeF1_blockU0_DCTU0_simdwi2_compu2
design_name=dct_bx8_by32_simdType1_simdLoc2_blockSizeF1_blockU0_DCTU0_simdwi2_compu1
design_name=dct_bx8_by8_simdType0_simdLoc2_blockSizeF1_blockU0_DCTU0_simdwi1_compu1
design_name=dct_bx8_by8_simdType0_simdLoc2_blockSizeF1_blockU0_DCTU0_simdwi2_compu2
