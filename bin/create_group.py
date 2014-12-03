#!/usr/bin/env python
# -*- mode: Python; tab-width: 4; indent-tabs-mode: nil; -*-
# ex: set tabstop=4
# Please do not change the two lines above. See PEP 8, PEP 263.
'''Create a group object from command line arguments'''
__author__ = 'Jim Olsen (jim.olsen@tanium.com)'
__version__ = '0.8.0'

import os
import sys

sys.dont_write_bytecode = True
my_file = os.path.abspath(__file__)
my_dir = os.path.dirname(my_file)
parent_dir = os.path.dirname(my_dir)
path_adds = [parent_dir]

for aa in path_adds:
    if aa not in sys.path:
        sys.path.append(aa)

import pytan
from pytan import utils


def process_handler_args(parser, all_args):
    handler_grp_names = ['Handler Authentication', 'Handler Options']
    handler_opts = utils.get_grp_opts(parser, handler_grp_names)
    handler_args = {k: all_args.pop(k) for k in handler_opts}

    h = pytan.Handler(**handler_args)
    print str(h)
    return h


utils.version_check(__version__)
parser = utils.setup_parser(__doc__, True)
arggroup = parser.add_argument_group('Create User Options')

arggroup.add_argument(
    '-n',
    '--name',
    required=True,
    action='store',
    dest='name',
    default=None,
    help='Name of group to create',
)

arggroup.add_argument(
    '-f',
    '--filter',
    required=False,
    action='append',
    dest='filters',
    default=[],
    help='Filters to use for group, supply --filter-help to see filter help',
)

arggroup.add_argument(
    '-o',
    '--option',
    required=False,
    action='append',
    dest='filter_options',
    default=[],
    help='Filter options to use for group, supply --option-help to see options'
    ' help',
)

args = parser.parse_args()
all_args = args.__dict__
handler = process_handler_args(parser, all_args)
group_obj = handler.create_group(
    groupname=args.name,
    filters=args.filters,
    filter_options=args.filter_options,
)
m = "New group {!r} created with ID {!r}, filter text: {!r}".format
print(m(group_obj.name, group_obj.id, group_obj.text))