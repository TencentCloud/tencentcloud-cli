**Example 1: 获取sql文件夹详情**



Input: 

```
tccli wedata GetSQLFolder --cli-unfold-argument  \
    --ProjectId 1464962169590902784 \
    --FolderId 8b6d64db-98a5-492b-9a39-6bab69ebca5c
```

Output: 
```
{
    "Response": {
        "Data": {
            "AccessScope": "SHARED",
            "Children": null,
            "CreateUserUin": "100028649389",
            "Id": "8b6d64db-98a5-492b-9a39-6bab69ebca5c",
            "IsLeaf": null,
            "Name": "develop_test",
            "NodePermission": null,
            "OwnerUin": "100028649389",
            "Params": null,
            "ParentFolderPath": null,
            "Path": "/develop_test",
            "Type": null
        },
        "RequestId": "a60c81cd-6e53-4154-a815-d84c3a899b67"
    }
}
```

