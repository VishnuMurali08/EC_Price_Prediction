# EC_Price_Prediction
Scalable machine learning solution for predicting Executive Condominium prices at key milestones, using a Postgres database in Docker and a Python API for data-driven insights

# Executive Condominium Price Prediction
## Overview
This project develops a scalable machine learning solution to predict Executive Condominium (EC) prices in Singapore at critical time points—5 years after lease commencement (post Minimum Occupancy Period) and 10 years when ECs become privatized. The solution leverages a PostgreSQL database hosted in Docker and integrates data from the URA's private residential property transactions API.

## Current Progress
Database Setup and Data Integration

A PostgreSQL database has been set up within a Docker container.
Configured to import data from the URA’s private residential property transactions API.
Diagram of the data model included (please refer to data_model_diagram.pptx).
Machine Learning Model

A preliminary machine learning model has been trained to predict the price of ECs.
Currently, the model utilizes basic features extracted from the URA transaction data.

# Future Work

Develop a Python-based RESTful API to expose the ML model predictions.
Containerize the API using Docker for scalability and easy deployment.

## Cloud Deployment

Deploy the API to a cloud platform to allow for scalable access.
Provide a public URL for easy access to the API functionalities.
