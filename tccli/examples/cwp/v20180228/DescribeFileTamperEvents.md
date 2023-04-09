**Example 1: 核心文件监控事件列表**



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
        "TotalCount": 1,
        "List": [
            {
                "Status": 1,
                "RuleId": 1,
                "Uuid": "xx",
                "EventCount": 1,
                "Pstree": "xx",
                "HostName": "xx",
                "RuleName": "xx",
                "Id": 1,
                "ProcessArgv": "xx",
                "ProcessExe": "xx",
                "Quuid": "xx",
                "ModifyTime": "xx",
                "HostIp": "xx",
                "Type": 1,
                "CreateTime": "xx",
                "Target": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

