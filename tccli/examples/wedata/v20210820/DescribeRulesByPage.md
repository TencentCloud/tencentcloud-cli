**Example 1: 分页查询质量规则**



Input: 

```
tccli wedata DescribeRulesByPage --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 1 \
    --Filters.0.Name tableId \
    --Filters.0.Values 79tugiojbfvdesc \
    --OrderFields.0.Name id \
    --OrderFields.0.Direction asc \
    --ProjectId 5346789087654
```

Output: 
```
{
    "Response": {
        "Data": {
            "TotalCount": 1,
            "Items": [
                {
                    "RuleId": 1,
                    "RuleGroupId": 1,
                    "TableId": "79tyugihbksda",
                    "Name": "规则",
                    "Type": 1,
                    "RuleTemplateId": 1,
                    "RuleTemplateContent": "cont",
                    "QualityDim": 1,
                    "SourceObjectType": 1,
                    "SourceObjectDataType": 1,
                    "SourceObjectDataTypeName": "string",
                    "SourceObjectValue": "1",
                    "ConditionType": 1,
                    "ConditionExpression": ">",
                    "CustomSql": "abc",
                    "CompareRule": {
                        "Items": [
                            {
                                "CompareType": 1,
                                "Operator": ">",
                                "ValueComputeType": 1,
                                "ValueList": [
                                    {
                                        "ValueType": 1,
                                        "Value": "1"
                                    }
                                ]
                            }
                        ],
                        "CycleStep": 1,
                        "ComputeExpression": "expr"
                    },
                    "AlarmLevel": 1,
                    "Description": "描述",
                    "Operator": "zhangsan",
                    "TargetDatabaseId": "70afsdfaasyighb",
                    "TargetDatabaseName": "dbName",
                    "TargetTableId": "8y9uhojt79u",
                    "TargetTableName": "test",
                    "TargetConditionExpr": "0",
                    "RelConditionExpr": "sourceTable.id = targetTable.id",
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
                                "DatabaseId": "7p9gyuih78tgy",
                                "DatabaseName": "dbTest",
                                "TableId": "7t8ygihb670ygo",
                                "TableName": "test",
                                "TableKey": "asdfsdf",
                                "FieldConfig": [
                                    {
                                        "FieldKey": "id",
                                        "FieldValue": "12",
                                        "FieldDataType": "int"
                                    }
                                ]
                            }
                        ]
                    },
                    "MultiSourceFlag": true,
                    "WhereFlag": true,
                    "TemplateSql": "select1",
                    "SubQualityDim": 1,
                    "TargetObjectType": 1,
                    "TargetObjectDataType": 1,
                    "TargetObjectDataTypeName": "int",
                    "TargetObjectValue": "1",
                    "SourceEngineTypes": [
                        1
                    ],
                    "TableName": "test",
                    "TableOwnerName": "zhangsan",
                    "ExecStrategy": {
                        "RuleGroupId": 1,
                        "MonitorType": 1,
                        "ExecQueue": "test",
                        "ExecutorGroupId": "6578987685",
                        "ExecutorGroupName": "name",
                        "Tasks": [
                            {
                                "TaskId": "576890867",
                                "TaskName": "任务名",
                                "WorkflowId": "79tyughib87yu9"
                            }
                        ],
                        "StartTime": "2023-10-01",
                        "EndTime": "2023-10-01",
                        "CycleType": "D",
                        "DelayTime": 1,
                        "CycleStep": 1,
                        "TaskAction": "abc",
                        "ExecEngineType": "HIVE",
                        "ExecPlan": "2024-04-07 00:00:00 ~ 2099-12-31 23:59:59，每间隔10分钟执行一次",
                        "RuleId": 1,
                        "RuleName": "规则1"
                    },
                    "Subscription": {
                        "RuleGroupId": 1,
                        "Receivers": [
                            {
                                "ReceiverUserId": 1,
                                "ReceiverName": "zhangsan"
                            }
                        ],
                        "SubscribeType": [
                            1
                        ],
                        "WebHooks": [
                            {
                                "HookType": "1",
                                "HookAddress": "http://www.test.com"
                            }
                        ],
                        "RuleId": 1,
                        "RuleName": "规则1"
                    },
                    "CreateTime": "2023-10-01",
                    "DatasourceId": 1,
                    "DatabaseId": "ssddyhhjj-daskk",
                    "MonitorStatus": 0,
                    "TriggerCondition": "固定值 小于 2"
                }
            ]
        },
        "RequestId": "0ff4e8ab68e69"
    }
}
```

