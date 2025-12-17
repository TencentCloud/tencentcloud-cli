**Example 1: DescribeTables示例**



Input: 

```
tccli tccatalog DescribeTables --cli-unfold-argument  \
    --CatalogName system_catalog \
    --SchemaName sys_tclake \
    --TableNames tccatalog_schema_meta
```

Output: 
```
{
    "Response": {
        "Tables": [
            {
                "Audit": {
                    "CreatedAt": null,
                    "CreatedTime": "",
                    "Creator": "",
                    "LastModifiedAt": null,
                    "LastModifiedTime": "",
                    "LastModifier": ""
                },
                "Columns": [
                    {
                        "Comment": "",
                        "FieldSetting": "",
                        "IsPrimaryKey": false,
                        "Name": "schema_id",
                        "Type": "decimal(20,0)"
                    }
                ],
                "Comment": "",
                "FormatType": "v2",
                "Name": "tccatalog_schema_meta",
                "Properties": [
                    {
                        "Key": "current-snapshot-id",
                        "Value": "4143924622182415042"
                    }
                ],
                "TableFormat": "TCIceberg"
            }
        ],
        "RequestId": "bcf2a84d-2ee6-4d0c-bfe3-d1e215d6dbb6"
    }
}
```

