#!/bin/bash

kubectl run webserver --replicas=1 --labels='app=webserver' --image=628641662978.dkr.ecr.eu-west-1.amazonaws.com/capstone --port=80
kubectl get pods -o wide
kubectl create -f loadbalancer.yaml
kubectl get service/loadbalancer -o wide
