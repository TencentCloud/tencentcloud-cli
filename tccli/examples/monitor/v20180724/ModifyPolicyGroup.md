**Example 1: 更新策略组**



Input: 

```
tccli monitor ModifyPolicyGroup --cli-unfold-argument  \
    --Module monitor \
    --GroupId 1998785 \
    --ViewName cvm_device \
    --GroupName NewPolicyGroup \
    --IsUnionRule 0 \
    --Conditions.0.MetricId 33 \
    --Conditions.0.RuleId 5001614 \
    --Conditions.0.CalcType 1 \
    --Conditions.0.CalcValue 50 \
    --Conditions.0.CalcPeriod 300 \
    --Conditions.0.ContinuePeriod 3 \
    --Conditions.0.AlarmNotifyType 0 \
    --Conditions.0.AlarmNotifyPeriod 7200
```

Output: 
```
{
    "Response": {
        "GroupId": 1998785,
        "RequestId": "dfa8ff38-8272-4165-8ec2-357d76c43457"
    }
}
```

