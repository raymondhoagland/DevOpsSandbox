#! /bin/bash
serf agent -config-file /etc/serf/config.json &
salt-minion &
cd /code && python app.py &
