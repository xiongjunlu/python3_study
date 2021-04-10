# from modules import say_hi, __version__
import modules

__version__ = '1.0.0'

modules.say_hi()
print('Version', __version__, modules.__version__)

print('dir()===>', dir())