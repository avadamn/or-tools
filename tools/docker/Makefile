# General commands
.PHONY: help
help:
	@echo "Tools to generate various deliveries for linux distros"
	@echo "<distro>: debian-9, centos-7, ubuntu-14.04, ubuntu-16.04, ubuntu-17.10, all"
	@echo "<language>: cc, java, dotnet, all"
	@echo
	@echo "usage:"
	@echo "make help: Print this help."
	@echo "make archives: Build all OR-Tools archives in export."
	@echo "make python: Build manylinux python 'ortools' wheel packages (2.7, 3.5, 3.6)."
	@echo "make delivery: Build 'archives' and 'python' targets."
	@echo
	@echo "make test_archives: Test OR-Tools archives for all supported <distro> for all supported <language>."
	@echo "make test_python: Test OR-Tools python wheel package archive."
	@echo "make test_delivery: Test 'archives' and 'python' targets."
	@echo
	@echo "make test_<distro>_<language>: Test OR-Tools archive on <distro> distro for <language> language."
	@echo "make clean: Clean all docker images but keep archives (aka don\'t touch export directory)."
	@echo "make distclean: Clean all docker images and remove all archives."
	@echo

#################
###  DELIVERY  ##
#################
#.PHONY: delivery
#delivery: archives python
#
#.PHONY: archives
#archives: \
#	centos-7-archive \
#	debian-9-archive \
#	ubuntu-14.04-archive \
#	ubuntu-16.04-archive \
#	ubuntu-17.10-archive
#
#.PHONY: python
#python: manylinux1-pypi
#
#################
###  ARCHIVES  ##
#################
#
## Ubuntu 14.04 images
#ubuntu-14.04-image:
#	docker build -f ubuntu-14.04.Dockerfile -t or-tools-ubuntu-14.04-image .
#
#ubuntu-14.04-image-no-cache:
#	docker build --no-cache -f ubuntu-14.04.Dockerfile -t or-tools-ubuntu-14.04-image .
#
#ubuntu-14.04-archive: ubuntu-14.04-image | export
#	docker run -w /root/or-tools -v `pwd`/export:/export or-tools-ubuntu-14.04-image:latest /bin/bash -c \
# "git pull; \
# make clean; \
# make all -j 5; \
# make test; \
# make archive fz_archive; \
# cp *.tar.gz /export"
#
#ubuntu-14.04-test: export ubuntu-14.04-image
#	docker run -w /root/or-tools -v `pwd`/export:/export or-tools-ubuntu-14.04-image:latest /bin/bash -c \
# "git pull; \
# make clean; \
# make all -j 5; \
# make test"
#
#ubuntu-14.04-bash: export ubuntu-14.04-image
#	docker run -it or-tools-ubuntu-14.04-image:latest /bin/bash
#
## Ubuntu 16.06 images
#ubuntu-16.04-image:
#	docker build -f ubuntu-16.04.Dockerfile -t or-tools-ubuntu-16.04-image .
#
#ubuntu-16.04-image-no-cache:
#	docker build --no-cache -f ubuntu-16.04.Dockerfile -t or-tools-ubuntu-16.04-image .
#
#ubuntu-16.04-archive: ubuntu-16.04-image | export
#	docker run -w /root/or-tools -v `pwd`/export:/export or-tools-ubuntu-16.04-image:latest /bin/bash -c \
# "git pull; \
# make clean; \
# make all -j 5; \
# make test; \
# make archive fz_archive; \
# cp *.tar.gz /export"
#
#ubuntu-16.04-test: export ubuntu-16.04-image
#	docker run -w /root/or-tools -v `pwd`/export:/export or-tools-ubuntu-16.04-image:latest /bin/bash -c \
# "git pull; \
# make clean; \
# make all -j 5; \
# make test"
#
#ubuntu-16.04-bash: export ubuntu-16.04-image
#	docker run -it or-tools-ubuntu-16.04-image:latest /bin/bash
#
## Ubuntu 17.10 images
#ubuntu-17.10-image:
#	docker build -f ubuntu-17.10.Dockerfile -t or-tools-ubuntu-17.10-image .
#
#ubuntu-17.10-image-no-cache:
#	docker build --no-cache -f ubuntu-17.10.Dockerfile -t or-tools-ubuntu-17.10-image .
#
#ubuntu-17.10-archive: export ubuntu-17.10-image
#	docker run -w /root/or-tools -v `pwd`/export:/export or-tools-ubuntu-17.10-image:latest /bin/bash -c \
#		"git pull; \
#		make clean; \
#		make all -j 5; \
#		make test; \
#		make archive fz_archive; \
#		cp *.tar.gz /export"
#
#ubuntu-17.10-test: export ubuntu-17.10-image
#	docker run -w /root/or-tools -v `pwd`/export:/export or-tools-ubuntu-17.10-image:latest /bin/bash -c \
#		"git pull; \
#		make clean; \
#		make all -j 5; \
#		make test"
#
## Debian 9 images
#debian-9-image:
#	docker build -f debian-9.Dockerfile -t or-tools-debian-9-image .
#
#debian-9-image-no-cache:
#	docker build --no-cache -f debian-9.Dockerfile -t or-tools-debian-9-image .
#
#debian-9-archive: export debian-9-image
#	docker run -w /root/or-tools -v `pwd`/export:/export or-tools-debian-9-image:latest /bin/bash -c \
#		"git pull; \
#		make clean; \
#		make all -j 5; \
#		make test; \
#		make archive fz_archive; \
#		cp *.tar.gz /export"
#
#debian-9-test: export debian-9-image
#	docker run -w /root/or-tools -v `pwd`/export:/export or-tools-debian-9-image:latest /bin/bash -c \
#		"git pull; \
#		make clean; \
#		make all -j 5; \
#		make test"
#
## Centos 7 images
#%-image: %.Dockerfile
#	docker build -f $< -t or-tools-$* .
#
#%-image-no-cache: %.Dockerfile
#	docker build --no-cache -f $< -t or-tools-$* .
#
#%-bash: %-image
#	docker run -it or-tools-$*:latest /bin/bash
#
#%-archive: %-image | export
#	docker run -w /root/or-tools -v `pwd`/export:/export or-tools-$*:latest /bin/bash -c \
# "git pull; \
# make clean; \
# make all -j 5; \
# make test; \
# make archive fz_archive; \
# cp *.tar.gz /export"
#
#%-test: %-image | export
#	docker run -w /root/or-tools -v `pwd`/export:/export or-tools-$*:latest /bin/bash -c \
# "git pull; \
# make clean; \
# make all -j 5; \
# make test"
#
## manylinux1 images
#manylinux1-image:
#	docker build -f manylinux1.Dockerfile -t or-tools-manylinux1-image .
#
#manylinux1-image-no-cache:
#	docker build --no-cache -f manylinux1.Dockerfile -t or-tools-manylinux1-image .
#
#manylinux1-pypi: export manylinux1-image
#	docker run -v `pwd`/export:/export or-tools-manylinux1-image:latest /bin/bash -c \
#		"/root/build/build-manylinux1.sh /root/src /root/build /export"
#
#manylinux1-bash: export manylinux1-image
#	docker run --rm -it --init or-tools-manylinux1-image:latest /bin/bash

