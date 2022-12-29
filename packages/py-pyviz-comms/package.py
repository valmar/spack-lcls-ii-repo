# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPyvizComms(PythonPackage):
    """Bidirectional communication for the HoloViz ecosystem."""

    homepage = "https://www.example.com"
    pypi = "pyviz_comms/pyviz_comms-2.2.1.tar.gz"

    maintainers = ["valmar"]

    version("2.2.1", sha256="a26145b8ce43d2d934b3c6826d77b913ce105c528eb2e494c890b3e3525ddf33")

    depends_on("python@3.6:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-param", type=("build", "run"))
