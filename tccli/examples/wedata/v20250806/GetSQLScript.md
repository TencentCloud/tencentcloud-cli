**Example 1: 成功响应**



Input: 

```
tccli wedata GetSQLScript --cli-unfold-argument  \
    --ScriptId 971c1520-836f-41be-b13f-7a6c637317c8 \
    --ProjectId 1460947878944567296
```

Output: 
```
{
    "Response": {
        "Data": {
            "AccessScope": "SHARED",
            "CreateTime": "2025-08-26 16:41:04",
            "OwnerUin": "100028579606",
            "ParentFolderPath": "",
            "Path": "/test_sql2",
            "ProjectId": "1460947878944567296",
            "ScriptConfig": {
                "AdvanceConfig": "",
                "ComputeResource": "warehouse01",
                "DatasourceEnv": null,
                "DatasourceId": "54396",
                "ExecutorGroupId": "20240306201326014948",
                "Params": null
            },
            "ScriptContent": "c2hvdyBkYXRhYmFzZTs=",
            "ScriptId": "971c1520-836f-41be-b13f-7a6c637317c8",
            "ScriptName": "test_sql2",
            "UpdateTime": "2025-09-17 11:22:55",
            "UpdateUserUin": "100028579606"
        },
        "RequestId": "5f3544ca-7354-4b86-b5c9-0e50b60d4e98"
    }
}
```

