**Example 1: 高危命令事件列表**



Input: 

```
tccli cwp DescribeBashEventsNew --cli-unfold-argument  \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Uuid": "02db9a21-78fe-4a4c-b96f-a11bf819a962",
                "Id": 3148114,
                "Quuid": "02db9a21-78fe-4a4c-b96f-a11bf819a962",
                "HostIp": "192.168.111.28",
                "User": "root",
                "Platform": 4,
                "BashCmd": "./r3hook_tool moc -var www.test123.com",
                "RuleId": 0,
                "RuleName": "sysrule_custom_procmon_1",
                "RuleLevel": 1,
                "Status": 0,
                "CreateTime": "2022-09-01 17:28:39",
                "MachineName": "v_llzlu恶意请求",
                "DetectBy": 0,
                "Pid": "0",
                "Exe": "",
                "ModifyTime": "0001-01-01 00:00:00",
                "RegexBashCmd": "\\./r3hook_tool moc -var www\\.test123\\.com",
                "MachineType": 0,
                "RuleCategory": 0
            }
        ],
        "RequestId": "c787b780-0a35-4fa5-aca3-db339b9a20e8",
        "TotalCount": 51315
    }
}
```

