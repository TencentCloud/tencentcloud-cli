**Example 1: 告警中心全量告警示例**



Input: 

```
tccli csip DescribeAlertList --cli-unfold-argument  \
    --MemberId abc \
    --OperatedMemberId abc \
    --AssetType 0 \
    --Filter.Limit 0 \
    --Filter.Offset 0 \
    --Filter.Order abc \
    --Filter.By abc \
    --Filter.Filters.0.Name abc \
    --Filter.Filters.0.Values abc \
    --Filter.Filters.0.OperatorType 0 \
    --Filter.StartTime abc \
    --Filter.EndTime abc
```

Output: 
```
{
    "Response": {
        "AlertList": [
            {
                "ID": "abc",
                "Name": "abc",
                "Source": "abc",
                "Level": 1,
                "Attacker": {
                    "IP": "abc",
                    "HostIP": "abc",
                    "Port": 1,
                    "InstanceID": "abc",
                    "City": "abc",
                    "Province": "abc",
                    "Country": "abc",
                    "Address": "abc",
                    "Latitude": "abc",
                    "Longitude": "abc",
                    "Info": "abc",
                    "Domain": "abc",
                    "Name": "abc",
                    "Account": "abc",
                    "Family": "abc",
                    "VirusName": "abc",
                    "MD5": "abc",
                    "FileName": "abc"
                },
                "Victim": {
                    "IP": "abc",
                    "HostIP": "abc",
                    "Port": 1,
                    "InstanceID": "abc",
                    "City": "abc",
                    "Province": "abc",
                    "Country": "abc",
                    "Address": "abc",
                    "Latitude": "abc",
                    "Longitude": "abc",
                    "Info": "abc",
                    "Domain": "abc",
                    "Name": "abc",
                    "Account": "abc",
                    "Family": "abc",
                    "VirusName": "abc",
                    "MD5": "abc",
                    "FileName": "abc"
                },
                "EvidenceData": "abc",
                "EvidenceLocation": "abc",
                "EvidencePath": "abc",
                "CreateTime": "abc",
                "UpdateTime": "abc",
                "Count": 1,
                "UrgentSuggestion": "abc",
                "RemediationSuggestion": "abc",
                "RiskInvestigation": "abc",
                "RiskTreatment": "abc",
                "Status": 1,
                "ProcessType": "abc",
                "Type": "abc",
                "SubType": "abc",
                "ExtraInfo": {
                    "RelateEvent": {
                        "EventID": "abc",
                        "Description": "abc",
                        "RelatedCount": 0
                    },
                    "LeakContent": "abc",
                    "LeakAPI": "abc",
                    "SecretID": "abc",
                    "Rule": "abc",
                    "RuleDesc": "abc",
                    "ProtocolPort": "abc",
                    "AttackContent": "abc",
                    "AttackIPProfile": "abc",
                    "AttackIPTags": "abc",
                    "RequestMethod": "abc",
                    "HttpLog": "abc",
                    "AttackDomain": "abc",
                    "FilePath": "abc",
                    "UserAgent": "abc",
                    "RequestHeaders": "abc",
                    "LoginUserName": "abc",
                    "VulnerabilityName": "abc",
                    "CVE": "abc",
                    "ServiceProcess": "abc",
                    "FileName": "abc",
                    "FileSize": "abc",
                    "FileMD5": "abc",
                    "FileLastAccessTime": "abc",
                    "FileModifyTime": "abc",
                    "RecentAccessTime": "abc",
                    "RecentModifyTime": "abc",
                    "VirusName": "abc",
                    "VirusFileTags": "abc",
                    "BehavioralCharacteristics": "abc",
                    "ProcessNamePID": "abc",
                    "ProcessPath": "abc",
                    "ProcessCommandLine": "abc",
                    "ProcessPermissions": "abc",
                    "ExecutedCommand": "abc",
                    "AffectedFileName": "abc",
                    "DecoyPath": "abc",
                    "MaliciousProcessFileSize": "abc",
                    "MaliciousProcessFileMD5": "abc",
                    "MaliciousProcessNamePID": "abc",
                    "MaliciousProcessPath": "abc",
                    "MaliciousProcessStartTime": "abc",
                    "CommandContent": "abc",
                    "StartupUser": "abc",
                    "UserGroup": "abc",
                    "NewPermissions": "abc",
                    "ParentProcess": "abc",
                    "ClassName": "abc",
                    "ClassLoader": "abc",
                    "ClassFileSize": "abc",
                    "ClassFileMD5": "abc",
                    "ParentClassName": "abc",
                    "InheritedInterface": "abc",
                    "Comment": "abc",
                    "PayloadContent": "abc",
                    "CallbackAddressPortrait": "abc",
                    "CallbackAddressTag": "abc",
                    "ProcessMD5": "abc",
                    "FilePermission": "abc",
                    "HitProbe": "abc",
                    "HitHoneyPot": "abc",
                    "CommandList": "abc",
                    "AttackEventDesc": "abc",
                    "ProcessInfo": "abc",
                    "UserNameAndPwd": "abc"
                },
                "Key": "abc",
                "Date": "abc",
                "AppID": "abc",
                "NickName": "abc",
                "Uin": "abc"
            }
        ],
        "AlertTypeCount": [
            {
                "Name": "abc",
                "Count": 1
            }
        ],
        "TotalCount": 1,
        "RequestId": "abc"
    }
}
```

