# POLMO - Software
## Table of contents
- [POLMO - Software](#polmo---software)
  - [Table of contents](#table-of-contents)
  - [Polmo API Endpoint - FastAPI](#polmo-api-endpoint---fastapi)
    - [Visit API Endpoints Documentation](#visit-api-endpoints-documentation)
  - [Polmo Dashboard - React JS](#polmo-dashboard---react-js)
    - [Demo Login](#demo-login)
  - [Polmo Full WebApp - Flask webserver (Discontinued)](#polmo-full-webapp---flask-webserver-discontinued)

## Polmo API Endpoint - FastAPI
We used Fast API to get data from IBM Cloudant DB to public. Currently API Endpoint will only fetch realtime data, which is used to display on the dashboard. API Will be expanded and provided much more data fetching options. We also use a simple user database and support user registration and login using API Endpoint. JWT Authentication is used for session management.
<br />
Fast API is currently the fastest API app with validation. Sample code is uploaded [here](./Fast%20API%20-%20Backend/).

[![FastApi](https://img.shields.io/badge/FastAPI-v0.68.0-yellowgreen?logo=fastapi)](https://github.com/amjed-ali-k/Polmo-FastAPI-backend)
![GitHub top language](https://img.shields.io/github/languages/top/amjed-ali-k/Polmo-FastAPI-backend)
![GitHub issues](https://img.shields.io/github/issues/amjed-ali-k/Polmo-FastAPI-backend)
![GitHub](https://img.shields.io/github/license/amjed-ali-k/Polmo-FastAPI-backend)
![GitHub last commit](https://img.shields.io/github/last-commit/amjed-ali-k/Polmo-FastAPI-backend)

### Visit API Endpoints Documentation
[![SWaggerUI](https://img.shields.io/badge/Swagger%20UI-API%20Docs-%2385EA2D?logo=swagger)](https://6ejhix.deta.dev/docs)
[![Redoc](https://img.shields.io/badge/ReDoc-API%20Docs-%238CA1AF?logo=Read%20the%20Docs)](https://6ejhix.deta.dev/redoc)
[![Redoc](https://img.shields.io/badge/Visit-Website-%236BA539?logo=OpenAPI%20Initiative)](https://6ejhix.deta.dev)

## Polmo Dashboard - React JS
For realtime data visualization we made a dashboard using React framework. It will send API calls to the FastAPI backend and displays data realtime. Dashboard work is still in progress. Currently it only displays on Polmo Sensor node.

[![VisitWebsite](https://img.shields.io/badge/Visit-Website-a13d5e?style=social&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAixJREFUOE9Vk79rFEEUxz9vw0kQRPBHKaRQO0FJLyiC2hjQHAS9PbN38ZqITYyWnmBpLBQLJXd7ZhKJXqI2ohZiEdAq8Q8QG4s0QQu5eMjJPZmZ3c3esAw7M2/e+77v9zuCHeJmPzTZEKjrneAQ38aqLL22IemR//H3/Ac0GT9Yob1l14K6mCblM4LOVsScVU1P0io+pfhweCalWwrbkZrHaYEWZdNHi126B6ZZ7dgLLynu6jB8sYJZzsDbXDHhtKKPBJnpIW8L9I/1kQWB3UA5wpiYaFjprQiyGWFqDlMChCaXrwpBKwMoYGF7mIKqfg+Q3wonEB5EamYG6GtRuqTISo5OT0/Sj2XFV7OT3I1YqNu14wBRGloeE/SNPRe1ceroHEjg8ditm1XMXCbBvBT3DTH8BeWovyGukE2UqTuw1o0h5GQZsy1PqBUKdD8InHKXfb+JuF7ifDLXgedmNZKlosSETxG9lkU6DzjwiVlcP3nvZNwI3JOYyZG+/AsDDULQI5nJdipllvPI3MEvoB2ImryJJab0ELju2oA1Uf2q0BHYD1JLqP3UYev8DXn/d0fGxA2xls6BvAN6fXojU7zYTOVraPhR4LQKs1U19z1LmbTeNQ0u7AnY+1OFVxU1E0lex0mTcFxE26o6WpHFDSe1bS7nFZezQfhZ0NsRi2upS22oV+vP+g8OH69Lve/ga2Ll/CueJ5yYUrPsHllaJhGkxZXRSZ6vJ+I6ef8DHNju1CxiaEQAAAAASUVORK5CYII=)](https://polmo-react-app.vercel.app/)
![GitHub package.json dependency version (prod)](https://img.shields.io/github/package-json/dependency-version/amjed-ali-k/Polmo-react-app/react?logo=react)
![GitHub last commit](https://img.shields.io/github/last-commit/amjed-ali-k/Polmo-react-app)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/amjed-ali-k/Polmo-react-app)


### Demo Login
username: `test`
password: `test`

## Polmo Full WebApp - Flask webserver (Discontinued)
When the time of testing and collecting bulk data from Polmo Sensor node, we used a Flask webserver and Jinja Templating engine for displaying data. This was made for temporary use for analysing data.

Code Archive is [uploaded here](Flask%20Web%20server%20-%20Old/)

