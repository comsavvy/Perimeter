#!/bin/bash
./perimeter.py $@ > total_output.txt
cat total_output.txt
echo "Total processed data: $#"
