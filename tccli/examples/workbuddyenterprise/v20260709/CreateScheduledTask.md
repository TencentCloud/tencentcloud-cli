**Example 1: 创建任务**



Input: 

```
tccli workbuddyenterprise CreateScheduledTask --cli-unfold-argument  \
    --TaskName 每日晨报 \
    --Description 工作日报 \
    --AgentConfig.Prompt 总结昨天的项目进展 \
    --AgentConfig.AgentId ag-xxx \
    --FrequencyType CRON \
    --CronExpr 0 0 9 * * * \
    --DeliveryTargetSet.0.Type BOT_CHANNEL \
    --DeliveryTargetSet.0.Enabled True \
    --DeliveryTargetSet.0.Options.ChannelType QQ \
    --DeliveryTargetSet.0.Options.ChannelId 1905263717 \
    --DeliveryTargetSet.0.Options.RecipientIdSet oc_xxx
```

Output: 
```
{
    "Response": {
        "TaskId": 1001,
        "TaskKey": "task-20260720090000-a1b2c3",
        "Status": "ACTIVE",
        "NextRunTime": "2026-07-21T09:00:00+08:00",
        "RequestId": "3c6d138e-1234-5678-9abc-def012345678"
    }
}
```

