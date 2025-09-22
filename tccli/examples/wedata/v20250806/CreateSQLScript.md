**Example 1: 创建**



Input: 

```
tccli wedata CreateSQLScript --cli-unfold-argument  \
    --ScriptName test_sql2 \
    --ProjectId 2912854921119117312 \
    --ParentFolderPath  \
    --ScriptContent c2VsZWN0IDE7 \
    --AccessScope SHARED
```

Output: 
```
{
    "Response": {
        "Data": {
            "AccessScope": "SHARED",
            "CreateTime": "2025-08-28 17:20:31",
            "OwnerUin": "100032159948",
            "ParentFolderPath": "",
            "Path": "/test_sql2",
            "ProjectId": "2912854921119117312",
            "ScriptConfig": {
                "AdvanceConfig": null,
                "ComputeResource": null,
                "DatasourceEnv": null,
                "DatasourceId": null,
                "ExecutorGroupId": null,
                "Params": null
            },
            "ScriptContent": "c2VsZWN0IDE7",
            "ScriptId": "bf6a325f-ab82-4fba-9eac-1b6ae58f20f6",
            "ScriptName": "test_sql2",
            "UpdateTime": "2025-08-28 17:20:31",
            "UpdateUserUin": "100032159948"
        },
        "RequestId": "619c3bba-7376-4af3-b7f6-511cf9ebf1bd"
    }
}
```

