cmake_minimum_required (VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)


set(alembic_version $ENV{REZ_BUILD_PROJECT_VERSION})
rez_set_archive(
  url_alembic 
  ${alembic_version}.tar.gz
  https://github.com/alembic/alembic/archive/${alembic_version}.tar.gz
  )


# rez_find_packages(PREFIX pkgs AUTO)


# # make set stick in subdirectories:
# macro(set_option option value)
#   set(${option} ${value} CACHE INTERNAL "" FORCE)
# endmacro()
# # http://edsiper.linuxchile.cl/blog/2016/01/08/cmake-override-subdirectory-options/

# set_option(BOOST_ROOT $ENV{REZ_BOOST_ROOT})
# set_option(PYILMBASE_ROOT $ENV{REZ_PYILMBASE_ROOT})
# set_option(ALEMBIC_PYILMBASE_MODULE_DIRECTORY $ENV{REZ_PYILMBASE_ROOT}/lib64/python2.7/site-packages)
# set_option(ILMBASE_ROOT $ENV{REZ_ILMBASE_ROOT})
# set_option(USE_PYALEMBIC TRUE)
# set_option(USE_IEXMATH TRUE)
# set_option(LIBPYTHON_VERSION 2.7)
# set_option(BUILD_STATIC_LIBS FALSE)
# set_option(BUILD_SHARED_LIBS TRUE)

if(${REZ_BUILD_INSTALL})
  set(INSTALL make -j$ENV{REZ_BUILD_THREAD_COUNT} install)
else()
  set(INSTALL ${CMAKE_COMMAND} -E echo "Skipping install step...")
endif()


EXECUTE_PROCESS(COMMAND python -c "\
import sys; print(sys.executable)"
  OUTPUT_VARIABLE PYTHON_EXECUTABLE
  )
set_option(PYTHON_EXECUTABLE ${PYTHON_EXECUTABLE})


EXECUTE_PROCESS(COMMAND python -c "\
import os; import distutils.sysconfig as sysconfig; \
print(os.path.join(sysconfig.get_config_var('LIBDIR'), \
sysconfig.get_config_var('LDLIBRARY')))" 
  OUTPUT_VARIABLE PYTHON_LIBRARY
  )
set_option(PYTHON_LIBRARY ${PYTHON_LIBRARY})

# This command points to the python headers
EXECUTE_PROCESS(COMMAND 
  python -c "\
from distutils.sysconfig import get_python_inc; \
print(get_python_inc())"
  OUTPUT_VARIABLE PYTHON_INCLUDE_DIR
  )
set_option(PYTHON_INCLUDE_DIR ${PYTHON_INCLUDE_DIR})


set(PYTHON_EXECUTABLE ~/.pyenv/versions/2.7.14/bin/python)
message(${PYTHON_EXECUTABLE})
message($ENV{REZ_BUILD_PATH})
message(${CMAKE_INSTALL_PREFIX})

ExternalProject_add(
  alembic
  URL ${url_alembic}
  PREFIX alembic
  CONFIGURE_COMMAND
      env CC=${CMAKE_C_COMPILER} CXX=${CMAKE_CXX_COMPILER} ${CMAKE_COMMAND}
      -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
      -DCMAKE_CXXFLAGS=-Wno-deprecated-declarations
      -DILMBASE_ROOT=$ENV{REZ_ILMBASE_ROOT}
      -DBOOST_ROOT=$ENV{REZ_BOOST_ROOT}
      -DPYILMBASE_ROOT=$ENV{REZ_PYILMBASE_ROOT}
      -DLIBPYTHON_VERSION=2.7
      -DUSE_ARNOLD=OFF
      -DUSE_EXAMPLES=OFF
      -DUSE_MAYA=OFF
      -DUSE_OPENGL=OFF
      -DUSE_PRMAN=OFF
      -DUSE_TESTS=OFF
      -DUSE_HDF5=ON
      -DUSE_IEXMATH=ON
      -DUSE_PYALEMBIC=ON
      -DALEMBIC_PYILMBASE_MODULE_DIRECTORY=$ENV{REZ_PYILMBASE_ROOT}/lib64/python2.7/site-packages
  BUILD_IN_SOURCE 1
  BUILD_COMMAND make -j$ENV{REZ_BUILD_THREAD_COUNT}
  INSTALL_COMMAND ${INSTALL}
)
      # -DALEMBIC_GLEW_LINK_STATIC=ON

#       -DPYTHON_EXECUTABLE=$ENV{PYENV_ROOT}/versions/2.7.14/bin/python
#       -DPYTHON_INCLUDE_DIR=$ENV{PYENV_ROOT}/versions/2.7.14/include/python2.7
#       -DPYTHON_LIBRARY=$ENV{PYENV_ROOT}/versions/2.7.14/libpython2.7.a
# # set_option(CMAKE_SOURCE_DIR ${CMAKE_SOURCE_DIR}/alembic-1.5.8)
# # add_subdirectory("alembic-1.5.8")

      # -DALEMBIC_ILMBASE_LINK_STATIC=ON
      # -DALEMBIC_SHARED_LIBS=ON
      # -DALEMBIC_LIB_USES_BOOST=ON
      # -DALEMBIC_LIB_USES_TR1=OFF
