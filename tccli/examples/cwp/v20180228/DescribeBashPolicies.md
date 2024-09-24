**Example 1: 策略列表**



Input: 

```
tccli cwp DescribeBashPolicies --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Name": "白名单1",
                "Enable": 1,
                "White": 0,
                "BashAction": 2,
                "Rule": "curl www.qq.com",
                "Level": 2,
                "Scope": 2,
                "Id": 10004,
                "Descript": "message \"白名单1\" not found in language \"zh-CN\"",
                "EventId": 0,
                "CreateTime": "2022-08-19 15:57:45",
                "ModifyTime": "2022-08-30 23:54:43",
                "Uuids": [],
                "DealOldEvents": 0,
                "Quuids": [
                    ""
                ],
                "Category": 1,
                "Rules": {
                    "Process": {
                        "Exe": "/tmp/test"
                    },
                    "PProcess": null,
                    "AProcess": null
                }
            }
        ],
        "RequestId": "f3fe3ac0-099b-4afc-b383-fbf58e8c385a",
        "TotalCount": 1
    }
}
```

