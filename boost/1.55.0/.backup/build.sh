#! /bin/bash

if [[ ! -d "./boost_1_55_0" ]]; then
  wget http://sourceforge.net/projects/boost/files/boost/1.55.0/boost_1_55_0.tar.gz
  tar -xf boost_1_55_0.tar.gz
fi

# Check if install directory exists, if not build to it
if [[ ! -d "$REZ_BUILD_INSTALL_PATH" ]]; then
  mkdir -p $REZ_BUILD_INSTALL_PATH
fi 

echo $REZ_BUILD_INSTALL_PATH


cd boost_1_55_0
./bootstrap.sh --prefix=$REZ_BUILD_INSTALL_PATH
./bjam cxxflags=-fPIC --disable-icu -a install
cd ..
# cp package.py $REZ_BUILD_INSTALL_PATH

# ./clean.sh
