#!/usr/bin/env python3
import os
import subprocess

# Fixed absolute paths
MAIN_PY_PATH = "/usr/src/app/main.py"
CONFIG_PATH = "/usr/src/mount_input_output/input_config_paramters.json"

def main():
    # Check files
    if not os.path.isfile(MAIN_PY_PATH):
        raise FileNotFoundError(f"[run_app] main.py not found at {MAIN_PY_PATH}")

    if not os.path.isfile(CONFIG_PATH):
        print(f"[run_app] WARNING: Config not found at {CONFIG_PATH} — app may fail.")

    # Build command
    cmd = ["python", MAIN_PY_PATH, CONFIG_PATH]

    # Run the command
    print(f"[run_app] Running: {' '.join(cmd)}")
    subprocess.run(cmd, check=True)

if __name__ == "__main__":
    main()
