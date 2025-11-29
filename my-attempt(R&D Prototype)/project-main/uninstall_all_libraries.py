import subprocess
import pkg_resources
import sys

installed_packages = [pkg.key for pkg in pkg_resources.working_set]
subprocess.check_call([sys.executable, "-m", "pip", "uninstall", "-y"] + installed_packages)
