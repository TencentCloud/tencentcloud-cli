**Example 1: 提交规则组运行任务接口**

提交规则组运行任务接口

Input: 

```
tccli wedata CommitRuleGroupTask --cli-unfold-argument  \
    --RuleGroupId 1 \
    --TriggerType 1 \
    --ExecRuleConfig.0.RuleId 1 \
    --ExecRuleConfig.0.ConditionType 1 \
    --ExecRuleConfig.0.Condition 2024-04-11 11:00:00 \
    --ExecRuleConfig.0.TargetCondition ct='${yyyy-mm-dd-1}' \
    --ExecConfig.QueueName default \
    --ExecConfig.ExecutorGroupId 567890 \
    --ExecConfig.EngineType 2 \
    --ProjectId 456789 \
    --EngineType HIVE
```

Output: 
```
{
    "Response": {
        "Data": {
            "RuleGroupExecId": 1,
            "RuleGroupId": 1,
            "TriggerType": 1,
            "ExecTime": "1712804400000",
            "Status": 1,
            "AlarmRuleCount": 1,
            "TotalRuleCount": 1,
            "TableOwnerName": "zhangsan",
            "TableName": "dq",
            "TableId": "697ytfgquhewfa21we",
            "DatabaseId": "85rft7qie3svwukacdavk",
            "DatasourceId": "456789",
            "Permission": true,
            "ExecDetail": "2023-09-07 ~ 2099-12-31，每天07:00执行一次",
            "EngineType": "HIVE",
            "RuleExecResultVOList": [
                {
                    "RuleExecId": 1,
                    "RuleGroupExecId": 1,
                    "RuleGroupId": 1,
                    "RuleId": 1,
                    "RuleName": "规则",
                    "RuleType": 1,
                    "SourceObjectDataTypeName": "int",
                    "SourceObjectValue": "age",
                    "ConditionExpression": "pt=substring('${yyyyMMddHHmmss-1H}',1,10)",
                    "ExecResultStatus": 1,
                    "TriggerResult": "",
                    "CompareResult": {
                        "Items": [
                            {
                                "FixResult": 1,
                                "ResultValue": "0",
                                "Values": [
                                    {
                                        "ValueType": 1,
                                        "Value": "2"
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
                    "TemplateName": "模版",
                    "QualityDim": 1,
                    "TargetDBTableName": "targaetName",
                    "TargetObjectValue": "value",
                    "TargetObjectDataType": "1",
                    "FieldConfig": {
                        "WhereConfig": [
                            {
                                "FieldKey": "param_1",
                                "FieldValue": "id",
                                "FieldDataType": "int"
                            }
                        ],
                        "TableConfig": [
                            {
                                "DatabaseId": "NW0VL_YYPESvi8w",
                                "DatabaseName": "default",
                                "TableId": "EHdPET2IKQ2KBhGw",
                                "TableName": "dq_student",
                                "TableKey": "table_1",
                                "FieldConfig": [
                                    {
                                        "FieldKey": "table_1.column_1",
                                        "FieldValue": "id",
                                        "FieldDataType": "int"
                                    }
                                ]
                            }
                        ]
                    },
                    "RelConditionExpr": "sourceTable.id=targetTable.id",
                    "StartTime": "2023-10-01",
                    "AlarmLevel": 1
                }
            ]
        },
        "RequestId": "0ff4e8ae-ebea-4a41-8aa2-1f6bc4b68e69"
    }
}
```

