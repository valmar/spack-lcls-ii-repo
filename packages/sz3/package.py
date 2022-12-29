# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.builtin.sz3 import Sz3 as BuiltinSz3


class Sz3(BuiltinSz3):
    """SZ3 is the next generation of the SZ compressor framework"""

    version("3.1.7", commit="c49fd17f2d908835c41000c1286c510046c0480e")
    version("3.1.6", commit="d22e8ef25b3920b791e2a1cad330a5b2d4a7b11d")
