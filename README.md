# Pokémon Randomiser
## _devops-practical-project_

---
## Contents
* [Introduction](#introduction)
	* [Objective](#objective) 
	* [Outline](#outline) 
* [Project Plan](#project-plan)
	* [Continuous Integration Pipeline](#continuous-integration-pipeline)
	* [Risk Assessment](#risk-assessment)  
	* [Kanban Board](#kanban-board)
	* [Entity Diagram](#entity-diagram)
* [Development](#development)
	* [Unit Testing in VS Code](#unit-testing-in-vs-code)
	* [Unit Testing with CI server](#unit-testing-with-ci-server)
	* [Front-End](#front-end)
* [Footer](#footer)
	* [Future Improvements](#future-improvements)
	* [Author](#author)
	* [Acknowledgements](#acknowledgements)

<br><br>
## Introduction
---
<br>

### Objective

The overall objective with this project is the following: 

    - To create a service-orientated architecture for an application, composed of at least 4 services that work together.

#### Service 1

The core service – this will render the Jinja2 templates you need to interact with your application, it will also be responsible for communicating with the other 3 services, and finally for persisting some data in an SQL database.
<br>

#### Service 2 & 3

These will both generate a random “Object”.
<br>

#### Service 4

This service will also create an “Object” however this “Object” must be based upon the results of service #2 + #3 using some pre-defined rules.

<br>

### Outline

The application created for this project is a Pokémon randomiser. Just like in the original series of Pokémon games, users will be able to choose from 1 of 3 Poké Balls that appear on the screen, in which they will then receive a Pokémon. In this application, the Pokémon that the user receives will be generated completely randomly.

<br>

<br><br>

## Project Plan
---
<br>

### Continuous Integration Pipeline

The tech stack I used for this project is as follows: 

	- Kanban Board: Jira
    - Version Control: GitHub
    - CI Server: Jenkins
    - Configuration Management: Ansible
    - Cloud server: GCP Compute Engine
    - Containerisation: Docker Compose
    - Orchestration Tool: Docker Swarm
    - Reverse Proxy: NGINX

<br>

### Risk Assessment

<br>

### Kanban Board

<br>

### Entity Diagram

Here is the initial entity diagram for this application:

![Initial ED](./images/initial-ed.png)
<br><br>
Here is the final entity diagram:

![Final ED](./images/updated-ed.png)
<br><br>

## Development
---
<br>

### Jenkins Pipeline

![Jenkins Pipeline](./images/jenkins-pipeline.png)

### Unit Testing with CI server

Here is the testing output from the Jenkins pipeline, which shows 7 passed tests and 98% overall coverage.

![Test Output](./images/jenkins-test.png)
<br><br>

Here is the Cobertura coverage report, which shows the test coverage across all areas of the application:

![Cobertura](./images/cobertura.png)
<br><br>

Here is the JUnit test output, which reports 0 failures for every function in every test class:

![JUnit](./images/junit.png)
<br><br>

Here is the webhook configured to trigger a Jenkins build once there has been a push to GitHub. This allows for automated testing for every change that is made to the source code:

![GitHub Webhook](./images/github-webhook.png)
<br><br>

![Jenkins-side Webhook](./images/jenkins-webhook.png)

<br><br>

### Refactoring

[Insert here stuff about storing images locally to improve speed.]

[Insert here stuff about changing code for forms in application/routes to "order_attr" dictionary which simplified code and boosted test coverage]

[Delete Selenium and unnneccesary dependencies]
<br><br>

### Front-End

![Start Page](./images/start-page.png)
<br><br>

![Home Page](./images/home-page.png)
<br><br>

![Home Page 2](./images/home-page2.png)
<br><br>

![Home Page 3](./images/home-page3.png)

<br>

## Footer
---
<br>

### Future Improvements

<br>

### Author

Gavin Williams

<br>

### Acknowledgements

* [Oliver Nichols](https://github.com/OliverNichols/)
* Ryan Wright