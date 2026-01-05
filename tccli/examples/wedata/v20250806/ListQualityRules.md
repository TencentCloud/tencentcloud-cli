**Example 1: 分页查询规则**

分页查询规则

Input: 

```
tccli wedata ListQualityRules --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 10 \
    --ProjectId 1464962169590902784
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [],
            "TotalCount": 0
        },
        "RequestId": "2b5b3144-1af7-4896-9427-dc92b0254b8b"
    }
}
```

**Example 2: 分页查询项目下某个数据源下的规则列表**



Input: 

```
tccli wedata ListQualityRules --cli-unfold-argument  \
    --ProjectId 1470547050521227264 \
    --PageNumber 1 \
    --PageSize 1 \
    --Filters.0.Name DatasourceType \
    --Filters.0.Values 3 \
    --Filters.1.Name CatalogName \
    --Filters.1.Values DataLakeCatalog \
    --Filters.2.Name DatasourceId \
    --Filters.2.Values 8860 \
    --Filters.3.Name DatabaseName \
    --Filters.4.Name SchemaName
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "AlarmLevel": 2,
                    "AspectTaskId": "20251231160201243",
                    "CatalogName": "DataLakeCatalog",
                    "CompareRule": {
                        "ComputeExpression": "0",
                        "CycleStep": null,
                        "Items": [
                            {
                                "CompareType": 1,
                                "Operator": "<=",
                                "ValueComputeType": null,
                                "ValueList": [
                                    {
                                        "Value": "10",
                                        "ValueType": 3
                                    }
                                ]
                            }
                        ]
                    },
                    "ConditionExpression": null,
                    "ConditionType": 1,
                    "CreateTime": "2025-12-31 16:02:19",
                    "CustomSql": null,
                    "DatabaseId": null,
                    "DatabaseName": "at_dlc_cloud_gz_prod_mc",
                    "DatasourceId": 8860,
                    "DatasourceName": "dlc_DLC_hx756s1y",
                    "DatasourceType": 3,
                    "Description": "row count",
                    "DsEnvType": 0,
                    "ExecStrategy": {
                        "CycleStep": null,
                        "CycleType": null,
                        "DelayTime": 0,
                        "DlcGroupName": "default-rg-17tv8vfgvy",
                        "EndTime": null,
                        "EngineParam": null,
                        "ExecEngineType": "DLC",
                        "ExecPlan": null,
                        "ExecQueue": "dlc_lina测试勿动",
                        "ExecutorGroupId": "20240222212719833743",
                        "ExecutorGroupName": "qfh_test",
                        "MonitorType": 2,
                        "RuleGroupId": 727,
                        "RuleGroupName": "gee01_202511211444",
                        "RuleId": 1079,
                        "RuleName": "new_rule_5",
                        "ScheduleTimeZone": null,
                        "StartTime": null,
                        "TaskAction": null,
                        "Tasks": [
                            {
                                "InChargeIdList": null,
                                "InChargeNameList": null,
                                "ScheduleTimeZone": null,
                                "TaskId": "20251121143935616",
                                "TaskName": "1121testkkk",
                                "TaskType": "1",
                                "WorkflowId": "49e2197f-957b-43c1-bc8f-162e6ffe9432"
                            }
                        ],
                        "TriggerTypes": [
                            "CYCLE"
                        ]
                    },
                    "FailMsg": null,
                    "FieldConfig": null,
                    "GroupType": "DEFAULT",
                    "MonitorStatus": 1,
                    "MultiSourceFlag": null,
                    "Name": "new_rule_5",
                    "Operator": "wenjieyao",
                    "ProjectId": "1470547050521227264",
                    "ProjectName": "wedata数据开发_新",
                    "QualityDim": 1,
                    "RelConditionExpr": null,
                    "RuleGroupId": 727,
                    "RuleId": 1079,
                    "RuleTemplateContent": "准确性: 表行数",
                    "RuleTemplateId": 6142,
                    "SchemaName": null,
                    "SourceEngineTypes": [
                        2
                    ],
                    "SourceObjectDataType": null,
                    "SourceObjectDataTypeName": "table",
                    "SourceObjectType": 2,
                    "SourceObjectValue": "表",
                    "SubQualityDim": null,
                    "Subscription": null,
                    "TableId": "328",
                    "TableName": "gee01",
                    "TableOwnerName": null,
                    "TargetCatalogName": null,
                    "TargetConditionExpr": null,
                    "TargetDatabaseId": null,
                    "TargetDatabaseName": null,
                    "TargetObjectDataType": null,
                    "TargetObjectDataTypeName": null,
                    "TargetObjectType": null,
                    "TargetObjectValue": null,
                    "TargetSchemaName": null,
                    "TargetTableId": null,
                    "TargetTableName": null,
                    "TemplateSql": null,
                    "TriggerCondition": "固定值 小于等于 10",
                    "Type": 1,
                    "UpdateTime": "2025-12-31 16:02:19",
                    "WhereFlag": null
                }
            ],
            "TotalCount": 12
        },
        "RequestId": "bcb0da72-e4bd-4074-8f06-6ba4da1c10d5"
    }
}
```

