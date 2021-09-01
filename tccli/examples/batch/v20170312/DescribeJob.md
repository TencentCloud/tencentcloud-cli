**Example 1: 查询作业详细信息**



Input: 

```
tccli batch DescribeJob --cli-unfold-argument  \
    --JobId job-97zcl3wt
```

Output: 
```
{
    "Response": {
        "JobState": "SUCCEED",
        "TaskSet": [
            {
                "EndTime": "2018-02-07T09:30:31Z",
                "TaskName": "A",
                "TaskState": "SUCCEED",
                "CreateTime": "2018-02-07T09:29:09Z"
            },
            {
                "EndTime": "2018-02-07T09:31:49Z",
                "TaskName": "B",
                "TaskState": "SUCCEED",
                "CreateTime": "2018-02-07T09:29:09Z"
            },
            {
                "EndTime": "2018-02-07T09:31:48Z",
                "TaskName": "C",
                "TaskState": "SUCCEED",
                "CreateTime": "2018-02-07T09:29:09Z"
            },
            {
                "EndTime": "2018-02-07T09:33:01Z",
                "TaskName": "D",
                "TaskState": "SUCCEED",
                "CreateTime": "2018-02-07T09:29:09Z"
            }
        ],
        "Zone": "ap-guangzhou-2",
        "TaskMetrics": {
            "PendingCount": 0,
            "FailedCount": 0,
            "StartingCount": 0,
            "SucceedCount": 4,
            "FailedInterruptedCount": 0,
            "SubmittedCount": 0,
            "RunnableCount": 0,
            "RunningCount": 0
        },
        "JobName": "test job",
        "JobId": "job-97zcl3wt",
        "Priority": 1,
        "StateReason": "",
        "TaskInstanceMetrics": {
            "PendingCount": 0,
            "FailedCount": 0,
            "StartingCount": 0,
            "SucceedCount": 4,
            "FailedInterruptedCount": 0,
            "SubmittedCount": 0,
            "RunnableCount": 0,
            "RunningCount": 0
        },
        "EndTime": "2018-02-07T09:33:01Z",
        "DependenceSet": [
            {
                "StartTask": "A",
                "EndTask": "B"
            },
            {
                "StartTask": "A",
                "EndTask": "C"
            },
            {
                "StartTask": "B",
                "EndTask": "D"
            },
            {
                "StartTask": "C",
                "EndTask": "D"
            }
        ],
        "CreateTime": "2018-02-07T09:29:09Z",
        "Tags": [
            {
                "Key": "batch-test-tag-job-key",
                "Value": "batch-test-tag-job-value"
            }
        ],
        "NextAction": "",
        "RequestId": "d1b08863-b8ee-49d4-aa08-f464499f97a0"
    }
}
```

