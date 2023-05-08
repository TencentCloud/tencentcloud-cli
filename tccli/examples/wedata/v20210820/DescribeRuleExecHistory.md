**Example 1: 查询规则执行历史， 最近30条**

查询规则执行历史， 最近30条

Input: 

```
tccli wedata DescribeRuleExecHistory --cli-unfold-argument  \
    --ProjectId 1 \
    --RuleId 1
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "RuleType": 1,
                "QualityDim": 1,
                "RuleId": 1,
                "RuleExecId": 1,
                "ConditionExpression": "xx",
                "RuleGroupId": 1,
                "ExecResultStatus": 1,
                "SourceObjectValue": "xx",
                "RuleGroupExecId": 1,
                "SourceObjectDataTypeName": "xx",
                "RuleName": "xx",
                "TriggerResult": "xx",
                "TemplateName": "xx",
                "CompareResult": {
                    "Items": [
                        {
                            "ResultValue": "xx",
                            "FixResult": 1,
                            "ValueComputeType": 1,
                            "Values": [
                                {
                                    "ValueType": 1,
                                    "Value": "xx"
                                }
                            ],
                            "CompareType": 1,
                            "Operator": "xx"
                        }
                    ]
                }
            }
        ],
        "RequestId": "xx"
    }
}
```

