**Example 1: 编辑告警策略触发条件**

编辑告警策略触发条件示例如下

Input: 

```
tccli monitor ModifyAlarmPolicyCondition --cli-unfold-argument  \
    --Module monitor \
    --PolicyId policy-hi498gw3h2 \
    --Condition.IsUnionRule 1 \
    --Condition.Rules.0.MetricName cpu_usage \
    --Condition.Rules.0.Period 60 \
    --Condition.Rules.0.Operator ge \
    --Condition.Rules.0.Value 85 \
    --Condition.Rules.0.ContinuePeriod 1 \
    --Condition.Rules.0.NoticeFrequency 3600 \
    --Condition.Rules.0.IsPowerNotice 0 \
    --EventCondition.Rules.0.MetricName ping_unreach
```

Output: 
```
{
    "Response": {
        "RequestId": "29ghj2hh-45-h53h234h-23"
    }
}
```

