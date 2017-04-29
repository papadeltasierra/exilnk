from __future__ import print_function
import serial
import argparse
import os
import logging
import random

# Set up a specific logger with our desired output level
logger = logging.getLogger("__main__")

SAMSUNG_REQUEST_PREFIX = '\x08\x22'
SAMSUNG_RESPONSE_SUCCESS = '\x03\x0C\xF1'
SAMSUNG_RESPONSE_FAILURE = '\x03\x0C\xFF'


def hexStr(array):
    """
    Convert an array of integers into a string of hex values (without 0x)
    """
    return ' '.join([('%2.2x' % i) for i in bytearray(array)])


class SamsungTV(object):
    def __init__(self):
        self._port = None
        self._tv = None
        self._args = self._init_parser()

    def _init_parser(self):
        parser = argparse.ArgumentParser(
            description='Emulate Samsung TV and repond to commands.')

        parser.add_argument(
            '-p', '--port', metavar='serialport', type=str,
            default='/dev/ttyUSB0',
            help=('Serial port connected to a Samsung TV via '
                  'ex-link cable (/dev/ttyUSB0 by default)'))

        parser.add_argument(
            '-f', '--failures', action='store', type=int, default=0,
            help='fail this percentage of commands')

        parser.add_argument(
            '-v', '--verbose', action='store_true',
            help='verbose output')

        return parser.parse_args()

    def _readCommand(self):
        self._command = self._tv.read(7)
        print('%s: ' % hexStr(self._command), end='')
        # self._command = bytearray(self._command)

    def _checkPrefix(self):
        if self._command[0:2] != SAMSUNG_REQUEST_PREFIX:
            logger.error('invalid command prefix: %s' % hexStr(self._command[0:1]))
            if self._args.verbose:
                print('Bad prefix: %s: ' % hexStr(self._command[0:1]), end='')
            return False
        else:
            return True

    def _checkChecksum(self):
        """
        Confirm the checksum for the received command.
        """
        chk = 0
        for ch in self._command[0:6]:
            chk = (chk + ord(ch)) % 256
        chk = (~chk + 1) % 256
        chk = chr(chk)
 
        if self._args.verbose and (self._command[6] != chk):
            print('Bad checksum: %s != %s: ' % (hexStr(self._command[6]), hexStr(chk)), end='')
        return (self._command[6] == chk)


    def _maybeFail(self):
        if (self._args.failures > 0 and
                random.randint(0, 100) <= self._args.failures):
            logger.info('failing the request')
            if self._args.verbose:
                print('Random failure: ', end='')
            return False
        else:
            return True

    def _success(self):
        print('success.')
        self._tv.write(SAMSUNG_RESPONSE_SUCCESS)

    def _failure(self):
        print('rejected.')
        self._tv.write(SAMSUNG_RESPONSE_FAILURE)

    def run(self):
        self._tv = serial.Serial(self._args.port,
                                 baudrate=9600,
                                 bytesize=8,
                                 parity='N',
                                 stopbits=1,
                                 # timeout=3,
                                 writeTimeout=1)

        while True:
            logger.debug('waiting for command...')
            print('waiting...: ', end='')
            self._readCommand()
            if (self._checkPrefix() and
                    self._checkChecksum() and
                    self._maybeFail()):
                self._success()
            else:
                self._failure()


if __name__ == "__main__":
    """
    Start a Samsung TV emulator and respond to incoming requests.
    """

    # Create a log file so that we can diagnose upgrade problems.
    # Note that when installing, the /var/log/ams directory will not exist
    # at the point this script is run.
    log_name = "%s.log" % os.path.splitext(os.path.basename(__file__))[0]
    logging.basicConfig(format="%(asctime)12.12s %(filename)-20.20s " +
                               "%(lineno)5.5d: 00000000 %(funcName)-31.31s " +
                               "%(message)s",
                        datefmt='%H:%M:%S.000',
                        filename=log_name,
                        filemode='w',
                        level=logging.DEBUG)
    logger.setLevel(logging.DEBUG)

    tv = SamsungTV()
    tv.run()
