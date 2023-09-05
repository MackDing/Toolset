#!/bin/bash

beijing_time=$(TZ='Asia/Shanghai' date "+%Y_%m_%d-%H_%M_%S")
# Specify the input directory containing the dataset files
input_dir="./dataset"
# Specify the output directory
output_dir="./output"
# Define the variable for the -a parameter
a_param='{"polygon_1":["POLYGON((0.6060606060606061 0.45,0.6727272727272727 0.475,0.43333333333333335 0.9875,0.004545454545454545 0.995,0.004545454545454545 0.9575))"],"use_background_modelling":true,"use_person_detection":false,"use_segment_detection":false,"use_segment_for_box_output":[false,false,false,false,false,false,false,false,false]}'

# Iterate over files in the input directory
for file in "$input_dir"/*
do
    if [ -f "$file" ]; then
        # Extract the filename (without the path)
        filename=$(basename "$file")
        
        # Define the command to process a single file with the -a parameter as a variable
        command="/usr/local/ev_sdk/bin/test-ji-api -f 1 -i '$file' -a '$a_param' -o '$output_dir/res_$filename'"
        
        # Execute the command
        eval "$command"
    fi
done

zip_filename="res_${beijing_time}.zip"
zip -r "$zip_filename" "$output_dir"
