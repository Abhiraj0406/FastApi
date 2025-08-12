---- Python FastApi ----
1. select the python interpreter (ctrl + shift + p)
    i. venv
    ii. global (windows)

2. create the venv, use cmd -> "python -m venv venv"
3. activate the venv, use cmd -> "venv\Scripts\activate.bat"
4. update the pip, use cmd -> "python.exe -m pip install --upgrade pip"
5. install fastapi and uvicorn.
    i. Uvicorn is an ASGI server required to run FastAPI applications. -> "pip install fastapi uvicorn"
    ii. install all optional dependencies for FastAPI (e.g., for database integration, templating) -> "pip install fastapi[all]  uvicorn"

**Note: if want to see the pakages installed, use cms -> "pip freeze".

6. Run the FastAPI Server:
    i. "uvicorn main:app --reload"
    ii. "fastapi dev main.py"