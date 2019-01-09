# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Panda(CMakePackage):
    """PANDA: Parallel AdjaceNcy Decomposition Algorithm"""
    homepage = "http://comopt.ifi.uni-heidelberg.de/software/PANDA/index.html"
    url      = "http://comopt.ifi.uni-heidelberg.de/software/PANDA/downloads/panda-2016-03-07.tar"

    version('2016-03-07', 'b06dc312ee56e13eefea9c915b70fcef')

    # Note: Panda can also be built without MPI support

    depends_on('cmake@2.6.4:', type='build')
    depends_on('mpi')
