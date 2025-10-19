**Example 1: 查询边缘函数触发规则列表**

查询站点 zone-293e7s5jne1i 下的函数规则。

Input: 

```
tccli teo DescribeFunctionRules --cli-unfold-argument  \
    --ZoneId zone-293e7s5jne1i
```

Output: 
```
{
    "Response": {
        "RequestId": "d7213f7f-a67b-4602-b630-ed6740e1a124",
        "FunctionRules": [
            {
                "RuleId": "rule-53qpdadi",
                "FunctionRuleConditions": [
                    {
                        "RuleConditions": [
                            {
                                "Operator": "equal",
                                "Target": "url",
                                "Values": [
                                    "/test3"
                                ],
                                "IgnoreCase": false,
                                "Name": ""
                            }
                        ]
                    }
                ],
                "TriggerType": "region",
                "RegionMappingSelections": [
                    {
                        "FunctionId": "ef-1pakhnuy",
                        "Regions": [
                            "CN"
                        ]
                    },
                    {
                        "FunctionId": "ef-1wekxwnu",
                        "Regions": [
                            "Default"
                        ]
                    }
                ],
                "FunctionId": "",
                "FunctionName": "",
                "Priority": 2,
                "Remark": "my function rule",
                "CreateTime": "2023-04-19T07:32:09Z",
                "UpdateTime": "2023-04-19T07:36:43Z"
            }
        ]
    }
}
```

