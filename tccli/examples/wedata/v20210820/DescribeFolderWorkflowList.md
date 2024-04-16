**Example 1: 拉取文件夹下的工作流示例**

拉取文件夹下的工作流

Input: 

```
tccli wedata DescribeFolderWorkflowList --cli-unfold-argument  \
    --ProjectId 15316096090365952 \
    --ParentsFolderId ae1875b0-df51-11ee-8d4ae120f8272 \
    --PageNumber 1 \
    --PageSize 20
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "FolderId": "ae1875b0-df51-11ee-8d4ae120f8272",
                    "Owner": "jack",
                    "OwnerId": "100028427",
                    "ProjectId": "15316096090365952",
                    "ProjectIdent": "project_wedata",
                    "ProjectName": "project_wedata",
                    "UserGroupId": null,
                    "UserGroupName": null,
                    "WorkflowDesc": "",
                    "WorkflowId": "b2487621-df51-11ee-8a4ae120f8272",
                    "WorkflowName": "demo"
                }
            ],
            "PageNumber": 0,
            "PageSize": 0,
            "TotalCount": 1
        },
        "RequestId": "b316ed89-2840-4eeb-8fbd-7240473f44f3"
    }
}
```

