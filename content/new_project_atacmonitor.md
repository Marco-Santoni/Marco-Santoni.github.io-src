Title: Monitoring Bus Frequencies in Rome
Date: 2017-01-21 18:00
Slug: monitoring_bus_frequencies_in_rome
Status: published

I have just launched [atacmonitor](http://atacmonitor.com/). It is a website providing information about the waiting time at bus stops in Rome.

![Waiting times]({filename}/images/atacmonitor.gif)

## Overview

The datasource is live data about bus waiting time of ATAC, Rome's public transport company. The transport office provides [public API](https://romamobilita.it/it/azienda/open-data/api-real-time) with real-time data.

I have implemented a [simple application](https://github.com/Marco-Santoni/atacmonitor-data) that is regularly pulling such data and storing it in a PostgreSQL database. The data is presented via AirBnB's [Supereset](http://airbnb.io/superset/), an open source visualization platform. I deployed such application via [Heroku](www.heroku.com) PaaS.

I have kicked-off the project and just few bus stops are being monitored. The goal is to have all bus stops monitored soon.
