#packages are a set of modules that can be imported into a program
#inside a package, we must have a __init__.py file

# this is how to export a module in the init fie :
# __all__ = ["module1", "module2"]
# we specify the modules that we want, 
# this approach provides explicit control over what gets 
# imported and can prevent accidental or unwanted imports of modules from a package.

# to import a module from a package, we use :
# from package_name import module_name
# to automatically import all the module, we use :
# from package_name import *

