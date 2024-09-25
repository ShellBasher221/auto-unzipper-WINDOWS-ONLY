import importlib.util
import os

package_list = ['numpy', 'rarfile', 'winshell']

for module in package_list: 
    if importlib.util.find_spec (module) is None:
        print(module, " is not installed.")
        #os.system(f'pip install {package_name}')
    else:
        print(module, " is installed.")