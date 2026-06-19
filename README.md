# DevOps & Systems Automation Portfolio

Welcome to my hands-on systems engineering and automation repository. This project serves as a comprehensive technical log of my work in DevOps, cloud infrastructure orchestration, and infrastructure hardening.

---

## 📁 Repository Structure
* `linux_automation_labs/` - Enterprise shell scripting, core utilities, and permission auditing.

---

## 🛠️ Module 1: Linux Core Systems Automation & Hardening (Week 1)

This module focused on developing scalable environment logic, utilizing low-level Linux systems utilities, and enforcing architectural security access controls.

### 🚀 Technical Implementation Highlights

#### 1. Shell Scripting Foundations & Variable Elasticity
* Engineered modular Bash scripts featuring explicit interpreter routing (`#!/bin/bash`).
* Utilized dynamic variable blocks to ensure execution environment elasticity and modular automation logic.
* Practiced clean file execution flows across multiple test directories.

#### 2. Infrastructure Telemetry & Data Parsing
* Developed a live **System Health Auditor** utility.
* Programmatically scraped physical server resource metrics (disk utilization percentages and available memory pools) directly from the hardware layer using command-line stream filters.

#### 3. Linux Stream Manipulation & Log Management
* Deep-dived into input/output stream redirections using Linux standard descriptors (`stdin`, `stdout`, `stderr`).
* Configured robust log routing by piping standard operation metrics into persistent `.log` system tracking files.
* Suppressed debugging errors and execution noise by safely routing error streams to null blocks (`&>/dev/null`).

#### 4. Resource Access Control & Hardening
* Applied strict architectural hardening parameters to lab scripts and local system files.
* Audited 3-tier POSIX permission boundaries (**User**, **Group**, **Others**) via `chmod` and `chown`.
* Enforced the **Principle of Least Privilege (PoLP)** by deliberately stripping untrusted or non-administrative actors of unnecessary read/write permissions.

#### 5. Local Git Workspace Architecture
* Configured a centralized terminal workspace integrated with Git version control.
* Standardized commit tracking logic utilizing **Conventional Commit specifications** (`feat:`, `fix:`, `docs:`) to guarantee clear, traceable pipeline history.

---

## 🛠️ Core Competencies Verified
`Linux System Administration` | `Bash Shell Scripting` | `Systems Automation` | `Git Version Control` | `Network Security` | `Access Control (IAM)`
