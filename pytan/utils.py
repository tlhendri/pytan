#!/usr/bin/env python
# -*- mode: Python; tab-width: 4; indent-tabs-mode: nil; -*-
# ex: set tabstop=4
# Please do not change the two lines above. See PEP 8, PEP 263.
"""Generic Utility Functions"""
import sys

# disable python from creating .pyc files everywhere
sys.dont_write_bytecode = True

import socket
import time
import getpass
import logging
import json
import itertools
import re
from collections import OrderedDict
from . import __version__
from . import constants


def version_check(reqver):
    """for scripts using this API to validate the version of the API

    :param reqver: string containing version number to check against
    """
    log_tpl = (
        "{}: {} version {}, required {}").format
    if not __version__ >= reqver:
        s = "Script and API Version mismatch!"
        logging.error(log_tpl(s, __file__, __version__, reqver))
        sys.exit(100)
    s = "Script and API Version match"
    logging.debug(log_tpl(s, __file__, __version__, reqver))


def jsonify(v, indent=4, sort_keys=True):
    return json.dumps(v, indent=indent, sort_keys=sort_keys)


def is_list(l):
    return type(l) in [list, tuple]


def is_str(l):
    return type(l) in [unicode, str]


def is_dict(l):
    return type(l) in [dict, OrderedDict]


def is_num(l):
    return type(l) in [float, int, long]


def prompt_username():
    """for scripts using this API to prompt the user for a username

    :return: :class:`str`
    """
    print('Username: '),
    username = sys.stdin.readline()
    return username.strip()


def prompt_password():
    """for scripts using this API to prompt the user for a password

    :return: :class:`str`
    """
    password = getpass.getpass('Password: ')
    return password.strip()


def get_now():
    """return current time in human friendly format

    :return: :class:`str`
    """
    return human_time(time.localtime())


def fn_gen(ext, pname):
    fn = "{}_{}.{}".format(get_now(), pname, ext)
    return fn


def human_time(t, tformat='%Y_%m_%d-%H_%M_%S-%Z'):
    """return time in human friendly format

    :param t: either a epoch or struct_time time object
    :param tformat: strftime format string
    :return: :class:`str`
    """
    if is_num(t):
        t = time.localtime(t)
    return time.strftime(tformat, t)


# not in use
# def datetime_diff(t=False):
#     """Get the dtdiff of now - time

#     :param t: either a epoch or datatime object
#     :return: :class:`datatime.timedelta`
#     """
#     now = datetime.now()

#     if is_num(t):
#         dtdiff = now - datetime.fromtimestamp(t)
#     elif isinstance(t, datetime):
#         dtdiff = now - t
#     else:
#         dtdiff = now - now

#     # dtdiff = SoapUtil.datetime_diff(timestamp)
#     # minutes_dtdiff = dtdiff.seconds / 60

#     #second_dtdiff = dtdiff.seconds
#     #minute_dtdiff = dtdiff.seconds / 60
#     #hour_dtdiff = minute_dtdiff / 60
#     #day_dtdiff = dtdiff.days
#     return dtdiff


def port_check(address, port, timeout=5):
    """Check if address:port can be reached within timeout

    :param address: string of host to connect to
    :param port: string of port to connect to
    :param timeout: int of seconds to wait until connection fails

    :return: :class:`bool`
    """
    try:
        return socket.create_connection((address, port), timeout)
    except socket.error:
        return False


class SplitStreamHandler(logging.Handler):
    def __init__(self):
        logging.Handler.__init__(self)

    def emit(self, record):
        try:
            msg = self.format(record)
            if record.levelno < logging.WARNING:
                stream = sys.stdout
            else:
                stream = sys.stderr
            fs = "%s\n"
            try:
                is_unicode = isinstance(msg, unicode)
                if is_unicode and getattr(stream, 'encoding', None):
                    ufs = u'%s\n'
                    try:
                        stream.write(ufs % msg)
                    except UnicodeEncodeError:
                        stream.write((ufs % msg).encode(stream.encoding))
                else:
                    stream.write(fs % msg)
            except UnicodeError:
                stream.write(fs % msg.encode("UTF-8"))
            self.flush()
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)


