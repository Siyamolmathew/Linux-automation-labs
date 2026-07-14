import os
import subprocess
import json
from datetime import datetime

def execute_script(script_name):
    """Safely runs a sub-script and captures its status and output."""
    print(f"[*] Executing pipeline component: {script_name}...")
    
    if not os.path.exists(script_name):
        print(f"   [❌ ERROR] File {script_name} not found in current directory.")
        return "FAILED", "File not found"
        
    try:
        # Runs the script and captures stdout/stderr
        result = subprocess.run(
            ["python", script_name],
            capture_output=True,
            text=True,
            check=True
        )
        print(f"   [✅ SUCCESS] {script_name} completed successfully.")
        return "SUCCESS", result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"   [❌ CRITICAL] {script_name} crashed with exit code {e.returncode}.")
        return "FAILED", e.stderr.strip()

def main():
    print("=========================================================")
    print("🚀 LAUNCHING WEEK 3 CENTRALIZED AUTOMATION HARNESS 🚀")
    print("=========================================================")
    
    # Define the execution pipeline sequence
    pipeline = [
        "day15_metrics_serializer.py",
        "day_18_log_rotator.py",
        "day19_backup_archiver.py"
    ]
    
    harness_report = {
        "orchestration_timestamp": datetime.now().isoformat(),
        "pipeline_results": {},
        "overall_status": "SUCCESS"
    }
    
    # Execute each script in the pipeline sequentially
    for script in pipeline:
        status, details = execute_script(script)
        harness_report["pipeline_results"][script] = {
            "status": status,
            "runtime_logs": details
        }
        if status == "FAILED":
            harness_report["overall_status"] = "DEGRADED / FAILED"

    # Write out a centralized execution master log
    report_filename = "master_pipeline_report.json"
    with open(report_filename, "w", encoding="utf-8") as f:
        json.dump(harness_report, f, indent=4)
        
    print("=========================================================")
    print(f"[🎉 PIPELINE COMPLETE] Master log saved to {report_filename}")
    print("=========================================================")

if __name__ == "__main__":
    main()