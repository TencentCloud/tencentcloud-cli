**Example 1: 调试运行集成任务**

调试运行集成任务

Input: 

```
tccli wedata GetOfflineInstanceList --cli-unfold-argument  \
    --ProjectId xx \
    --PageIndex xx \
    --SearchCondition.Sort xx \
    --SearchCondition.Instance.ResourceGroup 1 \
    --SearchCondition.Instance.ExecutionSpace 1 \
    --SearchCondition.Instance.ProductName 1 \
    --SearchCondition.SortCol xx \
    --SearchCondition.Keyword xx \
    --PageSize 1
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "List": [
            {
                "UpdateTime": "xx",
                "OwnerUin": "xx",
                "OperatorUin": "xx",
                "IssueId": "xx",
                "CurRunDate": "xx",
                "CreateUin": "xx",
                "InlongTaskId": "xx",
                "InstanceKey": "xx",
                "ResourceGroup": "xx",
                "State": "xx",
                "WorkspaceId": "xx",
                "StartTime": "xx",
                "AppId": "xx",
                "TaskId": "xx",
                "EndTime": "xx",
                "CreateTime": "xx",
                "TaskRunType": 1
            }
        ],
        "RequestId": "xx"
    }
}
```

