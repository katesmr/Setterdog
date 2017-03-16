import os
from src.debug import debug
from src.DictObj import DictObj
from src.Analyzer import Analyzer
from src.ArgsParser import ArgsParser
from src.Configuration import Configuration
from src.StdoutData import StdoutData
from src.Reporter import Reporter
from src.Helper import Helper


def main():
    arguments = DictObj(vars(ArgsParser.getArgv(ArgsParser.createParser())))
    # arguments = DictObj({"command": "dir", "file": "D:\PyProject\setterdog\src\\user_config.json", "debug": 0})
    # print(arguments)
    debug.getInstance(arguments.debug, "./logger.log", 0, 0)

    Configuration.getInstance(arguments.file, arguments.command)
    # print(Configuration.GI().config)

    """
    debug.getInstance(logging.getLevelName(Configuration.GI().config.debug.logLevel),
                      Configuration.GI().config.debug.fileName, 0, 0)"""

    Helper.createFolder(Configuration.GI().config.output.outputDir)
    Helper.createFolder(Configuration.GI().config.report.reportDir)

    outputFile = os.path.join(Configuration.GI().config.output.outputDir,
                              Configuration.GI().config.output.outputFileNamePattern.
                              format(date=Helper.getCurrentDate()))
    stdout = StdoutData(Configuration.GI().config.launchCommand, True, outputFile)

    a = Analyzer(Configuration.GI().config.pattern)
    a.calculatePatternMatches(stdout.getOutputData())

    report = Reporter(Configuration.GI().config.report.reportDir,
                      Configuration.GI().config.report.reportFileNamePattern.format(date=Helper.getCurrentDate()),
                      a.expandedPattern)
    report.writeReport()
    a.returnCode(stdout.returnCode)

if __name__ == '__main__':
    main()
