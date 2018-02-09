#!/bin/bash

ts=$(date +%F-%H-%M)
echo $ts
design_name=mm_b16_subx1_suby1_simdx1_simdy1_simdwi8_compu1_unrollb16
source_file_name="$design_name"".cl"
folder_rpt_name="$design_name""_report"
if [ ! -f ./$folder_rpt_name/quartus_sh_compile.log ]
then
   time aoc --board p385a_sch_ax115 $source_file_name

   mkdir $folder_rpt_name
   cp $design_name/*.txt $folder_rpt_name
   cp $design_name/*.log $folder_rpt_name

   rm -r $design_name
fi

design_name=mm_b16_subx1_suby2_simdx1_simdy1_simdwi2_compu4_unrollp2
source_file_name="$design_name"".cl"
folder_rpt_name="$design_name""_report"
if [ ! -f ./$folder_rpt_name/quartus_sh_compile.log ]
then
   time aoc --board p385a_sch_ax115 $source_file_name

   mkdir $folder_rpt_name
   cp $design_name/*.txt $folder_rpt_name
   cp $design_name/*.log $folder_rpt_name

   rm -r $design_name
fi

design_name=mm_b2_subx1_suby2_simdx1_simdy1_simdwi2_compu1_unrollp2
source_file_name="$design_name"".cl"
folder_rpt_name="$design_name""_report"
if [ ! -f ./$folder_rpt_name/quartus_sh_compile.log ]
then
   time aoc --board p385a_sch_ax115 $source_file_name

   mkdir $folder_rpt_name
   cp $design_name/*.txt $folder_rpt_name
   cp $design_name/*.log $folder_rpt_name

   rm -r $design_name
fi

design_name=mm_b2_subx1_suby4_simdx1_simdy1_simdwi1_compu1_unrollb2
source_file_name="$design_name"".cl"
folder_rpt_name="$design_name""_report"
if [ ! -f ./$folder_rpt_name/quartus_sh_compile.log ]
then
   time aoc --board p385a_sch_ax115 $source_file_name

   mkdir $folder_rpt_name
   cp $design_name/*.txt $folder_rpt_name
   cp $design_name/*.log $folder_rpt_name

   rm -r $design_name
fi

design_name=mm_b32_subx1_suby1_simdx1_simdy1_simdwi8_compu1_unrollb16
source_file_name="$design_name"".cl"
folder_rpt_name="$design_name""_report"
if [ ! -f ./$folder_rpt_name/quartus_sh_compile.log ]
then
   time aoc --board p385a_sch_ax115 $source_file_name

   mkdir $folder_rpt_name
   cp $design_name/*.txt $folder_rpt_name
   cp $design_name/*.log $folder_rpt_name

   rm -r $design_name
fi

design_name=mm_b4_subx1_suby4_simdx4_simdy1_simdwi1_compu2_unrollb2
source_file_name="$design_name"".cl"
folder_rpt_name="$design_name""_report"
if [ ! -f ./$folder_rpt_name/quartus_sh_compile.log ]
then
   time aoc --board p385a_sch_ax115 $source_file_name

   mkdir $folder_rpt_name
   cp $design_name/*.txt $folder_rpt_name
   cp $design_name/*.log $folder_rpt_name

   rm -r $design_name
fi

design_name=mm_b4_subx1_suby8_simdx1_simdy1_simdwi1_compu1_unrollb2
source_file_name="$design_name"".cl"
folder_rpt_name="$design_name""_report"
if [ ! -f ./$folder_rpt_name/quartus_sh_compile.log ]
then
   time aoc --board p385a_sch_ax115 $source_file_name

   mkdir $folder_rpt_name
   cp $design_name/*.txt $folder_rpt_name
   cp $design_name/*.log $folder_rpt_name

   rm -r $design_name
fi

design_name=mm_b4_subx1_suby8_simdx1_simdy1_simdwi1_compu1_unrollb4
source_file_name="$design_name"".cl"
folder_rpt_name="$design_name""_report"
if [ ! -f ./$folder_rpt_name/quartus_sh_compile.log ]
then
   time aoc --board p385a_sch_ax115 $source_file_name

   mkdir $folder_rpt_name
   cp $design_name/*.txt $folder_rpt_name
   cp $design_name/*.log $folder_rpt_name

   rm -r $design_name
fi

design_name=mm_b4_subx2_suby1_simdx1_simdy4_simdwi2_compu1_unrollp2
source_file_name="$design_name"".cl"
folder_rpt_name="$design_name""_report"
if [ ! -f ./$folder_rpt_name/quartus_sh_compile.log ]
then
   time aoc --board p385a_sch_ax115 $source_file_name

   mkdir $folder_rpt_name
   cp $design_name/*.txt $folder_rpt_name
   cp $design_name/*.log $folder_rpt_name

   rm -r $design_name
fi

design_name=mm_b8_subx1_suby1_simdx1_simdy1_simdwi1_compu2_unrollb8
source_file_name="$design_name"".cl"
folder_rpt_name="$design_name""_report"
if [ ! -f ./$folder_rpt_name/quartus_sh_compile.log ]
then
   time aoc --board p385a_sch_ax115 $source_file_name

   mkdir $folder_rpt_name
   cp $design_name/*.txt $folder_rpt_name
   cp $design_name/*.log $folder_rpt_name

   rm -r $design_name
fi

design_name=mm_b8_subx1_suby1_simdx1_simdy4_simdwi1_compu1_unrollb2
source_file_name="$design_name"".cl"
folder_rpt_name="$design_name""_report"
if [ ! -f ./$folder_rpt_name/quartus_sh_compile.log ]
then
   time aoc --board p385a_sch_ax115 $source_file_name

   mkdir $folder_rpt_name
   cp $design_name/*.txt $folder_rpt_name
   cp $design_name/*.log $folder_rpt_name

   rm -r $design_name
fi

design_name=mm_b8_subx1_suby1_simdx2_simdy1_simdwi1_compu1_unrollb2
source_file_name="$design_name"".cl"
folder_rpt_name="$design_name""_report"
if [ ! -f ./$folder_rpt_name/quartus_sh_compile.log ]
then
   time aoc --board p385a_sch_ax115 $source_file_name

   mkdir $folder_rpt_name
   cp $design_name/*.txt $folder_rpt_name
   cp $design_name/*.log $folder_rpt_name

   rm -r $design_name
fi

design_name=mm_b8_subx1_suby1_simdx4_simdy1_simdwi2_compu1_unrollb4
source_file_name="$design_name"".cl"
folder_rpt_name="$design_name""_report"
if [ ! -f ./$folder_rpt_name/quartus_sh_compile.log ]
then
   time aoc --board p385a_sch_ax115 $source_file_name

   mkdir $folder_rpt_name
   cp $design_name/*.txt $folder_rpt_name
   cp $design_name/*.log $folder_rpt_name

   rm -r $design_name
fi

design_name=mm_b8_subx1_suby1_simdx8_simdy1_simdwi1_compu4_unrollb2
source_file_name="$design_name"".cl"
folder_rpt_name="$design_name""_report"
if [ ! -f ./$folder_rpt_name/quartus_sh_compile.log ]
then
   time aoc --board p385a_sch_ax115 $source_file_name

   mkdir $folder_rpt_name
   cp $design_name/*.txt $folder_rpt_name
   cp $design_name/*.log $folder_rpt_name

   rm -r $design_name
fi

design_name=mm_b8_subx1_suby2_simdx2_simdy1_simdwi2_compu4_unrollp2
source_file_name="$design_name"".cl"
folder_rpt_name="$design_name""_report"
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

design_name=mm_b8_subx1_suby4_simdx1_simdy1_simdwi8_compu1_unrollb4
design_name=mm_b8_subx1_suby4_simdx1_simdy1_simdwi8_compu1_unrollp4
design_name=mm_b8_subx1_suby4_simdx2_simdy1_simdwi1_compu1_unrollb4
design_name=mm_b8_subx1_suby8_simdx2_simdy1_simdwi1_compu2_unrollp4
design_name=mm_b8_subx2_suby1_simdx1_simdy1_simdwi2_compu1_unrollb8
design_name=mm_b8_subx2_suby1_simdx1_simdy2_simdwi1_compu1_unrollb2
design_name=mm_b8_subx8_suby1_simdx1_simdy1_simdwi2_compu1_unrollb8
