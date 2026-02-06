**Example 1: 查询规则组执行结果**

查询规则组执行结果

Input: 

```
tccli wedata ListQualityRuleGroupExecResultsByPage --cli-unfold-argument  \
    --ProjectId 1470547050521227264 \
    --PageNumber 1 \
    --PageSize 10 \
    --Filters.0.Name TriggerType \
    --Filters.1.Name Status \
    --Filters.2.Name StartTime \
    --Filters.2.Values 1766592000 \
    --Filters.3.Name EndTime \
    --Filters.3.Values 1767196799 \
    --Filters.4.Name InstanceStatus \
    --Filters.5.Name DatasourceType \
    --Filters.5.Values 3 \
    --Filters.6.Name CatalogName \
    --Filters.6.Values DatalakeCatalog \
    --Filters.7.Name DatasourceId \
    --Filters.7.Values 8860 \
    --Filters.8.Name DatabaseName \
    --Filters.9.Name SchemaName
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "AlarmRuleCount": 1,
                    "BizCatalogId": "",
                    "BizCatalogName": "",
                    "ClusterDeployType": null,
                    "DatabaseId": null,
                    "DatabaseName": "at_dlc_cloud_gz_prod_mc",
                    "DatasourceId": "8860",
                    "DsEnvType": 0,
                    "EngineType": "DLC",
                    "ExecDetail": "",
                    "ExecTime": "2025-12-31 17:37:02",
                    "FailMsg": null,
                    "FinishTime": "未结束",
                    "InstanceId": "6820251231173705074_2025-12-31T17:37:04+08:00",
                    "InstanceStatus": "RUNNING",
                    "Permission": false,
                    "ProjectId": "1470547050521227264",
                    "ProjectName": "wedata数据开发_新",
                    "RuleExecResultVOList": [
                        {
                            "AlarmLevel": 2,
                            "AspectTaskId": null,
                            "CatalogName": null,
                            "CompareResult": {
                                "ComputeExpression": "0",
                                "Items": [
                                    {
                                        "CompareType": 1,
                                        "FixResult": null,
                                        "Operator": "<=",
                                        "ResultValue": null,
                                        "ValueComputeType": null,
                                        "Values": [
                                            {
                                                "Value": "10",
                                                "ValueType": 3
                                            }
                                        ]
                                    }
                                ],
                                "PassRows": null,
                                "TotalRows": null,
                                "TriggerRows": null
                            },
                            "ConditionExpression": "全表 ",
                            "DatabaseName": null,
                            "DatasourceId": null,
                            "DatasourceName": null,
                            "DatasourceType": null,
                            "ExecResultStatus": 0,
                            "FieldConfig": null,
                            "FinishTime": null,
                            "GroupType": null,
                            "MonitorType": null,
                            "QualityDim": 1,
                            "RelConditionExpr": null,
                            "RuleExecId": 383982,
                            "RuleGroupExecId": 419788,
                            "RuleGroupExist": null,
                            "RuleGroupId": 727,
                            "RuleGroupName": null,
                            "RuleGroupTableId": null,
                            "RuleId": 1074,
                            "RuleName": "new_rule",
                            "RuleType": 1,
                            "SchemaName": null,
                            "SourceObjectDataTypeName": "table",
                            "SourceObjectValue": "表",
                            "StartTime": "2025-12-31 17:37:02",
                            "TableName": null,
                            "TargetDBTableName": "",
                            "TargetObjectDataType": null,
                            "TargetObjectValue": null,
                            "TemplateName": "表行数",
                            "TriggerCondition": "固定值 小于等于 10",
                            "TriggerResult": null
                        }
                    ],
                    "RuleGroupExecId": 419788,
                    "RuleGroupExist": 1,
                    "RuleGroupId": 727,
                    "RuleGroupName": "gee01_202511211444",
                    "RuleGroupTableId": 328,
                    "StartTime": "2025-12-31 17:37:02",
                    "Status": 2,
                    "TableId": "4IVfcrRcAnAV_hbp-NTz8g",
                    "TableName": "gee01",
                    "TableOwnerName": null,
                    "TotalRuleCount": 1,
                    "TriggerType": 1
                }
            ],
            "TotalCount": 1
        },
        "RequestId": "682d050b-f3f7-4606-8dd3-d63f3261d917"
    }
}
```

