# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PySysvIpc(PythonPackage):
    """System V IPC for Python."""

    homepage = "https://semanchuk.com/philip/sysv_ipc"
    pypi = "sysv_ipc/sysv_ipc-1.1.0.tar.gz"

    maintainers = ["valmar"]

    version("1.1.0", sha256="0f063cbd36ec232032e425769ebc871f195a7d183b9af32f9901589ea7129ac3")

    depends_on("py-setuptools", type="build")
