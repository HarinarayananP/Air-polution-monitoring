# POLMO - Advanced Air pollution monitoring system

[![License](https://img.shields.io/badge/License-Apache2-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0) [![Community](https://img.shields.io/badge/Join-Community-blue)](https://developer.ibm.com/callforcode/get-started/) ![GitHub last commit](https://img.shields.io/github/last-commit/HarinarayananP/Air-polution-monitoring) ![GitHub repo size](https://img.shields.io/github/repo-size/HarinarayananP/Air-polution-monitoring) [![Website](https://img.shields.io/badge/View-Website-blue)](#)

A basic GitHub repository example for new [Call for Code](https://developer.ibm.com/callforcode/) projects and those that join the Call for Code with The Linux Foundation deployment initiative. Not all sections or files are required. You can make this as simple or as in-depth as you need. And don't forget to [register for Call for Code 2021](https://developer.ibm.com/callforcode/get-started/)!


## Contents

- [Polmo Project](#polmo-advanced-air-pollution-monitoring-system)
  - [Contents](#contents)
  - [Short description](#short-description)
    - [What's the problem?](#whats-the-problem)
    - [How can technology help?](#how-can-technology-help)
    - [The idea](#the-idea)
  - [Demo video](#demo-video)
  - [The architecture](#the-architecture)
  - [Long description](#long-description)
  - [Project roadmap](#project-roadmap)
  - [Getting started](#getting-started)
  - [Live demo](#live-demo)
  - [Built with](#built-with)
  - [Contributing](#contributing)
  - [Authors](#authors)
  - [License](#license)

## Short description

### What's the problem?

Air pollution adversely affects human health, plant life, and agricultural crop production.  Agricultural crops can be injured when exposed to high concentrations of various air pollutants.  In a recent study, researchers have analysed 30 years of data on yields of wheat and rice alongside data on air pollution and climate in India and concluded that significant decreases in yield could be attributed to air pollutants.

### How can technology help?

Regular monitoring and controlling air pollution leads to increased yield from agricultural and livestock products. The warning can be given to farmers using pollution related predictions, precautions can be taken to protect plants, plan for the right cultivation time to get more yield.  There is an increased demand for localized IoT enabled automated air pollution monitoring systems which provide air pollution related information for people through an easy interface.  For realizing such a system gas sensors with advanced sensing technologies, IoT, cloud computing, and machine learning can be Incorporated.

### The idea

Developing and deploying low cost, low power, quicker, and real time air pollution monitoring system at pollution affected area. For this, array sensor nodes are developed by incorporating major air pollutants sensors and NodeMCU.  This embedded system uploads the air pollution data to the IBM Watson IoT cloud over Wi-Fi protocol. 

## Demo video

[![Watch the video](https://github.com/HarinarayananP/Air-polution-monitoring/blob/main/images/YT-Thumbnail.png)](https://youtu.be/6nTHpyTWLMA)

## The architecture

![Video transcription/translation app](https://developer.ibm.com/developer/tutorials/cfc-starter-kit-speech-to-text-app-example/images/cfc-covid19-remote-education-diagram-2.png)

1. The user navigates to the site and uploads a video file.
2. Watson Speech to Text processes the audio and extracts the text.
3. Watson Translation (optionally) can translate the text to the desired language.
4. The app stores the translated text as a document within Object Storage.

## Long description

[More detail is available here](./docs/DESCRIPTION.md)

## Project roadmap

The project currently does the following things.
- Sense Major Pollutants.
- Sent readings seperatly to IBM Watson IOT cloud.
- Display Realtime data at Webendpoint
- Provide API to fetch Realtime and historical data.

See below for our past road map before Call for Code 2021 submission.

![RoadmapSW](./images/Road-map-sw.png)
![RoadmapHW](./images/Road-map-hw.png)

## Getting started

In this section you add the instructions to run your project on your local machine for development and testing purposes. You can also add instructions on how to deploy the project in production.

- [Polmo Hardware](./'POLMO Sofware'/)
- [Polmo Software](./'POLMO Hardware'/)

## Live demo

Live demo link will be uploaded very soon.

## Built with

- [IBM Cloudant](https://cloud.ibm.com/catalog?search=cloudant#search_results) - The NoSQL database used
- [IBM Cloud Functions](https://cloud.ibm.com/catalog?search=cloud%20functions#search_results) - The compute platform for handing logic
- [IBM API Connect](https://cloud.ibm.com/catalog?search=api%20connect#search_results) - The FastAPI Web Framework


## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

<a href="https://github.com/HarinarayananP/Air-polution-monitoring/graphs/contributors">
</a>

- **Harinarayanan P** - [GitHub](https://github.com/HarinarayananP)
- **Amjed Ali K** - [GitHub](https://github.com/amjed-ali-k)

## License

This project is licensed under the Apache 2 License - see the [LICENSE](LICENSE) file for details.

## Acknoledgemnt

We sincerly inform our gratitudes to
- [Sebastián Ramírez] (https://github.com/tiangolo) - For FastAPI framework
- [Creative Tim] (https://www.creative-tim.com/) - For Argon free dashboard template
- [Webkom] (https://github.com/0wczar/airframe-react) - For a beautiful react Dashboard
- [Freepik] (https://freepik.com) - For design files and templates
- All family, friends, collegues who helped and appreciated us in this journey.