############
##  TEST  ##
############
.PHONY: test_delivery
test_delivery: test_archives test_python

.PHONY: test_python
test_python:
	echo ToDo !!!

include ../../Version.txt
OR_TOOLS_PATCH := $(shell git rev-list --count HEAD)
OR_TOOLS_VERSION := $(OR_TOOLS_MAJOR).$(OR_TOOLS_MINOR).$(OR_TOOLS_PATCH)
$(info version: $(OR_TOOLS_VERSION))
IMAGE := or-tools

# Docker
.PHONY: docker docker_centos-7 docker_debian-9 docker_ubuntu-14.04 docker_ubuntu-16.04 docker_ubuntu-17.10
docker: docker_centos-7 docker_debian-9 docker_ubuntu-14.04 docker_ubuntu-16.04 docker_ubuntu-17.10
docker_centos-7: export/centos-7/docker_devel.tar
docker_debian-9: export/debian-9/docker_devel.tar
docker_ubuntu-14.04: export/ubuntu-14.04/docker_devel.tar
docker_ubuntu-16.04: export/ubuntu-16.04/docker_devel.tar
docker_ubuntu-17.10: export/ubuntu-17.10/docker_devel.tar
export/%/docker_devel.tar: %.Dockerfile | export/%
	@docker image rm -f ${IMAGE}_$*:devel 2>/dev/null
	docker build --no-cache -t ${IMAGE}_$*:devel -f $< .
	docker save ${IMAGE}_$*:devel -o $@

