from spires.invert import *
from spires.interpolator import *
from spires.process import *
import spires.legacy

# Version from setuptools_scm
from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("spires")
except PackageNotFoundError:
    __version__ = "unknown"
