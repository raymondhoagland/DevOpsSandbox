#! /bin/bash
serf agent -config-file /etc/serf/config.json &
salt-minion -d
redis-server &
