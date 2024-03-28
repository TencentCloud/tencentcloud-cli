**Example 1: 查询规则执行结果详情**



Input: 

```
tccli wedata DescribeRuleExecDetail --cli-unfold-argument  \
    --ProjectId abc \
    --RuleExecId 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "DatasourceId": 1,
            "DatasourceName": "hive89yuhihutg",
            "DatabaseId": "89y7hui87by",
            "DatabaseName": "dbName",
            "InstanceId": "978uijhbb87",
            "TableId": "0oi8hejnfc",
            "TableName": "test",
            "RuleExecResult": {
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
                "TriggerResult": "res",
                "CompareResult": {
                    "Items": [
                        {
                            "FixResult": 1,
                            "ResultValue": "value",
                            "Values": [
                                {
                                    "ValueType": 1,
                                    "Value": "10"
                                }
                            ],
                            "Operator": ">",
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
                            "FieldKey": "name",
                            "FieldValue": "zhangsan",
                            "FieldDataType": "string"
                        }
                    ],
                    "TableConfig": [
                        {
                            "DatabaseId": "897yuhijjhu8h89u",
                            "DatabaseName": "name",
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
                "StartTime": "abc",
                "AlarmLevel": 1
            },
            "TableOwnerUserId": 1,
            "DatasourceType": 1
        },
        "RequestId": "0ff4e8ae-ebea-4a41-8aa2-1f6bc4b68e69"
    }
}
```

