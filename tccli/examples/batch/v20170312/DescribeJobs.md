**Example 1: 查询作业信息**



Input: 

```
tccli batch DescribeJobs --cli-unfold-argument  \
    --JobIds job-7e7evk2x job-3n2weaqt
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "JobSet": [
            {
                "EndTime": null,
                "JobState": "STARTING",
                "Tags": [
                    {
                        "Key": "batch-test-tag-job-key",
                        "Value": "batch-test-tag-job-value"
                    }
                ],
                "TaskMetrics": {
                    "PendingCount": 0,
                    "FailedCount": 0,
                    "StartingCount": 1,
                    "SucceedCount": 0,
                    "FailedInterruptedCount": 0,
                    "SubmittedCount": 0,
                    "RunnableCount": 0,
                    "RunningCount": 0
                },
                "JobId": "job-3n2weaqt",
                "Priority": 1,
                "Placement": {
                    "Zone": "ap-guangzhou-4"
                },
                "JobName": "hello-test-job",
                "CreateTime": "2020-09-22T07:14:54Z"
            },
            {
                "EndTime": "2020-09-21T08:59:45Z",
                "JobState": "FAILED",
                "Tags": [
                    {
                        "Key": "job-key1",
                        "Value": "job-value1"
                    },
                    {
                        "Key": "job-key",
                        "Value": "job-value"
                    }
                ],
                "TaskMetrics": {
                    "PendingCount": 0,
                    "FailedCount": 1,
                    "StartingCount": 0,
                    "SucceedCount": 0,
                    "FailedInterruptedCount": 0,
                    "SubmittedCount": 0,
                    "RunnableCount": 0,
                    "RunningCount": 0
                },
                "JobId": "job-7e7evk2x",
                "Priority": 1,
                "Placement": {
                    "Zone": "ap-guangzhou-4"
                },
                "JobName": "hello-test-job",
                "CreateTime": "2020-09-21T08:57:01Z"
            }
        ],
        "RequestId": "ba5df388-51bd-434d-81aa-d640f284b4e7"
    }
}
```

