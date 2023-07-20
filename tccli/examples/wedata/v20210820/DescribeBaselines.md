**Example 1: 例子**

例子

Input: 

```
tccli wedata DescribeBaselines --cli-unfold-argument  \
    --Filters.0.Name abc \
    --Filters.0.Values abc \
    --PageNumber 0 \
    --PageSize 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "Baselines": [
                {
                    "Id": 0,
                    "BaselineName": "abc",
                    "BaselineType": "abc",
                    "CreateTime": "2020-09-22T00:00:00+00:00",
                    "PromiseTasks": [
                        {
                            "Id": 0,
                            "BaselineId": 0,
                            "TaskId": "abc",
                            "TaskName": "abc",
                            "EstimatedCostTime": 0,
                            "UpstreamTaskIds": {
                                "PreviewRecord": [
                                    "abc"
                                ]
                            },
                            "DownstreamTaskIds": {
                                "PreviewRecord": [
                                    "abc"
                                ]
                            },
                            "IsPromiseTask": true,
                            "UserUin": "abc",
                            "OwnerUin": "abc",
                            "ProjectId": "abc",
                            "AppId": "abc",
                            "WorkflowName": "abc",
                            "WorkflowId": "abc",
                            "TaskCycle": "abc",
                            "TaskInChargeUin": "abc",
                            "TaskInChargeName": "abc",
                            "AccessBenchmark": "abc",
                            "AccessBenchmarkDesc": "abc",
                            "CreateTime": "abc",
                            "UpdateTime": "abc"
                        }
                    ],
                    "AlarmRule": {
                        "AlarmRuleId": "abc",
                        "AlarmLevelType": "abc"
                    },
                    "BaselineStatus": "abc",
                    "LatestBaselineInstanceStatus": "abc",
                    "WarningMargin": 0,
                    "PromiseTime": "2020-09-22T00:00:00+00:00",
                    "InChargeUin": "abc",
                    "InChargeName": "abc",
                    "UserUin": "abc",
                    "UserName": "abc",
                    "OwnerUin": "abc",
                    "ProjectId": "abc",
                    "AppId": "abc",
                    "UpdateTime": "abc"
                }
            ],
            "TotalCount": 0
        },
        "RequestId": "abc"
    }
}
```

