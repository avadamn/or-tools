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
	@echo "make docker_<distro>: Build image containing or-tools and its prerequisite."
	@echo "make bash_<distro>: Run container using the docker_<distro> image."
	@echo "make test_<distro>: Test OR-Tools archive for all specified language for the specified <distro>."
	@echo "make test_<distro>_<lang>: Test OR-Tools archive for the specified <distro> and <lang>."
	@echo "make bash_<distro>_<lang>: Run container using the docker_<distro>_<lang> image."
	@echo
	@echo "make test_<distro>_<language>: Test OR-Tools archive on <distro> distro for <language> language."
	@echo "make clean: Clean all docker images but keep archives (aka don\'t touch export directory)."
	@echo "make distclean: Clean all docker images and remove all archives."
	@echo

#################
###  DELIVERY  ##
#################
.PHONY: delivery
delivery: archives python
#
.PHONY: archives
archives: build
#	centos-7-archive \
#	debian-9-archive \
#	ubuntu-14.04-archive \
#	ubuntu-16.04-archive \
#	ubuntu-17.10-archive

.PHONY: python
python: manylinux1-pypi

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
# keep all intermediate files
# src: https://www.gnu.org/software/make/manual/html_node/Special-Targets.html
.SECONDARY:

.PHONY: test_delivery
test_delivery: test_archives test_python

.PHONY: test_python
test_python:
	echo ToDo !!!

include ../../Version.txt
OR_TOOLS_PATCH := $(shell git rev-list --count HEAD)
OR_TOOLS_VERSION := $(OR_TOOLS_MAJOR).$(OR_TOOLS_MINOR).$(OR_TOOLS_PATCH)
$(info version: $(OR_TOOLS_VERSION))
OR_TOOLS_BRANCH := $(shell git rev-parse --abbrev-ref HEAD)
$(info branch: $(OR_TOOLS_BRANCH))
IMAGE := or-tools
DOCKER_RUN_CMD := docker run --rm -it
#DOCKER_BUILD_CMD := docker build --no-cache
DOCKER_BUILD_CMD := docker build

# Docker
.PHONY: docker \
docker_centos-7 \
docker_debian-9 \
docker_ubuntu-14.04 \
docker_ubuntu-16.04 \
docker_ubuntu-17.10
docker: docker_centos-7 docker_debian-9 docker_ubuntu-14.04 docker_ubuntu-16.04 docker_ubuntu-17.10
docker_centos-7: export/docker_centos-7.tar
docker_debian-9: export/docker_debian-9.tar
docker_ubuntu-14.04: export/docker_ubuntu-14.04.tar
docker_ubuntu-16.04: export/docker_ubuntu-16.04.tar
docker_ubuntu-17.10: export/docker_ubuntu-17.10.tar
export/docker_%.tar: %.Dockerfile | export
	-docker image rm -f $(IMAGE)_$*:devel 2>/dev/null
	$(DOCKER_BUILD_CMD) --build-arg SRC_GIT_BRANCH=$(OR_TOOLS_BRANCH) -t $(IMAGE)_$*:devel -f $< .
	docker save $(IMAGE)_$*:devel -o $@

# Docker Bash
.PHONY: bash_centos-7 bash_debian-9 bash_ubuntu-14.04 bash_ubuntu-16.04 bash_ubuntu-17.10
bash_centos-7: export/docker_centos-7.tar
	$(DOCKER_RUN_CMD) $(IMAGE)_centos-7:devel /bin/bash
bash_debian-9: export/docker_debian-9.tar
	$(DOCKER_RUN_CMD) $(IMAGE)_debian-9:devel /bin/bash
bash_ubuntu-14.04: export/docker_ubuntu-14.04.tar
	$(DOCKER_RUN_CMD) $(IMAGE)_ubuntu-14.04:devel /bin/bash
bash_ubuntu-16.04: export/docker_ubuntu-16.04.tar
	$(DOCKER_RUN_CMD) $(IMAGE)_ubuntu-16.04:devel /bin/bash
bash_ubuntu-17.10: export/docker_ubuntu-17.10.tar
	$(DOCKER_RUN_CMD) $(IMAGE)_ubuntu-17.10:devel /bin/bash

