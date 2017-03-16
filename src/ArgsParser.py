import logging
import argparse
from src.debug import debug


class ArgsParser:
    @staticmethod
    def createParser():
        """
            @return {class argparse.ArgumentParser} - return argparse object
        """
        parser = argparse.ArgumentParser(description="Analyzer tool for lint and build reports",
                                         usage="python %(prog)s [-h] [-c command] [-f file name] [-d log level]")
        parser.add_argument('-c', '--command', nargs='?', type=str, help='Command name', required=False)
        parser.add_argument('-f', '--file', nargs='?', type=str, help='Path to config file', required=False)
        parser.add_argument('-d', '--debug', nargs='?', required=False, default=logging.getLevelName(0),
                            help='Debug log level: NOTSET, DEBUG, INFO, WARNING, ERROR, CRITICAL',
                            choices=[logging.getLevelName(0), logging.getLevelName(10), logging.getLevelName(20),
                                     logging.getLevelName(30), logging.getLevelName(40), logging.getLevelName(50)])
        return parser

    @staticmethod
    def getArgv(parser_obj):
        """
            @param parser_obj {class argparse.ArgumentParser}
            @return {class argparse.Namespace} - returns argument strings like attributes of the namespace
        """
        try:
            return parser_obj.parse_args()
        except TypeError as err:
            debug.log().error(err)
