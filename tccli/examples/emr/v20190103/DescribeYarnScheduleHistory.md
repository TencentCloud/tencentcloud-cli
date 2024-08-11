**Example 1: 查看yarn资源调度的调度历史**



Input: 

```
tccli emr DescribeYarnScheduleHistory --cli-unfold-argument  \
    --InstanceId emr-a903oah8 \
    --StartTime 1722873600 \
    --EndTime 1722959999 \
    --Limit 10 \
    --Offset 0 \
    --SchedulerType All \
    --TaskState -99
```

Output: 
```
{
    "Response": {
        "RequestId": "c38e1833-e164-488c-9817-e8ca75d8d214",
        "SchedulerNameList": [
            "Capacity Scheduler",
            "Fair Scheduler"
        ],
        "StateList": [
            0,
            1,
            2,
            -1
        ],
        "Tasks": [
            {
                "CreateTime": "2024-08-07 19:13:38",
                "Details": [
                    {
                        "FailReason": "",
                        "JobId": 40005,
                        "Progress": "9%",
                        "Step": "开始"
                    },
                    {
                        "FailReason": "",
                        "JobId": 40005,
                        "Progress": "45%",
                        "Step": "写 capacity-scheduler.xml"
                    },
                    {
                        "FailReason": "",
                        "JobId": 40005,
                        "Progress": "63%",
                        "Step": "重启 resource manager"
                    },
                    {
                        "FailReason": "",
                        "JobId": 40005,
                        "Progress": "100%",
                        "Step": "结束"
                    }
                ],
                "EndTime": "2024-08-07 19:13:48",
                "OperatorName": "change capacity scheduler,disable label,refresh dynamic pools,restart resource manager",
                "SchedulerName": "Capacity Scheduler",
                "State": 2
            },
            {
                "CreateTime": "2024-08-06 14:30:02",
                "Details": [
                    {
                        "FailReason": "",
                        "JobId": 40000,
                        "Progress": "9%",
                        "Step": "开始"
                    },
                    {
                        "FailReason": "",
                        "JobId": 40000,
                        "Progress": "45%",
                        "Step": "写 capacity-scheduler.xml"
                    },
                    {
                        "FailReason": "The task was canceled because of a timeout",
                        "JobId": 40000,
                        "Progress": "63%",
                        "Step": "重启 resource manager"
                    }
                ],
                "EndTime": "2024-08-06 14:35:05",
                "OperatorName": "change capacity scheduler,disable label,refresh dynamic pools,restart resource manager",
                "SchedulerName": "Capacity Scheduler",
                "State": -1
            },
            {
                "CreateTime": "2024-08-06 11:29:15",
                "Details": [
                    {
                        "FailReason": "",
                        "JobId": 39994,
                        "Progress": "9%",
                        "Step": "开始"
                    },
                    {
                        "FailReason": "",
                        "JobId": 39994,
                        "Progress": "45%",
                        "Step": "写 capacity-scheduler.xml"
                    },
                    {
                        "FailReason": "",
                        "JobId": 39994,
                        "Progress": "63%",
                        "Step": "重启 resource manager"
                    },
                    {
                        "FailReason": "",
                        "JobId": 39994,
                        "Progress": "100%",
                        "Step": "结束"
                    }
                ],
                "EndTime": "2024-08-06 11:29:25",
                "OperatorName": "change capacity scheduler,disable label,refresh dynamic pools,restart resource manager",
                "SchedulerName": "Capacity Scheduler",
                "State": 2
            }
        ],
        "Total": 3
    }
}
```

