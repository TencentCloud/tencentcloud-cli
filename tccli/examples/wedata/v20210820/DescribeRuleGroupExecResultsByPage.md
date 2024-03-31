**Example 1: 规则组执行结果分页查询接口**



Input: 

```
tccli wedata DescribeRuleGroupExecResultsByPage --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 1 \
    --Filters.0.Name abc \
    --Filters.0.Values abc \
    --OrderFields.0.Name abc \
    --OrderFields.0.Direction abc \
    --ProjectId abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "TotalCount": 1,
            "Items": [
                {
                    "RuleGroupExecId": 1,
                    "RuleGroupId": 1,
                    "TriggerType": 1,
                    "ExecTime": "abc",
                    "Status": 1,
                    "AlarmRuleCount": 1,
                    "TotalRuleCount": 1,
                    "TableOwnerName": "abc",
                    "TableName": "abc",
                    "TableId": "abc",
                    "DatabaseId": "abc",
                    "DatasourceId": "abc",
                    "Permission": true,
                    "ExecDetail": "abc",
                    "EngineType": "abc",
                    "RuleExecResultVOList": [
                        {
                            "RuleExecId": 1,
                            "RuleGroupExecId": 1,
                            "RuleGroupId": 1,
                            "RuleId": 1,
                            "RuleName": "abc",
                            "RuleType": 1,
                            "SourceObjectDataTypeName": "abc",
                            "SourceObjectValue": "abc",
                            "ConditionExpression": "abc",
                            "ExecResultStatus": 1,
                            "TriggerResult": "abc",
                            "CompareResult": {
                                "Items": [
                                    {
                                        "FixResult": 1,
                                        "ResultValue": "abc",
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
                            "TemplateName": "abc",
                            "QualityDim": 1,
                            "TargetDBTableName": "abc",
                            "TargetObjectValue": "abc",
                            "TargetObjectDataType": "abc",
                            "FieldConfig": {
                                "WhereConfig": [
                                    {
                                        "FieldKey": "abc",
                                        "FieldValue": "abc",
                                        "FieldDataType": "abc"
                                    }
                                ],
                                "TableConfig": [
                                    {
                                        "DatabaseId": "abc",
                                        "DatabaseName": "abc",
                                        "TableId": "abc",
                                        "TableName": "abc",
                                        "TableKey": "abc",
                                        "FieldConfig": [
                                            {
                                                "FieldKey": "abc",
                                                "FieldValue": "abc",
                                                "FieldDataType": "abc"
                                            }
                                        ]
                                    }
                                ]
                            },
                            "RelConditionExpr": "abc",
                            "StartTime": "abc",
                            "AlarmLevel": 1
                        }
                    ]
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

