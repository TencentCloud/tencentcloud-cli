**Example 1: 查询定时器列表**



Input: 

```
tccli gse DescribeTimerScalingPolicies --cli-unfold-argument  \
    --FleetId fleet-qp3g3caa-mg4w88ho \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "s1611556817860590511",
        "TimerScalingPolicies": [
            {
                "TimerId": "",
                "TimerStatus": 1,
                "TimerName": "11111111",
                "TimerFleetCapacity": {
                    "FleetId": "fleet-qp3g3caa-mkurlvoa",
                    "DesiredInstances": 1,
                    "MinSize": 0,
                    "MaxSize": 1,
                    "ScalingInterval": 10,
                    "ScalingType": "ScalingTypeAuto",
                    "TargetConfiguration": {
                        "TargetValue": 23
                    }
                },
                "TimerConfiguration": {
                    "TimerType": "TimerTypeDay",
                    "TimerValue": {
                        "Day": 1,
                        "WeekDays": [],
                        "FromDay": 0,
                        "ToDay": 0
                    },
                    "BeginTime": "2021-01-14T14:04:29.496Z",
                    "EndTime": "2022-01-14T14:04:29.496Z"
                }
            }
        ],
        "TotalCount": 0
    }
}
```

