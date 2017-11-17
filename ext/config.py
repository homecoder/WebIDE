# -*- coding: utf-8 -*-
"""
WebIDE Extensions
Copyright 2017 - Michael Ruggiero <ruggierom@gmail.com>

Rationale:
    I had a need (want) to be able to click a button from the laptop to run the app I was working on in Pythonista.

    From there - I decided to create a much LARGER version of WebIDE, with some updates to make my life easier.
"""
# System imports
import os, json, six, sys

# Let's try to import some YAML
HAS_YAML=False

try:
    # We may be working off of a computer w/ yaml
    import yaml
    HAS_YAML = True
except ImportError:
    try:
        import pureyaml as yaml
        HAS_YAML=True
    except ImportError:
        pass



# Configuration Module

class Config (object):

    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'config')
    config_filename = 'WebIDE_config'
    config = None
    serializer = None

    base_config = {
        'web_ide_debug_mode' : False,
        'enable_bonjour' : False,
        'disable_device_sleep' : True,
        'enable_run' : True,
        'run_export_globals' : False,
        'run_export_globals_internals' : False,
        'run_set_name' : '__main__',
    }

    base_config_descriptions = {
        'web_ide_debug_mode' : 'Enable Debug Mode in Web IDE (Bottle Debug mode)',
        'enable_bonjour' : 'Enable Bonjour - <a href="help:bonjour">More Information</a>',
        'disable_device_sleep' : 'Prevent your iPhone/iPad/iPod from sleeping while running WebIDE',
        'enable_run' : 'Enable "Run" from WebIDE - Run the script you are working on in Pythonista. '
                       '<a href="help:enable_run">More Information"</a>',
        'run_export_globals' : "Return a list of globals initialized by apps you run with Run feature.",
        'run_export_globals_internals' : False,
        'run_set_name' : '__main__',
    }


    def __init__(self):
        # Safety check, make sure no period in the end of the filename, yeah, I did that before.

        try:
            with open(self.config_filename) as f:
                config = f.read()
        except IOError:
            pass
        except Exception as e:
            six.reraise(BaseException,e)

        # Check if folder exist
        if not os.path.exists((self.config_path)):
            try:
                os.mkdir(self.config_path)

            except Exception as e:
                six.reraise(BaseException, e)


