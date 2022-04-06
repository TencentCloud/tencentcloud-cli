**Example 1: 查询任务详情**



Input: 

```
tccli batch DescribeTask --cli-unfold-argument  \
    --JobId job-97zcl3wt \
    --TaskName A \
    --Filters.0.Name task-instance-state \
    --Filters.0.Values SUCCEED
```

Output: 
```
{
    "Response": {
        "TaskInstanceSet": [
            {
                "TaskInstanceIndex": 1,
                "RedirectInfo": {
                    "StderrRedirectFileName": "stderr.job-97zcl3wt.A.1.log",
                    "StdoutRedirectFileName": "stdout.job-97zcl3wt.A.1.log",
                    "StdoutRedirectPath": "cos://dondonbatch-1251783334.cosgz.myqcloud.com/hello2/logs/",
                    "StderrRedirectPath": "cos://dondonbatch-1251783334.cosgz.myqcloud.com/hello2/logs/"
                },
                "RunningTime": "2018-02-07T09:29:55Z",
                "LaunchTime": "2018-02-07T09:29:09Z",
                "StateReason": "",
                "StateDetailedReason": "xx",
                "ComputeNodeInstanceId": null,
                "EndTime": "2018-02-07T09:30:23Z",
                "TaskInstanceState": "SUCCEED",
                "CreateTime": "2018-02-07T09:29:09Z",
                "ExitCode": 0
            },
            {
                "TaskInstanceIndex": 0,
                "RedirectInfo": {
                    "StderrRedirectFileName": "stderr.job-97zcl3wt.A.0.log",
                    "StdoutRedirectFileName": "stdout.job-97zcl3wt.A.0.log",
                    "StdoutRedirectPath": "cos://dondonbatch-1251783334.cosgz.myqcloud.com/hello2/logs/",
                    "StderrRedirectPath": "cos://dondonbatch-1251783334.cosgz.myqcloud.com/hello2/logs/"
                },
                "RunningTime": "2018-02-07T09:30:02Z",
                "LaunchTime": "2018-02-07T09:29:09Z",
                "StateReason": "",
                "StateDetailedReason": "xx",
                "ComputeNodeInstanceId": null,
                "EndTime": "2018-02-07T09:30:31Z",
                "TaskInstanceState": "SUCCEED",
                "CreateTime": "2018-02-07T09:29:09Z",
                "ExitCode": 0
            }
        ],
        "TaskState": "SUCCEED",
        "JobId": "job-97zcl3wt",
        "TaskInstanceMetrics": {
            "PendingCount": 0,
            "FailedCount": 0,
            "StartingCount": 0,
            "SucceedCount": 2,
            "FailedInterruptedCount": 0,
            "SubmittedCount": 0,
            "RunnableCount": 0,
            "RunningCount": 0
        },
        "TaskInstanceTotalCount": 2,
        "TaskName": "A",
        "EndTime": "2018-02-07T09:30:31Z",
        "CreateTime": "2018-02-07T09:29:09Z",
        "RequestId": "f4723b24-e080-4599-b12d-b7eb657faefe"
    }
}
```

