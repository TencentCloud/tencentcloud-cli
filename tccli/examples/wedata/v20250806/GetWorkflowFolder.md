**Example 1: 查询工作流文件夹详情**

查询工作流文件夹详情

Input: 

```
tccli wedata GetWorkflowFolder --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --FolderId b6fa5e4c-a8d7-11f0-9366-7c8c09fca71c
```

Output: 
```
{
    "Response": {
        "Data": {
            "CreateUserUin": "100028578763",
            "FolderId": "b6fa5e4c-a8d7-11f0-9366-7c8c09fca71c",
            "FolderName": "wd",
            "FolderPath": "/caaa/wd",
            "ParentFolderPath": "/caaa",
            "ProjectId": "1460947878944567296"
        },
        "RequestId": "cc519301-5176-455a-b5f0-9a81d33ee1a3"
    }
}
```

