#!/bin/bash

echo "======================================="
echo "     STARTING PERMISSION HARDENING     "
echo "======================================="
# 1. Create a secure directory
echo "Creating secure directory  'secure_vault'..."
mkdir -p secure_vault

# 2. Create a sensitive data file inside it
echo "Generating sensitive log file..."
echo "CONFIDENTIAL: System access keys updated." > secure_vault/system_vitals.log

# 3. Checking permissions before hardening
echo "Permission before hardening: "
ls -ld secure_vault

echo "----------------------------------------"

# 4. Hardening the directory
# 'go-rwx' means: Remove (-) Read (r), Write (w), and Execute (x) for Group (g) and Others (o)
echo "Restricting access to owner only..."
chmod go-rwx secure_vault

# 5.Check permissions after hardening
echo "Permission after hardening (Should show 'drwx-----'): "
ls -ld secure_vault

echo "========================================"