# Docker Bash
DOCKER_DEVEL_CMD := docker run --rm -it

.PHONY: bash_centos-7 bash_debian-9 bash_ubuntu-14.04 bash_ubuntu-16.04 bash_ubuntu-17.10
bash_centos-7: export/centos-7/docker_devel.tar
	${DOCKER_DEVEL_CMD} ${IMAGE}_centos-7:devel /bin/bash
bash_debian-9: export/debian-9/docker_devel.tar
	${DOCKER_DEVEL_CMD} ${IMAGE}_debian-9:devel /bin/bash
bash_ubuntu-14.04: export/ubuntu-14.04/docker_devel.tar
	${docker_devel_cmd} ${image}_ubuntu-14.04:devel /bin/bash
bash_ubuntu-16.04: export/ubuntu-16.04/docker_devel.tar
	${docker_devel_cmd} ${image}_ubuntu-16.04:devel /bin/bash
bash_ubuntu-17.10: export/ubuntu-17.10/docker_devel.tar
	${docker_devel_cmd} ${image}_ubuntu-17.10:devel /bin/bash

# Build Archive
.PHONY: build build_centos-7 build-debian-9 build-ubuntu-14.04 build-ubuntu-16.04 build-ubuntu-17.10
build: build_centos-7 build-debian-9 build-ubuntu-14.04 build-ubuntu-16.04 build-ubuntu-17.10
build_centos-7: export/centos-7/build.log
build_debian-9: export/debian-9/build.log
build_ubuntu-14.04: export/ubuntu-14.04/build.log
build_ubuntu-16.04: export/ubuntu-16.04/build.log
build_ubuntu-17.10: export/ubuntu-17.10/build.log
export/%/build.log: export/%/docker_devel.tar
	@docker load -i $<
	${DOCKER_DEVEL_CMD} -w /root/or-tools -v `pwd`/export:/export ${IMAGE}_$*:devel /bin/sh -c \
		"git pull; \
     make clean; \
     make all -j 5; \
     make test; \
     make archive fz_archive; \
     mv ${IMAGE}_flatzink_*.tar.gz /export/${IMAGE}_flatzink_$*_v${OR_TOOLS_VERSION}.tar.gz; \
     mv ${IMAGE}_*.tar.gz /export/${IMAGE}_$*_v${OR_TOOLS_VERSION}.tar.gz"
	@date > $@

# Test Archive
.PHONY: test test_centos-7 test-debian-9 test-ubuntu-14.04 test-ubuntu-16.04 test-ubuntu-17.10
test: test_centos-7 test-debian-9 test-ubuntu-14.04 test-ubuntu-16.04 test-ubuntu-17.10

.PHONY: test_centos-7_cc test_centos-7_java test_centos-7_dotnet
test_centos-7: test_centos-7_cc test_centos-7_java test_centos-7_dotnet
test_centos-7_cc: export/centos-7/docker_test_cc.tar
test_centos-7_java: export/centos-7/docker_test_java.tar
test_centos-7_dotnet: export/centos-7/docker_test_dotnet.tar

.PHONY: test_debian-9_cc test_debian-9_java test_debian-9_dotnet
test_debian-9: test_debian-9_cc test_debian-9_java test_debian-9_dotnet
test_debian-9_cc: export/debian-9/docker_test_cc.tar
test_debian-9_java: export/debian-9/docker_test_java.tar
test_debian-9_dotnet: export/debian-9/docker_test_dotnet.tar

.PHONY: test_ubuntu-14.04_cc test_ubuntu-14.04_java test_ubuntu-14.04_dotnet
test_ubuntu-14.04: test_ubuntu-14.04_cc test_ubuntu-14.04_java test_ubuntu-14.04_dotnet
test_ubuntu-14.04_cc: export/ubuntu-14.04/docker_test_cc.tar
test_ubuntu-14.04_java: export/ubuntu-14.04/docker_test_java.tar
test_ubuntu-14.04_dotnet: export/ubuntu-14.04/docker_test_dotnet.tar

