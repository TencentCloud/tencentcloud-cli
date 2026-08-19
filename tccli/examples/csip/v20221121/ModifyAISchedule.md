**Example 1: 修改定时记录**



Input: 

```
tccli csip ModifyAISchedule --cli-unfold-argument  \
    --ScheduleId sched-a1b2c3d4 \
    --Name 每日安全扫描 \
    --Prompts 请执行全量安全扫描 \
    --MaxFireCount 0 \
    --StartTime 1704067200000 \
    --EndTime 0 \
    --Triggers.0.TriggerId trig-x1y2z3 \
    --Triggers.0.TriggerType 1 \
    --UpdateTriggers False
```

Output: 
```
{
    "Response": {
        "RequestId": "afacf06f-cf9f-44a5-8c96-70a4bd9bfe46"
    }
}
```

