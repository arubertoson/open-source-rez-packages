CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)


set(hdf5_version $ENV{REZ_BUILD_PROJECT_VERSION})
rez_set_archive(
    url_hdf5
    hdf5-${hdf5_version}.tar
    https://support.hdfgroup.org/ftp/HDF5/releases/hdf5-1.8/hdf5-${hdf5_version}/src/hdf5-${hdf5_version}.tar
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
    CONFIGURE_COMMAND 
        ${CMAKE_COMMAND}
        -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
        -DCMAKE_BUILD_TYPE=Release
        -DBUILD_SHARED_LIBS=OFF
        -DBUILD_TESTING=OFF
    INSTALL_COMMAND "${INSTALL}"
    BUILD_IN_SOURCE 1
    BUILD_COMMAND make -j$ENV{REZ_BUILD_THREAD_COUNT}
)
