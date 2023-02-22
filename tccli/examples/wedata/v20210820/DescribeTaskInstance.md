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
            "BrokerIp": "xx",
            "UpdateTime": "xx",
            "OwnerUin": 1,
            "TaskRunId": "xx",
            "TaskRunType": 1,
            "CurRunDate": "xx",
            "CreateUin": 1,
            "ProjectId": "xx",
            "InlongTaskId": "xx",
            "State": 1,
            "PodName": "xx",
            "OperatorUin": 1,
            "StartTime": "xx",
            "AppId": 1,
            "TaskId": "xx",
            "TaskName": "xx",
            "EndTime": "xx",
            "IssueDate": "xx",
            "CreateTime": "xx",
            "ExecutorGroupId": "xx",
            "NextRunDate": "xx"
        },
        "Data": {
            "BrokerIp": "xx",
            "UpdateTime": "xx",
            "OwnerUin": 1,
            "TaskRunId": "xx",
            "TaskRunType": 1,
            "CurRunDate": "xx",
            "CreateUin": 1,
            "ProjectId": "xx",
            "InlongTaskId": "xx",
            "State": 1,
            "PodName": "xx",
            "OperatorUin": 1,
            "StartTime": "xx",
            "AppId": 1,
            "TaskId": "xx",
            "TaskName": "xx",
            "EndTime": "xx",
            "IssueDate": "xx",
            "CreateTime": "xx",
            "ExecutorGroupId": "xx",
            "NextRunDate": "xx"
        },
        "RequestId": "xx"
    }
}
```

