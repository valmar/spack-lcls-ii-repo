# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.builtin.py_ipdb import PyIpdb as BuiltinPyIpdb


class PyIpdb(BuiltinPyIpdb):
    """ipdb is the iPython debugger and has many additional features, including
    a better interactive debugging experience via colorized output."""

    depends_on("py-setuptools@:57.6", type="build")
