**Example 1: 示例1**



Input: 

```
tccli dlc DescribeCatalogTableInfo --cli-unfold-argument  \
    --CatalogName chenfan_test_1 \
    --SchemaName default \
    --TableName sdfsdf
```

Output: 
```
{
    "Response": {
        "Table": {
            "Audit": {
                "CreatedAt": 1788503053534,
                "CreatedTime": "2026-09-04 14:24:13",
                "Creator": "700002744585",
                "LastModifiedTime": "",
                "LastModifier": ""
            },
            "CatalogName": "chenfan_test_1",
            "Columns": [
                {
                    "Comment": "xdv",
                    "FieldSetting": "",
                    "IsPrimaryKey": false,
                    "Name": "sdfsdf",
                    "Type": "double",
                    "TypeText": "double"
                }
            ],
            "Comment": "sdfsdf",
            "FormatType": "",
            "Name": "sdfsdf",
            "Properties": [
                {
                    "Key": "format",
                    "Value": "lance"
                }
            ],
            "SchemaName": "default",
            "TableFormat": "Lance",
            "TableMode": "",
            "TableType": "Managed"
        },
        "RequestId": "8e1bb12b-d1d0-4125-a96e-f64abca6adca"
    }
}
```

