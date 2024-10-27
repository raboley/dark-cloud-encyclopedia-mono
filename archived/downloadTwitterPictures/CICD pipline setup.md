# Setup guide

This is meant to be a guide to follow the same steps to setup a fully automated CICD pipleline using docker and ansible to get things into the cloud. The steps will assume using a Mac.

## Initial setup

1. Install and update Brew

``` bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

1. Install Docker

``` bash
brew install docker-compose
brew install docker
brew install docker-machine
```

install python (2.7)

``` bash
brew install python
```

install ansible 2.0 or later

``` bash
pip install ansible --upgrade
```

install packages needed for ansible modules that will work to communicate with AWS

``` bash
pip install boto boto3
```

install aws command line tools

``` bash
pip install awscli
```

installing other tools

## creating a docker virtual machine

?? do I need to do this still?
docker-machine create --driver

## Setting up the sample application

install django, the web framework for python

``` bash
pip install django==1.9
```

next create a new django project

``` bash
django-admin startproject todobackend
```