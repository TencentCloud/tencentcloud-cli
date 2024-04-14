**Example 1: 规则组执行结果分页查询接口**



Input: 

```
tccli wedata DescribeRuleGroupExecResultsByPage --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 1 \
    --Filters.0.Name StartTime \
    --Filters.0.Values 1712160000 \
    --OrderFields.0.Name CitationCount \
    --OrderFields.0.Direction DESC \
    --ProjectId 66661616161616161616
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "AlarmRuleCount": 1,
                    "DatabaseId": "sqhsS5G57A",
                    "DatasourceId": "92",
                    "EngineType": "HIVE",
                    "ExecDetail": "2024-04-07 00:00:00 ~ 2099-12-31 23:59:59，每间隔10分钟执行一次",
                    "ExecTime": "2024-04-10 17:01:23",
                    "Permission": true,
                    "RuleExecResultVOList": [
                        {
                            "AlarmLevel": 3,
                            "CompareResult": {
                                "Items": [
                                    {
                                        "CompareType": 1,
                                        "FixResult": 1,
                                        "Operator": ">",
                                        "ResultValue": "2.0000",
                                        "ValueComputeType": null,
                                        "Values": [
                                            {
                                                "Value": "1",
                                                "ValueType": 3
                                            }
                                        ]
                                    }
                                ],
                                "PassRows": null,
                                "TotalRows": null,
                                "TriggerRows": null
                            },
                            "ConditionExpression": null,
                            "ExecResultStatus": 2,
                            "FieldConfig": null,
                            "QualityDim": 2,
                            "RelConditionExpr": null,
                            "RuleExecId": 3047,
                            "RuleGroupExecId": 1071,
                            "RuleGroupId": 1726,
                            "RuleId": 14723,
                            "RuleName": "文件上传规则",
                            "RuleType": 3,
                            "SourceObjectDataTypeName": "table",
                            "SourceObjectValue": "表",
                            "StartTime": "2024-04-10 17:01:23",
                            "TargetDBTableName": "null.null",
                            "TargetObjectDataType": null,
                            "TargetObjectValue": null,
                            "TemplateName": "用户定义SQL",
                            "TriggerResult": "发送告警成功, 阻断任务成功"
                        }
                    ],
                    "RuleGroupExecId": 1057371,
                    "RuleGroupId": 1726,
                    "Status": 4,
                    "TableId": "fr7xvusttwfQ",
                    "TableName": "at_1",
                    "TableOwnerName": "AUEST",
                    "TotalRuleCount": 1,
                    "TriggerType": 3
                }
            ],
            "TotalCount": 1
        },
        "RequestId": "15bb9da3584b"
    }
}
```

