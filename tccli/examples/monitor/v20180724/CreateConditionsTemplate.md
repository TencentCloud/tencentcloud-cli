**Example 1: 创建告警条件模板**



Input: 

```
tccli monitor CreateConditionsTemplate --cli-unfold-argument  \
    --EventConditions.0.EventID 123 \
    --EventConditions.0.AlarmNotifyType 0 \
    --EventConditions.0.AlarmNotifyPeriod 123 \
    --EventConditions.0.RuleID 0 \
    --Remark abcd \
    --ViewName cvm \
    --Module monitor \
    --IsUnionRule 0 \
    --GroupName abcd \
    --IsShielded 0 \
    --ComplexExpression (1 AND 2) OR 3 \
    --ParentGroupID 0 \
    --Conditions.0.RuleID 0 \
    --Conditions.0.MetricID 0 \
    --Conditions.0.CalcType 1 \
    --Conditions.0.AlarmNotifyPeriod 0 \
    --Conditions.0.ContinuePeriod 1 \
    --Conditions.0.AlarmNotifyType 0 \
    --Conditions.0.CalcPeriod 60 \
    --Conditions.0.CalcValue 0
```

Output: 
```
{
    "Response": {
        "GroupID": 1998842,
        "RequestId": "'4cf37d0d-99f9-4050-a08e-88e2b97017a8"
    }
}
```

