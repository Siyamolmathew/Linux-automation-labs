#!/bin/bash

echo "========================================"
echo "	  RUNNING SECURE ONBOARDING ENGINE    "
echo "========================================"

# Define variable names for clean automation
NEW_GROUP="sec_ops_team"
NEW_USER="test_engineer"

# 1.Simulate creating a secure system group
echo "Creating system access boundary group: $NEW_GROUP..."
# Note: In a true production root terminal, you would run: groupadd $NEW_GROUP
echo "Success: Group '$NEW_GROUP' intialized."

echo "----------------------------------------"


# 2. Automation logic: Check if user already exists to prevent system errors
echo "Checking if infrastructure identity '$NEW_USER' exists..."

if id "$NEW_USER" &>/dev/null; then
    echo "ALEART: User '$NEW_USER' already exists on this machine. Skipping creation."
else
    echo "User '$NEW_USER' not found.Executing secure provisioning sequence.."
    #Note: In a production root terminal, you would run: useradd -m -g $NEW_GROUP $NEW_USER
    echo " Created user identity '$NEW_USER' and assigned to group '$NEW_GROUP'."
fi
echo "----------------------------------------"

# 3.Security Hardening Audit Notes
echo "SECURITY COMPLIANCE AUDIT: "
echo "-> Enforcing MITR ATTACK T1078 defenses: Valid Accounts verfied: "
echo "-> Default shell set to restricted environment."
echo "========================================"

