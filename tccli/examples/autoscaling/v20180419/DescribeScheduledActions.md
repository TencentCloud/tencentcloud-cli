**Example 1: 查询定时任务**



Input: 

```
tccli as DescribeScheduledActions --cli-unfold-argument  \
    --ScheduledActionIds asst-caa5ha40
```

Output: 
```
{
    "Response": {
        "RequestId": "cc207181-288d-4a39-a1d1-63a5e1ba1d2b",
        "TotalCount": 1,
        "ScheduledActionSet": [
            {
                "ScheduledActionId": "asst-jf898dps",
                "ScheduledActionName": "test",
                "AutoScalingGroupId": "asg-keqt9eg1",
                "StartTime": "2022-02-22T16:00:00+08:00",
                "Recurrence": "0 0 * * *",
                "EndTime": "2024-02-22T16:00:00+08:00",
                "MaxSize": 15,
                "DesiredCapacity": 1,
                "MinSize": 1,
                "CreatedTime": "2022-02-21T02:19:52Z",
                "ScheduledType": "CRONTAB"
            }
        ]
    }
}
```

