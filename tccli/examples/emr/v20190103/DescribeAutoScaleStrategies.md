**Example 1: 获取自动扩缩容规则**



Input: 

```
tccli emr DescribeAutoScaleStrategies --cli-unfold-argument  \
    --InstanceId emr-123 \
    --GroupId 0
```

Output: 
```
{
    "Response": {
        "LoadAutoScaleStrategies": [
            {
                "CalmDownTime": 60,
                "ConfigGroupAssigned": "",
                "GraceDownFlag": false,
                "GraceDownTime": 0,
                "LoadMetricsConditions": {
                    "LoadMetrics": [
                        {
                            "Conditions": [
                                {
                                    "CompareMethod": 1,
                                    "Threshold": 16
                                }
                            ],
                            "LoadMetrics": "AvailableVCores#root.default",
                            "MetricId": 1,
                            "StatisticPeriod": 60,
                            "TriggerThreshold": 1
                        }
                    ]
                },
                "MeasureMethod": "INSTANCE",
                "PeriodValid": "",
                "Priority": 3,
                "ProcessMethod": 3,
                "ScaleAction": 2,
                "ScaleNum": 2,
                "StrategyId": 1521,
                "StrategyName": "负载缩容",
                "StrategyStatus": 3,
                "Tags": [],
                "YarnNodeLabel": ""
            }
        ],
        "RequestId": "272c1c07-2840-44c8-8753-a761617f71fd",
        "TimeBasedAutoScaleStrategies": [
            {
                "CompensateFlag": 1,
                "ConfigGroupAssigned": "{\"HDFS-3.2.2\":-1,\"IMPALA-4.1.0\":-1,\"KYUUBI-1.6.0\":-1,\"TRINO-389\":-1,\"YARN-3.2.2\":-1}",
                "GraceDownFlag": false,
                "GraceDownTime": 0,
                "GroupId": 0,
                "IntervalTime": 300,
                "MaxUse": 0,
                "MeasureMethod": "INSTANCE",
                "Priority": 1,
                "RepeatStrategy": {
                    "DayRepeat": {
                        "ExecuteAtTimeOfDay": "08:30:00",
                        "Step": 1
                    },
                    "Expire": "2024-09-11 23:59:59",
                    "MonthRepeat": {
                        "DaysOfMonthRange": null,
                        "ExecuteAtTimeOfDay": ""
                    },
                    "NotRepeat": {
                        "ExecuteAt": ""
                    },
                    "RepeatType": "DAY",
                    "WeekRepeat": {
                        "DaysOfWeek": null,
                        "ExecuteAtTimeOfDay": ""
                    }
                },
                "RetryValidTime": 300,
                "ScaleAction": 1,
                "ScaleNum": 1,
                "ServiceNodeInfo": [
                    7
                ],
                "SoftDeployInfo": [
                    1,
                    2
                ],
                "StrategyId": 1274,
                "StrategyName": "时间伸缩扩容周期性",
                "StrategyStatus": 3,
                "Tags": [
                    {
                        "TagKey": "key09993",
                        "TagValue": "value1"
                    },
                    {
                        "TagKey": "key09991",
                        "TagValue": "value1"
                    }
                ],
                "TerminatePolicy": "DEFAULT"
            },
            {
                "CompensateFlag": 0,
                "ConfigGroupAssigned": "",
                "GraceDownFlag": true,
                "GraceDownTime": 180,
                "GroupId": 0,
                "IntervalTime": 60,
                "MaxUse": 0,
                "MeasureMethod": "INSTANCE",
                "Priority": 2,
                "RepeatStrategy": {
                    "DayRepeat": {
                        "ExecuteAtTimeOfDay": "09:30:00",
                        "Step": 1
                    },
                    "Expire": "2024-09-11 23:59:59",
                    "MonthRepeat": {
                        "DaysOfMonthRange": null,
                        "ExecuteAtTimeOfDay": ""
                    },
                    "NotRepeat": {
                        "ExecuteAt": ""
                    },
                    "RepeatType": "DAY",
                    "WeekRepeat": {
                        "DaysOfWeek": null,
                        "ExecuteAtTimeOfDay": ""
                    }
                },
                "RetryValidTime": 60,
                "ScaleAction": 2,
                "ScaleNum": 1,
                "ServiceNodeInfo": null,
                "SoftDeployInfo": null,
                "StrategyId": 1275,
                "StrategyName": "时间伸缩缩容周期性-开启优雅缩容",
                "StrategyStatus": 3,
                "Tags": [],
                "TerminatePolicy": "DEFAULT"
            }
        ]
    }
}
```

