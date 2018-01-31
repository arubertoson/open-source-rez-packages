CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)


set(hdf5_version $ENV{REZ_BUILD_PROJECT_VERSION})
rez_set_archive(
    url_hdf5
    hdf5-${hdf5_version}.tar
    https://support.hdfgroup.org/ftp/HDF5/releases/hdf5-1.8/hdf5-1.8.9/src/hdf5-${hdf5_version}.tar
)


if(${REZ_BUILD_INSTALL})
  set(INSTALL make install)
else()
  set(INSTALL ${CMAKE_COMMAND} -E echo "Skipping install step...")
endif()

ExternalProject_add(
    hdf5
    URL ${url_hdf5}
    PREFIX hdf5
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ./configure --prefix=${CMAKE_INSTALL_PREFIX} --with-pic --disable-shared --disable-debug --enable-threadsafe
    INSTALL_COMMAND "${INSTALL}"
    BUILD_IN_SOURCE 1
    BUILD_COMMAND make -j$ENV{REZ_BUILD_THREAD_COUNT}
)

