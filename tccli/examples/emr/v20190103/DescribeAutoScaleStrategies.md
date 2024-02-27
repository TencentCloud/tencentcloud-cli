**Example 1: 获取自动扩缩容规则**



Input: 

```
tccli emr DescribeAutoScaleStrategies --cli-unfold-argument  \
    --InstanceId abc \
    --GroupId 0
```

Output: 
```
{
    "Response": {
        "TimeBasedAutoScaleStrategies": [
            {
                "StrategyId": 1,
                "StrategyName": "abc",
                "IntervalTime": 1,
                "ScaleAction": 1,
                "ScaleNum": 1,
                "StrategyStatus": 1,
                "Priority": 1,
                "RetryValidTime": 1,
                "RepeatStrategy": {
                    "RepeatType": "abc",
                    "DayRepeat": {
                        "ExecuteAtTimeOfDay": "abc",
                        "Step": 1
                    },
                    "WeekRepeat": {
                        "ExecuteAtTimeOfDay": "abc",
                        "DaysOfWeek": [
                            1
                        ]
                    },
                    "MonthRepeat": {
                        "ExecuteAtTimeOfDay": "abc",
                        "DaysOfMonthRange": [
                            1
                        ]
                    },
                    "NotRepeat": {
                        "ExecuteAt": "abc"
                    },
                    "Expire": "abc"
                },
                "GraceDownFlag": true,
                "GraceDownTime": 0,
                "Tags": [
                    {
                        "TagKey": "abc",
                        "TagValue": "abc"
                    }
                ],
                "ConfigGroupAssigned": "abc",
                "MeasureMethod": "abc",
                "TerminatePolicy": "abc",
                "MaxUse": 0,
                "SoftDeployInfo": [
                    0
                ],
                "ServiceNodeInfo": [
                    0
                ],
                "CompensateFlag": 0,
                "GroupId": 0
            }
        ],
        "RequestId": "abc"
    }
}
```

