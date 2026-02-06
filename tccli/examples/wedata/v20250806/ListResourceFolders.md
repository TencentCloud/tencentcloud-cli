**Example 1: 查看资源文件列表**



Input: 

```
tccli wedata ListResourceFolders --cli-unfold-argument  \
    --ProjectId 2153380***734784 \
    --PageNumber 1 \
    --PageSize 10 \
    --ParentFolderPath /datastud***ce/ascvb
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "CreateUserName": "qmi**iu",
                    "CreateUserUin": "1000***8885",
                    "FolderId": "c39ef029-590***d9ae972dbdff",
                    "FolderName": "ascvb",
                    "FolderPath": "/datastud***ce/ascvb"
                }
            ],
            "PageNumber": 1,
            "PageSize": 10,
            "TotalCount": 1,
            "TotalPageNumber": 1
        },
        "RequestId": "f7a73c6a-364c-4f88-acd2-89cdd82dc74a"
    }
}
```

