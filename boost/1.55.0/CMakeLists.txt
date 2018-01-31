cmake_minimum_required(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)


set(boost_version $ENV{REZ_BUILD_PROJECT_VERSION})


# Look for already downloaded repos where REZ_REPO_PAYLOAD_DIR points to.
# There are no automatic downloads you would have to use the url to manually
# fetch it.
rez_set_archive(
  url_boost boost_1_55_0.tar.gz
  http://downloads.sourceforge.net/project/boost/boost/1.55.0/boost_1_55_0.tar.gz
  )


# NOTE: Should most likely live in a cmake module
# When using a system like pyenv finding the python location can be frustrating,
# using a python command we will get direct paths no matter what developing 
# environment we use for python, this specific command will get the full path 
# to the python library
EXECUTE_PROCESS(COMMAND python -c "\
import os; import distutils.sysconfig as sysconfig; \
print(os.path.join(sysconfig.get_config_var('LIBDIR'), \
sysconfig.get_config_var('LDLIBRARY')))" 
  OUTPUT_VARIABLE PYTHON_LIBRARY
  )

# This command points to the python headers
EXECUTE_PROCESS(COMMAND 
  python -c "\
from distutils.sysconfig import get_python_inc; \
print(get_python_inc())"
  OUTPUT_VARIABLE PYTHON_INCLUDE_DIR
  )

# build arguments for boosts build system
set(B2_ARGS 
  threading=multi 
  variant=release 
  link=static 
  runtime-link=shared 
  cxxflags=-fPIC 
  -q)


message(${REZ_BUILD_INSTALL})
if(${REZ_BUILD_INSTALL})
  set(install_cmd ./b2 ${B2_ARGS} --prefix=${CMAKE_INSTALL_PREFIX} install)
else()
  set(install_cmd "")
endif()

# Since boost has it's own build tools we use ExternalProject to create a build
# setup for cmake.
ExternalProject_add(
  boost
  URL ${url_boost}
  PREFIX boost
  UPDATE_COMMAND ""
  CONFIGURE_COMMAND ./bootstrap.sh --prefix=${CMAKE_INSTALL_PREFIX}
  INSTALL_COMMAND ${install_cmd}
  BUILD_IN_SOURCE 1
  BUILD_COMMAND ./b2 ${B2_ARGS} stage
  )
