CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)


set(pyilmbase_version $ENV{REZ_BUILD_PROJECT_VERSION})
rez_set_archive(
    url_pyilmbase
    pyilmbase-${pyilmbase_version}.tar.gz
    http://download.savannah.gnu.org/releases/openexr/pyilmbase-${pyilmbase_version}.tar.gz
)


if(${REZ_BUILD_INSTALL})
  set(INSTALL make install)
else()
  set(INSTALL ${CMAKE_COMMAND} -E echo "Skipping install step...")
endif()

message($ENV{REZ_BOOST_ROOT}/include)
message($ENV{REZ_BOOST_ROOT}/lib)

ExternalProject_add(
    pyilmbase
    URL ${url_pyilmbase}
    PREFIX pyilmbase
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ./configure --prefix=${CMAKE_INSTALL_PREFIX} --with-boost-include-dir=$ENV{REZ_BOOST_ROOT}/include --with-boost-lib-dir=$ENV{REZ_BOOST_ROOT}/lib --with-boost-python-libname=boost_python
    INSTALL_COMMAND "${INSTALL}"
    BUILD_IN_SOURCE 1
    BUILD_COMMAND make -j$ENV{REZ_BUILD_THREAD_COUNT}
)
