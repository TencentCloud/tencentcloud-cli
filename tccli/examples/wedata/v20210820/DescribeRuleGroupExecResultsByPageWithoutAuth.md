**Example 1: 示例**



Input: 

```
tccli wedata DescribeRuleGroupExecResultsByPageWithoutAuth --cli-unfold-argument ```

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
                    "TableOwnerName": "zhangsan",
                    "TableName": "test",
                    "TableId": "234rewfcd",
                    "DatabaseId": "23434rt3fewc3f",
                    "DatasourceId": "78987623",
                    "Permission": true,
                    "ExecDetail": "abc",
                    "EngineType": "abc",
                    "RuleExecResultVOList": [
                        {
                            "RuleExecId": 1,
                            "RuleGroupExecId": 1,
                            "RuleGroupId": 1,
                            "RuleId": 1,
                            "RuleName": "规则1",
                            "RuleType": 1,
                            "SourceObjectDataTypeName": "int",
                            "SourceObjectValue": "1",
                            "ConditionExpression": "abc",
                            "ExecResultStatus": 1,
                            "TriggerResult": "abc",
                            "CompareResult": {
                                "Items": [
                                    {
                                        "FixResult": 1,
                                        "ResultValue": "value",
                                        "Values": [
                                            {
                                                "ValueType": 1,
                                                "Value": "1"
                                            }
                                        ],
                                        "Operator": "zhangsan",
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
                            "TargetDBTableName": "test",
                            "TargetObjectValue": "1",
                            "TargetObjectDataType": "int",
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
                                        "DatabaseId": "79ughjib",
                                        "DatabaseName": "test",
                                        "TableId": "679yu89h0-97ug",
                                        "TableName": "test",
                                        "TableKey": "asdf2we3r",
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
                }
            ]
        },
        "RequestId": "0ff4e8ae-ebea-4a41-8aa2-1f6bc4b68e69"
    }
}
```

