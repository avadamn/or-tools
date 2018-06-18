# General commands
.PHONY: help
help:
	@echo "Tools to generate various deliveries for linux distros"
	@echo "<distro>: debian-9, centos-7, ubuntu-14.04, ubuntu-16.04, ubuntu-17.10, all"
	@echo "<language>: cc, java, dotnet, all"
	@echo
	@echo "usage:"
	@echo "make help: Print this help."
	@echo "make delivery: Build 'archives' and 'python' targets."
	@echo "make test_delivery: Build 'test_archives' and 'test_python' targets."
	@echo
	@echo "make archives: Build all OR-Tools archives in export."
	@echo "make test_archives: Test all OR-Tools archives in export for each language."
	@echo "make python: Build manylinux python 'ortools' wheel packages (2.7, 3.5, 3.6)."
	@echo "make test_python: Test manylinux python 'ortools' wheel packages (2.7, 3.5, 3.6)."
	@echo
	@echo "make docker_<distro>: Build image containing or-tools with its third party prebuilt."
	@echo "make bash_<distro>: Run container using the docker_<distro> image."
	@echo "make archive_<distro>: Build OR-Tools archive for the specified <distro>."
	@echo "make docker_<distro>_<lang>: Build test image containing or-tools archive and <lang> prerequisites."
	@echo "make test_<distro>_<lang>: Test OR-Tools archive for the specified <distro> and <lang>."
	@echo "make bash_<distro>_<lang>: Run container using the docker_<distro>_<lang> image."
	@echo "make test_<distro>: Test OR-Tools archive for all specified language for the specified <distro>."
	@echo
	@echo "make test_<distro>_<language>: Test OR-Tools archive on <distro> distro for <language> language."
	@echo "make clean: Clean all docker images but keep archives (aka don\'t touch export directory)."
	@echo "make distclean: Clean all docker images and remove all archives."
	@echo

# keep all intermediate files e.g. export/docker_*.tar
# src: https://www.gnu.org/software/make/manual/html_node/Special-Targets.html
.SECONDARY:

OR_TOOLS_BRANCH := $(shell git rev-parse --abbrev-ref HEAD)
$(info branch: $(OR_TOOLS_BRANCH))
include ../../Version.txt
OR_TOOLS_PATCH := $(shell git rev-list --count HEAD)
OR_TOOLS_VERSION := $(OR_TOOLS_MAJOR).$(OR_TOOLS_MINOR).$(OR_TOOLS_PATCH)
$(info version: $(OR_TOOLS_VERSION))
DOCKER_RUN_CMD := docker run --rm -it --init
#DOCKER_BUILD_CMD := docker build --no-cache
DOCKER_BUILD_CMD := docker build

#################
###  DELIVERY  ##
#################
.PHONY: delivery
delivery: python archives

.PHONY: test_delivery
test_delivery: test_python test_archives

###############
###  PYTHON  ##
###############

.PHONY: python
python: manylinux1-pypi

# manylinux1 images
manylinux1-image: | export
	docker build -f manylinux1.Dockerfile -t or-tools_manylinux1 .

manylinux1-image-no-cache: | export
	docker build --no-cache -f manylinux1.Dockerfile -t or-tools_manylinux1 .

manylinux1-pypi: manylinux1-images
	docker run -v `pwd`/export:/export or-tools_manylinux1:latest /bin/bash -c \
		"/root/build/build-manylinux1.sh /root/src /root/build /export"

manylinux1-bash: manylinux1-image
	$(DOCKER_RUN_CMD) or-tools_manylinux1:latest /bin/bash

.PHONY: test_python
test_python: manylinux1-test

#################
###  ARCHIVES  ##
#################

# Create build docker images
.PHONY: docker \
docker_centos-7 \
docker_debian-9 \
docker_ubuntu-14.04 \
docker_ubuntu-16.04 \
docker_ubuntu-17.10
docker: \
docker_centos-7 \
docker_debian-9 \
docker_ubuntu-14.04 \
docker_ubuntu-16.04 \
docker_ubuntu-17.10
docker_centos-7: export/docker_centos-7.tar
docker_debian-9: export/docker_debian-9.tar
docker_ubuntu-14.04: export/docker_ubuntu-14.04.tar
docker_ubuntu-16.04: export/docker_ubuntu-16.04.tar
docker_ubuntu-17.10: export/docker_ubuntu-17.10.tar
export/docker_%.tar: %.Dockerfile ../Makefile.cc ../../ortools | export
	-docker image rm -f or-tools_$*:devel 2>/dev/null
	$(DOCKER_BUILD_CMD) --build-arg SRC_GIT_BRANCH=$(OR_TOOLS_BRANCH) -t or-tools_$*:devel -f $< .
	docker save or-tools_$*:devel -o $@

