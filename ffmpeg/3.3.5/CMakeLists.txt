CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)


set(ffmpeg_version $ENV{REZ_BUILD_PROJECT_VERSION})
rez_set_archive(
    url_ffmpeg
    n${ffmpeg_version}.tar.gz
    https://github.com/FFmpeg/FFmpeg/archive/n${ffmpeg_version}.tar.gz
)


if(${REZ_BUILD_INSTALL})
  set(INSTALL make install)
else()
  set(INSTALL ${CMAKE_COMMAND} -E echo "Skipping install step...")
endif()


ExternalProject_add(
    ffmpeg
    URL ${url_ffmpeg}
    PREFIX ffmpeg
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ./configure --prefix=${CMAKE_INSTALL_PREFIX} --enable-shared
    INSTALL_COMMAND "${INSTALL}"
    BUILD_IN_SOURCE 1
    BUILD_COMMAND make -j$ENV{REZ_BUILD_THREAD_COUNT}
)
