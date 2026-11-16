# Streamlit – Important Commands

A practical reference for installing, running, testing, and debugging Streamlit applications.

## 1. Installation and Environment Setup

**Create a virtual environment**

```powershell
python -m venv venv
```

Creates an isolated Python environment for the project.

**Activate the virtual environment (Windows PowerShell)**

```powershell
.\venv\Scripts\Activate.ps1
```

Activates the environment so packages are installed locally for this project.

**Install Streamlit**

```powershell
pip install streamlit
```

Installs the Streamlit framework.

**Install project dependencies**

```powershell
pip install -r requirements.txt
```

Installs all packages listed in the project's requirements file.

**Check the installed Streamlit version**

```powershell
streamlit --version
```

Displays the currently installed Streamlit version.

## 2. Running Streamlit Applications

**Run an application**

```powershell
streamlit run app.py
```

Starts the Streamlit application using `app.py` as its entry point.

**Run on a specific port**

```powershell
streamlit run app.py --server.port 8502
```

Runs the application on port 8502 instead of the default port 8501.

**Run on a specific address**

```powershell
streamlit run app.py --server.address 0.0.0.0
```

Allows the application to listen on all network interfaces. Commonly used inside Docker containers.

**Run with debug logging**

```powershell
streamlit run app.py --logger.level debug
```

Displays detailed application logs that help identify errors.

**Stop the application**

```text
Ctrl + C
```

Stops the running Streamlit server in the terminal.

## 3. Testing and Verification

**Run the Streamlit example application**

```powershell
streamlit hello
```

Launches Streamlit's built-in demonstration application. Useful for checking whether Streamlit is installed and working.

**Check Python syntax**

```powershell
python -m py_compile app.py
```

Checks `app.py` for Python syntax errors without running the application.

**Check installed package information**

```powershell
pip show streamlit
```

Displays the installed Streamlit version, location, and package information.

**Check dependency compatibility**

```powershell
pip check
```

Checks whether installed Python packages have dependency conflicts.

**Test the application manually**

1. Start the application.
2. Open the local URL in a browser.
3. Test all input fields and buttons.
4. Check whether the expected output is displayed.
5. Check the terminal for errors.

## 4. Debugging and Troubleshooting

**Enable detailed logging**

```powershell
streamlit run app.py --logger.level debug
```

Provides more detailed logs when investigating application errors.

**Clear Streamlit's cached data**

```powershell
streamlit cache clear
```

Clears cached data when an application displays outdated results or unexpected cached values.

**Display Streamlit configuration**

```powershell
streamlit config show
```

Displays the available configuration settings and their current values.

**Display Streamlit command help**

```powershell
streamlit --help
```

Shows available Streamlit commands and command-line options.

## 5. Common Problems

| Problem | What to check |
|---|---|
| `streamlit` command not found | Activate the virtual environment and install Streamlit |
| Port 8501 already in use | Stop the existing application or select another port |
| Module not found | Install the missing Python package |
| Application does not open | Check the terminal for errors and verify the local URL |
| Changes are not reflected | Save the file and rerun the application |
| Old results are displayed | Clear the Streamlit cache |
| API connection error | Verify the backend URL and check whether the API is running |

## 6. Useful URLs

| Purpose | URL |
|---|---|
| Default local application | `http://localhost:8501` |
| Alternative local address | `http://127.0.0.1:8501` |

