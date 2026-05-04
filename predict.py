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

# Change to the directory the script is in
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Unnecessary when containerized
#print("Verifying requirements...")
#run("pip install -r requirements.txt --quiet")

#Warnings quieting
warnings.filterwarnings("ignore", category=UserWarning)

#print("Forming predictions ...")
run('papermill "Varroa Infestation Prediction - Predictor.ipynb" /dev/null', cwd=os.path.join(script_dir, "pipeline"))

# Read the config to find out what the output file is named
with open(os.path.join(script_dir, "configs", "predict_config.json"), "r") as f:
    config = json.load(f)

start_date = config["prediction_period_start_date"]
end_date = config["prediction_period_end_date"]
output_file = os.path.join(script_dir, "predictions", f"varroa_pred_{start_date}_to_{end_date}.txt")

#print("Opening output file...")
system = platform.system()
if system == "Windows":
    os.startfile(output_file)
elif system == "Darwin":
    subprocess.run(["open", output_file])
else:
    subprocess.run(["cat", output_file])
    #subprocess.run(["xdg-open", output_file])