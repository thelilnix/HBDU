#!/bin/bash

GREEN='\033[1;32m'
NO_COLOR='\033[0m'

echo -e "$GREEN 1 $NO_COLOR. Production(for release server)"
echo -e "$GREEN 2 $NO_COLOR. Development"
echo -n "Select your env> "
read env
export FLASK_APP=src/HBDU/
if [[ $env -eq 1 ]];then
    export FLASK_ENV=production
else
    export FLASK_ENV=development
fi
flask run
