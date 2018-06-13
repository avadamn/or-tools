FROM centos:7
LABEL maintainer="corentinl@google.com"

RUN yum -y update
RUN yum -y groupinstall 'Development Tools'

ADD or-tools_CentOS-7.5*.tar.gz .
RUN tar xzf or-tools_CentOS-7.5*.tar.gz .

