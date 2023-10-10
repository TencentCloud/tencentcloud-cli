**Example 1: 核心文件监控事件列表**



Input: 

```
tccli cwp DescribeMachineFileTamperRules --cli-unfold-argument  \
    --Limit 1 \
    --Uuid xx \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "List": [
            {
                "Rule": [
                    {
                        "Action": "xx",
                        "ProcessPath": "xx",
                        "Target": "xx"
                    }
                ],
                "Name": "xx",
                "RuleCategory": 1,
                "Id": 1
            }
        ],
        "RequestId": "c741a4fd-776f-499b-85a2-7bc70fd5b92s"
    }
}
```

