**Example 1: 获取终端自定义分组划分规则**

获取终端自定义分组划分规则

Input: 

```
tccli ioa DescribeAutoVirtualGroupRule --cli-unfold-argument  \
    --DomainInstanceId 3 \
    --VirtualGroupId 9 \
    --OsType 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "AutoMinute": 10,
            "AutoRules": {
                "SimpleRules": [
                    {
                        "Expressions": [
                            {
                                "Items": [
                                    {
                                        "Key": "mid",
                                        "Operate": "等于",
                                        "Value": "111111111"
                                    }
                                ]
                            }
                        ]
                    }
                ]
            },
            "IsAuto": true,
            "RuleId": 2,
            "TimeType": 3,
            "VirtualGroupId": 9
        },
        "RequestId": "69cc6953-259a-4414-9a86-172744f3032a"
    }
}
```

