#!/bin/bash
app="hbdu"
echo -n "Which port> "
read port
sudo docker build -t ${app} .
sudo docker run -p ${port}:80 --name=${app} ${app}
