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
                "Name": "rule1",
                "RuleCategory": 1,
                "Rule": [
                    {
                        "ProcessPath": "/data/process1",
                        "Target": "/a/b.txt",
                        "Action": "skip",
                        "FileAction": "write"
                    }
                ],
                "Id": 1
            }
        ],
        "RequestId": "8564b09e-0e04-4516-bb59-db09742503c2"
    }
}
```

