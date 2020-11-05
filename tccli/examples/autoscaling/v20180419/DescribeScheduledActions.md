**Example 1: Querying a scheduled action**



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
                "ScheduledActionId": "asst-caa5ha40",
                "ScheduledActionName": "testv2-0",
                "AutoScalingGroupId": "asg-2nr9xh8h",
                "StartTime": "2018-09-28T00:00:00+08:00",
                "Recurrence": "0 0 * * *",
                "EndTime": "2018-09-28T23:59:59+08:00",
                "MaxSize": 10,
                "DesiredCapacity": 0,
                "MinSize": 0,
                "CreatedTime": "2018-09-24T07:41:54Z"
            }
        ]
    }
}
```

