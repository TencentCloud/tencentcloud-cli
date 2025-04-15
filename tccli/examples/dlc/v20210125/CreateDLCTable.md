**Example 1: 创建表**



Input: 

```
tccli dlc CreateDLCTable --cli-unfold-argument  \
    --TableBaseInfo.DatabaseName database1 \
    --TableBaseInfo.TableName table2 \
    --TableBaseInfo.DatasourceConnectionName DataLakeCatalog \
    --TableBaseInfo.TableComment test comment \
    --TableBaseInfo.Type MANAGED_TABLE \
    --TableBaseInfo.TableFormat iceberg \
    --TableBaseInfo.UserAlias t********g \
    --TableBaseInfo.UserSubUin 1*********9 \
    --TableBaseInfo.SmartPolicy.BaseInfo.Uin 1**********9 \
    --TableBaseInfo.SmartPolicy.BaseInfo.PolicyType Table \
    --TableBaseInfo.SmartPolicy.BaseInfo.Catalog DataLakeCatalog \
    --TableBaseInfo.SmartPolicy.BaseInfo.Database database1 \
    --TableBaseInfo.SmartPolicy.BaseInfo.Table table2 \
    --TableBaseInfo.SmartPolicy.BaseInfo.AppId 1********3 \
    --TableBaseInfo.SmartPolicy.Policy.Inherit default \
    --TableBaseInfo.SmartPolicy.Policy.Written.WrittenEnable disable \
    --TableBaseInfo.SmartPolicy.Policy.Written.AdvancePolicy.TargetFileSizeBytes 0 \
    --TableType MANAGED_TABLE \
    --Columns.0.Name id \
    --Columns.0.Type int \
    --Columns.0.Comment test col \
    --Columns.0.NotNull False \
    --Partitions.0.Name id \
    --Partitions.0.Type int \
    --Partitions.0.Comment test partition \
    --Partitions.0.Transform identity \
    --Properties.0.Key testPro \
    --Properties.0.Value test \
    --DataEngineName public-engine
```

Output: 
```
{
    "Response": {
        "DLCTable": {
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
        },
        "Execution": "CREATE TABLE IF NOT EXISTS `DataLakeCatalog`.`database1`.`table2` (\n`column1` int COMMENT 'test col')\nCOMMENT 'test comment'\nPARTITIONED BY (`column1`)\nTBLPROPERTIES ('property1'='test property', 'write.distribution-mode'='hash', 'write.metadata.delete-after-commit.enabled'='true', 'write.metadata.previous-versions-max'='100', 'write.metadata.metrics.default'='full', 'smart-optimizer.inherit'='default');",
        "RequestId": "********-****-****-****-a15272e7f1b0"
    }
}
```