# Run container using build docker image
.PHONY: bash_centos-7 bash_debian-9 bash_ubuntu-14.04 bash_ubuntu-16.04 bash_ubuntu-17.10
bash_centos-7: export/docker_centos-7.tar
	$(DOCKER_RUN_CMD) or-tools_centos-7:devel /bin/bash
bash_debian-9: export/docker_debian-9.tar
	$(DOCKER_RUN_CMD) or-tools_debian-9:devel /bin/bash
bash_ubuntu-14.04: export/docker_ubuntu-14.04.tar
	$(DOCKER_RUN_CMD) or-tools_ubuntu-14.04:devel /bin/bash
bash_ubuntu-16.04: export/docker_ubuntu-16.04.tar
	$(DOCKER_RUN_CMD) or-tools_ubuntu-16.04:devel /bin/bash
bash_ubuntu-17.10: export/docker_ubuntu-17.10.tar
	$(DOCKER_RUN_CMD) or-tools_ubuntu-17.10:devel /bin/bash

# Build Archives
.PHONY: archive \
archive_centos-7 \
archive_debian-9 \
archive_ubuntu-14.04 \
archive_ubuntu-16.04 \
archive_ubuntu-17.10
archive: \
archive_centos-7 \
archive_debian-9 \
archive_ubuntu-14.04 \
archive_ubuntu-16.04 \
archive_ubuntu-17.10
archive_centos-7: export/or-tools_centos-7_v$(OR_TOOLS_VERSION).tar.gz
archive_debian-9: export/or-tools_debian-9_v$(OR_TOOLS_VERSION).tar.gz
archive_ubuntu-14.04: export/or-tools_ubuntu-14.04_v$(OR_TOOLS_VERSION).tar.gz
archive_ubuntu-16.04: export/or-tools_ubuntu-16.04_v$(OR_TOOLS_VERSION).tar.gz
archive_ubuntu-17.10: export/or-tools_ubuntu-17.10_v$(OR_TOOLS_VERSION).tar.gz
export/or-tools_%_v$(OR_TOOLS_VERSION).tar.gz: export/docker_%.tar | export/%
	@docker load -i $<
	$(DOCKER_RUN_CMD) -w /root/or-tools -v `pwd`/export:/export or-tools_$*:devel /bin/sh -c \
		"make test; make archive; cp *.tar.gz /export/$*"
	$(DOCKER_RUN_CMD) -w /root/or-tools -v `pwd`/export:/export or-tools_$*:devel /bin/sh -c \
		"make test_fz; make fz_archive; cp *.tar.gz /export/$*"
	mv export/$*/or-tools_flatzinc_*.tar.gz export/or-tools_flatzinc_$*_v$(OR_TOOLS_VERSION).tar.gz
	mv export/$*/or-tools_*.tar.gz export/or-tools_$*_v$(OR_TOOLS_VERSION).tar.gz
	rmdir export/$*

# Export Dir
export:
	mkdir export
# genric rule export/% prevent other rules
# e.g. export/%/dokcer.devel.tar -> need an exhaustive list
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

############
##  TEST  ##
############

# Create test docker image for each language
.PHONY: \
docker_centos-7_cc docker_centos-7_java docker_centos-7_dotnet \
docker_debian-9_cc docker_debian-9_java docker_debian-9_dotnet \
docker_ubuntu-14.04_cc docker_ubuntu-14.04_java docker_ubuntu-14.04_dotnet \
docker_ubuntu-16.04_cc docker_ubuntu-16.04_java docker_ubuntu-16.04_dotnet \
docker_ubuntu-17.10_cc docker_ubuntu-17.10_java docker_ubuntu-17.10_dotnet
docker_centos-7_cc: export/docker_centos-7_cc.tar
docker_centos-7_java: export/docker_centos-7_java.tar
docker_centos-7_donet: export/docker_centos-7_dotnet.tar
docker_debian-9_cc: export/docker_debian-9_cc.tar
docker_debian-9_java: export/docker_debian-9_java.tar
docker_debian-9_python: export/docker_debian-9_python.tar
docker_ubuntu-14.04_cc: export/docker_ubuntu-14.04_cc.tar
docker_ubuntu-14.04_java: export/docker_ubuntu-14.04_java.tar
docker_ubuntu-14.04_python: export/docker_ubuntu-14.04_python.tar
docker_ubuntu-16.04_cc: export/docker_ubuntu-16.04_cc.tar
docker_ubuntu-16.04_java: export/docker_ubuntu-16.04_java.tar
docker_ubuntu-16.04_python: export/docker_ubuntu-16.04_python.tar
docker_ubuntu-17.10_cc: export/docker_ubuntu-17.10_cc.tar
docker_ubuntu-17.10_java: export/docker_ubuntu-17.10_java.tar
docker_ubuntu-17.10_dotnet: export/docker_ubuntu-17.10_dotnet.tar
export/docker_%_cc.tar: test/%/cc.Dockerfile export/or-tools_%_v$(OR_TOOLS_VERSION).tar.gz
	-docker image rm -f or-tools_$*:cc 2>/dev/null
	$(DOCKER_BUILD_CMD) -t or-tools_$*:cc -f $< export
	docker save or-tools_$*:cc -o $@
