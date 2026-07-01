#!/bin/bash

# ===================================================================
#  DAY 6 LAB: SYSTEM HEALTH & SECURITY AUDITOR
# Core Skills: Variables, File Creation, Hardening Permissions, Loops
# suppressing Errors, Resource Checks
# ===================================================================

# 1. Define Variables
LAB_USER="Siyamol"
BACKUP_DIR="security_backups"
CRITICAL_LOG="system_audit.log"

echo "==============================================================="
echo "   Initialising System Health Sweep for Engineer: $LAB_USER    "
echo "==============================================================="

# 2. Folder Authentication & Hardening (Day 3 & 4 Skills)
echo "Step 1: Preparing secure backup infrastructure.."
if [ -d "BACKUP_DIR" ] ; then
    echo " -> Backup directory 'BACKUP_DIR' already exists."
else
    mkdir "$BACKUP_DIR"
    echo " -> SUCCESS: Created '$BACKUP_DIR' directory."
fi

# Haedening permissions: Only owner can Read/Write/Execute this folder
chmod 700 "$BACKUP_DIR"
echo " -> SECURITY HARDENING: Permission locked down to strict owner-access (700).."

# 3.Suppressing Errors & System Verification (Day 5 Skills)
echo "Step 2: Checking for critical audit logs..."


# We check if the file exists, sending any potential errors to the black hole
if  ls "$CRITICAL_LOG" &>/dev/null; then
    echo "-> Log file found:Preserving existiong data."
else
    echo " -> WARNING: '$CRITICAL_LOG' not found. Provisioning a fresh database log..."
    touch "$CRITICAL_LOG"
    echo "TIMESTAMP: $(date) - Initializing secure lab log track." >> "$CRITICAL_LOG"
fi

# 4. Live Resource Monitoring
echo "Step 3: Analyzing live hardware vital signs.."

# Grab the percentage of disk space used on your main drive
DISK_USAGE=$(df -h / | awk 'NR==2 {print $5}'')
echo " -> Total Storage Space Used: $DISK_USAGE"

# Grab the amount of free memory available
FREE_MEM=$(free -m | awk 'NR==2 {print $4}')
echo " ->Available System Memory: ${FREE_MEM}MB" 
# 5. Final Verification Summary
echo "=============================================================="
echo "      WEEK 1 LAB COMPLETE: Audit system state is stables!     "
echo "=============================================================="
