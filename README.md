# Overview

This project will demonstrate how to build a CI/CD pipeline utilizing Azure Cloud shell, GitHub, GitHub Actions and Azure Pipeline from the Azure DevOps services.

## Project Plan

* [Project Trello Board.] (https://trello.com/b/utPUpbKs/azure-webapp-pipeline)
* A link to a spreadsheet that includes the original and final project plan>

## Instructions
![Azure Pipeline](https://user-images.githubusercontent.com/89496176/159104344-83559ddd-c537-4ccd-9bc0-603344079cf7.jpg)

* Dependencies
1. Create an [Azure Account](https://portal.azure.com)
2. Install the [Azure command line interface](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest)
3. Create [GitHub Account](https://docs.github.com/en/get-started/signing-up-for-github/signing-up-for-a-new-github-account)
4. Create [Azure DevOps Account](https://azure.microsoft.com/en-us/services/devops/)

* Setup Cloud-based Deployment Environment
1. Fork [GitHub Repo] (https://github.com/Jake4PCAPS/azure-pipeline)
2. Integrate Azure Cloud Shell with GitHub
Generate [SSH Key] (https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
Add [SSH Key to GitHub Account] (https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)
3. Clone GitHub Repo to a directory in Azure Cloud shell
screen shot here

* Setup the Project Scaffolding
1. Makefile
2. Create & Activate a Python Virtual Environment
screen shot here

3. Run Local test
Run the command make all
screen shot results

* Setup Github Actions
1. Under Actions tab in the GitHub repository, select "set up a workflow yourself"
insert screenshot
2. Edit the pythonapp.yml file with the following ```
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
3. Validate the remote tests pass
insert screen short

* Deploy Flask ML Web App
1. Create a webapp service in Azure Cloud Shell:
az webapp up -n <your-appservice>
2. Validate the deployed application is working by accessing it from a web browser and inspecting the logs
https://<your-appservice>.azurewebsites.net/
```bash
udacity@Azure:~$ az webapp log tail
```
3. Edit the line in the make_predict_azure_app.sh to match the app name
-X POST https://<yourappname>.azurewebsites.net:$PORT/predict
4. Sucessful prediction Output
screen shot

* Continious Deliver using Azure Pipelines and Azure App service
1. Integrate [Azure Pipelines and GitHub](https://docs.microsoft.com/en-us/azure/devops/pipelines/repos/github?view=azure-devops&tabs=yaml)
2. Create an new Azure DevOps Project and establish Azure connection
Follow [Azure DevOps] (https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops#create-an-azure-devops-project-and-connect-to-azure)
3. Test the deployment by editing the app.py home function
screen shot

# Overview

<TODO: complete this with an overview of your project>

## Project Plan
<TODO: Project Plan

* A link to a Trello board for the project
* A link to a spreadsheet that includes the original and final project plan>

## Instructions

<TODO:  
* Architectural Diagram (Shows how key parts of the system work)>

<TODO:  Instructions for running the Python project.  How could a user with no context run this project without asking you for any help.  Include screenshots with explicit steps to create that work. Be sure to at least include the following screenshots:

* Project running on Azure App Service

* Project cloned into Azure Cloud Shell

* Passing tests that are displayed after running the `make all` command from the `Makefile`

* Output of a test run

* Successful deploy of the project in Azure Pipelines.  [Note the official documentation should be referred to and double checked as you setup CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).

* Running Azure App Service from Azure Pipelines automatic deployment

* Successful prediction from deployed flask app in Azure Cloud Shell.  [Use this file as a template for the deployed prediction](https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code/blob/master/C2-AgileDevelopmentwithAzure/project/starter_files/flask-sklearn/make_predict_azure_app.sh).
The output should look similar to this:

```bash
udacity@Azure:~$ ./make_predict_azure_app.sh
Port: 443
{"prediction":[20.35373177134412]}
```

* Output of streamed log files from deployed application

> 

## Enhancements

<TODO: A short description of how to improve the project in the future>

## Demo 

<TODO: Add link Screencast on YouTube>

# Passing GitHub Actions Build
![image](https://user-images.githubusercontent.com/89496176/158027589-48a6dab7-f8f7-43c5-bfa2-31a030de7ff2.png)


[![Python application test with Github Actions](https://github.com/Jake4PCAPS/azure-pipeline/actions/workflows/pythonapp.yml/badge.svg)](https://github.com/Jake4PCAPS/azure-pipeline/actions/workflows/pythonapp.yml)
