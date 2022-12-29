# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPyopengl(PythonPackage):
    """Standard OpenGL bindings for Python."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://pyopengl.sourceforge.net"
    pypi = "PyOpenGL/PyOpenGL-3.1.6.tar.gz"

    maintainers = ["valmar"]

    version("3.1.6", sha256="8ea6c8773927eda7405bffc6f5bb93be81569a7b05c8cac50cd94e969dce5e27")

    depends_on("py-setuptools", type="build")
