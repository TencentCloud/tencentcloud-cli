**Example 1: 创建质量规则接口**

创建质量规则组中单个规则

Input: 

```
tccli wedata CreateRule --cli-unfold-argument  \
    --ProjectId 11114192353510111488 \
    --RuleGroupId 1 \
    --Name autotest_s3mC \
    --TableId E-UEBWQB-XRjERluUg \
    --RuleTemplateId 1 \
    --Type 1 \
    --QualityDim 1 \
    --SourceObjectDataTypeName int \
    --SourceObjectValue age \
    --ConditionType 1 \
    --ConditionExpression pt=substring('${yyyyMMddHHmmss-1H}',1,10) \
    --CustomSql SELECT id,name FROM `at_hive_bj`.`at_hive_22`; \
    --CompareRule.Items.0.CompareType 1 \
    --CompareRule.Items.0.Operator > \
    --CompareRule.Items.0.ValueComputeType 1 \
    --CompareRule.Items.0.ValueList.0.ValueType 3 \
    --CompareRule.Items.0.ValueList.0.Value 0 \
    --CompareRule.CycleStep 1 \
    --CompareRule.ComputeExpression 0 \
    --AlarmLevel 1 \
    --Description 测试 \
    --DatasourceId 678990 \
    --DatabaseId 97yuhijbkh08y97uhi \
    --TargetDatabaseId 97yuhijbkh08y97uhi \
    --TargetTableId E-UEBWQB-XRjERluUg \
    --TargetConditionExpr ct='${yyyy-mm-dd-1}' \
    --RelConditionExpr sourceTable.id=targetTable.id \
    --FieldConfig.TableConfig.0.DatabaseId NW0VL_YYPESvi8w \
    --FieldConfig.TableConfig.0.DatabaseName default \
    --FieldConfig.TableConfig.0.TableId EHdPET2IKQ2KBhGw \
    --FieldConfig.TableConfig.0.TableName dq_student \
    --FieldConfig.TableConfig.0.TableKey table_1 \
    --FieldConfig.TableConfig.0.FieldConfig.0.FieldKey table_1.column_1 \
    --FieldConfig.TableConfig.0.FieldConfig.0.FieldDataType int \
    --FieldConfig.TableConfig.0.FieldConfig.0.FieldValue id \
    --FieldConfig.WhereConfig.0.FieldKey param_1 \
    --FieldConfig.WhereConfig.0.FieldDataType int \
    --FieldConfig.WhereConfig.0.FieldValue id \
    --TargetObjectValue value \
    --SourceEngineTypes 2 4
```

Output: 
```
{
    "Response": {
        "Data": {
            "RuleId": 1,
            "RuleGroupId": 1,
            "TableId": "E-UEBWsQB-XRjERluUg",
            "TableName": "dq",
            "DatabaseId": "roeqgaBtT4m22RyjnMQ",
            "DatasourceId": 6789789,
            "Name": "测试",
            "Type": 1,
            "RuleTemplateId": 1,
            "RuleTemplateContent": "描述",
            "QualityDim": 1,
            "SourceObjectType": 1,
            "SourceObjectDataType": 1,
            "SourceObjectDataTypeName": "int",
            "SourceObjectValue": "age",
            "ConditionType": 1,
            "ConditionExpression": "pt=substring('${yyyyMMddHHmmss-1H}',1,10)",
            "CustomSql": "SELECT id,name FROM `at_hive_bj`.`at_hive_22`;",
            "CreateTime": "2024-02-22 21:49:55",
            "TableOwnerName": "AUTO_TEST",
            "SourceEngineTypes": [
                2,
                4,
                16
            ],
            "ExecStrategy": {
                "CycleStep": null,
                "CycleType": null,
                "DelayTime": null,
                "EndTime": null,
                "ExecEngineType": null,
                "ExecPlan": null,
                "ExecQueue": null,
                "ExecutorGroupId": null,
                "ExecutorGroupName": null,
                "MonitorType": 2,
                "RuleGroupId": null,
                "RuleId": 1263,
                "RuleName": "field_minimum_trigger_fail",
                "StartTime": null,
                "TaskAction": null,
                "Tasks": [
                    {
                        "TaskId": "20240205135835",
                        "TaskName": "at_qualire_task_1708606293AquG",
                        "WorkflowId": "1c2a85c6-d181-11eeb-b8cef68a6637"
                    }
                ]
            },
            "Subscription": {
                "Receivers": [
                    {
                        "ReceiverName": "yukzhang",
                        "ReceiverUserId": 100581064
                    }
                ],
                "RuleGroupId": null,
                "RuleId": 125,
                "RuleName": null,
                "SubscribeType": [
                    1
                ],
                "WebHooks": []
            },
            "CompareRule": {
                "Items": [
                    {
                        "CompareType": 1,
                        "Operator": ">",
                        "ValueComputeType": 1,
                        "ValueList": [
                            {
                                "ValueType": 3,
                                "Value": "0"
                            }
                        ]
                    }
                ],
                "CycleStep": 1
            },
            "AlarmLevel": 2,
            "Description": "测试",
            "Operator": "zhangsan",
            "TargetDatabaseId": "6788897uigygh967q23e",
            "TargetDatabaseName": "test",
            "TargetTableId": "y8o97hufe378qygfvbqd",
            "TargetTableName": "dq",
            "TargetConditionExpr": "ct='${yyyy-mm-dd-1}'",
            "RelConditionExpr": "sourceTable.id=targetTable.id",
            "FieldConfig": {
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
                                "FieldDataType": "int",
                                "FieldValue": "id"
                            }
                        ]
                    }
                ],
                "WhereConfig": [
                    {
                        "FieldKey": "param_1",
                        "FieldDataType": "int",
                        "FieldValue": "id"
                    }
                ]
            },
            "MultiSourceFlag": true,
            "WhereFlag": true,
            "TemplateSql": "select count(${table_1.column_1}) from ${table_1}",
            "SubQualityDim": 1,
            "TargetObjectType": 1,
            "TargetObjectDataType": 1,
            "TargetObjectDataTypeName": "name",
            "TargetObjectValue": "value"
        },
        "RequestId": "e447b6ad-c3c3-44b5-b473-dbfc39591f93"
    }
}
```

