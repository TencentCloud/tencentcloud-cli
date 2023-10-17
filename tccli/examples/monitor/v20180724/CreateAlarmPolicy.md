**Example 1: 创建告警策略**

策略类型为“云服务器-基础监控”，触发指标为CPU使用率大于等于99.9%，触发事件为“ping不可达”，绑定两个通知规则，绑定一个弹性伸缩策略

Input: 

```
tccli monitor CreateAlarmPolicy --cli-unfold-argument  \
    --Module monitor \
    --PolicyName 云服务器告警策略 \
    --Remark 这是一句备注 \
    --MonitorType MT_QCE \
    --Enable 1 \
    --ProjectId 0 \
    --Namespace cvm_device \
    --Condition.IsUnionRule 1 \
    --Condition.Rules.0.MetricName CvmDiskUsage \
    --Condition.Rules.0.Period 60 \
    --Condition.Rules.0.Operator ge \
    --Condition.Rules.0.Value 99.9 \
    --Condition.Rules.0.ContinuePeriod 1 \
    --Condition.Rules.0.NoticeFrequency 3600 \
    --Condition.Rules.0.IsPowerNotice 0 \
    --EventCondition.Rules.0.MetricName ping_unreach \
    --NoticeIds notice-bv9b4ghqbg notice-gj2n9wnt29 \
    --TriggerTasks.0.Type AS \
    --TriggerTasks.0.TaskConfig {"Region":"ap-guangzhou","Group":"asg-0zhspjx","Policy":"asp-ganig28"}
```

Output: 
```
{
    "Response": {
        "RequestId": "29ghj2hh-45-h53h234h-23",
        "PolicyId": "policy-hi498gw3h2",
        "OriginId": "1234556"
    }
}
```

