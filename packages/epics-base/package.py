# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class EpicsBase(MakefilePackage):
    """This is the main core of EPICS, the Experimental Physics and Industrial
    Control System, comprising the build system and tools, common and OS-interface
    libraries, network protocol client and server libraries, static and run-time
    database access routines, the database processing code, and standard record,
    device and driver support."""

    homepage = "https://epics-controls.org"
    url = "https://epics-controls.org/download/base/base-7.0.6.1.tar.gz"

    maintainers = ["glenn-horton-smith"]

    version("7.0.6.1", sha256="8ff318f25e2b70df466f933636a2da85e4b0c841504b9e89857652a4786b6387")

    depends_on("readline")
    depends_on('binutils', type='build')
    depends_on("perl", type=("build", "run"))


    @property
    def install_targets(self):
        return ["INSTALL_LOCATION={0}".format(self.prefix), "install"]

    def get_epics_host_arch(self):
        perl = which("perl", required=True)
        return perl("%s/perl/EpicsHostArch.pl" % self.prefix.lib, output=str, error=str).strip()

    def setup_build_environment(self, env):
        env.set("EPICS_BASE", self.prefix)

    def setup_dependent_build_environment(self, env, dependent_spec):
        epics_host_arch = self.get_epics_host_arch()
        env.set("EPICS_HOST_ARCH", epics_host_arch)
        env.set("EPICS_BASE", self.prefix)

    def setup_run_environment(self, env):
        epics_host_arch = self.get_epics_host_arch()
        env.set("EPICS_HOST_ARCH", epics_host_arch)
        env.set("EPICS_BASE", self.prefix)
        env.prepend_path("PATH", join_path(self.prefix.bin, epics_host_arch))

    def edit(self, spec, prefix):
        common_linux = FileFilter("configure/CONFIG.gnuCommon")
        common_linux.filter("CC = $(GNU_BIN)/$(CMPLR_PREFIX)gcc$(CMPLR_SUFFIX)", "CC = gcc", string=True)
        common_linux.filter("CCC = $(GNU_BIN)/$(CMPLR_PREFIX)g++$(CMPLR_SUFFIX)", "CCC = g++", string=True)
        common_linux.filter("AR = $(GNU_BIN)/$(CMPLR_PREFIX)ar$(CMPLR_SUFFIX) -rc", "AR = ar -rc", string=True)
        common_linux.filter("LD = $(GNU_BIN)/$(CMPLR_PREFIX)ld$(CMPLR_SUFFIX) -r", "LD = ld -r", string=True)
        common_linux.filter("RANLIB = $(GNU_BIN)/$(CMPLR_PREFIX)ranlib$(CMPLR_SUFFIX)", "RANLIB = ranlib", string=True)
        common = FileFilter("configure/CONFIG_COMMON")
        common.filter("PERL = perl -CSD", "PERL = perl", string=True)
