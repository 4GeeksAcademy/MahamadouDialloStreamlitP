# ML web app with Streamlit: diabetes prediction

## Introduction

This repository contains the minimum requirements to get a web application up and running using the model trained in one of our prior projects. The model deployed will be the diabetes prediction decision tree classifier. I have set-up much of the nit-picky configuration for you, but it is up to you to build the heart of the app and get it deployed to Render.

The project consists of three main parts:

1. **Model inference function**: This function is the heart of the app. You will write it in Python. It sends input data to the pre-trained model for inference and returns the prediction.
2. **[Streamlit](https://github.com/streamlit/streamlit)**: Streamlit is a framework to build and run web applications in python.
3. **[Render](https://render.com/)**: Render is the cloud hosting service we will use to actually run our application. This allows us to have a public URL where the application can be accessed by users.

## Render deployment

Once you have your application running in a codespace with no errors, it is time to deploy to Render. Go to [render.com](https://render.com/) and click 'Get started for free'. The site will ask for an email address and password and then send you a conformation link. After clicking the link, you are asked to fill out some basic profile details and finally taken to the 'service type' page on the Render Dashboard page. From there we create a new service for our application:

1. Choose 'New web service' from the service type dashboard tab
2. On the Configure tab, select 'Public Git Repository' and paste the link to your project repository
3. Click 'Connect'

This will take you to the new webservice's dashboard. Then, from the settings tab set the following values:

- **Name**: whatever you want
- **Project**: don't need to add to a project for a minimal deployment
- **Language**: Python 3
- **Branch**: main
- **Region**: Ohio (US east) - or whatever is closest to you
- **Root directory**: src
- **Build command**: pip install -r ../requirements.txt
- **Start command**: streamlit run app.py

Only real gotcha here is the root directory. Setting it to src means that Render will run all commands from there. This is what we want in the case of our application. But, since the requirements file is in the project home (i.e. one directory above src) we need to make sure we set the path right while pip installing.

After that, set the instance type to free, and you can leave everything else alone. Click 'Deploy Web Service'! You should see the requirements.txt being installed in the log terminal and then Streamlit starting. If there were no problems, you can now access your web app at the URL provided at the top of the page, under the project name and GitHub repository link.
