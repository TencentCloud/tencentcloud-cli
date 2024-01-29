**Example 1: 回收站任务列表**

回收站任务列表

Input: 

```
tccli wedata DescribeRecycleTaskList --cli-unfold-argument  \
    --ProjectId abc \
    --Keyword abc \
    --PageNumber 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Data": {
            "PageNumber": 0,
            "PageSize": 0,
            "Rows": [
                {
                    "TaskId": "abc",
                    "TaskName": "abc",
                    "WorkflowId": "abc",
                    "WorkflowName": "abc",
                    "InCharge": "abc",
                    "InChargeId": "abc",
                    "ProjectId": "abc",
                    "ProjectIdent": "abc",
                    "ProjectName": "abc",
                    "TypeDesc": "abc",
                    "TypeId": 0,
                    "RecycleTips": "abc",
                    "RecycleUser": "abc",
                    "ProductName": "abc",
                    "OwnId": "abc",
                    "UserId": "abc",
                    "TenantId": "abc",
                    "UpdateUser": "abc",
                    "UpdateTime": "abc",
                    "UpdateUserId": "abc",
                    "Properties": [
                        {
                            "ParamKey": "abc",
                            "ParamValue": "abc"
                        }
                    ],
                    "VirtualFlag": true,
                    "VirtualTaskId": "abc",
                    "UserFileId": "abc"
                }
            ],
            "TotalCount": 0,
            "TotalPageNumber": 0
        },
        "RequestId": "abc"
    }
}
```

