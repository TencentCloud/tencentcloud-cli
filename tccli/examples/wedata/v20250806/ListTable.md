**Example 1: 查询表列表**

查询表列表

Input: 

```
tccli wedata ListTable --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 10 \
    --CatalogName 0 \
    --DatasourceId 62159 \
    --DatabaseName test_db \
    --SchemaName public \
    --Keyword table
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "BusinessMetadata": {
                        "TagNames": []
                    },
                    "CreateTime": "2025-07-24T16:54:34+08:00",
                    "DatabaseName": "test_db",
                    "Description": null,
                    "Guid": "bONctN4uSTN9qL_im1kfYA",
                    "Name": "table_262",
                    "SchemaName": "public",
                    "TableType": "TABLE",
                    "TechnicalMetadata": {
                        "Location": null,
                        "Owner": null,
                        "StorageSize": 0
                    },
                    "UpdateTime": "2025-07-24T16:54:34+08:00"
                }
            ],
            "PageCount": 0,
            "PageNumber": 1,
            "PageSize": 1,
            "TotalCount": 2
        },
        "RequestId": "b0e64ba5-8c5a-4c09-8075-9ce4f06236fd"
    }
}
```

**Example 2: OpenAPI-查询数据表**

OpenAPI-查询数据表

Input: 

```
tccli wedata ListTable --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 2 \
    --Keyword tab
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "BusinessMetadata": {
                        "TagNames": []
                    },
                    "CreateTime": "2025-10-09T14:58:22+08:00",
                    "DatabaseName": "abetest",
                    "Description": "",
                    "Guid": "2fELSlxKuxbP6P9jRb6gjw",
                    "Name": "unpacked_abe_inference_table",
                    "SchemaName": null,
                    "TableType": "EXTERNAL_TABLE",
                    "TechnicalMetadata": {
                        "Location": null,
                        "Owner": "root",
                        "StorageSize": 0
                    },
                    "UpdateTime": "2025-10-09T14:58:50+08:00"
                },
                {
                    "BusinessMetadata": {
                        "TagNames": []
                    },
                    "CreateTime": "2025-10-09T14:58:22+08:00",
                    "DatabaseName": "abetest",
                    "Description": "",
                    "Guid": "kBYWxZbWRrtKxOIQm4-YqQ",
                    "Name": "unpacked_abe_inference_table",
                    "SchemaName": null,
                    "TableType": "EXTERNAL_TABLE",
                    "TechnicalMetadata": {
                        "Location": null,
                        "Owner": "root",
                        "StorageSize": 0
                    },
                    "UpdateTime": "2025-10-09T14:58:50+08:00"
                }
            ],
            "PageCount": 0,
            "PageNumber": 1,
            "PageSize": 15878,
            "TotalCount": 31755
        },
        "RequestId": "a74f877f-6202-47e1-ad08-ddeceb7b4232"
    }
}
```

