import subprocess
import sys
import os
import platform
import json
import warnings

def run(cmd, cwd=None):
    result = subprocess.run(cmd, shell=True, cwd=cwd)
    if result.returncode != 0:
        print(f"Command failed: {cmd}")
        sys.exit(1)

# Directory this script lives in (utilities/)
script_dir = os.path.dirname(os.path.abspath(__file__))

# Parent directory (project root)
root_dir = os.path.dirname(script_dir)

os.chdir(root_dir)

# Run notebook from pipeline folder (now relative to root)
run(
    'papermill "Varroa Infestation Prediction - Predictor.ipynb" /dev/null',
    cwd=os.path.join(root_dir, "pipeline")
)

# Read config from root/configs
with open(os.path.join(root_dir, "configs", "predict_config.json"), "r") as f:
    config = json.load(f)

start_date = config["prediction_period_start_date"]
end_date = config["prediction_period_end_date"]

# Output file in root/predictions
output_file = os.path.join(
    root_dir,
    "predictions",
    f"varroa_pred_{start_date}_to_{end_date}.txt"
)

# Open or print output
system = platform.system()
if system == "Windows":
    os.startfile(output_file)
elif system == "Darwin":
    subprocess.run(["open", output_file])
else:
    subprocess.run(["cat", output_file])