import re
import os
import sys
import json
from datetime import datetime
from src import debug


class Helper:
    """
        Some class with utility methods
    """
    @staticmethod
    def createNewFile(fileName, data, mode):
        """
            @param fileName {String}
            @param data {String}
            @mode {String}
            @return {void} - write to file data
        """
        try:
            if mode == 'w' or mode == 'a':
                with open(fileName + ".txt", mode) as file:
                    file.write(data + '\n')
            else:
                debug.log().warnning("Use 'a'(add) or 'w'(write) mode-access to file")
        except (OSError, TypeError) as err:
            debug.log().error(err)

    @staticmethod
    def parseJson(fileName):
        """
            @param fileName {String}
            @return {Dict} - returns deserialized json object like dictionary, else returns empty dictionary
        """
        res = {}
        try:
            with open(fileName) as jsonData:
                try:
                    res = json.load(jsonData)
                except ValueError:
                    debug.log().error("Invalid json file '{}'".format(fileName))
        except FileNotFoundError:
            debug.log().warnning("File '{}' don't exist".format(fileName))
        finally:
            return res

    @staticmethod
    def toJsonFile(fileName, data, mode):
        """
            @param fileName {String}
            @param data {Dict}
            @mode {String}
            @return {void} - write data in json
        """
        try:
            with open(fileName, mode) as file:
                try:
                    json.dump(data, file, indent=4)
                except TypeError:
                    debug.log().error("'{}' is not JSON serializable".format(data))
        except OSError as err:
            debug.log().error(err)

    @staticmethod
    def MergeDict(dict1, dict2):
        """
            @param dict1 {Dict}
            @param dict2 {Dict}
            @return {Dict} - returns expanded or updated dict
        """
        try:
            return {**dict1, **dict2}
        except TypeError as err:
            debug.log().error(err)

    @staticmethod
    def getAllMatches(source, pattern):
        """
            @param source {String}
            @param pattern {String}
            @return {List} - returns list of all matches
        """
        try:
            return re.findall(pattern, source)
        except TypeError as err:
            debug.log().error(err)

    @staticmethod
    def getCurrentDate():
        """
            For creation new file for each act
        """
        return datetime.now()

    @staticmethod
    def createFolder(directory):
        """
            @param directory {String} - path
            @return {void} - create new folder
        """
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
        except OSError as err:
            debug.log().error(err)

    @staticmethod
    def systemExit(exitCode=-1):
        sys.exit(exitCode)
