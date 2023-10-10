**Example 1: 获取漏洞防御事件详情**



Input: 

```
tccli cwp DescribeDefenceEventDetail --cli-unfold-argument  \
    --Id 123
```

Output: 
```
{
    "Response": {
        "Data": {
            "City": "深圳",
            "StackTrace": "xx",
            "Fix": "修复描述",
            "NetworkPayload": "xx",
            "Id": 0,
            "SourceIp": "xx",
            "Status": 0,
            "Description": "xx",
            "EventType": 1,
            "ExceptionPstree": "xx",
            "MergeTime": "xx",
            "Count": 0,
            "MachineStatus": "ONLINE",
            "VulName": "xx",
            "Alias": "xx",
            "MainClass": "xx.class",
            "CveId": "xx",
            "Pid": 0,
            "PrivateIp": "xx",
            "PublicIp": "xx",
            "Quuid": "xx",
            "EventDetail": "xx",
            "SourcePort": [
                1
            ],
            "CreateTime": "xx"
        },
        "RequestId": "xx"
    }
}
```

