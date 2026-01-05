**Example 1: 创建dlc表的质量监控任务**



Input: 

```
tccli wedata CreateQualityRuleGroup --cli-unfold-argument  \
    --RuleGroupExecStrategyBOList.0.MonitorType 3 \
    --RuleGroupExecStrategyBOList.0.RuleGroupName dlc_test_rule_group_1 \
    --RuleGroupExecStrategyBOList.0.DatabaseName at_dlc_cloud_gz_prod \
    --RuleGroupExecStrategyBOList.0.DatasourceId 8860 \
    --RuleGroupExecStrategyBOList.0.ExecQueue dlc_lina测试勿动 \
    --RuleGroupExecStrategyBOList.0.ExecutorGroupId 20240222212719833743 \
    --RuleGroupExecStrategyBOList.0.ExecutorGroupName qfh_test \
    --RuleGroupExecStrategyBOList.0.StartTime 2025-12-31 00:00:00 \
    --RuleGroupExecStrategyBOList.0.EndTime 2025-12-31 23:59:59 \
    --RuleGroupExecStrategyBOList.0.CycleType D \
    --RuleGroupExecStrategyBOList.0.DelayTime 0 \
    --RuleGroupExecStrategyBOList.0.CycleStep 1 \
    --RuleGroupExecStrategyBOList.0.TaskAction  \
    --RuleGroupExecStrategyBOList.0.ExecEngineType DLC \
    --RuleGroupExecStrategyBOList.0.DlcGroupName default-rg-17tv8vfgvy \
    --RuleGroupExecStrategyBOList.0.SchemaName  \
    --RuleGroupExecStrategyBOList.0.TableName at_src_mysql_bigint_unsigned_t1 \
    --RuleGroupExecStrategyBOList.0.Description 测试创建dlc表的规则组 \
    --RuleGroupExecStrategyBOList.0.ScheduleTimeZone UTC+5 \
    --RuleGroupExecStrategyBOList.0.CatalogName DataLakeCatalog \
    --ProjectId 1470547050521227264
```

Output: 
```
{
    "Response": {
        "Data": {
            "RuleGroupResultList": [
                {
                    "CatalogName": "DataLakeCatalog",
                    "DatabaseName": "at_dlc_cloud_gz_prod",
                    "DatasourceId": "8860",
                    "ExecDetail": null,
                    "FailMsg": "Creation failed, please contact technical support for problem diagnosis",
                    "Id": null,
                    "MonitorType": 3,
                    "Name": "dlc_test_rule_group_1",
                    "RuleGroupTableId": null,
                    "SchemaName": "",
                    "TableName": "at_src_mysql_bigint_unsigned_t1"
                }
            ]
        },
        "RequestId": "c6c361e9-fde9-4ee5-bdcd-56952e21d893"
    }
}
```

**Example 2: 创建规则组**

创建规则组

Input: 

```
tccli wedata CreateQualityRuleGroup --cli-unfold-argument  \
    --RuleGroupExecStrategyBOList.0.MonitorType 3 \
    --RuleGroupExecStrategyBOList.0.RuleGroupName mico_iceberg_table_202504181829 \
    --RuleGroupExecStrategyBOList.0.DatabaseName default \
    --RuleGroupExecStrategyBOList.0.DatasourceId 61949 \
    --RuleGroupExecStrategyBOList.0.ExecQueue default \
    --RuleGroupExecStrategyBOList.0.ExecutorGroupId 7645325746524236 \
    --RuleGroupExecStrategyBOList.0.ExecutorGroupName test_worker \
    --RuleGroupExecStrategyBOList.0.StartTime 2025-04-18 00:00:00 \
    --RuleGroupExecStrategyBOList.0.EndTime 2025-04-18 23:59:59 \
    --RuleGroupExecStrategyBOList.0.CycleType I \
    --RuleGroupExecStrategyBOList.0.DelayTime 0 \
    --RuleGroupExecStrategyBOList.0.CycleStep 10 \
    --RuleGroupExecStrategyBOList.0.TaskAction  \
    --RuleGroupExecStrategyBOList.0.ExecEngineType SPARK \
    --RuleGroupExecStrategyBOList.0.SchemaName  \
    --RuleGroupExecStrategyBOList.0.TableName mico_iceberg_table \
    --ProjectId 1464962169590902784
```

Output: 
```
{
    "Response": {
        "Data": {
            "RuleGroupResultList": [
                {
                    "CatalogName": null,
                    "DatabaseName": "default",
                    "DatasourceId": "61949",
                    "ExecDetail": null,
                    "FailMsg": "Parameter validation failed.:Data table does not exist.",
                    "Id": null,
                    "MonitorType": 3,
                    "Name": "mico_iceberg_table_202504181829",
                    "RuleGroupTableId": null,
                    "SchemaName": "",
                    "TableName": "mico_iceberg_table"
                }
            ]
        },
        "RequestId": "4d4a61d7-edd7-4590-b296-929e73b5ed20"
    }
}
```

