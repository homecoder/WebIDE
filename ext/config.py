# -*- coding: utf-8 -*-
"""
WebIDE Extensions
Copyright 2017 - Michael Ruggiero <ruggierom@gmail.com>

Rationale:
    I had a need (want) to be able to click a button from the laptop to run the app I was working on in Pythonista.

    From there - I decided to create a much LARGER version of WebIDE, with some updates to make my life easier.
"""
# System imports
import os, json, six

# Let's try to import some YAML - This will be used to export the config (optional)
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
    config_filename = 'WebIDE_config.json'
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
        'enable_bonjour' : 'Enable Bonjour',
        'disable_device_sleep' : 'Prevent your iPhone/iPad/iPod from sleeping while running WebIDE',
        'enable_run' : 'Enable "Run" from WebIDE - Run the script you are working on in Pythonista. ',
        'run_export_globals' : "Return a list of globals initialized by apps you run with Run feature.",
        'run_export_globals_internals' : "Include internals like __builtins__ with the export globals report.",
        'run_set_name' : '__main__',
    }


    def __init__(self):
        # Setup the filename with path & filename
        self.full_config = os.path.join(self.config_path,self.config_filename)

        try:
            with open(self.full_config) as f:
                config = f.read()
        except IOError:
            pass
        except Exception as e:
            six.reraise(BaseException,e)

        # Check if folder exist
        if not os.path.exists((self.config_path)):
            try:
                # Okay, the config doesn't exist, let's create a default set
                os.mkdir(self.config_path)
                self.config = {
                    'config' : self.base_config,
                    'config_descriptions' : self.base_config_descriptions,
                }

                with open(self.full_config,'w') as conf:
                    json.dump(conf,indent=2)
            except Exception as e:
                six.reraise(BaseException, e)

        # Now everythign should be there fine!



Config()