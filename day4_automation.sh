#!/bin/bash

echo "=================================================="
echo "		RUNNING ENVIRONMENT PROFILER		"
echo "=================================================="

# 1. Print standard system environment variables
echo "Current System User: $USER"
echo "Current DIrectory Path: $PWD"

echo "--------------------------------------------------"

# 2, Print out the system search paths (your $PATH)
echo "Your System PATH directories look like this: "
echo "$PATH" | tr ':' '\n' 

echo "--------------------------------------------------"

# 3. Create a custom project varible inside the script runtime
echo "Setting a custom project milestone variable..."
export LAB_STATUS="Day 4 Crushed"

echo "Validation: The value of LAB_STATUS is -> $LAB_STATUS"
echo "==================================================="


