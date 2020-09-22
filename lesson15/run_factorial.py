import warnings
import runpy

warnings.simplefilter("error", UserWarning)
runpy.run_module("factorial4")
