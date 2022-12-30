# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.builtin.py_loguru import PyLoguru as BuiltinPyLoguru


class PyLoguru(BuiltinPyLoguru):
    """Loguru is a library which aims to bring enjoyable logging in Python."""

    version("0.2.5", sha256="68297d9f23064c2f4764bb5d0c5c767f3ed7f9fc1218244841878f5fc7c94add")
