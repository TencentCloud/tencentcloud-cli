**Example 1: 查询质量规则列表**

{
  "ProjectId": "abc",
  "RuleGroupId": 1,
  "EngineType":"HIVE"
}

Input: 

```
tccli wedata DescribeRules --cli-unfold-argument  \
    --ProjectId 153161111111111111 \
    --RuleGroupId 1 \
    --EngineType HIVE
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "RuleId": 1,
                "RuleGroupId": 1,
                "TableId": "79tyugihbksda",
                "Name": "规则",
                "Type": 1,
                "RuleTemplateId": 1,
                "RuleTemplateContent": "准确性：表行数",
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
                    "ComputeExpression": "0"
                },
                "AlarmLevel": 1,
                "Description": "描述",
                "Operator": "zhangsan",
                "TargetDatabaseId": "easdsad-dasdas",
                "TargetDatabaseName": "db1",
                "TargetTableId": "dsadxc-dsada",
                "TargetTableName": "table1",
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
                "TemplateSql": "select count(*) from a",
                "SubQualityDim": 1,
                "TargetObjectType": 1,
                "TargetObjectDataType": 1,
                "TargetObjectDataTypeName": "int",
                "TargetObjectValue": "1",
                "SourceEngineTypes": [
                    2
                ],
                "TableName": "abc",
                "TableOwnerName": "abc",
                "ExecStrategy": {
                    "RuleGroupId": 1,
                    "MonitorType": 1,
                    "ExecQueue": "default",
                    "ExecutorGroupId": "2",
                    "ExecutorGroupName": "资源组",
                    "Tasks": [
                        {
                            "WorkflowId": "32131232323",
                            "TaskId": "321321321321",
                            "TaskName": "shell1",
                            "CycleType": 1
                        }
                    ],
                    "StartTime": "2023-10-01",
                    "EndTime": "2023-10-01",
                    "CycleType": "D",
                    "DelayTime": 1,
                    "CycleStep": 1,
                    "TaskAction": "",
                    "ExecEngineType": "HIVE",
                    "ExecPlan": "2024-04-07 00:00:00 ~ 2099-12-31 23:59:59，每间隔10分钟执行一次",
                    "RuleId": 1,
                    "RuleName": "规则",
                    "TriggerTypes": [
                        "2"
                    ]
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
                "DatabaseId": "sddyhhjj-daskk",
                "MonitorStatus": 0,
                "TriggerCondition": "固定值 小于 2"
            }
        ],
        "RequestId": "0ff4e8ab68e69"
    }
}
```

