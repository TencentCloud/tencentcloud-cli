**Example 1: 查询规则详情**



Input: 

```
tccli wedata DescribeRule --cli-unfold-argument  \
    --ProjectId 1 \
    --RuleId 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "RuleId": 1,
            "RuleGroupId": 1,
            "TableId": "678yghuh87u",
            "Name": "test",
            "Type": 1,
            "RuleTemplateId": 1,
            "RuleTemplateContent": "contnt",
            "QualityDim": 1,
            "SourceObjectType": 1,
            "SourceObjectDataType": 1,
            "SourceObjectDataTypeName": "int",
            "SourceObjectValue": "1",
            "ConditionType": 1,
            "ConditionExpression": "exp",
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
                "ComputeExpression": "exp"
            },
            "AlarmLevel": 1,
            "Description": "规则",
            "Operator": "zhangsan",
            "TargetDatabaseId": "768tgy97usedf",
            "TargetDatabaseName": "dbTest",
            "TargetTableId": "786yuh09pp78uyh",
            "TargetTableName": "test",
            "TargetConditionExpr": ">",
            "RelConditionExpr": "exp",
            "FieldConfig": {
                "WhereConfig": [
                    {
                        "FieldKey": "id",
                        "FieldValue": "1",
                        "FieldDataType": "int"
                    }
                ],
                "TableConfig": [
                    {
                        "DatabaseId": "697y8ghopniluh",
                        "DatabaseName": "dbTest",
                        "TableId": "abc",
                        "TableName": "test",
                        "TableKey": "ygkhub",
                        "FieldConfig": [
                            {
                                "FieldKey": "name",
                                "FieldValue": "zhangsan",
                                "FieldDataType": "string"
                            }
                        ]
                    }
                ]
            },
            "MultiSourceFlag": true,
            "WhereFlag": true,
            "TemplateSql": "select 1",
            "SubQualityDim": 1,
            "TargetObjectType": 1,
            "TargetObjectDataType": 1,
            "TargetObjectDataTypeName": "name",
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
                "ExecutorGroupId": "576878",
                "ExecutorGroupName": "执行队列",
                "Tasks": [
                    {
                        "TaskId": "5789",
                        "TaskName": "任务名称",
                        "WorkflowId": "5678tygiuv"
                    }
                ],
                "StartTime": "2023-10-01",
                "EndTime": "2023-10-01",
                "CycleType": "abc",
                "DelayTime": 1,
                "CycleStep": 1,
                "TaskAction": "abc",
                "ExecEngineType": "abc",
                "ExecPlan": "abc",
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
                        "HookType": "abc",
                        "HookAddress": "abc"
                    }
                ],
                "RuleId": 1,
                "RuleName": "规则1"
            },
            "CreateTime": "abc",
            "DatasourceId": 1,
            "DatabaseId": "abc",
            "MonitorStatus": 0,
            "TriggerCondition": "abc"
        },
        "RequestId": "0ff4e8ae-ebea-4a41-8aa2-1f6bc4b68e69"
    }
}
```

