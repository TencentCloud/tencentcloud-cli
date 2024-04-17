**Example 1: 调试运行集成任务**

调试运行集成任务

Input: 

```
tccli wedata GetOfflineDIInstanceList --cli-unfold-argument  \
    --ProjectId 1486446569620893696 \
    --SearchCondition.Instance.ExecutionSpace DRY_RUN \
    --SearchCondition.Instance.ProductName DATA_INTEGRATION \
    --SearchCondition.Instance.ResourceGroup 20240403154937113974 \
    --SearchCondition.SortCol CurRunDate \
    --SearchCondition.Sort desc \
    --SearchCondition.Keyword 20240408130054538 \
    --PageIndex 0 \
    --PageSize 1
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "AppId": "1315059999",
                "CreateTime": "2022-04-10 19:38:23",
                "CreateUin": "100028649999",
                "CurRunDate": "2022-04-10T19:38:21+08:00",
                "EndTime": null,
                "InlongTaskId": "dev_20220408130054538_1712749111_1712749111",
                "InstanceKey": "20220408130054538_2022-04-10T19:38:21+08:00",
                "IssueId": "2022-04-10 19:38:21",
                "OperatorUin": "100028649999",
                "OwnerUin": "100028448993",
                "ResourceGroup": "20240403154937113777",
                "StartTime": null,
                "State": "COMPLETED",
                "TaskId": "20220408130054538",
                "TaskRunType": 1,
                "UpdateTime": "2022-04-10 19:38:37",
                "WorkspaceId": "148644656962089399"
            }
        ],
        "RequestId": "ea9ec716-a23c-4adc-b7e8-cd54f562b9d3",
        "Total": 4
    }
}
```

