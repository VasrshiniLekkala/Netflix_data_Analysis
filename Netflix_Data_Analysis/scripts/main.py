import os
import subprocess

# ✅ Define base folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ✅ Script paths
scripts = [
    os.path.join(BASE_DIR, 'cleaning.py'),
    os.path.join(BASE_DIR, 'visualization.py'),
    os.path.join(BASE_DIR, 'summary_report.py'),
]

print("🚀 Starting Netflix Data Analysis Pipeline...\n")

# ✅ Run each script one by one
for script in scripts:
    script_name = os.path.basename(script)
    print(f"▶️ Running {script_name}...")
    try:
        subprocess.run(['python', script], check=True)
        print(f"✅ {script_name} completed successfully!\n")
    except subprocess.CalledProcessError:
        print(f"❌ Error while running {script_name}!\n")

print("🎉 All tasks completed successfully!")
print("📊 Check your 'outputs' folder for results.")
