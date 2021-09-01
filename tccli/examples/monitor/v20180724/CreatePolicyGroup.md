**Example 1: 增加策略组**



Input: 

```
tccli monitor CreatePolicyGroup --cli-unfold-argument  \
    --Module monitor \
    --GroupName test_group \
    --ViewName cvm_device \
    --ProjectId 0 \
    --Remark backup_group \
    --BackEndCall 0 \
    --IsUnionRule 1 \
    --Conditions.0.MetricId 19 \
    --Conditions.0.CalcType 1 \
    --Conditions.0.CalcValue 100 \
    --Conditions.0.CalcPeriod 1 \
    --Conditions.0.ContinuePeriod 1 \
    --Conditions.0.AlarmNotifyType 0 \
    --Conditions.0.AlarmNotifyPeriod 0 \
    --EventConditions.0.EventId 42 \
    --EventConditions.0.AlarmNotifyType 0 \
    --EventConditions.0.AlarmNotifyPeriod 0
```

Output: 
```
{
    "Response": {
        "GroupId": 1288099,
        "RequestId": "a91f70ed-e385-4817-9928-994ff06e56ec"
    }
}
```

