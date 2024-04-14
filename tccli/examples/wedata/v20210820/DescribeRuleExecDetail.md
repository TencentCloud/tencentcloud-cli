**Example 1: 查询规则执行结果详情**



Input: 

```
tccli wedata DescribeRuleExecDetail --cli-unfold-argument  \
    --ProjectId 19419808749824 \
    --RuleExecId 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "DatabaseId": "zw-oGh2Y9XSkZxkPQVA",
            "DatabaseName": "at_dlc_sh_dq",
            "DatasourceId": 6259,
            "DatasourceName": "dlc_qehpp208",
            "DatasourceType": 3,
            "InstanceId": "qep208",
            "RuleExecResult": {
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
                "RuleGroupExecId": 112532,
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
            },
            "TableId": "OE3C5Y0Qp5Sh40qq9g",
            "TableName": "auto_dlc_test_dq",
            "TableOwnerUserId": 10002056
        },
        "RequestId": "572b64f8-9-4207-8385-151c5e553ca1"
    }
}
```

