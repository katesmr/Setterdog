import copy
from src.debug import debug
from src.Helper import Helper


class Analyzer:
    """
        Class to analyze output of command with configuration considering
    """
    def __init__(self, patterns):
        """
            Class constructor
            @param patterns {List} - list of dict patterns
        """
        self.expandedPattern = copy.deepcopy(patterns)

    def calculatePatternMatches(self, source):
        """
            Method, which calculate count of matches for each regex
            @param source {String} - source, where search matches
        """
        if source:
            pattern_len = len(self.expandedPattern)
            for i in range(pattern_len):
                try:
                    self.expandedPattern[i]["count"] = \
                        len(Helper.getAllMatches(source, self.expandedPattern[i]["regex"]))
                except (TypeError, NameError, AttributeError) as err:
                    debug.log().error(err)

    def maxErrorCode(self):
        """
            Search maximum error code in patterns, where patterns were match
            (only those, whose quantity is greater than zero)
            @return {Integer}
        """
        res = None
        try:
            codes = [token["code"] for token in self.expandedPattern if token["count"] != 0]
            res = max(codes)
        except (TypeError, ValueError):
            # avoid event if matches not finding
            pass
        except AttributeError as err:
            debug.log().error(err)
        finally:
            return res

    def returnCode(self, returnCode=-1):
        maxCode = self.maxErrorCode()
        if maxCode:
            Helper.systemExit(maxCode)
        else:
            Helper.systemExit(returnCode)
