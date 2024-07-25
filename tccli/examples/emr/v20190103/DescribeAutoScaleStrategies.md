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
        "LoadAutoScaleStrategies": [
            {
                "StrategyId": 0,
                "StrategyName": "abc",
                "CalmDownTime": 0,
                "ScaleAction": 0,
                "ScaleNum": 0,
                "ProcessMethod": 0,
                "Priority": 0,
                "StrategyStatus": 0,
                "YarnNodeLabel": "abc",
                "PeriodValid": "abc",
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
                "LoadMetricsConditions": {
                    "LoadMetrics": [
                        {
                            "StatisticPeriod": 0,
                            "TriggerThreshold": 0,
                            "LoadMetrics": "abc",
                            "MetricId": 0,
                            "Conditions": [
                                {
                                    "CompareMethod": 0,
                                    "Threshold": 0
                                }
                            ]
                        }
                    ]
                }
            }
        ],
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

