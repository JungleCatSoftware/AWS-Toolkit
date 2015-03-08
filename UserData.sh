#!/bin/bash
maintainer=JungleCatSoftware
repo=AWS-Toolkit
release=0.0.1
targetdir=/opt/${maintainer}
mkdir -p ${targetdir} &&\
curl -L https://github.com/${maintainer}/${repo}/archive/${release}.tar.gz |\
tar -xz -C ${targetdir} &&\
mv ${targetdir}/${repo}-${release} ${targetdir}/${repo}
${targetdir}/${repo}/scripts/run.sh
