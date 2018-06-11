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

################
##  DELIVERY  ##
################
.PHONY: delivery
delivery: archives python

.PHONY: archives
archives: \
	centos-7-archive \
	debian-9-archive \
	ubuntu-14.04-archive \
	ubuntu-16.04-archive \
	ubuntu-17.10-archive

.PHONY: python
python: manylinux1-pypi

################
##  ARCHIVES  ##
################
export:
	mkdir export

# Ubuntu 14.04 images
ubuntu-14.04-image:
	docker build -f ubuntu-14.04.Dockerfile -t or-tools-ubuntu-14.04-image .

ubuntu-14.04-image-no-cache:
	docker build --no-cache -f ubuntu-14.04.Dockerfile -t or-tools-ubuntu-14.04-image .

ubuntu-14.04-archive: ubuntu-14.04-image | export
	docker run -w /root/or-tools -v `pwd`/export:/export or-tools-ubuntu-14.04-image:latest /bin/bash -c \
 "git pull; \
 make clean; \
 make all -j 5; \
 make test; \
 make archive fz_archive; \
 cp *.tar.gz /export"

ubuntu-14.04-test: export ubuntu-14.04-image
	docker run -w /root/or-tools -v `pwd`/export:/export or-tools-ubuntu-14.04-image:latest /bin/bash -c \
 "git pull; \
 make clean; \
 make all -j 5; \
 make test"

ubuntu-14.04-bash: export ubuntu-14.04-image
	docker run -it or-tools-ubuntu-14.04-image:latest /bin/bash

# Ubuntu 16.06 images
ubuntu-16.04-image:
	docker build -f ubuntu-16.04.Dockerfile -t or-tools-ubuntu-16.04-image .

ubuntu-16.04-image-no-cache:
	docker build --no-cache -f ubuntu-16.04.Dockerfile -t or-tools-ubuntu-16.04-image .

ubuntu-16.04-archive: ubuntu-16.04-image | export
	docker run -w /root/or-tools -v `pwd`/export:/export or-tools-ubuntu-16.04-image:latest /bin/bash -c \
 "git pull; \
 make clean; \
 make all -j 5; \
 make test; \
 make archive fz_archive; \
 cp *.tar.gz /export"

ubuntu-16.04-test: export ubuntu-16.04-image
	docker run -w /root/or-tools -v `pwd`/export:/export or-tools-ubuntu-16.04-image:latest /bin/bash -c \
 "git pull; \
 make clean; \
 make all -j 5; \
 make test"

ubuntu-16.04-bash: export ubuntu-16.04-image
	docker run -it or-tools-ubuntu-16.04-image:latest /bin/bash

# Ubuntu 17.10 images
ubuntu-17.10-image:
	docker build -f ubuntu-17.10.Dockerfile -t or-tools-ubuntu-17.10-image .

ubuntu-17.10-image-no-cache:
	docker build --no-cache -f ubuntu-17.10.Dockerfile -t or-tools-ubuntu-17.10-image .

ubuntu-17.10-archive: export ubuntu-17.10-image
	docker run -w /root/or-tools -v `pwd`/export:/export or-tools-ubuntu-17.10-image:latest /bin/bash -c \
		"git pull; \
		make clean; \
		make all -j 5; \
		make test; \
		make archive fz_archive; \
		cp *.tar.gz /export"

ubuntu-17.10-test: export ubuntu-17.10-image
	docker run -w /root/or-tools -v `pwd`/export:/export or-tools-ubuntu-17.10-image:latest /bin/bash -c \
		"git pull; \
		make clean; \
		make all -j 5; \
		make test"

# Debian 9 images
debian-9-image:
	docker build -f debian-9.Dockerfile -t or-tools-debian-9-image .

debian-9-image-no-cache:
	docker build --no-cache -f debian-9.Dockerfile -t or-tools-debian-9-image .

debian-9-archive: export debian-9-image
	docker run -w /root/or-tools -v `pwd`/export:/export or-tools-debian-9-image:latest /bin/bash -c \
		"git pull; \
		make clean; \
		make all -j 5; \
		make test; \
		make archive fz_archive; \
		cp *.tar.gz /export"

debian-9-test: export debian-9-image
	docker run -w /root/or-tools -v `pwd`/export:/export or-tools-debian-9-image:latest /bin/bash -c \
		"git pull; \
		make clean; \
		make all -j 5; \
		make test"

# Centos 7 images
%-image: %.Dockerfile
	docker build -f $< -t or-tools-$* .

%-image-no-cache: %.Dockerfile
	docker build --no-cache -f $< -t or-tools-$* .

%-bash: %-image
	docker run -it or-tools-$*:latest /bin/bash

%-archive: %-image | export
	docker run -w /root/or-tools -v `pwd`/export:/export or-tools-$*:latest /bin/bash -c \
 "git pull; \
 make clean; \
 make all -j 5; \
 make test; \
 make archive fz_archive; \
 cp *.tar.gz /export"

%-test: %-image | export
	docker run -w /root/or-tools -v `pwd`/export:/export or-tools-$*:latest /bin/bash -c \
 "git pull; \
 make clean; \
 make all -j 5; \
 make test"

# manylinux1 images
manylinux1-image:
	docker build -f manylinux1.Dockerfile -t or-tools-manylinux1-image .

manylinux1-image-no-cache:
	docker build --no-cache -f manylinux1.Dockerfile -t or-tools-manylinux1-image .

manylinux1-pypi: export manylinux1-image
	docker run -v `pwd`/export:/export or-tools-manylinux1-image:latest /bin/bash -c \
		"/root/build/build-manylinux1.sh /root/src /root/build /export"

manylinux1-bash: export manylinux1-image
	docker run --rm -it --init or-tools-manylinux1-image:latest /bin/bash

############
##  TEST  ##
############
.PHONY: test_delivery
test_delivery: test_archives test_python

.PHONY: test_python
test_python:
	echo ToDo !!!

-include generated.mk

#DISTROLIST = centos-7 debian-9 ubuntu-14.04 ubuntu-16.04 ubuntu-17.10
DISTROLIST = centos-7
#LANGLIST = cc java dotnet
LANGLIST = cc

generated.mk: Makefile
	-@rm -f $@
# Generate the meta rules
	@echo -n "test_archives: generated.mk" > $@;
	@for distro in $(DISTROLIST) ; do \
  for lang in $(LANGLIST) ; do \
    echo -n " test_$${distro}-archive_$${lang}"; \
  done >> $@; \
done
	@echo "" >> $@;
	@echo "" >> $@;
# Generate all test inside containers rules
	@for distro in $(DISTROLIST) ; do \
  for lang in $(LANGLIST) ; do \
    echo "test_$${distro}-archive_$${lang}: $${distro}-archive"; \
    echo "	docker build -f test/$${distro}/$${lang}.Dockerfile -t $${distro}_$${lang}:testing export"; \
    echo ""; \
  done >> $@; \
done

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
