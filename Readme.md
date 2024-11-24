### Step 1: Download the Release Package ⬇️

1. Go to the [Releases Page](https://github.com/nihsioK/ROBT310ProjectSignature/releases) of the repository.
2. Download the source code and weights for the desired release (e.g., `v1.0`).

   Alternatively, use the following commands:

   **For Unix-based systems (Linux/Mac):**

   ```bash
   wget https://github.com/nihsioK/ROBT310ProjectSignature/archive/refs/tags/v1.0.zip
   wget https://github.com/nihsioK/ROBT310ProjectSignature/releases/download/v1.0/my_model.h5 -O models/my_model.h5
   ```

   **For Windows (PowerShell):**

   ```powershell
   Invoke-WebRequest -Uri https://github.com/nihsioK/ROBT310ProjectSignature/archive/refs/tags/v1.0.zip -OutFile v1.0.zip
   Invoke-WebRequest -Uri https://github.com/nihsioK/ROBT310ProjectSignature/releases/download/v1.0/my_model.h5 -OutFile models\my_model.h5
   ```

---

### Step 2: Extract the Package 🗂️

**For Unix-based systems (Linux/Mac):**

```bash
unzip v1.0.zip
cd ROBT310ProjectSignature-v1.0
```

**For Windows (PowerShell):**

```powershell
Expand-Archive -Path v1.0.zip -DestinationPath .\ROBT310ProjectSignature-v1.0
cd ROBT310ProjectSignature-v1.0
```

---

### Step 3: Create a Virtual Environment 🌐

Ensure Python 3.11 is installed. Create a virtual environment:

**For Unix-based systems (Linux/Mac):**

```bash
python3 -m venv venv
```

**For Windows (PowerShell):**

```powershell
python -m venv venv
```

---

### Step 4: Install Required Libraries 📦

Activate the virtual environment and install dependencies:

**For Unix-based systems (Linux/Mac):**

```bash
source venv/bin/activate
pip install -r requirements.txt
```

**For Windows (PowerShell):**

```powershell
.\venv\Scripts\activate
pip install -r requirements.txt
```

---

### Step 5: Place the Model Weights 🎯

Ensure the `my_model.h5` file is in the correct directory (e.g., `models/my_model.h5`). You may need to create the `models` directory if it does not exist.

**For Unix-based systems (Linux/Mac):**

```bash
mkdir -p models
mv my_model.h5 models/my_model.h5
```

**For Windows (PowerShell):**

```powershell
New-Item -ItemType Directory -Path models
Move-Item -Path my_model.h5 -Destination models\my_model.h5
```

---

### Step 6: Run the Project ▶️

Run the application:

**For Both Unix-based systems and Windows:**

```bash
streamlit run aidana.py
```

---

### Step 7: Access the Application 🌟

Open the following URL in your browser:

```bash
http://localhost:8501/
```
