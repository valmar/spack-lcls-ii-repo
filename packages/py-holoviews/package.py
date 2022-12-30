# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyHoloviews(PythonPackage):
    """HoloViews is an open-source Python library designed to make data analysis and visualization seamless and simple."""

    homepage = "https://www.holoviews.org"
    pypi = "holoviews/holoviews-1.15.3.tar.gz"

    maintainers = ["valmar"]

    version("1.15.3", sha256="a45891cd2b8fcd408742cffff351c928fbf4cf1ef7d1f04442c7d8786ee8e994")

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-param@1.9.3:2", type=("build", "run"))
    depends_on("py-numpy@1.0:", type=("build", "run"))
    depends_on("py-pyviz-comms@0.7.4:", type=("build", "run"))
    depends_on("py-panel@0.13.1:", type=("build", "run"))
    depends_on("py-colorcet", type=("build", "run"))
    depends_on("py-packaging", type=("build", "run"))
    depends_on("py-pandas@0.20.0:", type=("build", "run"))