# Build Archive
.PHONY: build \
build_centos-7 \
build_debian-9 \
build_ubuntu-14.04 \
build_ubuntu-16.04 \
build_ubuntu-17.10
build: build_centos-7 build_debian-9 build_ubuntu-14.04 build_ubuntu-16.04 build_ubuntu-17.10
build_centos-7: export/$(IMAGE)_centos-7_v$(OR_TOOLS_VERSION).tar.gz
build_debian-9: export/$(IMAGE)_debian-9_v$(OR_TOOLS_VERSION).tar.gz
build_ubuntu-14.04: export/$(IMAGE)_ubuntu-14.04_v$(OR_TOOLS_VERSION).tar.gz
build_ubuntu-16.04: export/$(IMAGE)_ubuntu-16.04_v$(OR_TOOLS_VERSION).tar.gz
build_ubuntu-17.10: export/$(IMAGE)_ubuntu-17.10_v$(OR_TOOLS_VERSION).tar.gz
export/$(IMAGE)_%_v$(OR_TOOLS_VERSION).tar.gz: export/docker_%.tar | export/%
	@docker load -i $<
	$(DOCKER_RUN_CMD) -w /root/or-tools -v `pwd`/export:/export $(IMAGE)_$*:devel /bin/sh -c \
		"git pull; \
     make clean; \
     make all -j 5; \
     make test; \
     make archive fz_archive; \
     cp *.tar.gz /export/$*"
	mv export/$*/$(IMAGE)_flatzinc_*.tar.gz export/$(IMAGE)_flatzinc_$*_v$(OR_TOOLS_VERSION).tar.gz
	mv export/$*/$(IMAGE)_*.tar.gz export/$(IMAGE)_$*_v$(OR_TOOLS_VERSION).tar.gz
	rmdir export/$*

# Test Archive
.PHONY: test \
test_centos-7 \
test_debian-9 \
test_ubuntu-14.04 \
test_ubuntu-16.04 \
test_ubuntu-17.10
test: test_centos-7 test_debian-9 test_ubuntu-14.04 test_ubuntu-16.04 test_ubuntu-17.10
test_centos-7: test_centos-7_cc test_centos-7_java test_centos-7_dotnet
test_debian-9: test_debian-9_cc test_debian-9_java test_debian-9_dotnet
test_ubuntu-14.04: test_ubuntu-14.04_cc test_ubuntu-14.04_java test_ubuntu-14.04_dotnet
test_ubuntu-16.04: test_ubuntu-16.04_cc test_ubuntu-16.04_java test_ubuntu-16.04_dotnet
test_ubuntu-17.10: test_ubuntu-17.10_cc test_ubuntu-17.10_java test_ubuntu-17.10_dotnet

.PHONY: test_centos-7_cc test_centos-7_java test_centos-7_dotnet
test_centos-7_cc: export/docker_centos-7_cc.tar
test_centos-7_java: export/docker_centos-7_java.tar
test_centos-7_dotnet: export/docker_centos-7_dotnet.tar

.PHONY: test_debian-9_cc test_debian-9_java test_debian-9_dotnet
test_debian-9_cc: export/docker_debian-9_cc.tar
test_debian-9_java: export/docker_debian-9_java.tar
test_debian-9_dotnet: export/docker_debian-9_dotnet.tar

.PHONY: test_ubuntu-14.04_cc test_ubuntu-14.04_java test_ubuntu-14.04_dotnet
test_ubuntu-14.04_cc: export/docker_ubuntu-14.04_cc.tar
test_ubuntu-14.04_java: export/docker_ubuntu-14.04_java.tar
test_ubuntu-14.04_dotnet: export/docker_ubuntu-14.04_dotnet.tar

.PHONY: test_ubuntu-16.04_cc test_ubuntu-16.04_java test_ubuntu-16.04_dotnet
test_ubuntu-16.04_cc: export/docker_ubuntu-16.04_cc.tar
test_ubuntu-16.04_java: export/docker_ubuntu-16.04_java.tar
test_ubuntu-16.04_dotnet: export/docker_ubuntu-16.04_dotnet.tar

.PHONY: test_ubuntu-17.10_cc test_ubuntu-17.10_java test_ubuntu-17.10_dotnet
test_ubuntu-17.10_cc: export/docker_ubuntu-17.10_cc.tar
test_ubuntu-17.10_java: export/docker_ubuntu-17.10_java.tar
test_ubuntu-17.10_dotnet: export/docker_ubuntu-17.10_dotnet.tar

export/docker_%_cc.tar: test/%/cc.Dockerfile export/$(IMAGE)_%_v$(OR_TOOLS_VERSION).tar.gz
	-docker image rm -f $(IMAGE)_$*:cc 2>/dev/null
	$(DOCKER_BUILD_CMD) -t $(IMAGE)_$*:cc -f $< export
	docker save $(IMAGE)_$*:cc -o $@
