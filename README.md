# Coral Reef Bleaching and Recovery Visualization

A Streamlit web application for visualizing coral reef bleaching and recovery data worldwide. This project transforms Jupyter notebook analysis into an interactive web interface deployable on Streamlit Community Cloud.

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/amzn-vizcon-2025-coral-reef.git
   cd amzn-vizcon-2025-coral-reef
   ```

2. **Create and activate a virtual environment**
   ```bash
   python3 -m venv coral_env
   source coral_env/bin/activate  # On Windows: coral_env\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Run the Streamlit application**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser**
   The application will automatically open at `http://localhost:8501`

### Team Collaboration

#### Adding New Dependencies

1. **Activate the virtual environment**
   ```bash
   source coral_env/bin/activate  # On Windows: coral_env\Scripts\activate
   ```

2. **Install the new package**
   ```bash
   pip install package-name
   ```

3. **Update requirements.txt**
   ```bash
   pip freeze > requirements.txt
   ```

4. **Commit the updated requirements.txt**
   ```bash
   git add requirements.txt
   git commit -m "Add package-name dependency"
   ```

#### Working with the Repository

- Always activate the virtual environment before working: `source coral_env/bin/activate`
- Install dependencies from requirements.txt when pulling updates: `pip install -r requirements.txt`
- Update requirements.txt whenever you add new packages
- The `coral_env/` folder is gitignored - each team member creates their own