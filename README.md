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
---

## 🔹 Week 2: Python Systems Automation & Network Diagnostics

This module marked the transition from local shell scripts to structured object-oriented automation using Python, focusing on defensive programming, resource-efficient file streaming, and network layer auditing.

### 📁 Core Engineering Labs
* **Day 8: Environment Configuration Inspection Engine**
  * [cite_start]Developed a system-tracking utility utilizing native runtime wrappers (`os` and `sys`) to programmatically scrape system paths, usernames, and evaluate interpreter execution boundaries[cite: 2970, 3039].
* **Day 9: Defensive File Provisioning Tool**
  * [cite_start]Implemented a programmatic file-auditor utilizing Boolean validation layers (`os.path.exists`) to execute relative filesystem routing (`..`) and provision backup directories defensively[cite: 2971, 3041].
* **Day 10: Memory-Efficient Security Log Parser**
  * [cite_start]Engineered a high-performance log-parsing utility that streams text files line-by-line using generators (`enumerate`) to conserve system RAM while isolating system error states using string overrides[cite: 2972, 3042].
* **Days 11-13: Network Boundary Mapper & Diagnostic Framework**
  * [cite_start]Designed an enterprise-grade network boundary probe leveraging raw socket programming (`socket.AF_INET`, `socket.SOCK_STREAM`)[cite: 2973, 3044]. [cite_start]Programmatically audited internal network interface cards (NICs) while executing multi-target external TCP handshakes using non-breaking exit codes (`connect_ex`) and strict latency timeouts[cite: 2973, 3044].

### 🎯 Key Interview Competencies
* [cite_start]**Defensive Software Design:** Verifying underlying infrastructure states before code execution to eliminate runtime crashes[cite: 2691, 2700].
* [cite_start]**Resource Optimization:** Streaming massive datasets line-by-line to protect system hardware memory bounds[cite: 2708, 2719].
* [cite_start]**Network Socket Programming:** Programmatically mapping perimeters and analyzing connection return codes over standard communication protocols[cite: 2792, 2931].
# Week 3: Advanced Automation and Configuration Pipeline

This directory contains a modular, production-grade infrastructure automation pipeline developed as part of the core infrastructure and security engineering track. The scripts automate routine system administration tasks, handle errors gracefully, and are managed by a centralized orchestration harness.

## 🚀 Pipeline Components

1. **Day 15: Metrics Serialization (`day15_metrics_serializer.py`)**
   * Automatically gathers and logs mock system telemetry (CPU, RAM, storage points) into structured format.
2. **Day 16 & 17: Environment Hardening & CLI Tools**
   * Scripts focused on maintaining baseline environment health and providing interactive command-line access.
3. **Day 18: Log Rotation Engine (`day_18_log_rotator.py`)**
   * Monitors active logs, evaluates size constraints, and handles automatic archival rotations.
4. **Day 19: Backup Archiver (`day19_backup_archiver.py`)**
   * Isolates rotated raw log artifacts, packs them into timestamped, compressed `.tar.gz` bundles, and isolates them inside a secure backup vault.

## 🛠️ Centralized Orchestration

* **Master Harness (`day20_automation_harness.py`)**
  * Serves as the central control plane that executes the entire pipeline sequentially.
  * Implements strict UTF-8 stream isolation and error mapping using Python's `subprocess` module to ensure platform-agnostic execution and catch individual script crashes without stopping the pipeline.
  * Generates an execution snapshot report saved to `master_pipeline_report.json`.
