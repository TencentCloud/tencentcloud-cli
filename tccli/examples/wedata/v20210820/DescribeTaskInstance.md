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
            "TaskRunId": "TaskRunId",
            "TaskId": "TaskId",
            "CurRunDate": "2020-05-05 12:00:00",
            "IssueDate": "2020-05-05 12:04:18",
            "InlongTaskId": "InlongTaskId",
            "ExecutorGroupId": "ExecutorGroupId",
            "TaskRunType": 1,
            "State": 1,
            "StartTime": "2312321",
            "EndTime": "32312312",
            "BrokerIp": "10.0.0.1",
            "PodName": "PodName",
            "NextRunDate": "2020-05-05 12:00:00",
            "CreateUin": 1,
            "OperatorUin": 1,
            "OwnerUin": 1,
            "AppId": 1,
            "ProjectId": "1",
            "CreateTime": "2020-05-05 12:00:00",
            "UpdateTime": "2021-05-05 12:00:00",
            "TaskName": "TaskName"
        },
        "Data": {
            "TaskRunId": "TaskRunId",
            "TaskId": "TaskId",
            "CurRunDate": "2020-05-05 12:00:00",
            "IssueDate": "2020-05-05 12:04:18",
            "InlongTaskId": "InlongTaskId",
            "ExecutorGroupId": "ExecutorGroupId",
            "TaskRunType": 1,
            "State": 1,
            "StartTime": "2312323",
            "EndTime": "3123131312",
            "BrokerIp": "192.1.1.168",
            "PodName": "PodName",
            "NextRunDate": "NextRunDate",
            "CreateUin": 1,
            "OperatorUin": 1,
            "OwnerUin": 1,
            "AppId": 1,
            "ProjectId": "1",
            "CreateTime": "2020-05-05 12:00:00",
            "UpdateTime": "2021-05-05 12:00:00",
            "TaskName": "TaskName"
        },
        "RequestId": "as1cs2c123asyi23bh213cc"
    }
}
```

