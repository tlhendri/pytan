#!/usr/bin/env python
"""
Deploy an action with parameters against only windows computers using human strings.

This will use the Package 'Custom Tagging - Add Tags' and supply two parameters. The second parameter will be ignored because the package in question only requires one parameter.
"""
# import the basic python packages we need
import os
import sys
import tempfile
import pprint
import traceback

# disable python from generating a .pyc file
sys.dont_write_bytecode = True

# change me to the path of pytan if this script is not running from EXAMPLES/PYTAN_API
pytan_loc = "~/gh/pytan"
pytan_static_path = os.path.join(os.path.expanduser(pytan_loc), 'lib')

# Determine our script name, script dir
my_file = os.path.abspath(sys.argv[0])
my_dir = os.path.dirname(my_file)

# try to automatically determine the pytan lib directory by assuming it is in '../../lib/'
parent_dir = os.path.dirname(my_dir)
pytan_root_dir = os.path.dirname(parent_dir)
lib_dir = os.path.join(pytan_root_dir, 'lib')

# add pytan_loc and lib_dir to the PYTHONPATH variable
path_adds = [lib_dir, pytan_static_path]
[sys.path.append(aa) for aa in path_adds if aa not in sys.path]

# import pytan
import pytan

# create a dictionary of arguments for the pytan handler
handler_args = {}

# establish our connection info for the Tanium Server
handler_args['username'] = "Administrator"
handler_args['password'] = "Tanium2015!"
handler_args['host'] = "10.0.1.240"
handler_args['port'] = "443"  # optional

# optional, level 0 is no output except warnings/errors
# level 1 through 12 are more and more verbose
handler_args['loglevel'] = 1

# optional, use a debug format for the logging output (uses two lines per log entry)
handler_args['debugformat'] = False

# optional, this saves all response objects to handler.session.ALL_REQUESTS_RESPONSES
# very useful for capturing the full exchange of XML requests and responses
handler_args['record_all_requests'] = True

# instantiate a handler using all of the arguments in the handler_args dictionary
print "...CALLING: pytan.handler() with args: {}".format(handler_args)
handler = pytan.Handler(**handler_args)

# print out the handler string
print "...OUTPUT: handler string: {}".format(handler)

# setup the arguments for the handler() class
kwargs = {}
kwargs["run"] = True
kwargs["action_filters"] = u'Operating System, that contains:Windows'
kwargs["package"] = u'Custom Tagging - Add Tags{$1=tag_should_be_added,$2=tag_should_be_ignore}'

print "...CALLING: handler.deploy_action with args: {}".format(kwargs)
response = handler.deploy_action(**kwargs)

print "...OUTPUT: Type of response: ", type(response)

print "...OUTPUT: Pretty print of response:"
print pprint.pformat(response)

print "...OUTPUT: Print of action object: "
print response['action_object']

# if results were returned (i.e. get_results=True was one of the kwargs passed in):
if response['action_results']:
    # call the export_obj() method to convert response to CSV and store it in out
    export_kwargs = {}
    export_kwargs['obj'] = response['action_results']
    export_kwargs['export_format'] = 'csv'
    print "...CALLING: handler.export_obj() with args {}".format(export_kwargs)
    out = handler.export_obj(**export_kwargs)

    # trim the output if it is more than 15 lines long
    if len(out.splitlines()) > 15:
        out = out.splitlines()[0:15]
        out.append('..trimmed for brevity..')
        out = '\n'.join(out)

    print "...OUTPUT: CSV Results of response: "
    print out

'''STDOUT from running this:
...CALLING: pytan.handler() with args: {'username': 'Administrator', 'record_all_requests': True, 'loglevel': 1, 'debugformat': False, 'host': '10.0.1.240', 'password': 'Tanium2015!', 'port': '443'}
...OUTPUT: handler string: PyTan v2.1.4 Handler for Session to 10.0.1.240:443, Authenticated: True, Platform Version: 6.5.314.4301
...CALLING: handler.deploy_action with args: {'action_filters': u'Operating System, that contains:Windows', 'run': True, 'package': u'Custom Tagging - Add Tags{$1=tag_should_be_added,$2=tag_should_be_ignore}'}
2015-09-14 19:59:12,302 INFO     pytan.pollers.QuestionPoller: ID 756: Reached Threshold of 99% (3 of 3)
2015-09-14 19:59:28,069 INFO     pytan.pollers.ActionPoller: ID 82: Reached Threshold for Seen Count of 100% (2 of 2)
2015-09-14 19:59:28,090 INFO     pytan.pollers.ActionPoller: ID 82: Reached Threshold for Finished Count of 100% (2 of 2)
...OUTPUT: Type of response:  <type 'dict'>
...OUTPUT: Pretty print of response:
{'action_info': <taniumpy.object_types.result_info.ResultInfo object at 0x102fa0510>,
 'action_object': <taniumpy.object_types.action.Action object at 0x1068fda90>,
 'action_result_map': {'failed': {'82:Expired.': [],
                                  '82:Failed.': [],
                                  '82:NotSucceeded.': [],
                                  '82:Stopped.': [],
                                  'total': 0},
                       'finished': {'82:Completed.': ['WIN-6U71ED4M23D',
                                                      'TPT1.pytanlab.com'],
                                    '82:Expired.': [],
                                    '82:Failed.': [],
                                    '82:NotSucceeded.': [],
                                    '82:Stopped.': [],
                                    '82:Succeeded.': [],
                                    '82:Verified.': [],
                                    'total': 2},
                       'running': {'82:Copying.': [],
                                   '82:Downloading.': [],
                                   '82:PendingVerification.': [],
                                   '82:Running.': [],
                                   '82:Waiting.': [],
                                   'total': 0},
                       'success': {'82:Completed.': ['WIN-6U71ED4M23D',
                                                     'TPT1.pytanlab.com'],
                                   '82:Verified.': [],
                                   'total': 2},
                       'unknown': {'total': 0}},
 'action_results': <taniumpy.object_types.result_set.ResultSet object at 0x1069c2890>,
 'group_object': <taniumpy.object_types.group.Group object at 0x106921390>,
 'package_object': <taniumpy.object_types.package_spec.PackageSpec object at 0x1068fda10>,
 'poller_object': <pytan.pollers.ActionPoller object at 0x102fa0490>,
 'poller_success': True,
 'saved_action_object': <taniumpy.object_types.saved_action.SavedAction object at 0x102d42190>}
...OUTPUT: Print of action object: 
Action, name: 'API Deploy Custom Tagging - Add Tags', id: 82
...CALLING: handler.export_obj() with args {'export_format': 'csv', 'obj': <taniumpy.object_types.result_set.ResultSet object at 0x1069c2890>}
...OUTPUT: CSV Results of response: 
Action Statuses,Computer Name
82:Completed.,WIN-6U71ED4M23D
82:Completed.,TPT1.pytanlab.com


'''

'''STDERR from running this:

'''
