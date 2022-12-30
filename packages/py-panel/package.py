# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPanel(PythonPackage):
    """A high level app and dashboarding solution for Python."""

    homepage = "https://panel.holoviz.org"
    pypi = "panel/panel-0.14.2.tar.gz"

    maintainers = ["valmar"]

    version("0.14.2", sha256="c22690833dfa508d72ae632e2d42ea7d63ee2a31347e23b7ecf8dcded312ec74")

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-setuptools@42:", type="build")
    depends_on("node-js", type="build")
    depends_on("py-bokeh@2.4.3:2.5.0", type=("build", "run"))
    depends_on("py-param@1.12.0:", type=("build", "run"))
    depends_on("py-pyviz-comms@0.7.4:", type=("build", "run"))
    depends_on("py-markdown", type=("build", "run"))
    depends_on("py-requests", type=("build", "run"))
    depends_on("py-tqdm@4.48.0:", type=("build", "run"))
    depends_on("py-pyct@0.4.4:", type=("build", "run"))
    depends_on("py-bleach", type=("build", "run"))
    depends_on("py-typing-extensions", type=("build", "run"))