export/docker_%_java.tar: test/%/java.Dockerfile export/$(IMAGE)_%_v$(OR_TOOLS_VERSION).tar.gz
	-docker image rm -f $(IMAGE)_$*:java 2>/dev/null
	$(DOCKER_BUILD_CMD) -t $(IMAGE)_$*:java -f $< export
	docker save $(IMAGE)_$*:java -o $@
export/docker_%_dotnet.tar: test/%/dotnet.Dockerfile export/$(IMAGE)_%_v$(OR_TOOLS_VERSION).tar.gz
	-docker image rm -f $(IMAGE)_$*:dotnet 2>/dev/null
	$(DOCKER_BUILD_CMD) -t $(IMAGE)_$*:dotnet -f $< export
	docker save $(IMAGE)_$*:dotnet -o $@

# Docker test Bash
.PHONY: bash_centos-7_cc bash_centos-7_java bash_centos-7_dotnet
bash_centos-7_cc: export/docker_centos-7_cc.tar
	$(DOCKER_RUN_CMD) $(IMAGE)_centos-7:cc /bin/bash
bash_centos-7_java: export/docker_centos-7_java.tar
	$(DOCKER_RUN_CMD) $(IMAGE)_centos-7:java /bin/bash
bash_centos-7_dotnet: export/docker_centos-7_dotnet.tar
	$(DOCKER_RUN_CMD) $(IMAGE)_centos-7:dotnet /bin/bash

.PHONY: bash_debian-9_cc bash_debian-9_java bash_debian-9_dotnet
bash_debian-9_cc: export/docker_debian-9_cc.tar
	$(DOCKER_RUN_CMD) $(IMAGE)_debian-9:cc /bin/bash
bash_debian-9_java: export/docker_debian-9_java.tar
	$(DOCKER_RUN_CMD) $(IMAGE)_debian-9:java /bin/bash
bash_debian-9_dotnet: export/docker_debian-9_dotnet.tar
	$(DOCKER_RUN_CMD) $(IMAGE)_debian-9:dotnet /bin/bash

.PHONY: bash_ubuntu-14.04_cc bash_ubuntu-14.04_java bash_ubuntu-14.04_dotnet
bash_ubuntu-14.04_cc: export/docker_ubuntu-14.04_cc.tar
	$(DOCKER_RUN_CMD) $(IMAGE)_ubuntu-14.04:cc /bin/bash
bash_ubuntu-14.04_java: export/docker_ubuntu-14.04_java.tar
	$(DOCKER_RUN_CMD) $(IMAGE)_ubuntu-14.04:java /bin/bash
bash_ubuntu-14.04_dotnet: export/docker_ubuntu-14.04_dotnet.tar
	$(DOCKER_RUN_CMD) $(IMAGE)_ubuntu-14.04:dotnet /bin/bash

.PHONY: bash_ubuntu-16.04_cc bash_ubuntu-16.04_java bash_ubuntu-16.04_dotnet
bash_ubuntu-16.04_cc: export/docker_ubuntu-16.04_cc.tar
	$(DOCKER_RUN_CMD) $(IMAGE)_ubuntu-16.04:cc /bin/bash
bash_ubuntu-16.04_java: export/docker_ubuntu-16.04_java.tar
	$(DOCKER_RUN_CMD) $(IMAGE)_ubuntu-16.04:java /bin/bash
bash_ubuntu-16.04_dotnet: export/docker_ubuntu-16.04_dotnet.tar
	$(DOCKER_RUN_CMD) $(IMAGE)_ubuntu-16.04:dotnet /bin/bash

.PHONY: bash_ubuntu-17.10_cc bash_ubuntu-17.10_java bash_ubuntu-17.10_dotnet
bash_ubuntu-17.10_cc: export/docker_ubuntu-17.10_cc.tar
	$(DOCKER_RUN_CMD) $(IMAGE)_ubuntu-17.10:cc /bin/bash
bash_ubuntu-17.10_java: export/docker_ubuntu-17.10_java.tar
	$(DOCKER_RUN_CMD) $(IMAGE)_ubuntu-17.10:java /bin/bash
bash_ubuntu-17.10_dotnet: export/docker_ubuntu-17.10_dotnet.tar
	$(DOCKER_RUN_CMD) $(IMAGE)_ubuntu-17.10:dotnet /bin/bash

# Export Dir
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

.PHONY: python-test
python-test: manylinux1-test

#############
##  CLEAN  ##
#############
.PHONY: clean
clean: clean_all_containers clean_all_images

.PHONY: clean_all_images
clean_all_images:
	-docker rmi `docker images -a -q`

.PHONY: clean_all_containers
clean_all_containers:
	-docker rm `docker ps -a -q`

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
