# Standard Python libraries
from __future__ import (absolute_import, print_function,
                        division, unicode_literals)
import os

# Define rootdir
rootdir = os.path.dirname(os.path.abspath(__file__))

# Read version from VERSION file
with open(os.path.join(rootdir, 'VERSION')) as version_file:
    __version__ = version_file.read().strip()

# atomman imports
from . import compatibility
from . import unitconvert
from . import crystal
from .core import *
#from . import defect
from . import lammps
from . import tools
from . import convert
from . import plot

# Define default working units
unitconvert.reset_units(length = 'angstrom', mass = 'amu', energy='eV', charge='e')
