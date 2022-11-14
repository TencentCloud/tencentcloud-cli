**Example 1: 提交规则组运行任务接口**



Input: 

```
tccli wedata CommitRuleGroupTask --cli-unfold-argument  \
    --ExecRuleConfig.0.ConditionType 1 \
    --ExecRuleConfig.0.Condition xx \
    --ExecRuleConfig.0.RuleId 1 \
    --ExecConfig.ExecutorGroupId 1 \
    --ExecConfig.QueueName xx \
    --TriggerType 1 \
    --RuleGroupId 1 \
    --ProjectId 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": 1,
            "AlarmRuleCount": 1,
            "DatabaseId": "xx",
            "RuleGroupId": 1,
            "RuleGroupExecId": 1,
            "TableName": "xx",
            "ExecTime": "xx",
            "TableId": "xx",
            "TableOwnerName": "xx",
            "TriggerType": 1,
            "DatasourceId": "xx",
            "TotalRuleCount": 1
        },
        "RequestId": "xx"
    }
}
```

