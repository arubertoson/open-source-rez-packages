CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)


set(openexr_version $ENV{REZ_BUILD_PROJECT_VERSION})
message(${openexr_version})
rez_set_archive(
    url_ilmbase 
    openexr-${openexr_version}.tar.gz
    http://download.savannah.nongnu.org/releases/openexr/openexr-${openexr_version}.tar.gz
)


if(${REZ_BUILD_INSTALL})
  set(INSTALL make install)
else()
  set(INSTALL ${CMAKE_COMMAND} -E echo "Skipping install step...")
endif()

ExternalProject_add(
    openexr
    URL ${url_ilmbase}
    PREFIX openexr
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ./configure --prefix=${CMAKE_INSTALL_PREFIX} --with-pic --disable-ilmbasetest --with-ilmbase-prefix=$ENV{REZ_ILMBASE_ROOT}
    INSTALL_COMMAND "${INSTALL}"
    BUILD_IN_SOURCE 1
    BUILD_COMMAND make -j$ENV{REZ_BUILD_THREAD_COUNT}
)

