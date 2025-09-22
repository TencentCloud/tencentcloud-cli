**Example 1: 成功响应**



Input: 

```
tccli wedata UpdateSQLScript --cli-unfold-argument  \
    --ScriptId 971c1520-836f-41be-b13f-7a6c637317c8 \
    --ProjectId 1460947878944567296 \
    --ScriptConfig.DatasourceId 54396 \
    --ScriptConfig.ComputeResource warehouse01 \
    --ScriptConfig.ExecutorGroupId 20240306201326014948 \
    --ScriptConfig.AdvanceConfig  \
    --ScriptContent c2hvdyBkYXRhYmFzZTs=
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
            "Path": null,
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
            "UpdateTime": "2025-09-22 20:08:19",
            "UpdateUserUin": "100028579606"
        },
        "RequestId": "30345134-cfad-499f-a956-9f060f7e65aa"
    }
}
```

