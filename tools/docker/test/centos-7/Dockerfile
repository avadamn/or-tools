FROM centos:7
LABEL maintainer="corentinl@google.com"

RUN yum -y update

RUN yum groupinstall 'Development Tools'

ADD centos* .
RUN tar xzf centos*.tar.gz

