**Example 1: 例子**

例子

Input: 

```
tccli wedata DescribeDiagnosticInfoByBaselineId --cli-unfold-argument  \
    --BaselineId abc \
    --ProjectId abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "BaselineTasks": [
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
            ]
        },
        "RequestId": "abc"
    }
}
```

