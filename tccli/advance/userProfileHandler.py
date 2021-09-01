__author__ = 'xxxx'
import os,sys
import linecache

#parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#sys.path.insert(0,parentdir)
#from .. import handleCmd

PY2 = sys.version_info[0] == 2

class ProfileCmd:
    useProfile = 'useProfile'
    delProfile = 'delProfile'
    addProfile = 'addProfile'
    name = 'name'
class ProfileHandler:
    def __init__(self):
        from .. import handleCmd
        self.handleCmd = handleCmd.handleCmd()

    def getProfileHandlerCmd(self):
        return [ProfileCmd.useProfile, ProfileCmd.addProfile]

    def getProfileHandlerOptions(self):
        return ['--name']

    def useProfileCmd(self, cmd, keyValues):
        if cmd.lower() == ProfileCmd.useProfile.lower():
            if ProfileCmd.name in keyValues and len(keyValues[ProfileCmd.name]) > 0:
                _value = keyValues[ProfileCmd.name][0] # use the first value
                if (self.setUserProfile(_value) == True):
                    print("Set user "+_value +" as the default user!")
            else:
                print("Your input is error! Please use cmd \'qcloudcli useprofile --name XX\' to set the default user.")
        else:
            print("[" + cmd + "] is not right, do you mean "+ProfileCmd.useProfile+" ?")


    def delProfileCmd(self, cmd, keyValues):
        if cmd.lower() == ProfileCmd.delProfile.lower():
            if ProfileCmd.name in keyValues and len(keyValues[ProfileCmd.name]) > 0:
                _value = keyValues[ProfileCmd.name][0]
                if (self.delUserProfile(_value) == True):
                    print("Successfully deleted user "+_value +"!")
            else:
                print("Your input is error! Please use cmd \'qcloudcli delprofile --name XX\' to delete user.")
        else:
            print("[" + cmd + "] is not right, do you mean "+ProfileCmd.delProfile+" ?")

    def addProfileCmd(self, keyValues):
        def user_input(text):
            if PY2:
                return raw_input(text)
            else:
                return input(text)

        userKey = ''
        userSecret = ''
        newProfileName = ''
        #check --name is valid
        if ProfileCmd.name in keyValues and len(keyValues[ProfileCmd.name]) > 0:
            _value = keyValues[ProfileCmd.name][0] # check the first value
            # only input key and secret
            newProfileName = _value
        else:
            # need input profilename key and value
            newProfileName = user_input("New profile name: ").strip()

        # check profile exist?
        _configurePath =os.path.join(self.handleCmd.showQcloudConfigurePath(),self.handleCmd.configure)
        with open(_configurePath, 'r') as f:
            contents = f.readlines()
        _sectionName = '[profile '+newProfileName+']'
        for i in range(len(contents)):
            line = contents[i]
            if line.strip() == _sectionName:
                print("profile %s has been existed, you can use 'qcloudcli configure --profile %s' to modify configure." % (newProfileName, newProfileName))
                return

        userKey = user_input("Qcloud API SecretId: ")
        userSecret = user_input("Qcloud API SecretKey: ")
        userRegion = user_input("Region Id(gz,hk,ca,sh,shjr,bj,sg): ")
        userOutput = user_input("Output Format(json,table,text): ")
        _credentialsPath = os.path.join(self.handleCmd.showQcloudConfigurePath(),self.handleCmd.credentials)
        if os.path.exists(_credentialsPath):
            f = open(_credentialsPath, 'a')
            try:
                content = "[profile "+newProfileName+"]\nqcloud_secretkey = "+userSecret+"\nqcloud_secretid = " +userKey+ "\n"
                f.write(content)
            finally:
                f.close()
        else:
            print("your input is not right, do you want "+ProfileCmd.addProfile+" ?")

        #_configurePath =os.path.join(self.handleCmd.showQcloudConfigurePath(),self.handleCmd.configure)
        if os.path.exists(_configurePath):
            f = open(_configurePath, 'a')
            try:
                content = "[profile " + newProfileName + "]\noutput = " + userOutput + "\nregion = " + userRegion + "\n"
                f.write(content)
            finally:
                f.close()
        else:
            print("your input is not right, do you mean "+ProfileCmd.addProfile+" ?")


    def setUserProfile(self,value):
        _configurePath =  os.path.join(self.handleCmd.showQcloudConfigurePath(), self.handleCmd.configure)
        _credentialsPath =  os.path.join(self.handleCmd.showQcloudConfigurePath(),self.handleCmd.credentials)
        useoutput = ''
        useregion = ''
        usekey = ''
        useid = ''
        if os.path.exists(_configurePath):
            va_flag = 0

            f = open(_configurePath, 'r+')
            flist = f.readlines()
            for i in range(len(flist)-2):
                #if flist[i].find("[profile %s]" % value) > 0:
                if flist[i].strip() == ("[profile %s]" % value):
                    va_flag = 1
                    flist[i] = "[flag]\n"
                    if (not "output" in flist[i+1] and not "output" in flist[i+2]) or (not "region" in flist[i+1] and not "region" in flist[i+2]):
                        print("You have not set user \'" + value + "\' output or region!")
                        return False
                    useoutput = flist[i+1]
                    useregion = flist[i+2]
                    break

            if va_flag == 0:
                print("Cannot find user name \'"+ value +"\'!")
                return False

            for j in range(len(flist)-2):
                #if flist[j].find("default") > 0:
                if flist[j].strip() == "[default]":
                    flist[j] = "[profile " + value + "]\n"
                    if "[" in flist[j+1]:
                        flist.insert(j, useoutput)
                        flist.insert(j + 1, useregion)
                        break
                    if "output" in flist[j+1] and not "region" in flist[j+2]:
                        flist.insert(j + 1, useregion)
                    if "region" in flist[j+1] and not "output" in flist[j+2]:
                        flist.insert(j, useoutput)
                    flist[j+1] = useoutput
                    flist[j + 2] = useregion

            for o in range(len(flist) - 2):
                if "flag" in flist[o]:
                    flist[o] = "[default]\n"
                    break

            f = open(_configurePath, 'w+')
            f.writelines(flist)
        else:
            print("Cannot find user name \'"+ value +"\'!")
            return False

        if os.path.exists(_credentialsPath):
            key_flag = 0
            id_flag = 0

            f = open(_credentialsPath, 'r+')
            flist = f.readlines()
            for l in range(len(flist)-2):
                #if flist[l].find("profile "+value) > 0:
                if flist[l].strip() == ("[profile %s]" % value):
                    key_flag = 1
                    flist[l] = "[flag]\n"
                    if (not "qcloud_secretkey" in flist[l+1] and not "qcloud_secretkey" in flist[l+2]) or (not "qcloud_secretid" in flist[l+1] and not "qcloud_secretid" in flist[l+2]):
                        print("You have not set user \'" + value + "\' SecretKey or SecretId!")
                        return False
                    usekey = flist[l + 1]
                    useid = flist[l + 2]
                    break

            if key_flag == 0:
                print("Cannot find user name \'" + value + "\'!")
                return False
            for m in range(len(flist)-2):
                #if flist[m].find("default") > 0:
                if flist[m].strip() == "[default]":
                    flist[m] = "[profile " + value + "]\n"
                    if "[" in flist[m + 1]:
                        flist.insert(m, usekey)
                        flist.insert(m + 1, useid)
                        break
                    if "qcloud_secretkey" in flist[m + 1] and not "qcloud_secretid" in flist[m + 2]:
                        flist.insert(m + 1, usekey)
                    if "qcloud_secretid" in flist[m + 1] and not "qcloud_secretkey" in flist[m + 2]:
                        flist.insert(m, useid)
                    flist[m + 1] = usekey
                    flist[m + 2] = useid

            for p in range(len(flist) - 2):
                if "flag" in flist[p]:
                    flist[p] = "[default]\n"
                    break

            f = open(_credentialsPath, 'w+')
            f.writelines(flist)
        else:
            print("Cannot find user name \'"+ value +"\'!")
            return False

        return True

    def delUserProfile(self, value):
        _configurePath = os.path.join(self.handleCmd.showQcloudConfigurePath(), self.handleCmd.configure)
        _credentialsPath = os.path.join(self.handleCmd.showQcloudConfigurePath(), self.handleCmd.credentials)
        useoutput = ''
        useregion = ''
        usekey = ''
        useid = ''
        if os.path.exists(_configurePath):
            va_flag = 0
            key_flag = 0
            f = open(_configurePath, 'r+')
            flist = f.readlines()
            for i in range(len(flist) - 2):
                #if flist[i].find("[profile %s]" % value) > 0:
                if flist[i].strip() == ("[profile %s]" % value):
                    va_flag = 1
                    flist[i] = ""
                    if (not "output" in flist[i + 1] and not "region" in flist[i + 1]):
                       break
                    flist[i + 1] = ""
                    if (not "output" in flist[i + 2] and not "region" in flist[i + 2]):
                       break
                    flist[i + 2] = ""
                    break

            if va_flag == 0:
                print("Cannot find user name \'" + value + "\'!")
                return False

            f = open(_configurePath, 'w+')
            f.writelines(flist)
        else:
            print("Cannot find user name \'"+ value +"\'!")
            return False

        if os.path.exists(_credentialsPath):

            f = open(_credentialsPath, 'r+')
            flist = f.readlines()
            for l in range(len(flist) - 2):
                #if flist[l].find("[profile %s]" % value) > 0:
                if flist[l].strip() == ("[profile %s]" % value):
                    key_flag = 1
                    flist[l] = ""
                    if (not "qcloud_secretkey" in flist[l + 1] and not "qcloud_secretid" in flist[l + 1]):
                        break
                    flist[l + 1] = ""
                    if (not "qcloud_secretkey" in flist[l + 2] and not "qcloud_secretid" in flist[l + 2]):
                        break
                    flist[l + 2] = ""
                    break

            if key_flag == 0:
                print("Cannot find user name \'" + value + "\'!")
                return False
            f = open(_credentialsPath, 'w+')
            f.writelines(flist)
        else:
            print("Cannot find user name \'"+ value +"\'!")
            return False

        return True

if __name__ == "__main__":
    pass
