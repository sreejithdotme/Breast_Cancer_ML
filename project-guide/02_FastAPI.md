# FastAPI – Important Commands

A practical reference for installing, running, testing, and debugging FastAPI applications.

## 1. Installation and Environment Setup

**Install FastAPI**

```powershell
pip install fastapi
```

Installs the FastAPI framework.

**Install Uvicorn**

```powershell
pip install "uvicorn[standard]"
```

Installs Uvicorn, the ASGI server used to run FastAPI applications.

**Install project dependencies**

```powershell
pip install -r requirements.txt
```

Installs all packages listed in the project's requirements file.

**Check FastAPI version**

```powershell
pip show fastapi
```

Displays the installed FastAPI version and package information.

**Check Uvicorn version**

```powershell
uvicorn --version
```

Displays the installed Uvicorn version.

## 2. Running FastAPI Applications

**Start the API server**

```powershell
uvicorn main:app
```

Runs the `app` FastAPI instance defined inside `main.py`.

**Run with automatic reload**

```powershell
uvicorn main:app --reload
```

Automatically restarts the server whenever Python source files change. Useful during development.

**Run on a specific port**

```powershell
uvicorn main:app --port 8080
```

Starts the API on port 8080 instead of the default port 8000.

**Run on all network interfaces**

```powershell
uvicorn main:app --host 0.0.0.0 --port 8000
```

Allows the API to accept connections from outside the local machine. Commonly used in Docker.

**Run with debug logging**

```powershell
uvicorn main:app --reload --log-level debug
```

Displays detailed server logs to help investigate errors.

**Stop the server**

```text
Ctrl + C
```

Stops the running API server.

> Note: `main:app` means the Python module `main.py` and the FastAPI instance named `app`. If your file is inside a package, adjust the import path. For example, `backend.main:app`.

## 3. API Testing

**Open Swagger UI**

```text
http://127.0.0.1:8000/docs
```

Provides an interactive interface to test API endpoints.

**Open ReDoc**

```text
http://127.0.0.1:8000/redoc
```

Displays automatically generated API documentation in an alternative format.

**Check the API root endpoint**

```text
http://127.0.0.1:8000/
```

Opens the root endpoint if one has been defined.

**Test using curl**

```powershell
curl.exe http://127.0.0.1:8000/health
```

Sends an HTTP GET request to the health endpoint. Replace `/health` with an endpoint defined in your API.

**Test a POST endpoint**

```powershell
curl.exe -X POST "http://127.0.0.1:8000/predict" `
  -H "Content-Type: application/json" `
  -d '{"feature": 5}'
```

Sends JSON data to a POST endpoint. Replace the URL and JSON fields with the ones your API expects.

## 4. Testing and Verification

**Check Python syntax**

```powershell
python -m py_compile main.py
```

Checks the Python file for syntax errors without starting the server.

**Check installed dependencies**

```powershell
pip check
```

Checks for incompatible or missing package dependencies.

**List installed packages**

```powershell
pip list
```

Displays all installed Python packages and their versions.

## 5. Debugging and Troubleshooting

| Problem | What to check |
|---|---|
| `ModuleNotFoundError` | Check imports and install missing packages |
| Port 8000 already in use | Stop the existing server or select another port |
| HTTP 404 | Verify the endpoint URL and HTTP method |
| HTTP 422 | Check request body, field names, and data types |
| HTTP 500 | Inspect the terminal traceback |
| API not responding | Check whether Uvicorn is running |
| Model not loading | Verify the model path and dependencies |

**View available Uvicorn options**

```powershell
uvicorn --help
```

Displays available server configuration options.

