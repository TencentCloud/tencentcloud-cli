**Example 1: 查询规则详情**



Input: 

```
tccli wedata DescribeRule --cli-unfold-argument  \
    --ProjectId 153160990365952 \
    --RuleId 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "AlarmLevel": 2,
            "CompareRule": {
                "ComputeExpression": "0",
                "CycleStep": 1,
                "Items": [
                    {
                        "CompareType": 1,
                        "Operator": ">",
                        "ValueComputeType": 1,
                        "ValueList": [
                            {
                                "Value": "10",
                                "ValueType": 3
                            }
                        ]
                    }
                ]
            },
            "ConditionExpression": "pt=substring('${yyyyMMddHHmmss-1H}',1,10)",
            "ConditionType": 1,
            "CreateTime": "2024-02-22 21:49:55",
            "CustomSql": "SELECT id,name FROM `at_hive_bj`.`at_hive_22`;",
            "DatabaseId": "roeqgaBtT4m22RyjnMQ",
            "DatasourceId": "678990",
            "Description": null,
            "ExecStrategy": {
                "CycleStep": 10,
                "CycleType": "I",
                "DelayTime": 0,
                "EndTime": "2099-12-31 23:59:59",
                "ExecEngineType": "HIVE",
                "ExecPlan": "2024-03-07 00:00:00 ~ 2099-12-31 23:59:59，每间隔10分钟执行一次",
                "ExecQueue": "default",
                "ExecutorGroupId": "20240307193015743960",
                "ExecutorGroupName": "wedata-test-use-sch-sh",
                "MonitorType": 3,
                "RuleGroupId": null,
                "RuleId": 1293,
                "RuleName": "表记录数小于10",
                "StartTime": "2024-03-07 00:00:00",
                "TaskAction": "",
                "Tasks": [
                    {
                        "TaskId": "20240205135835",
                        "TaskName": "at_qualire_task_1708606293AquG",
                        "WorkflowId": "1c2a85c6-d181-11eeb-b8cef68a6637"
                    }
                ]
            },
            "FieldConfig": null,
            "MonitorStatus": 0,
            "MultiSourceFlag": false,
            "Name": "表记录数小于10",
            "Operator": "dylandlwu",
            "QualityDim": 1,
            "RelConditionExpr": "sourceTable.id=targetTable.id",
            "RuleGroupId": 371,
            "RuleId": 1293,
            "RuleTemplateContent": "准确性: 表行数",
            "RuleTemplateId": 1,
            "SourceEngineTypes": [
                2,
                4,
                16
            ],
            "SourceObjectDataType": 3,
            "SourceObjectDataTypeName": "table",
            "SourceObjectType": 2,
            "SourceObjectValue": "表",
            "SubQualityDim": 0,
            "Subscription": {
                "Receivers": [
                    {
                        "ReceiverName": "solondeng",
                        "ReceiverUserId": 100596846
                    }
                ],
                "RuleGroupId": null,
                "RuleId": 1293,
                "RuleName": null,
                "SubscribeType": [
                    1,
                    2,
                    5
                ],
                "WebHooks": [
                    {
                        "HookAddress": "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=2477c-5a80-43f7-bb6b-6c606420e",
                        "HookType": "qywx"
                    }
                ]
            },
            "TableId": "O34kNIp-70pmT10q4vQ",
            "TableName": null,
            "TableOwnerName": null,
            "TargetConditionExpr": null,
            "TargetDatabaseId": null,
            "TargetDatabaseName": null,
            "TargetObjectDataType": null,
            "TargetObjectDataTypeName": null,
            "TargetObjectType": null,
            "TargetObjectValue": null,
            "TargetTableId": null,
            "TargetTableName": null,
            "TemplateSql": null,
            "TriggerCondition": "固定值大于10",
            "Type": 1,
            "WhereFlag": false
        },
        "RequestId": "b50caa8f-0c3a-45b3--64948ae52b0c"
    }
}
```

