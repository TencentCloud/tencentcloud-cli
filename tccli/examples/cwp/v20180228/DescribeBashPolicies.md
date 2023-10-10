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
                "Category": 1
            },
            {
                "Name": "拦截规则1",
                "Enable": 1,
                "White": 0,
                "BashAction": 2,
                "Rule": "curl www.test0527.com",
                "Level": 1,
                "Scope": 2,
                "Id": 10005,
                "Descript": "message \"拦截规则1\" not found in language \"zh-CN\"",
                "EventId": 0,
                "CreateTime": "2022-08-23 20:28:02",
                "ModifyTime": "2022-08-23 20:28:02",
                "Uuids": [],
                "DealOldEvents": 0,
                "Quuids": [
                    ""
                ],
                "Category": 1
            }
        ],
        "RequestId": "f3fe3ac0-099b-4afc-b383-fbf58e8c385a",
        "TotalCount": 2
    }
}
```

**Example 2: 策略列表1**



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
                "Descript": "白名单1",
                "EventId": 0,
                "CreateTime": "2022-08-19 15:57:45",
                "ModifyTime": "2022-08-30 23:54:43",
                "Uuids": [],
                "DealOldEvents": 0,
                "Quuids": [
                    ""
                ],
                "Category": 1
            },
            {
                "Name": "拦截规则1",
                "Enable": 1,
                "White": 0,
                "BashAction": 2,
                "Rule": "curl www.test0527.com",
                "Level": 1,
                "Scope": 2,
                "Id": 10005,
                "Descript": "拦截规则1",
                "EventId": 0,
                "CreateTime": "2022-08-23 20:28:02",
                "ModifyTime": "2022-08-23 20:28:02",
                "Uuids": [],
                "DealOldEvents": 0,
                "Quuids": [
                    ""
                ],
                "Category": 1
            }
        ],
        "RequestId": "ab327fc0-3d09-4129-ae1b-7fb7d61a0c01",
        "TotalCount": 2
    }
}
```

