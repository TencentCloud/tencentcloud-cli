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
            "TotalCount": 1,
            "Items": [
                {
                    "RuleExecId": 1,
                    "RuleGroupExecId": 1,
                    "RuleGroupId": 1,
                    "RuleId": 1,
                    "RuleName": "规则1",
                    "RuleType": 1,
                    "SourceObjectDataTypeName": "name",
                    "SourceObjectValue": "value",
                    "ConditionExpression": "exp",
                    "ExecResultStatus": 1,
                    "TriggerResult": "result",
                    "CompareResult": {
                        "Items": [
                            {
                                "FixResult": 1,
                                "ResultValue": "value",
                                "Values": [
                                    {
                                        "ValueType": 1,
                                        "Value": "abc"
                                    }
                                ],
                                "Operator": "abc",
                                "CompareType": 1,
                                "ValueComputeType": 1
                            }
                        ],
                        "TotalRows": 1,
                        "PassRows": 1,
                        "TriggerRows": 1
                    },
                    "TemplateName": "name",
                    "QualityDim": 1,
                    "TargetDBTableName": "name",
                    "TargetObjectValue": "value",
                    "TargetObjectDataType": "type",
                    "FieldConfig": {
                        "WhereConfig": [
                            {
                                "FieldKey": "name",
                                "FieldValue": "zhangsan",
                                "FieldDataType": "string"
                            }
                        ],
                        "TableConfig": [
                            {
                                "DatabaseId": "9uihjbkjhu78hui",
                                "DatabaseName": "dbtest",
                                "TableId": "abc",
                                "TableName": "test",
                                "TableKey": "abc",
                                "FieldConfig": [
                                    {
                                        "FieldKey": "id",
                                        "FieldValue": "1",
                                        "FieldDataType": "int"
                                    }
                                ]
                            }
                        ]
                    },
                    "RelConditionExpr": "expr",
                    "StartTime": "2023-10-01",
                    "AlarmLevel": 1
                }
            ]
        },
        "RequestId": "0ff4e8ae-ebea-4a41-8aa2-1f6bc4b68e69"
    }
}
```

