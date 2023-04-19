**Example 1: 核心文件监控事件列表**

正常获取

Input: 

```
tccli cwp DescribeFileTamperEvents --cli-unfold-argument  \
    --Offset 1 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "HostName": "abc",
                "HostIp": "abc",
                "CreateTime": "abc",
                "ModifyTime": "abc",
                "Id": 1,
                "Uuid": "abc",
                "Quuid": "abc",
                "Type": 1,
                "ProcessExe": "abc",
                "ProcessArgv": "abc",
                "Target": "abc",
                "Status": 1,
                "EventCount": 1,
                "RuleId": 1,
                "RuleName": "abc",
                "Pstree": "abc",
                "RuleCategory": 1,
                "MachineStatus": "abc",
                "Description": "abc",
                "Suggestion": "abc",
                "PrivateIp": "abc",
                "ExePermission": "abc",
                "UserName": "abc",
                "UserGroup": "abc",
                "ExeMd5": "abc",
                "ExeSize": 1,
                "ExeTime": 1,
                "TargetSize": 1,
                "TargetPermission": "abc",
                "TargetModifyTime": "abc",
                "TargetCreatTime": "abc",
                "ExePid": 1,
                "TargetName": "abc",
                "Reference": "abc",
                "Level": 1,
                "ExeName": "abc",
                "MachineExtraInfo": {
                    "WanIP": "abc",
                    "PrivateIP": "abc",
                    "NetworkType": 0,
                    "NetworkName": "abc",
                    "InstanceID": "abc",
                    "HostName": "abc"
                },
                "FileAction": "abc"
            }
        ],
        "TotalCount": 1,
        "RequestId": "abc"
    }
}
```

