**Example 1: 创建定时任务**



Input: 

```
tccli csip CreateAISchedule --cli-unfold-argument  \
    --Name 每日安全扫描 \
    --Prompts 请执行全量安全扫描并生成报告 \
    --Triggers.0.TriggerId trig-x1y2z3 \
    --Triggers.0.TriggerType 1 \
    --MaxFireCount 0 \
    --StartTime 1704067200000 \
    --EndTime 0
```

Output: 
```
{
    "Response": {
        "ScheduleId": "sched-mock-001",
        "RequestId": "41b66490-3a6d-4ea1-a40e-7481b3db1500"
    }
}
```

