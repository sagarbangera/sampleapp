#!/usr/bin/python

import os

strToSearch="<h2>This application was deployed using AWS CodeDeploy.</h2>"

strToReplace="<h2>This page for " + os.environ['APPLICATION_NAME'] + " application and " + os.environ['DEPLOYMENT_GROUP_NAME'] + " deployment group with " + os.environ['DEPLOYMENT_GROUP_ID'] +  "deployment group id was generated by a " + os.environ['LIFECYCLE_EVENT'] + " script during " + os.environ['DEPLOYMENT_ID'] + " deployment.</h2>"

fp=open("/var/www/html/index.html","r")
buffer=fp.read()
fp.close()

fp=open("/var/www/html/index.html","w")
fp.write(buffer.replace(strToSearch,strToReplace))
fp.close()