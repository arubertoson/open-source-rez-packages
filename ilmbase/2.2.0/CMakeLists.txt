CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)


set(ilmbase_version $ENV{REZ_BUILD_PROJECT_VERSION})
rez_set_archive(
    url_ilmbase 
    ilmbase-${ilmbase_version}.tar.gz
    http://download.savannah.nongnu.org/releases/openexr/ilmbase-${ilmbase_version}.tar.gz
)


if(${REZ_BUILD_INSTALL})
  set(INSTALL make install)
else()
  set(INSTALL ${CMAKE_COMMAND} -E echo "Skipping install step...")
endif()

ExternalProject_add(
    ilmbase
    URL ${url_ilmbase}
    PREFIX ilmbase
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ./configure --prefix=${CMAKE_INSTALL_PREFIX} --disable-shared --with-pic
    INSTALL_COMMAND "${INSTALL}"
    BUILD_IN_SOURCE 1
    BUILD_COMMAND make -j$ENV{REZ_BUILD_THREAD_COUNT}
)

