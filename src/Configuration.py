import os
from src.debug import debug
from src.Helper import Helper
from src.DictObj import DictObj
from src.Singletonmixin import Singleton


class Configuration(DictObj, Singleton):
    def __init__(self, userConfig=None, launchCommand=None):
        """
            Class constructor
            @param userConfig {Dict|None} - [optional]:None
            @param launchCommand {String|None} - [optional]:None
        """
        super().__init__()
        self._defaultConfig = Helper.parseJson("src/default_config.json")
        if not self._defaultConfig:
            debug.log().critical("Default config doesn't exist")
            Helper.systemExit()
        # Config in current folder, which program was run.
        self._currentConfig = Helper.parseJson(os.path.join(os.getcwd(), "current.json"))
        self.config = Helper.MergeDict(self._defaultConfig, self._currentConfig)
        if userConfig:
            self._userConfig = Helper.parseJson(userConfig)
            self.config = Helper.MergeDict(self.config, self._userConfig)
        if launchCommand:
            self.config.launchCommand = launchCommand
        # Keys, which must be in each pattern
        self.validKeys = ["code", "regex", "name"]
        self.checkValidConfigKey()

    def checkValidConfigKey(self):
        """
            Check the availability of required keys
        """
        for obj in self.config.pattern:
            for key in self.validKeys:
                if key not in obj:
                    debug.log().critical("Not valid config pattern {}".format(obj))
                    Helper.systemExit()

    @classmethod
    def GI(self):
        return self.getInstance()
