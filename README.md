# pdf-tools-test-automation
# Steps to initialize project

**Clone the repository**
```
git clone https://github.com/PortDocFormTools/pdf-tools-test-automation.git
```
**Navigate to the repository folder**
```
cd pdf-tools-test-automation
```
**Create a virtual environment**
```
python -m venv .venv
```
**Activate the virtual environment**
```
.venv\Scripts\activate
```
**Install required libraries**
```
pip install -r requirements.txt
```
**Create config.py based on config.py.example**
```
cp config.py.example config.py
```

# Workflow
Make sure to activate the venv every time you work on the project. This will ensure that the correct dependencies are used and avoid issues related to mismatched packages.

To deactivate the virtual environment when you're done use
```
deactivate
```
**Note:** Before running tests, make sure to initialize and start the main application project: [pdf-tools](https://github.com/PortDocFormTools/pdf-tools)

Then Copy Server URL from console after ```npm start```

**Update config.py**
```
BASE_URL = "copied URL"
```

**To run all tests use**
```
pytest
```
**Run a specific test file or suite**
```
pytest path/file.py
```