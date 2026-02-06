**Example 1: 查询资源管理文件夹详情**

查询资源管理文件夹详情

Input: 

```
tccli wedata GetResourceFolder --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --FolderId 35dcd49b-52d2-4b8f-944e-425312435f10
```

Output: 
```
{
    "Response": {
        "Data": {
            "CreateUserName": "kevinnie",
            "CreateUserUin": "100028578763",
            "FolderId": "35dcd49b-52d2-4b8f-944e-425312435f10",
            "FolderName": "dsd",
            "FolderPath": "/datastudio/resource/evanxue/dsd",
            "ParentFolderPath": "/datastudio/resource/evanxue",
            "ProjectId": "1460947878944567296"
        },
        "RequestId": "ce031380-92e2-4989-873e-e2f065808dd6"
    }
}
```

