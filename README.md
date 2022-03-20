# Overview

This project will demonstrate how to build a CI/CD pipeline utilizing Azure Cloud shell, GitHub, GitHub Actions and Azure Pipeline from the Azure DevOps services.

## Project Plan
* [Project Trello Board](https://trello.com/b/utPUpbKs/azure-webapp-pipeline)
* [Project Plan Spreadsheet](https://docs.google.com/spreadsheets/d/1YxOxBlr8zrpXSzDh7PlDraRNqhwDD2ab5f9H8kcbaOg/edit?usp=sharing)

## Instructions
![Azure Pipeline](https://user-images.githubusercontent.com/89496176/159104344-83559ddd-c537-4ccd-9bc0-603344079cf7.jpg)


### Dependencies
* Create an [Azure Account](https://portal.azure.com)
* Install the [Azure command line interface](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest)
* Create [GitHub Account](https://docs.github.com/en/get-started/signing-up-for-github/signing-up-for-a-new-github-account)
* Create [Azure DevOps Account](https://azure.microsoft.com/en-us/services/devops/)


### Setup Cloud-based Deployment Environment
* Fork Start File [GitHub Repo](https://github.com/Jake4PCAPS/azure-pipeline)
* Integrate Azure Cloud Shell with GitHub
⋅⋅1. Azure Cloud Shell [Generate SSH Key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
⋅⋅2. Add [SSH Key to GitHub Account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)
* Clone GitHub to Azure Cloud Shell (Use URL to your GitHub Repo)
![image](https://user-images.githubusercontent.com/89496176/159137779-4e7fa523-bf31-4e9a-985d-ad3b2bdec24e.png)

### Setup the Project Scaffolding
* Makefile
* Create & Activate a Python Virtual Environment (Choose your own name and directory)

```bash
example@Azure:~$ python3 -m venv ~/.test
example@Azure:~$ source ~/.test/bin/activate
(.test) example@Azure:~$ 
```


### Run Local test
* Run the Makefile
```bash
example@Azure:~$ make all
```
* Example of Passing Tests
![image](https://user-images.githubusercontent.com/89496176/159138090-b24bed2c-8610-4bfa-8032-135694bd9027.png)


### Setup Github Actions
* Under Actions tab in the GitHub repository, select **set up a workflow yourself**
![image](https://user-images.githubusercontent.com/89496176/159138274-e6302440-a224-4139-a476-76e9804c5f80.png)
* Edit the **pythonapp.yml** file with the following and **Start Commit** to the repo
```
name: Python application test with Github Actions

on: [push]

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python 3.5
      uses: actions/setup-python@v1
      with:
        python-version: 3.5
    - name: Install dependencies
      run: |
        make install
    - name: Lint with pylint
      run: |
        make lint
    - name: Test with pytest
      run: |
        make test
```

* Validate the remote tests pass
![image](https://user-images.githubusercontent.com/89496176/159138359-79b3f663-f049-4277-a4c2-49c5b16ddac0.png)

[![Python application test with Github Actions](https://github.com/Jake4PCAPS/azure-pipeline/actions/workflows/pythonapp.yml/badge.svg)](https://github.com/Jake4PCAPS/azure-pipeline/actions/workflows/pythonapp.yml)

### Deploy Flask ML Web App
* Create a webapp service in Azure Cloud Shell:
```bash
example@Azure:~$ az webapp up -n <your-appservice>
```
![image](https://user-images.githubusercontent.com/89496176/159143393-968232d8-171d-4d4e-a2a6-e92969ce978f.png)

* Validate the deployed application is working by accessing it from a web browser and inspecting the app service logs

![image](https://user-images.githubusercontent.com/89496176/159138982-76eeb19c-492c-42e9-bb0d-bce7ce4d23d2.png)

 ![image](https://user-images.githubusercontent.com/89496176/159139007-ba412cce-ee81-4267-a804-b39779df7327.png)

* Checking Log File
```bash
example@Azure:~$ az webapp log tail
2022-03-20T00:26:00.061Z INFO  - Initiating warmup request to container project2
-pipeline-app_7_16806125 for site example-app

2022-03-20T00:26:17.406Z INFO  - Container site example-app_7_16806125 for site site example-app initialized successfully and is ready to serve requests.
```

* Running load test with Locust
	
![image](https://user-images.githubusercontent.com/89496176/159144251-4663b344-689e-4772-aecd-7d4d2f9883b6.png)



### Validate the Flask ML Web App with **Make Predict** script
* Edit the following line in the **make_predict_azure_app.sh** file to match the web app name
![image](https://user-images.githubusercontent.com/89496176/159138930-01dcc042-95cd-44f3-a907-79c38c4ad46f.png)
* Sucessful prediction Output
```bash
example@Azure:~$ ./make_predict_azure_app.sh
Port: 443
{"prediction":[20.35373177134412]}
```


 ### Continious Deliver using Azure Pipelines and Azure App service
* Integrate [Azure Pipelines and GitHub](https://docs.microsoft.com/en-us/azure/devops/pipelines/repos/github?view=azure-devops&tabs=yaml)
* Create an new Azure DevOps Project and establish Azure connection
Follow [Azure DevOps](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops#create-an-azure-devops-project-and-connect-to-azure)
* Test the Azure pipeline by adding text to HTML heading in the **app.py** home function in Azure Cloud Shell
```python
@app.route("/")
def home():
    html = "<h3>Sklearn Prediction Home</h3>"
    return html.format(format)
```
* Commit edited file in Git and push the change to GitHub
```bash
example@Azure:~$ git add app.py
example@Azure:~$ git commit
example@Azure:~$ git push
```
* In Azure Pipeline under the **Run** tab, validate the job completes successfully
![image](https://user-images.githubusercontent.com/89496176/159143056-366ff6c1-a52c-4313-be0b-c193502e615b.png)

* Validate the Web App site is displaying the new text

![image](https://user-images.githubusercontent.com/89496176/159143220-c633f8f6-cc18-4452-a501-7da127ae9095.png)


## Enhancements

* Add new pytest tests in the Makefile 
* Use GitHub Actions for continious deliver instead of Azure Pipelines

## Demo 

<TODO: Add link Screencast on YouTube>
