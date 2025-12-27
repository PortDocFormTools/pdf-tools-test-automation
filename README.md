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
**Install playwright dependencies**
```
playwright install
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

**Run all tests**
```
pytest
```
**Run specific test file or suite**
```
pytest path/file.py
```

# Allure report
**Generate Allure results**
```
pytest --alluredir=allure-results --clean-alluredir
```
**Serve a temporary report (no files saved)**
```
allure serve allure-results    
```
**Generate Allure report**
```
allure generate allure-results -o allure-report --clean
```
**Open Allure report**
```
allure open allure-report
```