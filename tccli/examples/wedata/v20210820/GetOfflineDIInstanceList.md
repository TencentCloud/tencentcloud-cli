**Example 1: 调试运行集成任务**

调试运行集成任务

Input: 

```
tccli wedata GetOfflineDIInstanceList --cli-unfold-argument  \
    --PageIndex 1 \
    --PageSize 1 \
    --ProjectId abc \
    --SearchCondition.Keyword abc \
    --SearchCondition.Sort abc \
    --SearchCondition.SortCol abc \
    --SearchCondition.Instance.ExecutionSpace abc \
    --SearchCondition.Instance.ProductName abc \
    --SearchCondition.Instance.ResourceGroup abc
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "List": [
            {
                "CreateUin": "abc",
                "OperatorUin": "abc",
                "OwnerUin": "abc",
                "AppId": "abc",
                "WorkspaceId": "abc",
                "TaskId": "abc",
                "CurRunDate": "abc",
                "IssueId": "abc",
                "InlongTaskId": "abc",
                "ResourceGroup": "abc",
                "TaskRunType": 1,
                "State": "abc",
                "StartTime": "abc",
                "EndTime": "abc",
                "CreateTime": "abc",
                "UpdateTime": "abc",
                "InstanceKey": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

