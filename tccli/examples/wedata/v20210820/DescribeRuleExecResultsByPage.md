**Example 1: 示例**



Input: 

```
tccli wedata DescribeRuleExecResultsByPage --cli-unfold-argument ```

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
                    "SourceObjectValue": "1",
                    "ConditionExpression": "expr",
                    "ExecResultStatus": 1,
                    "TriggerResult": "abc",
                    "CompareResult": {
                        "Items": [
                            {
                                "FixResult": 1,
                                "ResultValue": "1",
                                "Values": [
                                    {
                                        "ValueType": 1,
                                        "Value": "1"
                                    }
                                ],
                                "Operator": "zhyangsan",
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
                                "DatabaseId": "abc6578trfgvyn",
                                "DatabaseName": "test",
                                "TableId": "89uhon890uoh",
                                "TableName": "test",
                                "TableKey": "6789tgy",
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
                    "StartTime": "abc",
                    "AlarmLevel": 1
                }
            ]
        },
        "RequestId": "0ff4e8ae-ebea-4a41-8aa2-1f6bc4b68e69"
    }
}
```

