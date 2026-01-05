**Example 1: 编辑质量监控任务**

编辑质量监控任务

Input: 

```
tccli wedata ModifyQualityRuleGroup --cli-unfold-argument  \
    --RuleGroupExecStrategyBOList.0.RuleGroupId 731 \
    --RuleGroupExecStrategyBOList.0.MonitorType 3 \
    --RuleGroupExecStrategyBOList.0.ExecQueue default \
    --RuleGroupExecStrategyBOList.0.ExecutorGroupId 3456743567868 \
    --RuleGroupExecStrategyBOList.0.ExecutorGroupName test_worker \
    --RuleGroupExecStrategyBOList.0.StartTime 2025-04-16 00:00:00 \
    --RuleGroupExecStrategyBOList.0.EndTime 2025-04-16 23:59:59 \
    --RuleGroupExecStrategyBOList.0.CycleType I \
    --RuleGroupExecStrategyBOList.0.DelayTime 0 \
    --RuleGroupExecStrategyBOList.0.CycleStep 10 \
    --RuleGroupExecStrategyBOList.0.TaskAction  \
    --RuleGroupExecStrategyBOList.0.ExecEngineType HIVE \
    --RuleGroupExecStrategyBOList.0.RuleGroupName 待删除监控 \
    --RuleGroupExecStrategyBOList.0.DatabaseName at_hive_sh_auto \
    --RuleGroupExecStrategyBOList.0.TableName at_hive_10 \
    --RuleGroupExecStrategyBOList.0.DatasourceId 61949 \
    --RuleGroupExecStrategyBOList.0.Description 3465asd \
    --ProjectId 1464962169590902784
```

Output: 
```
{
    "Response": {
        "Data": {
            "Result": true
        },
        "RequestId": "b69a3a9b-b8ea-4936-95e8-97ea56b4b7f8"
    }
}
```

**Example 2: 编辑质量监控任务DLC示例**

编辑质量监控任务DLC示例

Input: 

```
tccli wedata ModifyQualityRuleGroup --cli-unfold-argument  \
    --RuleGroupExecStrategyBOList.0.MonitorType 3 \
    --RuleGroupExecStrategyBOList.0.ExecutorGroupId 20240222212719833743 \
    --RuleGroupExecStrategyBOList.0.RuleGroupName mico_rule_group_101 \
    --RuleGroupExecStrategyBOList.0.DatabaseName at_dlc_cloud_gz_prod_mc \
    --RuleGroupExecStrategyBOList.0.DatasourceId 8860 \
    --RuleGroupExecStrategyBOList.0.TableName gee01 \
    --RuleGroupExecStrategyBOList.0.RuleGroupId 743 \
    --RuleGroupExecStrategyBOList.0.ExecQueue dlc_lina测试勿动 \
    --RuleGroupExecStrategyBOList.0.ExecutorGroupName qfh_test \
    --RuleGroupExecStrategyBOList.0.StartTime 2026-01-05 00:00:00 \
    --RuleGroupExecStrategyBOList.0.EndTime 2026-01-10 23:59:59 \
    --RuleGroupExecStrategyBOList.0.CycleType H \
    --RuleGroupExecStrategyBOList.0.DelayTime 0 \
    --RuleGroupExecStrategyBOList.0.CycleStep 12 \
    --RuleGroupExecStrategyBOList.0.TaskAction  \
    --RuleGroupExecStrategyBOList.0.ExecEngineType DLC \
    --RuleGroupExecStrategyBOList.0.DlcGroupName default-rg-17tv8vfgvy \
    --RuleGroupExecStrategyBOList.0.Description modify ruleGroup \
    --RuleGroupExecStrategyBOList.0.ScheduleTimeZone UTC+8 \
    --ProjectId 1470547050521227264
```

Output: 
```
{
    "Response": {
        "Data": {
            "Result": true
        },
        "RequestId": "f5a26557-6ed0-482b-a3a9-6d546d68e7c7"
    }
}
```

