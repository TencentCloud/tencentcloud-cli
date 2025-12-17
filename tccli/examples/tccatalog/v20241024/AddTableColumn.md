**Example 1: AddTableColumn**



Input: 

```
tccli tccatalog AddTableColumn --cli-unfold-argument  \
    --CatalogName DataLakeCatalog \
    --SchemaName aorakili_test \
    --TableName numbers \
    --Type string \
    --FieldName new_col
```

Output: 
```
{
    "Response": {
        "Table": {
            "Audit": {
                "CreatedAt": 1761651580860,
                "CreatedTime": "2025-10-28 19:39:40",
                "Creator": "700002196454",
                "LastModifiedAt": 1762436179110,
                "LastModifiedTime": "2025-11-06 21:36:19",
                "LastModifier": "1290245077@qq.com"
            },
            "Columns": [
                {
                    "Comment": "",
                    "FieldSetting": "",
                    "IsPrimaryKey": false,
                    "Name": "ssn",
                    "Type": "integer"
                }
            ],
            "Comment": "",
            "FormatType": "",
            "Name": "numbers",
            "Properties": [
                {
                    "Key": "write.parquet.compression-codec",
                    "Value": "zstd"
                }
            ],
            "TableFormat": ""
        },
        "RequestId": "8d7d9fcd-3d2f-4b5a-a5c6-8ab9fc54dd80"
    }
}
```

