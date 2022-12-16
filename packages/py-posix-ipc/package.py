# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPosixIpc(PythonPackage):
    """POSIX IPC for Python."""

    homepage = "https://github.com/osvenskan/posix_ipc"
    pypi = "posix_ipc/posix_ipc-1.1.0.tar.gz"

    maintainers = ["valmar"]

    version("1.1.0", sha256="f86a15b32b38573c78e305ebd9100d8198a3d9facc03ffafe39edc35833738e3")

    depends_on("py-setuptools", type="build")
