### Step 1: Download the Release Package ⬇️

1. Go to the [Releases Page](https://github.com/nihsioK/ROBT310ProjectSignature/releases) of the repository.
2. Download the source code and weights for the desired release (e.g., `v1.0`). Alternatively, use:

   ```bash
   wget https://github.com/nihsioK/ROBT310ProjectSignature/archive/refs/tags/v1.0.zip
   wget https://github.com/nihsioK/ROBT310ProjectSignature/releases/download/v1.0/my_model.h5 -O models/my_model.h5
   ```

### Step 2: Extract the Package 🗂️

Unzip the downloaded release package:

```bash
unzip v1.0.zip
cd ROBT310ProjectSignature-v1.0
```

### Step 3: Create a Virtual Environment 🌐

Ensure Python 3.11 is installed. Create a virtual environment:

```bash
python -m venv venv
```

### Step 4: Install Required Libraries 📦

Activate the virtual environment and install dependencies:

```bash
source venv/bin/activate  # On Linux/Mac
venv\Scripts\activate     # On Windows
pip install -r requirements.txt
```

### Step 5: Place the Model Weights 🎯

Ensure the `my_model.h5` file is in the correct directory (e.g., `models/my_model.h5`).

### Step 6: Run the Project ▶️

Run the application using:

```bash
streamlit run aidana.py
```

### Step 7: Access the Application 🌟

Open the following URL in your browser:

```bash
http://localhost:8501/
```