.PHONY: test_ubuntu-16.04_cc test_ubuntu-16.04_java test_ubuntu-16.04_dotnet
test_ubuntu-16.04: test_ubuntu-16.04_cc test_ubuntu-16.04_java test_ubuntu-16.04_dotnet
test_ubuntu-16.04_cc: export/ubuntu-16.04/docker_test_cc.tar
test_ubuntu-16.04_java: export/ubuntu-16.04/docker_test_java.tar
test_ubuntu-16.04_dotnet: export/ubuntu-16.04/docker_test_dotnet.tar

.PHONY: test_ubuntu-17.10_cc test_ubuntu-17.10_java test_ubuntu-17.10_dotnet
test_ubuntu-17.10: test_ubuntu-17.10_cc test_ubuntu-17.10_java test_ubuntu-17.10_dotnet
test_ubuntu-17.10_cc: export/ubuntu-17.10/docker_test_cc.tar
test_ubuntu-17.10_java: export/ubuntu-17.10/docker_test_java.tar
test_ubuntu-17.10_dotnet: export/ubuntu-17.10/docker_test_dotnet.tar

export/%/docker_test_cc.tar: test/%/cc.Dockerfile /export/%/build.log
	@docker image rm -f ${IMAGE}_$*_cc:install 2>/dev/null
	docker build --no-cache -t ${IMAGE}_$*_cc:install -f $< export
	docker save ${IMAGE}_$*_cc:install -o $@
export/%/docker_test_java.tar: test/%/java.Dockerfile export/%/build.log
	@docker image rm -f ${IMAGE}_$*_java:install 2>/dev/null
	docker build --no-cache -t ${IMAGE}_$*_java:install -f $< export
	docker save ${IMAGE}_$*_java:install -o $@
export/%/docker_test_dotnet.tar: test/%/dotnet.Dockerfile export/%/build.log
	@docker image rm -f ${IMAGE}_$*_dotnet:install 2>/dev/null
	docker build --no-cache -t ${IMAGE}_$*_dotnet:install -f $< export
	docker save ${IMAGE}_$*_dotnet:install -o $@

export:
	mkdir export
# rule export/% prevent other rules e.g. export/%/dokcer.devel.tar
export/centos-7: | export
	mkdir export/centos-7
export/debian-9: | export
	mkdir export/debian-9
export/ubuntu-14.04: | export
	mkdir export/ubuntu-14.04
export/ubuntu-16.04: | export
	mkdir export/ubuntu-16.04
export/ubuntu-17.10: | export
	mkdir export/ubuntu-17.10

#-include generated.mk
##DISTROLIST = centos-7 debian-9 ubuntu-14.04 ubuntu-16.04 ubuntu-17.10
#DISTROLIST = centos-7
##LANGLIST = cc java dotnet
#LANGLIST = cc
#
#generated.mk: Makefile
#	-@rm -f $@
## Generate the meta rules
#	@echo -n "test_archives: generated.mk" > $@;
#	@for distro in $(DISTROLIST) ; do \
#  for lang in $(LANGLIST) ; do \
#    echo -n " test_$${distro}-archive_$${lang}"; \
#  done >> $@; \
#done
#	@echo "" >> $@;
#	@echo "" >> $@;
## Generate all test inside containers rules
#	@for distro in $(DISTROLIST) ; do \
#  for lang in $(LANGLIST) ; do \
#    echo "test_$${distro}-archive_$${lang}: $${distro}-archive"; \
#    echo "	docker build -f test/$${distro}/$${lang}.Dockerfile -t $${distro}_$${lang}:testing export"; \
#    echo ""; \
#  done >> $@; \
#done

.PHONY: python-test
python-test: manylinux1-test

#############
##  CLEAN  ##
#############
.PHONY: clean
clean: clean_all_images clean_all_containers
	-rm generated.mk

.PHONY: clean_all_images
clean_all_images:
	docker rmi `docker images -a -q`

.PHONY: clean_all_containers
clean_all_containers:
	docker rm `docker ps -a -q`

.PHONY: distclean
distclean: clean
	rm -rf export

#################
##  DEPRECATED ##
#################
.PHONY: images
images: \
	ubuntu-14.04-image \
	ubuntu-16.04-image \
	ubuntu-17.10-image \
	centos-7-image \
	debian-9-image \
	manylinux1-image

.PHONY: images-no-cache
images-no-cache: \
	ubuntu-14.04-image-no-cache \
	ubuntu-16.04-image-no-cache \
	ubuntu-17.10-image-no-cache \
	centos-7-image-no-cache \
	debian-9-image-no-cache
