**Example 1: 告警中心全量告警示例**



Input: 

```
tccli csip DescribeAlertList --cli-unfold-argument  \
    --Filter.Filters.0.Name Status \
    --Filter.Filters.0.Values 0 \
    --Filter.Filters.0.OperatorType 7 \
    --Filter.Filters.1.Name Uin \
    --Filter.Filters.1.Values 1123213213 \
    --Filter.Filters.1.OperatorType 7 \
    --Filter.Limit 10 \
    --Filter.Offset 0 \
    --Filter.StartTime 2024-10-24 00:00:00 \
    --Filter.EndTime 2024-10-30 23:59:59 \
    --MemberId mem-tencent-1829
```

Output: 
```
{
    "Response": {
        "AlertList": [
            {
                "Action": 1,
                "AppID": "18742",
                "Attacker": {
                    "Account": "18742",
                    "Address": "中国上海",
                    "AssetType": 2,
                    "City": "上海",
                    "ContainerID": "ins-dd213833",
                    "ContainerName": "misakey",
                    "Country": "中国",
                    "Domain": "main.1872.net",
                    "Family": "APT",
                    "FileName": "notdad.exe",
                    "HostIP": "172.16.17.32",
                    "IP": "202.108.127.12",
                    "Info": "mail",
                    "InstanceID": "ins-dd213833",
                    "Latitude": "41.2",
                    "Longitude": "38.2",
                    "MD5": "d41d8cd98f00b204e9800998ecf8427e",
                    "Name": "sdb",
                    "OriginIP": "202.108.127.12",
                    "Port": 20,
                    "Province": "广东",
                    "VirusName": "ransomware"
                },
                "Count": 7,
                "CreateTime": "2024-10-30T09:09:14+08:00",
                "Date": "2024-10-30T00:00:00+08:00",
                "EvidenceData": "18742",
                "EvidenceLocation": "xin.1872.net",
                "EvidencePath": "path/to/file",
                "ExtraInfo": {
                    "AffectedFileName": "executable.exe",
                    "AttackIPTags": "APT",
                    "BehavioralCharacteristics": "cmd.exe",
                    "CallbackAddressTag": "APT",
                    "ClassName": "java.lang.Runtime",
                    "CommandContent": "mkdir /tmp/18742",
                    "DecoyPath": "path/to/file",
                    "ExecutedCommand": "sh -c /bin/bash",
                    "FileLastAccessTime": "2024-10-30T00:00:00+08:00",
                    "FileMD5": "d41d8cd98f00b204e9800998ecf8427e",
                    "FileModifyTime": "2024-10-30T00:00:00+08:00",
                    "FileName": "file",
                    "FilePath": "file/path/to/file",
                    "FilePermission": "0777",
                    "FileSize": "0.00B",
                    "LoginUserName": "user1",
                    "MaliciousProcessFileMD5": "d41d8cd98f00b204e9800998ecf8427e",
                    "MaliciousProcessFileSize": "0.00B",
                    "MaliciousProcessNamePID": "(0)",
                    "MaliciousProcessPath": "path/to/process",
                    "MaliciousProcessStartTime": "0001-01-01T08:05:43+08:05",
                    "NewPermissions": "0777",
                    "ParentProcess": "sh",
                    "ProcessCommandLine": "sh -c rm -rf /",
                    "ProcessName": "(0)",
                    "ProcessNamePID": "(0)",
                    "ProcessPath": "path/to/process",
                    "ProtocolPort": "8989",
                    "RecentAccessTime": "2024-10-10T09:09:14+08:00",
                    "RecentModifyTime": "2024-10-30T09:09:14+08:00",
                    "RelateEvent": {
                        "Description": "user1登录系统",
                        "EventID": "event-1232412",
                        "RelatedCount": 3
                    },
                    "Rule": "system1",
                    "StartupUser": "root",
                    "UserGroup": "admin",
                    "VirusFileTags": "APT",
                    "VirusName": "virus1"
                },
                "ID": "alert-a18d7e42",
                "Key": "main.1241.net#ins-1421",
                "Level": 5,
                "LogSearch": "id:alert-a18d7e42",
                "LogType": "2_3",
                "Name": "访问恶意地址或域名",
                "NickName": "nickname",
                "ProcessType": "BlockCallbackAddress,IsolateAsset",
                "RemediationSuggestion": "开启云防火墙-NAT边界防火墙，管控拦截恶意主动外联，前往主机安全进行深度安全检测",
                "RiskInvestigation": "none",
                "RiskTreatment": "none",
                "Source": "CWP",
                "Status": 0,
                "SubType": "MaliciousRequest",
                "Type": "ActiveOutbound",
                "Uin": "18342",
                "UpdateTime": "2024-10-30T09:10:55+08:00",
                "UrgentSuggestion": "封禁回连地址",
                "Victim": {
                    "Account": "12742",
                    "Address": "1.4.42.2 | 10.0.0.2",
                    "AssetType": 1,
                    "City": "上海",
                    "ContainerID": "ins-218742",
                    "ContainerName": "container1",
                    "Country": "中国",
                    "Domain": "www.domain.com",
                    "Family": "malware",
                    "FileName": "wodex.exe",
                    "HostIP": "10.0.0.2",
                    "IP": "1.4.42.2",
                    "Info": "mail",
                    "InstanceID": "ins-218742",
                    "Latitude": "27.1",
                    "Longitude": "12.9",
                    "MD5": "d41d8cd98f00b204e9800998ecf8427e",
                    "Name": "name1",
                    "OriginIP": "1.4.42.2",
                    "Port": 824,
                    "Province": "广东",
                    "VirusName": "virus1"
                }
            }
        ],
        "AlertTypeCount": [
            {
                "Count": 66,
                "Name": "SuspectIntrusion"
            },
            {
                "Count": 220,
                "Name": "InfoGathering"
            },
            {
                "Count": 94,
                "Name": "ActiveOutbound"
            },
            {
                "Count": 153,
                "Name": "ScanDetect"
            },
            {
                "Count": 58,
                "Name": "HostAbnormality"
            },
            {
                "Count": 4,
                "Name": "ContainerAbnormality"
            },
            {
                "Count": 9085,
                "Name": "AttackAttempts"
            }
        ],
        "RequestId": "123242123-d199-4c1c-9229-5731e460b8b6",
        "ReturnCode": 0,
        "ReturnMsg": "success",
        "TotalCount": 9680
    }
}
```

