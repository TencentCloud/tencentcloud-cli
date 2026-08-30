**Example 1: 创建定时任务**



Input: 

```
tccli thpc CreateScheduledAction --cli-unfold-argument  \
    --ClusterId hpc-qd1qqnyt \
    --QueueName lurka-auto-as \
    --ScheduledActionName scale-out-morning \
    --StartTime 2026-08-14T00:00:00+08:00 \
    --DesiredCapacity 3 \
    --EndTime 2026-08-31T23:59:59+08:00 \
    --Recurrence 0 9 * * 1-5
```

Output: 
```
{
    "Response": {
        "RequestId": "21aed752-2433-4ee7-8351-e986261f270d"
    }
}
```

