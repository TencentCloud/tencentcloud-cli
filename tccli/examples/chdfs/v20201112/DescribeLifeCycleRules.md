**Example 1: 查看生命周期规则列表**

查看生命周期规则列表

Input: 

```
tccli chdfs DescribeLifeCycleRules --cli-unfold-argument  \
    --FileSystemId f4mnvilzmdd
```

Output: 
```
{
    "Response": {
        "LifeCycleRules": [
            {
                "LifeCycleRuleId": 1,
                "LifeCycleRuleName": "test1",
                "Path": "/test1",
                "Transitions": [
                    {
                        "Days": 7,
                        "Type": 1
                    }
                ],
                "Status": 1,
                "CreateTime": "2019-07-30T16:24:38+08:00"
            },
            {
                "LifeCycleRuleId": 2,
                "LifeCycleRuleName": "test2",
                "Path": "/test2",
                "Transitions": [
                    {
                        "Days": 7,
                        "Type": 1
                    },
                    {
                        "Days": 7,
                        "Type": 2
                    }
                ],
                "Status": 1,
                "CreateTime": "2019-07-30T16:24:38+08:00"
            }
        ],
        "RequestId": "19d240f4-156d-4a3c-856c-216d64a6bb4a"
    }
}
```