def remove_logging_handler(name):
    root_logger = logging.getLogger()
    root_handlers = root_logger.handlers
    for h in root_handlers:
        if name == 'all':
            root_logger.removeHandler(h)
        elif h.name == name:
            root_logger.removeHandler(h)


def setup_console_logging():
    ch_name = 'console'
    remove_logging_handler('all')
    # add a console handler to the root logger that goes to STDOUT for INFO
    # and below, but STDERR for WARNING and above
    ch = SplitStreamHandler()
    ch.set_name(ch_name)
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(constants.INFO_FORMAT)
    root_logger = logging.getLogger()
    root_logger.addHandler(ch)
    root_logger.setLevel(logging.DEBUG)


def change_console_format(debug=False):
    root_logger = logging.getLogger()
    root_handlers = root_logger.handlers
    for h in root_handlers:
        if h.name == 'console':
            if debug:
                h.setFormatter(constants.DEBUG_FORMAT)
            else:
                h.setFormatter(constants.INFO_FORMAT)


def set_log_levels(loglevel=0):
    # print loglevel
    set_all_loglevels('WARN')
    for logmap in constants.LOG_LEVEL_MAPS:
        if loglevel >= logmap[0]:
            for lname, llevel in logmap[1].iteritems():
                # print 'setting %s to %s' % (lname, llevel)
                logging.getLogger(lname).setLevel(getattr(logging, llevel))


def set_all_loglevels(level='DEBUG'):
    for k, v in sorted(logging.Logger.manager.loggerDict.iteritems()):
        if not isinstance(v, logging.Logger):
            continue
        v.setLevel(getattr(logging, level))
        # m = 'set to %s' % level
        # v.debug(m)
        # v.info(m)
        # v.warn(m)
        # v.error(m)


def combinator1(l1, l2):
    l2_repeated = itertools.repeat(l2, len(l1))
    c = [dict(zip(l1, x)) for x in itertools.product(*l2_repeated)]
    return c


def combinator2(l1, l2, key):
    c = [
        dict(x[0].items() + {key: x[1]}.items())
        for x in itertools.product(l1, l2)
    ]
    return c


def build_fn_from_dict(d, key='fpostfix'):
    skips = ['ftype', key]
    parts = []
    for k, v in d.iteritems():
        if k in skips:
            continue
        new_k = ''.join([s[0] for s in k.split('_')])
        if is_list(v):
            if not v:
                new_v = 'null'
            else:
                new_v = ''.join([s[0] for s in v])
        else:
            new_v = str(v)[0]
        parts.append('_'.join([new_k, new_v]))
    parts = '-'.join(parts)
    d[key] = parts
    return d


def stringify_obj(o, max_len=80):
    s = json.dumps(o)
    s = re.sub(r'[^\w,:]', '', s)
    s = s.replace(':', '_')
    s = s.replace(',', '+')
    s = s[0:max_len]
    return s


def get_object_case(handler, objtype, qgrp_args):
    all_in_query = 'all' in [x.lower() for x in qgrp_args['query']]
    if all_in_query:
        print "++ Getting all objects for object type: %s" % (objtype)
        response = getattr(handler, 'get_all_%s_objects' % objtype)()
    else:
        print "++ Getting objects %s for object type: %s" % (
            json.dumps(qgrp_args), objtype)
        response = getattr(handler, 'get_%s_object' % objtype)(**qgrp_args)

    print "++ Received Response: ", str(response)
    return response


def write_object(handler, response, tgrp_args):
    print "++ Creating Report: ", json.dumps(tgrp_args)
    report_file = handler.reporter.write_response(response, **tgrp_args)
    print "++ Report created: ", report_file