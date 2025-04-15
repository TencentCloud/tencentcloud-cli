**Example 1: DLC元数据获取表**



Input: 

```
tccli dlc DescribeDLCTable --cli-unfold-argument  \
    --DbName api_test \
    --Catalog DataLakeCatalog \
    --Name test \
    --Pattern pattern \
    --Type  INTERNAL_TABLE
```

Output: 
```
{
    "Response": {
        "DLCTable": {
            "Columns": [
                {
                    "Comment": "",
                    "Default": "",
                    "Name": "column_name1",
                    "NotNull": false,
                    "Precision": 0,
                    "Scale": 0,
                    "Type": "string"
                }
            ],
            "CreateTime": "1733734839000",
            "ExternalDataConfiguration": {
                "LifeTime": 0,
                "PartitionKeys": null,
                "Partitions": null,
                "Retention": 0,
                "Sds": null,
                "ViewExpandedText": "",
                "ViewOriginalText": ""
            },
            "HeatValue": 1597,
            "InputFormat": "org.apache.hadoop.mapred.FileInputFormat",
            "Location": "cosn://********",
            "MapMaterializedViewName": "",
            "ModifiedTime": "1744339723000",
            "Partitions": [],
            "Properties": [
                {
                    "Key": "transient_lastDdlTime",
                    "Value": "1733734839"
                },
                {
                    "Key": "current-schema",
                    "Value": "{\"type\":\"struct\",\"schema-id\":0,\"fields\":[{\"id\":1,\"name\":\"column_name1\",\"required\":false,\"type\":\"string\"}]}"
                },
                {
                    "Key": "dlc_sub_uin",
                    "Value": "1000******40"
                },
                {
                    "Key": "snapshot-count",
                    "Value": "0"
                },
                {
                    "Key": "uuid",
                    "Value": "********-****-****-****-3ba761c9dc68"
                },
                {
                    "Key": "owner",
                    "Value": "********"
                },
                {
                    "Key": "EXTERNAL",
                    "Value": "TRUE"
                },
                {
                    "Key": "write.upsert.enabled",
                    "Value": "false"
                },
                {
                    "Key": "lakehouse.storage.type",
                    "Value": "lakefs"
                },
                {
                    "Key": "metadata_location",
                    "Value": "cosn://*******"
                },
                {
                    "Key": "table_type",
                    "Value": "ICEBERG"
                },
                {
                    "Key": "format-version",
                    "Value": "1"
                }
            ],
            "RecordCount": 0,
            "StorageSize": 0,
            "TableBaseInfo": {
                "DatabaseName": "api_test",
                "DatasourceConnectionName": "",
                "DbGovernPolicyIsDisable": "",
                "GovernPolicy": {
                    "InheritDataBase": "default",
                    "RuleType": "none"
                },
                "PrimaryKeys": null,
                "TableComment": null,
                "TableFormat": "ICEBERG",
                "TableName": "api_test",
                "Type": "MANAGED_TABLE",
                "UserAlias": "user1",
                "UserSubUin": "100********40"
            }
        },
        "RequestId": "********-****-****-****-16332e138487"
    }
}
```

