**Example 1: 分页查询指定路径的工作流文件夹下的直接子文件夹列表**



Input: 

```
tccli wedata ListWorkflowFolders --cli-unfold-argument  \
    --ProjectId 1464962169590902784 \
    --ParentFolderPath /u9ed8u8ba4u6587u4ef6u5939 \
    --PageNumber 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "CreateUserUin": null,
                    "FolderId": "be1c40fa-0cd3-436f-a3c0-6ff9ff473705",
                    "FolderPath": "/u9ed8u8ba4u6587u4ef6u5939/copy_wf_case",
                    "ProjectId": "1464962169590902784"
                }
            ],
            "PageNumber": 1,
            "PageSize": 10,
            "TotalCount": 7,
            "TotalPageNumber": 1
        },
        "RequestId": "8bbe44b7-856a-4849-9e07-44d7e5b89909"
    }
}
```

