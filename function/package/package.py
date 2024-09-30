# https://www.programiz.com/python-programming/package

# Package is a module containing multiple modules and other sub-packages. 
# It is a container that contains various functions to perform specific tasks.
import employee.swEngineer.getInfo
employee.swEngineer.getInfo.sweInfo()

# another way to import the module: 
from employee.manager import managerInfo
managerInfo.showInfo()

# another method (although this seems the easiest, this is not the recommended way since it can create confusion if more than one package contain the module with same name.)
from employee.finance.financeInfo import showInfo
showInfo()
# Note: A directory must contain a file named __init__.py in order for Python to consider it as a package.
# This file can be left empty but we generally place the initialization code for that package in this file.








