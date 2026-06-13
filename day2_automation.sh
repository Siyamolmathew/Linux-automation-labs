#!/bin/bash
echo "==========================================="
echo "	    RUNNING SYSTEM HEALTH MONITOR        "
echo "==========================================="
echo "Checking storage space used by this lab folder..."
du -sh
echo "-------------------------------------------"
df -h /c
echo "==========================================="
echo "Health check complete! System nominal."
