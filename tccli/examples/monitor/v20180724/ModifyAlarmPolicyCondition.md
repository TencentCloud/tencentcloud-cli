**Example 1: test**



Input: 

```
tccli monitor ModifyAlarmPolicyCondition --cli-unfold-argument  \
    --Module abc \
    --PolicyId abc \
    --ConditionTemplateId 0 \
    --Condition.IsUnionRule 0 \
    --Condition.Rules.0.MetricName abc \
    --Condition.Rules.0.Period 0 \
    --Condition.Rules.0.Operator abc \
    --Condition.Rules.0.Value abc \
    --Condition.Rules.0.ContinuePeriod 0 \
    --Condition.Rules.0.NoticeFrequency 0 \
    --Condition.Rules.0.IsPowerNotice 0 \
    --Condition.Rules.0.Filter.Type abc \
    --Condition.Rules.0.Filter.Dimensions abc \
    --Condition.Rules.0.Description abc \
    --Condition.Rules.0.Unit abc \
    --Condition.Rules.0.RuleType abc \
    --Condition.Rules.0.IsAdvanced 0 \
    --Condition.Rules.0.IsOpen 0 \
    --Condition.Rules.0.ProductId abc \
    --Condition.Rules.0.ValueMax 0 \
    --Condition.Rules.0.ValueMin 0 \
    --Condition.Rules.0.HierarchicalValue.Remind abc \
    --Condition.Rules.0.HierarchicalValue.Warn abc \
    --Condition.Rules.0.HierarchicalValue.Serious abc \
    --Condition.ComplexExpression abc \
    --EventCondition.Rules.0.MetricName abc \
    --EventCondition.Rules.0.Period 0 \
    --EventCondition.Rules.0.Operator abc \
    --EventCondition.Rules.0.Value abc \
    --EventCondition.Rules.0.ContinuePeriod 0 \
    --EventCondition.Rules.0.NoticeFrequency 0 \
    --EventCondition.Rules.0.IsPowerNotice 0 \
    --EventCondition.Rules.0.Filter.Type abc \
    --EventCondition.Rules.0.Filter.Dimensions abc \
    --EventCondition.Rules.0.Description abc \
    --EventCondition.Rules.0.Unit abc \
    --EventCondition.Rules.0.RuleType abc \
    --EventCondition.Rules.0.IsAdvanced 0 \
    --EventCondition.Rules.0.IsOpen 0 \
    --EventCondition.Rules.0.ProductId abc \
    --EventCondition.Rules.0.ValueMax 0 \
    --EventCondition.Rules.0.ValueMin 0 \
    --EventCondition.Rules.0.HierarchicalValue.Remind abc \
    --EventCondition.Rules.0.HierarchicalValue.Warn abc \
    --EventCondition.Rules.0.HierarchicalValue.Serious abc \
    --Filter.Type abc \
    --Filter.Dimensions abc \
    --GroupBy abc \
    --LogAlarmReqInfo.InstanceId abc \
    --LogAlarmReqInfo.Filter.0.Key abc \
    --LogAlarmReqInfo.Filter.0.Operator abc \
    --LogAlarmReqInfo.Filter.0.Value abc \
    --LogAlarmReqInfo.AlarmMerge abc \
    --LogAlarmReqInfo.AlarmMergeTime abc \
    --NoticeIds abc \
    --Enable 0 \
    --PolicyName abc \
    --EbSubject abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

**Example 2: 编辑告警策略触发条件**

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

