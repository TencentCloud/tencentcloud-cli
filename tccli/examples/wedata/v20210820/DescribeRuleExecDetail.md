**Example 1: 查询规则执行结果详情**



Input: 

```
tccli wedata DescribeRuleExecDetail --cli-unfold-argument  \
    --RuleExecId 1 \
    --ProjectId xx
```

Output: 
```
{
    "Response": {
        "Data": {
            "DatabaseId": "xx",
            "DatasourceName": "xx",
            "InstanceId": "xx",
            "TableName": "xx",
            "DatasourceId": 1,
            "DatabaseName": "xx",
            "RuleExecResult": {
                "RuleType": 1,
                "QualityDim": 1,
                "RelConditionExpr": "xx",
                "RuleGroupId": 1,
                "RuleExecId": 1,
                "ConditionExpression": "xx",
                "RuleId": 1,
                "ExecResultStatus": 1,
                "TargetDBTableName": "xx",
                "SourceObjectValue": "xx",
                "RuleGroupExecId": 1,
                "SourceObjectDataTypeName": "xx",
                "TargetObjectDataType": "xx",
                "RuleName": "xx",
                "TriggerResult": "xx",
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
                },
                "TargetObjectValue": "xx",
                "TemplateName": "xx",
                "FieldConfig": {
                    "WhereConfig": [
                        {
                            "FieldKey": "xx",
                            "FieldValue": "xx",
                            "FieldDataType": "xx"
                        }
                    ],
                    "TableConfig": [
                        {
                            "DatabaseId": "xx",
                            "FieldConfig": [
                                {
                                    "FieldKey": "xx",
                                    "FieldValue": "xx",
                                    "FieldDataType": "xx"
                                }
                            ],
                            "TableName": "xx",
                            "TableId": "xx",
                            "DatabaseName": "xx",
                            "TableKey": "xx"
                        }
                    ]
                }
            },
            "TableId": "xx"
        },
        "RequestId": "xx"
    }
}
```

