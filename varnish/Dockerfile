FROM ubuntu:14.04

EXPOSE 7496
EXPOSE 7373
EXPOSE 22
EXPOSE 80

# install basic deps
RUN apt-get update
RUN apt-get -y install nano wget unzip build-essential

# install serf
WORKDIR /tmp
RUN wget https://releases.hashicorp.com/serf/0.7.0/serf_0.7.0_linux_amd64.zip
RUN unzip serf_0.7.0_linux_amd64.zip && mv serf /usr/local/bin
ADD ./serf/config.json /etc/serf/config.json
ADD ./serf/event_handlers /etc/serf/event_handlers

# install salt
RUN wget -O - https://repo.saltstack.com/apt/ubuntu/14.04/amd64/latest/SALTSTACK-GPG-KEY.pub | sudo apt-key add -
RUN echo "deb http://repo.saltstack.com/apt/ubuntu/14.04/amd64/latest trusty main" > /etc/apt/sources.list.d/saltstack.list
RUN apt-get update
RUN apt-get install -y salt-master salt-minion salt-ssh salt-syndic salt-cloud salt-api

# install varnish
RUN apt-get -y install apt-transport-https curl
RUN curl https://repo.varnish-cache.org/GPG-key.txt | apt-key add -
RUN echo "deb https://repo.varnish-cache.org/ubuntu/ trusty varnish-4.1" \
     >> /etc/apt/sources.list.d/varnish-cache.list
RUN apt-get update
RUN apt-get -y install varnish
ADD ./deps/varnish /etc/default/varnish
ADD ./deps/user.vcl /etc/varnish/user.vcl

ADD ./deps/startup.sh /tmp/startup.sh
RUN chmod +x /tmp/startup.sh
CMD /tmp/startup.sh && /bin/bash
