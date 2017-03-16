# Setterdog

Simple Analyzer tool for analyze output of command with considering configuration.

Analyzer counts the number of matches in output for each pattern.

And write report in configuration.

# Running examples

Examples running in command line:

Show help message.
```
$ python main.py -h
```
Run without parameters, program use setting of default config.
```
$ python main.py
```
Run with command and user configuration.
```
$ python main.py -c 'COMMAND' -f PATH_TO_CONFIG -d LOG_LEVEL
```

# Config example

Some view of config (fields 'name', 'regex', 'code' must be set in patterns required).
```
{
    "launchCommand": "",
    "output": {
        "outputDir": "./output",
        "outputFileNAmePattern": "stdout"
    },
    "report": {
        "reportDir": "./report",
        "reportFileNAmePattern": "report"
    },
    "pattern": [
        {
            "regex": "regex1",
            "name": "example1",
            "code": 1,
            "description": ""
        },
        {
            "regex": "regex2",
            "name": "example2",
            "code": 2,
            "description": ""
        }
    ]
}
```

# Usage
```
import os
import logging
from src.debug import debug
from src.DictObj import DictObj
from src.Analyzer import Analyzer
from src.ArgsParser import ArgsParser
from src.Configuration import Configuration
from src.StdoutData import StdoutData
from src.Reporter import Reporter
from src.Helper import Helper
```
Get arguments of command line.
```
arguments = DictObj(vars(ArgsParser.getArgv(ArgsParser.createParser())))
```
Or run from IDE.
```
arguments = DictObj({"command": "YOUR COMMAND", "file": "PATH_TO_FILE", "debug": LOG_LEVEL_CODE})
```
Create debug object, which write errors in file.
```
debug.getInstance(arguments.debug, "./logger.log", 0, 0)
```
Create instance of Configuration class.
It merges data of default, user configs, config in current folder if them exist; or use only default config.
```
Configuration.getInstance(arguments.file, arguments.command)
```
```
Helper.createFolder(Configuration.GI().config.output.outputDir)
Helper.createFolder(Configuration.GI().config.report.reportDir)
```
Create StdoutData object with saving its in file.
```
outputFile = os.path.join(Configuration.GI().config.output.outputDir,
                          Configuration.GI().config.output.outputFileNamePattern.
                          format(date=Helper.getCurrentDate()))
data = StdoutData(Configuration.GI().config.launchCommand, True, outputFile)
```
Or without saving in file.
```
data = StdoutData(Configuration.GI().config.launchCommand)
```
Create Analyzer object.
```
analyzer = Analyzer(Configuration.GI().config.pattern)
analyzer.calculatePattern(data.getOutputData())
```
Create Reporter object.
```
report = Reporter(Configuration.GI().config.report.reportDir,
                  Configuration.GI().config.report.reportFileNamePattern.format(date=Helper.getCurrentDate()),
                  analyzer.expanded_pattern)
report.write_report()
```
Return exit-code, which equal maximum error code from set of patterns or return code of command.
```
returnCode(data.returnCode)
```
