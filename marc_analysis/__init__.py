"""
A package for analzying an aerosol-indirect effect
experiment with different activation parameterizations
in the CESM-MARC.

"""

from __future__ import absolute_import, division

# Set up some default imports to bring some of the
# tools to the marc_aie namespace.
# from . case_setup import *
from . analysis import *
from . convert import *
from . experiment import *
from . extract import *
from . io import *
from . regions import *
from . scripting import *
from . utilities import *
from . var import *

try:
    from . import plot
except ImportError:
    # Possibly thrown by cartopy; just don't import plotting if
    # it's not available
    pass

