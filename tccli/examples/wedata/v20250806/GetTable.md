**Example 1: 查询表详情**

查询表详情

Input: 

```
tccli wedata GetTable --cli-unfold-argument  \
    --TableGuid byV1bs2QGzbTepNlHhi2gA
```

Output: 
```
{
    "Response": {
        "Data": {
            "BusinessMetadata": {
                "TagNames": []
            },
            "CreateTime": "2025-09-03T10:36:03+08:00",
            "DatabaseName": "default",
            "Description": null,
            "Guid": "byV1bs2QGzbTepNlHhi2gA",
            "Name": "test_not_null_default_constraint_table",
            "SchemaName": null,
            "TableType": "MANAGED_TABLE",
            "TechnicalMetadata": {
                "Location": null,
                "Owner": null,
                "StorageSize": 0
            },
            "UpdateTime": "2025-09-03T10:36:03+08:00"
        },
        "RequestId": "179fe67d-3f98-4cd2-a23b-2670392a3552"
    }
}
```

**Example 2: OpenAPI-查询表详情**

OpenAPI-查询表详情

Input: 

```
tccli wedata GetTable --cli-unfold-argument  \
    --TableGuid hDMZH2AqXKoJMbe2tgdhhg
```

Output: 
```
{
    "Response": {
        "Data": {
            "BusinessMetadata": {
                "TagNames": []
            },
            "CreateTime": "2025-10-09T15:06:49+08:00",
            "DatabaseName": "db_uz25",
            "Description": null,
            "Guid": "hDMZH2AqXKoJMbe2tgdhhg",
            "Name": "table_normalqgqi",
            "SchemaName": null,
            "TableType": "MANAGED_TABLE",
            "TechnicalMetadata": {
                "Location": null,
                "Owner": "Wedata开发测试专用",
                "StorageSize": 0
            },
            "UpdateTime": "2025-10-09T15:06:49+08:00"
        },
        "RequestId": "3d261560-9b70-4f6d-a84f-d288e4a6c0d7"
    }
}
```

