FastAPI Base Scaffolding
=============================================================================

![GitHub](https://img.shields.io/github/license/blevinscm/fastapi-scaffold-base) ![GitHub contributors](https://img.shields.io/github/contributors/blevinscm/fastapi-scaffold-base) ![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/blevinscm/fastapi-scaffold-base?include_prereleases)


<img align="center" width="400" src="./docs/images/fastapi-logo.png"/>

#### Projected by : | [Rodrigo Melo](https://github.com/rodrigodma)

### [FastAPI](https://fastapi.tiangolo.com/)

## Dependencies: 

  |Package | Note |
  |:----|:------------|
  |[Python 3.6+](https://www.python.org/downloads/) | This project uses Python 3.9 but should work on Python 3.6+. |
  |[pip](https://pip.pypa.io/en/stable/installing/) | I use Pip for pacakage management and pin versions.  I don't think anything more complex than that is necessary.  Adjust for your flow. |
  |[virtualenv](https://virtualenv.pypa.io/en/stable/installation.html) | Again I am not trying to get fancy.  ```py -m pip install virtualenv```|
  |[FastAPI](https://github.com/tiangolo/fastapi) |  I usally install all related packages in my venv. ```pip install fastapi[all]```  |


## Get Started

1. Install Python if not already installed

2. Clone this repository: 
   ```git
    git clone https://github.com/rodrigodma/fastapi-poc.git
    ```

3. Install virtualenv
    ```zsh
    py -m pip install --user virtualenv
    ```
4. CD into project directory
    ```zsh
        cd dir 
    ```
5. Create virtual environment
    ```bash
    py -m venv env
    ```
6. Activate virtual environment
    ```bash
    source .\env\bin\activate
    ```
7. Install pip dependencies (This will install all FastAPI Modules.  If you do not want [all] plese adjust the req file.)
    ```bash
    pip install -r requirements.txt
    ```
8. Run the start-FastAPI for your system 

9. Go to https://localhost:8000 to see a basic HTML page with sections for content.

10. Go to https://localhost:8000/docs to see your FastAPI documentation and explore the sample docs.

11. To get out of venv
    ```bash
    deactivate
    ```

--TODO--
1) Add unit tests and Integrate Pytest
2) Add implicit support for Relational data
3) Add plug and play content through API calls