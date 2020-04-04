# Cloud DevOps Engineer Capstone Project

 Final project of the DevOps Udacity Nanodegree

## Introduction

In this project I will apply the skills and knowledge which were developed throughout the Cloud DevOps Nanodegree program. These include:

- Working in AWS
- Using Jenkins to implement Continuous Integration and Continuous Deployment
- Building pipelines
- Working with Ansible and CloudFormation to deploy clusters
- Building Kubernetes clusters
- Building Docker containers in pipelines

## Application

The application is my own Python script that generates HTML pages from Markdown files using a template. I use it to generate the blog posts on <https://blog.miguelangelnieto.net>. In this project there is one single page, named `index.md` that will be used as an example:

```
python3 html_generator.py 
```

By default it will convert all Markdown files to HTML.

## Jenkins Pipeline

To automate the publishing of the blog posts I have created a CI/CD pipeline with rolling deployment. The pipeline has these steps:

![Jenkins Pipeline](./doc/pipeline_steps.png "Logo Title Text 1")

**1. Python Req.**

The script's Python requirements are installed. They include `markdown`, `pylint` and `beautifulsoup4`.

**2. Python Lint**

Check the script's code with pylint. This is the output when the steps fails:



**2. Generage HTML**

The HEML pages are generated.

**3. Build & Push**