export/docker_%_java.tar: test/%/java.Dockerfile export/or-tools_%_v$(OR_TOOLS_VERSION).tar.gz
	-docker image rm -f or-tools_$*:java 2>/dev/null
	$(DOCKER_BUILD_CMD) -t or-tools_$*:java -f $< export
	docker save or-tools_$*:java -o $@
export/docker_%_dotnet.tar: test/%/dotnet.Dockerfile export/or-tools_%_v$(OR_TOOLS_VERSION).tar.gz
	-docker image rm -f or-tools_$*:dotnet 2>/dev/null
	$(DOCKER_BUILD_CMD) -t or-tools_$*:dotnet -f $< export
	docker save or-tools_$*:dotnet -o $@

# Run container using test docker image for each language
.PHONY: bash_centos-7_cc bash_centos-7_java bash_centos-7_dotnet
bash_centos-7_cc: export/docker_centos-7_cc.tar
	$(DOCKER_RUN_CMD) or-tools_centos-7:cc /bin/bash
bash_centos-7_java: export/docker_centos-7_java.tar
	$(DOCKER_RUN_CMD) or-tools_centos-7:java /bin/bash
bash_centos-7_dotnet: export/docker_centos-7_dotnet.tar
	$(DOCKER_RUN_CMD) or-tools_centos-7:dotnet /bin/bash

.PHONY: bash_debian-9_cc bash_debian-9_java bash_debian-9_dotnet
bash_debian-9_cc: export/docker_debian-9_cc.tar
	$(DOCKER_RUN_CMD) or-tools_debian-9:cc /bin/bash
bash_debian-9_java: export/docker_debian-9_java.tar
	$(DOCKER_RUN_CMD) or-tools_debian-9:java /bin/bash
bash_debian-9_dotnet: export/docker_debian-9_dotnet.tar
	$(DOCKER_RUN_CMD) or-tools_debian-9:dotnet /bin/bash

.PHONY: bash_ubuntu-14.04_cc bash_ubuntu-14.04_java bash_ubuntu-14.04_dotnet
bash_ubuntu-14.04_cc: export/docker_ubuntu-14.04_cc.tar
	$(DOCKER_RUN_CMD) or-tools_ubuntu-14.04:cc /bin/bash
bash_ubuntu-14.04_java: export/docker_ubuntu-14.04_java.tar
	$(DOCKER_RUN_CMD) or-tools_ubuntu-14.04:java /bin/bash
bash_ubuntu-14.04_dotnet: export/docker_ubuntu-14.04_dotnet.tar
	$(DOCKER_RUN_CMD) or-tools_ubuntu-14.04:dotnet /bin/bash

.PHONY: bash_ubuntu-16.04_cc bash_ubuntu-16.04_java bash_ubuntu-16.04_dotnet
bash_ubuntu-16.04_cc: export/docker_ubuntu-16.04_cc.tar
	$(DOCKER_RUN_CMD) or-tools_ubuntu-16.04:cc /bin/bash
bash_ubuntu-16.04_java: export/docker_ubuntu-16.04_java.tar
	$(DOCKER_RUN_CMD) or-tools_ubuntu-16.04:java /bin/bash
bash_ubuntu-16.04_dotnet: export/docker_ubuntu-16.04_dotnet.tar
	$(DOCKER_RUN_CMD) or-tools_ubuntu-16.04:dotnet /bin/bash

.PHONY: bash_ubuntu-17.10_cc bash_ubuntu-17.10_java bash_ubuntu-17.10_dotnet
bash_ubuntu-17.10_cc: export/docker_ubuntu-17.10_cc.tar
	$(DOCKER_RUN_CMD) or-tools_ubuntu-17.10:cc /bin/bash
