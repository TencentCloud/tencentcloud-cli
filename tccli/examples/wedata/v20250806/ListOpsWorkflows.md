**Example 1: 获取工作流列表**



Input: 

```
tccli wedata ListOpsWorkflows --cli-unfold-argument  \
    --ProjectId 2428908825624145920
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "CreateTime": "2025-09-01 14:24:26",
                    "FolderId": "e96fc104-c531-11ef-8c70-043f72d4907c",
                    "FolderName": "carlshi",
                    "OwnerUin": ";100028596846;",
                    "ProjectId": "2428908825624145920",
                    "ProjectName": "project_wedata_1u62e8u6d4bu4e13u7528",
                    "Status": "ALL_RUNNING",
                    "TaskCount": 4,
                    "UpdateTime": "2025-09-01 14:24:26",
                    "UpdateUserUin": "100028596846",
                    "WorkflowDesc": "",
                    "WorkflowId": "44083d5c-7448-414b-a8c7-0427bd9ee75a",
                    "WorkflowName": "makeuporder",
                    "WorkflowType": "cycle"
                }
            ],
            "PageNumber": 1,
            "PageSize": 10,
            "TotalCount": 540,
            "TotalPageNumber": 54
        },
        "RequestId": "8d95e83b-4fef-454d-a0bf-13b8e2c23177"
    }
}
```

