CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)


set(pyilmbase_version $ENV{REZ_BUILD_PROJECT_VERSION})
rez_set_archive(
    url_pyilmbase
    pyilmbase-${pyilmbase_version}.tar.gz
    https://github.com/openexr/openexr.git
)


# Python executable
EXECUTE_PROCESS(COMMAND python -c "\
import sys; print(sys.executable)"
  OUTPUT_VARIABLE PYTHON_EXECUTABLE
  )

# Python library
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


if(${REZ_BUILD_INSTALL})
  set(INSTALL make install)
else()
  set(INSTALL ${CMAKE_COMMAND} -E echo "Skipping install step...")
endif()

message("PYTHON ${PYTHON_EXECUTABLE}")
message("PYTHON ${PYTHON_INCLUDE_DIR}")
message("PYTHON ${PYTHON_LIBRARY}")
message("BOOOOST $ENV{REZ_BOOST_ROOT}")

set(BOOST_ROOT $ENV{REZ_BOOST_ROOT})
find_package(Boost COMPONENTS python)
message("BOOOST ${Boost_FOUND}")
message("BOOOST ${Boost_INCLUDE_DIR}")


ExternalProject_add(
    pyilmbase
    URL ${url_pyilmbase}
    PREFIX pyilmbase
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND 
        ${CMAKE_COMMAND}
        -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
        -DPYTHON_EXECUTABLE=~/.pyenv/versions/2.7.14/bin/python
        -DBOOST_ROOT=$ENV{REZ_BOOST_ROOT}
        -DILMBASE_PACKAGE_PREFIX=$ENV{REZ_ILMBASE_ROOT}
    INSTALL_COMMAND "${INSTALL}"
    BUILD_IN_SOURCE 1
    BUILD_COMMAND make -j$ENV{REZ_BUILD_THREAD_COUNT}
)

# install(CODE "message(STATUS Install Complete.)")
# ./configure --prefix=${CMAKE_INSTALL_PREFIX} --with-boost-include-dir=$ENV{REZ_BOOST_ROOT}/include --with-boost-lib-dir=$ENV{REZ_BOOST_ROOT}/lib --with-boost-python-libname=boost_python
        # -DLIB_TYPE=STATIC
