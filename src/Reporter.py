import os
from src.Helper import Helper


class Reporter:
    def __init__(self, dirName, fileName, obj):
        """
            Class constructor
            @param dirName {String}
            @param fileName {String}
            @param obj {Dict} - object, which serialized in json
        """
        self.file = os.path.join(dirName, fileName) + ".json"
        self.obj = obj

    def writeReport(self):
        Helper.toJsonFile(self.file, self.obj, 'w')
