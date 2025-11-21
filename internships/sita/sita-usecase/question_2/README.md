# SITA use case — data science and data engineering technical test

This repository contains my technical assignment for the SITA for Aircraft data science team. The objective of this test was to assess both data science (data processing, feature engineering, modeling) and data engineering (packaging, API development, deployment) skills.

## Repository structure

sita-usecase/
|
├── question_1/
│ └── question_1.ipynb
|
├── question_2/
│
│ ├── question2_api/
│ │ ├── app.py
│ │ ├── Dockerfile
│ │ └── requirements.txt
│ │
│ ├── question2_package/
│ │ ├── dist/
│ │ ├── question2/
│ │ ├── question2.egg-info/
│ │ ├── setup.py
│ │ └── requirements.txt
│ │
│ └── question2_4.ipynb


## Technologies

- Python 3.7+
- pandas 1.2.4+
- scikit-learn
- Flask
- Docker

## Question 1 — data science task

The goal of this part was to build a fuel flow prediction model based on simulated flight signals.

### Data description

The dataset includes time-indexed signals for multiple flights, stored as pandas dataframes in pickle format. The signals include:

- Fuel flow (lbs/sec)
- Altitude (feet)
- Wind (knots)
- Speed (km/h)

Each dataframe has time as the index and flight numbers as columns.

### Work performed

- Loaded, parsed, and synchronized time-series signals across flights.
- Conducted exploratory data analysis and data cleaning.
- Selected appropriate features and engineered relevant variables.
- Built several fuel flow models:
  - Model 1: Fuel flow as a function of effective speed range at a constant altitude of 8000 feet.
  - Model 2: Fuel flow as a function of altitude in the range [0, 15000] feet at a constant speed of 665 km/h.
  - Model 3 (bonus): Multivariate model combining speed and altitude.

### Results

- Performed feature selection and regression modeling.
- Analyzed the physical relationship between fuel consumption, speed, and altitude.
- Built interpretable models that could potentially support operational fuel optimization.

## Question 2 — data engineering task

### Python packaging

- Packaged a Python module implementing both regression and classification pipelines.
- Created a package structure with setup scripts and dependency management for installation via pip.

### API development

- Developed a Flask REST API exposing the packaged functionalities.
- Implemented the following routes:
  - `/`: health check
  - `/functions`: returns the list of available functions
  - `/process`: trains a model and returns metrics and predictions
  - `/classification/process`: classification task endpoint
  - `/regression/process`: regression task endpoint

### Docker deployment

- Created a Dockerfile to build a containerized version of the API for deployment.
- The Docker image includes the packaged module, API server, and all dependencies.

### Asynchronous access discussion

- Provided a brief discussion on scalable asynchronous solutions in `question2_4.ipynb`.
- Considered solutions include multithreading, multiprocessing, and frameworks such as FastAPI, Uvicorn, and Gunicorn.

## Notes

This repository was developed as part of a technical evaluation and is structured to demonstrate practical skills in both data science and software engineering domains.
