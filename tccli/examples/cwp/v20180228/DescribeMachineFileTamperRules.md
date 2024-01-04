**Example 1: 核心文件监控事件列表**



Input: 

```
tccli cwp DescribeMachineFileTamperRules --cli-unfold-argument  \
    --Offset 1 \
    --Limit 1 \
    --Uuid 10ee1dad-ed42-4f98-8c9e-bfaa48fcb787
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "List": [
            {
                "Name": "abc",
                "RuleCategory": 1,
                "Rule": [
                    {
                        "ProcessPath": "abc",
                        "Target": "abc",
                        "Action": "abc",
                        "FileAction": "abc"
                    }
                ],
                "Id": 1
            }
        ],
        "RequestId": "abc"
    }
}
```

