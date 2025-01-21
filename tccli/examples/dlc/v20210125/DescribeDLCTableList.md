**Example 1: DLC元数据获取表列表**



Input: 

```
tccli dlc DescribeDLCTableList --cli-unfold-argument  \
    --DbName wyh_db_auth \
    --Catalog DaataLakeCatalog \
    --Filters.Name table-name \
    --Filters.Values table2 \
    --Type MANAGED_TABLE \
    --Limit 10 \
    --Offset 0 \
    --Sort CreateTime \
    --Asc True \
    --TableFormat ICEBERG
```

Output: 
```
{
    "Response": {
        "RequestId": "********-****-****-****-079d7ab5f226",
        "TableList": [
            {
                "Columns": [
                    {
                        "Comment": "test col",
                        "Default": "",
                        "IsPartition": true,
                        "Name": "column1",
                        "NotNull": false,
                        "Precision": 0,
                        "Scale": 0,
                        "Type": "int"
                    }
                ],
                "CreateTime": "1736853257000",
                "ExternalDataConfiguration": {
                    "LifeTime": 0,
                    "PartitionKeys": null,
                    "Partitions": null,
                    "Retention": 0,
                    "Sds": null,
                    "ViewExpandedText": "",
                    "ViewOriginalText": ""
                },
                "HeatValue": 1,
                "InputFormat": "org.apache.hadoop.mapred.FileInputFormat",
                "Location": "cosn://**********",
                "MapMaterializedViewName": "",
                "ModifiedTime": "1736853257000",
                "Partitions": [
                    {
                        "Comment": "test col",
                        "Name": "column1",
                        "Transform": "identity",
                        "TransformArgs": [],
                        "Type": "int"
                    }
                ],
                "Properties": [
                    {
                        "Key": "dlc_sub_uin",
                        "Value": "1**********6"
                    },
                    {
                        "Key": "lakehouse.storage.type",
                        "Value": "lakefs"
                    },
                    {
                        "Key": "comment",
                        "Value": "test comment"
                    },
                    {
                        "Key": "property1",
                        "Value": "test property"
                    },
                    {
                        "Key": "snapshot-count",
                        "Value": "0"
                    },
                    {
                        "Key": "write.distribution-mode",
                        "Value": "hash"
                    },
                    {
                        "Key": "write.metadata.metrics.default",
                        "Value": "full"
                    },
                    {
                        "Key": "table_type",
                        "Value": "ICEBERG"
                    },
                    {
                        "Key": "owner",
                        "Value": "******Fg"
                    },
                    {
                        "Key": "transient_lastDdlTime",
                        "Value": "1736853257438"
                    },
                    {
                        "Key": "write.metadata.delete-after-commit.enabled",
                        "Value": "true"
                    },
                    {
                        "Key": "write.metadata.previous-versions-max",
                        "Value": "100"
                    },
                    {
                        "Key": "metadata_location",
                        "Value": "cosn://**********"
                    },
                    {
                        "Key": "current-schema",
                        "Value": "{\"type\":\"struct\",\"schema-id\":0,\"fields\":[{\"id\":1,\"name\":\"column1\",\"required\":false,\"type\":\"int\",\"doc\":\"test col\"}]}"
                    },
                    {
                        "Key": "uuid",
                        "Value": "********-****-****-****-b62d30fd42ae"
                    },
                    {
                        "Key": "smart-optimizer.inherit",
                        "Value": "default"
                    },
                    {
                        "Key": "default-partition-spec",
                        "Value": "{\"spec-id\":0,\"fields\":[{\"name\":\"column1\",\"transform\":\"identity\",\"source-id\":1,\"field-id\":1000}]}"
                    },
                    {
                        "Key": "EXTERNAL",
                        "Value": "TRUE"
                    }
                ],
                "RecordCount": 0,
                "StorageSize": 0,
                "TableBaseInfo": {
                    "DatabaseName": "database1",
                    "DatasourceConnectionName": "",
                    "DbGovernPolicyIsDisable": "",
                    "GovernPolicy": {
                        "InheritDataBase": "default",
                        "RuleType": "none"
                    },
                    "TableComment": null,
                    "TableFormat": "ICEBERG",
                    "TableName": "table2",
                    "Type": "MANAGED_TABLE",
                    "UserAlias": "t********g",
                    "UserSubUin": "1**********6"
                }
            }
        ],
        "TotalCount": 0
    }
}
```

