**Example 1: test**



Input: 

```
tccli monitor ModifyAlarmPolicyCondition --cli-unfold-argument  \
    --Module mol \
    --PolicyId policy-xxx \
    --ConditionTemplateId 0 \
    --Condition.IsUnionRule 0 \
    --Condition.Rules.0.MetricName metric1 \
    --Condition.Rules.0.Period 0 \
    --Condition.Rules.0.Operator = \
    --Condition.Rules.0.Value val \
    --Condition.Rules.0.ContinuePeriod 0 \
    --Condition.Rules.0.NoticeFrequency 0 \
    --Condition.Rules.0.IsPowerNotice 0 \
    --Condition.Rules.0.Filter.Type type \
    --Condition.Rules.0.Filter.Dimensions dim \
    --Condition.Rules.0.Description des \
    --Condition.Rules.0.Unit unit \
    --Condition.Rules.0.RuleType rule \
    --Condition.Rules.0.IsAdvanced 0 \
    --Condition.Rules.0.IsOpen 0 \
    --Condition.Rules.0.ProductId prod \
    --Condition.Rules.0.ValueMax 0 \
    --Condition.Rules.0.ValueMin 0 \
    --Condition.Rules.0.HierarchicalValue.Remind rem \
    --Condition.Rules.0.HierarchicalValue.Warn warn \
    --Condition.Rules.0.HierarchicalValue.Serious seri \
    --Condition.ComplexExpression cexpr \
    --EventCondition.Rules.0.MetricName metric \
    --EventCondition.Rules.0.Period 0 \
    --EventCondition.Rules.0.Operator op \
    --EventCondition.Rules.0.Value val \
    --EventCondition.Rules.0.ContinuePeriod 0 \
    --EventCondition.Rules.0.NoticeFrequency 0 \
    --EventCondition.Rules.0.IsPowerNotice 0 \
    --EventCondition.Rules.0.Filter.Type type \
    --EventCondition.Rules.0.Filter.Dimensions dims \
    --EventCondition.Rules.0.Description desc \
    --EventCondition.Rules.0.Unit unit \
    --EventCondition.Rules.0.RuleType rule \
    --EventCondition.Rules.0.IsAdvanced 0 \
    --EventCondition.Rules.0.IsOpen 0 \
    --EventCondition.Rules.0.ProductId prod \
    --EventCondition.Rules.0.ValueMax 0 \
    --EventCondition.Rules.0.ValueMin 0 \
    --EventCondition.Rules.0.HierarchicalValue.Remind rem \
    --EventCondition.Rules.0.HierarchicalValue.Warn warn \
    --EventCondition.Rules.0.HierarchicalValue.Serious ser \
    --Filter.Type type \
    --Filter.Dimensions dims \
    --GroupBy gb \
    --LogAlarmReqInfo.InstanceId instance-xxx \
    --LogAlarmReqInfo.Filter.0.Key key \
    --LogAlarmReqInfo.Filter.0.Operator = \
    --LogAlarmReqInfo.Filter.0.Value val \
    --LogAlarmReqInfo.AlarmMerge merge \
    --LogAlarmReqInfo.AlarmMergeTime time \
    --NoticeIds notice-xxx \
    --Enable 0 \
    --PolicyName policy \
    --EbSubject eb
```

Output: 
```
{
    "Response": {
        "RequestId": "reqid-xxxxx"
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

