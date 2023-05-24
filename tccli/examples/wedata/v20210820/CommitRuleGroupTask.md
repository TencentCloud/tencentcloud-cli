**Example 1: 提交规则组运行任务接口**

提交规则组运行任务接口

Input: 

```
tccli wedata CommitRuleGroupTask --cli-unfold-argument  \
    --RuleGroupId 1 \
    --TriggerType 1 \
    --ExecRuleConfig.0.RuleId 1 \
    --ExecRuleConfig.0.ConditionType 1 \
    --ExecRuleConfig.0.Condition abc \
    --ExecRuleConfig.0.TargetCondition abc \
    --ExecConfig.QueueName abc \
    --ExecConfig.ExecutorGroupId abc \
    --ProjectId abc \
    --EngineType abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "RuleGroupExecId": 1,
            "RuleGroupId": 1,
            "TriggerType": 1,
            "ExecTime": "abc",
            "Status": 1,
            "AlarmRuleCount": 1,
            "TotalRuleCount": 1,
            "TableOwnerName": "abc",
            "TableName": "abc",
            "TableId": "abc",
            "DatabaseId": "abc",
            "DatasourceId": "abc",
            "Permission": true,
            "ExecDetail": "abc"
        },
        "RequestId": "abc"
    }
}
```

