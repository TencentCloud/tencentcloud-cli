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
                "Id": 370572797,
                "Uuid": "1c26308c-5493-4eaf-a817-112ec25f499e",
                "Quuid": "1c26308c-5493-4eaf-a817-112ec25f499e",
                "HostIp": "0.0.0.0",
                "HostName": "销售许可测试机器",
                "Type": 0,
                "ProcessExe": "/usr/bin/crontab",
                "ProcessArgv": "crontab /root/cron.tmp",
                "Target": "/var/spool/cron/#tmp.VM-124-81-tencentos.XXXX2QUwZR",
                "Status": 0,
                "EventCount": 1,
                "RuleId": 1,
                "RuleName": "系统策略-篡改计划任务",
                "Pstree": "[{\"pid\":980959,\"exe\":\"/usr/bin/crontab\",\"account\":\"root:root\",\"cmdline\":\"crontab /root/cron.tmp\",\"start_time\":1729557954,\"type\":1},{\"pid\":2288,\"exe\":\"/root/chaos-executor\",\"account\":\"root:root\",\"cmdline\":\"./chaos-executor d -p 29785a94e8324 -f id_rsa.pub -n Production -s  Production\",\"start_time\":1729471587,\"type\":2}]",
                "CreateTime": "2024-10-22 08:45:58",
                "ModifyTime": "2024-10-22 08:45:58",
                "Level": 1,
                "RuleCategory": 0,
                "MachineStatus": "ONLINE",
                "Description": "检测到系统计划任务被修改",
                "Suggestion": "排查是否为正常业务需要的计划任务修改",
                "PrivateIp": "xx.xx.xx.xx",
                "ExePermission": "-rwsr-xr-x",
                "UserName": "0",
                "UserGroup": "0",
                "ExeMd5": "569f953571579ec4ae613cca7862930a",
                "ExeSize": 0,
                "ExeTime": 1669715461,
                "TargetSize": 981,
                "TargetPermission": "-rw-------",
                "TargetModifyTime": "2024-10-22 08:45:54",
                "TargetCreatTime": "2024-10-22 08:45:54",
                "ExePid": 980959,
                "TargetName": "#tmp.VM-124-81-tencentos.XXXX2QUwZR",
                "Reference": "",
                "ExeName": "crontab",
                "FileAction": "write",
                "MachineExtraInfo": {
                    "WanIP": "0.0.0.0",
                    "PrivateIP": "xx.xx.xx.xx",
                    "NetworkType": 0,
                    "NetworkName": "",
                    "InstanceID": "ins-dsdsds",
                    "HostName": ""
                }
            }
        ],
        "TotalCount": 1,
        "RequestId": "abc"
    }
}
```

