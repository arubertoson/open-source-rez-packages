CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)


set(ilmbase_version $ENV{REZ_BUILD_PROJECT_VERSION})
rez_set_archive(
    url_ilmbase 
    ilmbase-${ilmbase_version}.tar.gz
    https://github.com/openexr/openexr.git
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
    CONFIGURE_COMMAND 
        ${CMAKE_COMMAND}
        -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
        -DBUILD_SHARED_LIBS=OFF
    INSTALL_COMMAND "${INSTALL}"
    BUILD_IN_SOURCE 1
    BUILD_COMMAND make -j$ENV{REZ_BUILD_THREAD_COUNT}
)
