# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PrometheusCpp(CMakePackage):
    """Client Library for Modern C++."""

    homepage = "https://github.com/jupp0r/prometheus-cpp"
    git = "https://github.com/jupp0r/prometheus-cpp"

    maintainers = ["valmar"]

    version("0.9.0", tag="v0.9.0", submodules=True)

    patch("limits.patch")

    def cmake_args(self):
        args = ["-DBUILD_SHARED_LIBS=ON", "-DENABLE_PUSH=ON", "-DENABLE_COMPRESSION=ON"]
        return args
