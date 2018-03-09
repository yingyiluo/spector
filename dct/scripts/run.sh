M=1024

num_design=0
num_iters=$1
#echo "" > run_results.txt

i=1
cat dct_params.csv | while IFS=',' read -r blockdim_x blockdim_y simd_type simd_loc block_size_f block_unroll dct_unroll simd_wi comp_u || [ -n "$blockdim_x" ]
do
	echo $i
        comp_u=$(echo "$comp_u" | tr -d '\r')
	HOST_CODE_FILE_NAME="dct_bx""$blockdim_x""_by""$blockdim_y""_simdType""$simd_type""_simdLoc""$simd_loc""_blockSizeF""$block_size_f""_blockU""$block_unroll""_DCTU""$dct_unroll""_simdwi""$simd_wi""_compu""$comp_u"
	echo $HOST_CODE_FILE_NAME
	export MYOPENCL_HOST_CODE_FILE_NAME=$HOST_CODE_FILE_NAME

	#aocx_file_name=""
	aocx_file_name=$HOST_CODE_FILE_NAME
	aocx_file_name="$aocx_file_name"".aocx"
	echo $aocx_file_name
	if [ -f ./$aocx_file_name ]
	then
#		echo "enter if, found aocx file"
		host_program_name=""
		host_program_name+=$HOST_CODE_FILE_NAME
		host_program_name+="_host"
		num_design=$(($num_design+1))
		echo "design number:" > "run_results_""$i".txt
		echo $num_design > "run_results_""$i".txt
		echo $host_program_name > "run_results_""$i".txt
		make fpga
		#run host program
#		aocl program acl0 $aocx_file_name
		./$host_program_name fpga $num_iters > "run_results_""$i".txt
		i=$(($i+1))
	fi
	sleep 120s
done
