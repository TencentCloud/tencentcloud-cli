**Example 1: 规则执行结果列表查询**



Input: 

```
tccli wedata DescribeRuleExecResults --cli-unfold-argument  \
    --RuleGroupExecId 1 \
    --ProjectId 123456
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "AlarmLevel": 1,
                    "CompareResult": {
                        "Items": [
                            {
                                "CompareType": 5,
                                "FixResult": null,
                                "Operator": "==",
                                "ResultValue": "3.0000",
                                "ValueComputeType": null,
                                "Values": [
                                    {
                                        "Value": "0",
                                        "ValueType": 3
                                    }
                                ]
                            }
                        ],
                        "PassRows": null,
                        "TotalRows": 3,
                        "TriggerRows": null
                    },
                    "ConditionExpression": "全表",
                    "ExecResultStatus": 1,
                    "FieldConfig": null,
                    "QualityDim": 5,
                    "RelConditionExpr": null,
                    "RuleExecId": 341876,
                    "RuleGroupExecId": 11232,
                    "RuleGroupId": 308,
                    "RuleId": 885,
                    "RuleName": "data_in_time_fail",
                    "RuleType": 1,
                    "SourceObjectDataTypeName": "table",
                    "SourceObjectValue": "表",
                    "StartTime": "2024-04-09 21:10:25",
                    "TargetDBTableName": "null.null",
                    "TargetObjectDataType": null,
                    "TargetObjectValue": null,
                    "TemplateName": "数据产出及时性",
                    "TriggerResult": "无"
                }
            ],
            "TotalCount": 1
        },
        "RequestId": "8150d24f-6ee7-4797-a7fccc771e008"
    }
}
```

