import os
import subprocess
import json
from datetime import datetime

def execute_script(script_name):
    print(f"[*] Executing pipeline component: {script_name}...")
    if not os.path.exists(script_name):
        print(f"   [❌ ERROR] File {script_name} not found.")
        return "FAILED", "File not found"
        
    try:
        custom_env = os.environ.copy()
        custom_env["PYTHONIOENCODING"] = "utf-8"
        
        # We explicitly specify encoding and error handling at the subprocess execution level
        result = subprocess.run(
            ["python", script_name],
            capture_output=True,
            text=True,
            check=True,
            env=custom_env,
            encoding="utf-8",
            errors="replace"
        )
        print(f"   [✅ SUCCESS] {script_name} completed successfully.")
        return "SUCCESS", result.stdout.strip() if result.stdout else "No output"
    except subprocess.CalledProcessError as e:
        print(f"   [❌ CRITICAL] {script_name} dropped execution.")
        return "FAILED", e.stderr.strip() if e.stderr else "Execution error"

def main():
    print("=========================================================")
    print("🚀 LAUNCHING WEEK 3 CENTRALIZED AUTOMATION HARNESS 🚀")
    print("=========================================================")
    
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
    
    for script in pipeline:
        status, details = execute_script(script)
        harness_report["pipeline_results"][script] = {
            "status": status,
            "runtime_logs": details
        }
        if status == "FAILED":
            harness_report["overall_status"] = "DEGRADED / FAILED"

    with open("master_pipeline_report.json", "w", encoding="utf-8") as f:
        json.dump(harness_report, f, indent=4)
        
    print("=========================================================")
    print("[🎉 PIPELINE COMPLETE] Master log saved successfully.")
    print("=========================================================")

if __name__ == "__main__":
    main()