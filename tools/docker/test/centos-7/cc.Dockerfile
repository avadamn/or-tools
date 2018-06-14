FROM centos:7
LABEL maintainer="corentinl@google.com"

RUN yum -y update && \
yum -y groupinstall 'Development Tools' && \
yum -y install which zlib-devel

WORKDIR /root

# automatically uncompress archive
# src: https://docs.docker.com/engine/reference/builder/#add
ADD or-tools_centos-7_v*.tar.gz .

#RUN cd or-tools_*_v* && \
#make cc
