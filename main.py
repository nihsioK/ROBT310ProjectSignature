import subprocess
import sys
import os


def run_script_in_venv(venv_path, script_name, image_path):

    try:
        python_executable = os.path.join(venv_path, "Scripts", "python.exe")  # For Windows venv

        if not os.path.exists(python_executable):
            raise FileNotFoundError(f"Python executable not found in the virtual environment: {python_executable}")

        result = subprocess.run([python_executable, script_name, image_path], check=True)

    except subprocess.CalledProcessError as e:
        sys.exit(1)
    except FileNotFoundError as e:
        sys.exit(1)


if __name__ == "__main__":
    venv_path = "venv"

    if len(sys.argv) < 2:
        sys.exit(1)

    image_path = sys.argv[1]

    scripts = ["final_cropping_with_lines.py", "ocr.py", "crop_signatures.py", "crop_sign.py"]

    for script in scripts:
        run_script_in_venv(venv_path, script, image_path)
