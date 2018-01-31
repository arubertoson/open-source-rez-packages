#! /bin/bash

PACKAGE_INSTALLATION_ROOT="${HOME}/.rez/packages"
PACKAGE_NAME=ilmbase
PACKAGE_VERSION=2.2.0
PACKAGE_PLATFORM=platform-linux
PACKAGE_ARCH=arch-x86_64
MAKE_THREADS=28


INSTALL_DIRECTORY=$PACKAGE_INSTALLATION_ROOT/$PACKAGE_NAME/$PACKAGE_VERSION
if [[ ! -d "$INSTALL_DIRECTORY" ]]; then
  mkdir -p $INSTALL_DIRECTORY
fi

MANPATH=$(env | rg REZ_BUILD)
# Replace colons with spaces to create list.
for path in ${MANPATH// / }; do
    echo "$path"
done

# cd ilmbase-2.2.0
# ./configure --prefix=$INSTALL_DIRECTORY
# make -j$MAKE_THREADS
# make install -j$MAKE_THREADS
# cd ..
# cp package.py $INSTALL_DIRECTORY
