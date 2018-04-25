__author__ = ''
import os,sys
from .. import format_output
#parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#sys.path.insert(0,parentdir)
#from .. import handleCmd
class ConfigCmd:
    showConfig = 'showConfig'
    importConfig = 'importConfig'
    exportConfig = 'exportConfig'
    name = '--filename'
class ConfigHandler:
    def __init__(self):
        from .. import handleCmd
        self.handleCmd = handleCmd.handleCmd()
    def getConfigHandlerCmd(self):
        return [ConfigCmd.showConfig,ConfigCmd.importConfig,ConfigCmd.exportConfig]

    def getConfigHandlerOptions(self):
        return [ConfigCmd.name]

    def showConfig(self):
        _credentialsPath = os.path.join(self.handleCmd.showQcloudConfigurePath(),
                                            self.handleCmd.credentials)
        _configurePath = os.path.join(self.handleCmd.showQcloudConfigurePath(),
                                          self.handleCmd.configure)

        config = dict()
        configContent =  dict()
        credentialsContent = dict()
        pro="aa"
        prof="bb"

        if os.path.exists(_configurePath):
            for line in open(_configurePath):
                line = line.strip('\n')
                if line.find("profile") > 0:
                    a=line.split(" ", 1)
                    b=a[1].split("]",1)
                    pro="profile "+b[0]
                if line.find("default") > 0:
                    pro = 'default profile'
                if line.find('=') > 0:
                    list = line.split("=", 1)
                    if pro not in configContent:
                        configContent[pro]={}
                    configContent[pro][list[0]]=list[1]
                else:
                    pass
        config['Configure'] = configContent

        if os.path.exists(_credentialsPath):
            for line in open(_credentialsPath):
                line = line.strip('\n')
                if line.find("profile") > 0:
                    a=line.split(" ", 1)
                    b=a[1].split("]",1)
                    prof="profile "+b[0]
                if line.find("default") > 0:
                    prof = 'default profile'
                if line.find('=') > 0:
                    list = line.split("=", 1)
                    if prof not in credentialsContent:
                        credentialsContent[prof] = {}
                    credentialsContent[prof][list[0]] = list[1]
            else:
                pass
        config['SecretId and Key'] = credentialsContent
        format_output.display_result("showConfigure", config, 'table')
    def importConfig(self):
        pass
    def exportConfig(self):
        pass



if __name__ == "__main__":
    handler = ConfigHandler()
    handler.showConfig()
