# ROBT310ProjectSignature 🚀

## Step 1: Clone the Project 🖥️

Firstly, clone the project using the following command:

```bash
git clone https://github.com/nihsioK/ROBT310ProjectSignature
```

Navigate to the project directory:

```bash
cd ROBT310ProjectSignature
```

---

## Step 2: Download the Weights Manually ⬇️

1. Go to the [Releases Page](https://github.com/nihsioK/ROBT310ProjectSignature/releases) of the repository.
2. Locate the release version (e.g., `v1.0`).
3. Manually download the weights file by clicking on `my_model.h5`.

---

## Step 3: Move the Weights File to the Cloned Directory 🎯

After downloading, move the `my_model.h5` file into the `models` folder within the cloned directory.

**For Unix-based systems (Linux/Mac):**

```bash
mv /path/to/my_model.h5 models/my_model.h5
```

**For Windows (PowerShell):**

```powershell
Move-Item -Path "C:\path\to\my_model.h5" -Destination models\my_model.h5
```

---

## Step 4: Create a Virtual Environment 🌐

Ensure Python 3.11 is installed. Create a virtual environment in the project directory:

**For Unix-based systems (Linux/Mac):**

```bash
python3 -m venv venv
source venv/bin/activate
```

**For Windows (PowerShell):**

```powershell
python -m venv venv
.\venv\Scripts\activate
```

---

## Step 5: Install Required Libraries 📦

Install the dependencies:

```bash
pip install -r requirements.txt
```

---

## Step 6: Run the Project ▶️

Run the application using:

```bash
streamlit run aidana.py
```

---

## Step 7: Access the Application 🌟

Open the following URL in your browser:

```bash
http://localhost:8501/
```
