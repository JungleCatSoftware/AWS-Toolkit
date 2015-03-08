#!/bin/bash

scriptroot=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
distro=$(lsb_release -i | sed -r 's/^Distributor ID:\W*(.*)$/\L\1/')
release=$(lsb_release -c | sed -r 's/^Codename:\W*(.*)$/\L\1/')

# Add global scripts directory
globalscripts="${scriptroot}/global"
if [ -d "${globalscripts}" ]; then
  PATH="${globalscripts}:${PATH}"
fi

# Add distro-specific scripts directory
distroscripts="${scriptroot}/${distro}/all"
if [ -d "${distroscripts}" ]; then
  PATH="${distroscripts}:${PATH}"
fi

# Add release-specific scripts directory
releasescripts="${scriptroot}/${distro}/${release}"
if [ -d "${releasescripts}" ]; then
  PATH="${releasescripts}:${PATH}"
fi

