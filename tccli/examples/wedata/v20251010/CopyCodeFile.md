**Example 1: 复制代码文件**

复制代码文件

Input: 

```
tccli wedata CopyCodeFile --cli-unfold-argument  \
    --WorkspaceId workspaceId_test \
    --CodeFileId a887780d-245c-4a4d-b78e-4510d15a05fe \
    --CodeFileName test12335.txt \
    --ExtensionType ide
```

Output: 
```
{
    "Response": {
        "Data": {
            "AppId": "251436191",
            "BundleId": "",
            "BundleInfo": "",
            "CodeFileConfig": {
                "Params": ""
            },
            "CodeFileId": "c8f100a4-9352-44e2-b744-16410fe65c32",
            "CodeFileName": "test12335.txt",
            "CreateTime": "1761948864452",
            "CreateUserUin": "700002164618",
            "ExtensionType": "ide",
            "InchargeUserUin": "700002164618",
            "ParentFolderId": "",
            "Path": "/test12335.txt",
            "Status": "active",
            "UpdateTime": "1761948864452",
            "UpdateUserUin": "700002164618",
            "WorkspaceId": "workspaceId_test"
        },
        "RequestId": "e00e579b-d0a6-4333-9d9d-05217dad054b"
    }
}
```