bash_ubuntu-17.10_java: export/docker_ubuntu-17.10_java.tar
	$(DOCKER_RUN_CMD) or-tools_ubuntu-17.10:java /bin/bash
bash_ubuntu-17.10_dotnet: export/docker_ubuntu-17.10_dotnet.tar
	$(DOCKER_RUN_CMD) or-tools_ubuntu-17.10:dotnet /bin/bash

# Test Archive
.PHONY: test_archives test_archives_cc test_archives_java test_archives_dotnet \
test_centos-7 \
test_debian-9 \
test_ubuntu-14.04 \
test_ubuntu-16.04 \
test_ubuntu-17.10
test_archives: \
test_centos-7 \
test_debian-9 \
test_ubuntu-14.04 \
test_ubuntu-16.04 \
test_ubuntu-17.10

test_archives_cc: \
test_centos-7_cc \
test_debian-9_cc \
test_ubuntu-14.04_cc \
test_ubuntu-16.04_cc \
test_ubuntu-17.10_cc

test_archives_java: \
test_centos-7_java \
test_debian-9_java \
test_ubuntu-14.04_java \
test_ubuntu-16.04_java \
test_ubuntu-17.10_java

test_archives_dotnet: \
test_centos-7_dotnet \
test_debian-9_dotnet \
test_ubuntu-14.04_dotnet \
test_ubuntu-16.04_dotnet \
test_ubuntu-17.10_dotnet

test_centos-7: test_centos-7_cc test_centos-7_java test_centos-7_dotnet
test_debian-9: test_debian-9_cc test_debian-9_java test_debian-9_dotnet
test_ubuntu-14.04: test_ubuntu-14.04_cc test_ubuntu-14.04_java test_ubuntu-14.04_dotnet
test_ubuntu-16.04: test_ubuntu-16.04_cc test_ubuntu-16.04_java test_ubuntu-16.04_dotnet
test_ubuntu-17.10: test_ubuntu-17.10_cc test_ubuntu-17.10_java test_ubuntu-17.10_dotnet

.PHONY: test_centos-7_cc test_centos-7_java test_centos-7_dotnet
test_centos-7_cc: export/test_centos-7_cc.log
test_centos-7_java: export/test_centos-7_java.log
test_centos-7_dotnet: export/test_centos-7_dotnet.log

.PHONY: test_debian-9_cc test_debian-9_java test_debian-9_dotnet
test_debian-9_cc: export/test_debian-9_cc.log
test_debian-9_java: export/test_debian-9_java.log
test_debian-9_dotnet: export/test_debian-9_dotnet.log

.PHONY: test_ubuntu-14.04_cc test_ubuntu-14.04_java test_ubuntu-14.04_dotnet
test_ubuntu-14.04_cc: export/test_ubuntu-14.04_cc.log
test_ubuntu-14.04_java: export/test_ubuntu-14.04_java.log
test_ubuntu-14.04_dotnet: export/test_ubuntu-14.04_dotnet.log

.PHONY: test_ubuntu-16.04_cc test_ubuntu-16.04_java test_ubuntu-16.04_dotnet
test_ubuntu-16.04_cc: export/test_ubuntu-16.04_cc.log
test_ubuntu-16.04_java: export/test_ubuntu-16.04_java.log
test_ubuntu-16.04_dotnet: export/test_ubuntu-16.04_dotnet.log

.PHONY: test_ubuntu-17.10_cc test_ubuntu-17.10_java test_ubuntu-17.10_dotnet
test_ubuntu-17.10_cc: export/test_ubuntu-17.10_cc.log
test_ubuntu-17.10_java: export/test_ubuntu-17.10_java.log
test_ubuntu-17.10_dotnet: export/test_ubuntu-17.10_dotnet.log

export/test_%_cc.log: export/docker_%_cc.tar
	@docker load -i $<
	$(DOCKER_RUN_CMD) or-tools_$*:cc /bin/sh -c "cd or-tools_*_v* && make test_cc" > $@
export/test_%_java.log: export/docker_%_java.tar
	@docker load -i $<
	$(DOCKER_RUN_CMD) or-tools_$*:java /bin/sh -c "cd or-tools_*_v* && make test_java" > $@
export/test_%_dotnet.log: export/docker_%_dotnet.tar
	@docker load -i $<
	$(DOCKER_RUN_CMD) or-tools_$*:dotnet /bin/sh -c "cd or-tools_*_v* && make test_dotnet" > $@

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
