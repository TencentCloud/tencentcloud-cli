**Example 1: 离线任务实例详情**

离线任务实例详情

Input: 

```
tccli wedata DescribeTaskInstance --cli-unfold-argument  \
    --ProjectId 1 \
    --TaskId 202205058668886 \
    --CurRunDate 2020-05-05 12:00:00 \
    --IssueDate 2020-05-05 12:04:18
```

Output: 
```
{
    "Response": {
        "TaskInstanceDetail": {
            "TaskRunId": "abc",
            "TaskId": "abc",
            "CurRunDate": "abc",
            "IssueDate": "abc",
            "InlongTaskId": "abc",
            "ExecutorGroupId": "abc",
            "TaskRunType": 1,
            "State": 1,
            "StartTime": "abc",
            "EndTime": "abc",
            "BrokerIp": "abc",
            "PodName": "abc",
            "NextRunDate": "abc",
            "CreateUin": 1,
            "OperatorUin": 1,
            "OwnerUin": 1,
            "AppId": 1,
            "ProjectId": "abc",
            "CreateTime": "abc",
            "UpdateTime": "abc",
            "TaskName": "abc"
        },
        "Data": {
            "TaskRunId": "abc",
            "TaskId": "abc",
            "CurRunDate": "abc",
            "IssueDate": "abc",
            "InlongTaskId": "abc",
            "ExecutorGroupId": "abc",
            "TaskRunType": 1,
            "State": 1,
            "StartTime": "abc",
            "EndTime": "abc",
            "BrokerIp": "abc",
            "PodName": "abc",
            "NextRunDate": "abc",
            "CreateUin": 1,
            "OperatorUin": 1,
            "OwnerUin": 1,
            "AppId": 1,
            "ProjectId": "abc",
            "CreateTime": "abc",
            "UpdateTime": "abc",
            "TaskName": "abc"
        },
        "RequestId": "abc"
    }
}
```

