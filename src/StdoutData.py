import os
from subprocess import PIPE, Popen
from src import debug
from src.Helper import Helper


class StdoutData:
    def __init__(self, command, writeToFile=False, fileName=None):
        """
            Class constructor
            @param command {String|List}
            @param writeToFile {Boolean|None} - [optional]:None - set record in file
            @param fileName {String|None} - [optional]:None
        """
        self.command = command
        self.writeToFile = writeToFile
        self.fileName = fileName
        self.returnCode = None

    def getOutputData(self):
        """
            @return {String} - returns output of command
        """
        try:
            process = Popen(self.command, stdout=PIPE)
            # output = str(process.stdout.read())  # Use for big data of stdout
            (output, error) = process.communicate()  # Store data in clipboard
            self.returnCode = process.returncode
            if self.returnCode == 0:
                res = None
                if output:
                    res = str(output)
                    if self.writeToFile and self.fileName:
                        lines = res.split('\\n')
                        Helper.createNewFile(self.fileName, os.linesep.join(lines), 'w')
                return res
            else:
                debug.log().error("Command '{}' failed, exit-code = {}, error = {}".format(self.command,
                                                                                           self.returnCode,
                                                                                           str(error)))
        except (ValueError, OSError, TypeError) as err:
            debug.log().critical(err)
            Helper.systemExit()
