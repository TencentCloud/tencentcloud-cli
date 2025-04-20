**Example 1: 查询表**



Input: 

```
tccli dlc DescribeDMSTable --cli-unfold-argument  \
    --DbName api_test \
    --SchemaName api_test \
    --Name testName \
    --Catalog  \
    --Keyword  \
    --Type  EXTERNAL_TABLE \
    --DatasourceConnectionName DataLakeCatalog
```

Output: 
```
{
    "Response": {
        "Asset": {
            "BizParams": [],
            "Catalog": "hive",
            "CreateTime": "2020-09-22T00:00:00+00:00",
            "DataVersion": 0,
            "DatasourceId": 0,
            "Description": "",
            "Guid": "un0hFApITjaahQW99mDNFw",
            "Id": 11078081,
            "ModifiedTime": "2020-09-22T00:00:00+00:00",
            "Name": "",
            "Owner": "root",
            "OwnerAccount": "",
            "Params": [
                {
                    "Key": "current-schema",
                    "Value": "{\"type\":\"struct\",\"schema-id\":0,\"fields\":[{\"id\":1,\"name\":\"name\",\"required\":false,\"type\":\"string\"},{\"id\":2,\"name\":\"age\",\"required\":false,\"type\":\"int\"},{\"id\":3,\"name\":\"id\",\"required\":false,\"type\":\"int\"}]}"
                },
                {
                    "Key": "metadata_location",
                    "Value": "lakefs://10000034ec8fbe9c69533aa6685ed55676c8967a6e926f96e96e8f8294028d81060f6b3b@dlcfbe4-100018379117-1639652301-100017307912-1304028854/1305424723/warehouse/api_test/test/metadata/00000-d899e972-e96d-4451-9589-0dd2529894be.metadata.json"
                },
                {
                    "Key": "snapshot-count",
                    "Value": "0"
                },
                {
                    "Key": "table_type",
                    "Value": "ICEBERG"
                },
                {
                    "Key": "write.metadata.metrics.default",
                    "Value": "full"
                },
                {
                    "Key": "dlc.ao.data.govern.inherit",
                    "Value": "default"
                },
                {
                    "Key": "dlc.ao.data.govern.policy.rule-type",
                    "Value": "none"
                },
                {
                    "Key": "dlc_sub_uin",
                    "Value": "100016327396"
                },
                {
                    "Key": "owner",
                    "Value": "zYBEmJFg"
                },
                {
                    "Key": "transient_lastDdlTime",
                    "Value": "1690197650243"
                },
                {
                    "Key": "write.distribution-mode",
                    "Value": "hash"
                },
                {
                    "Key": "write.upsert.enabled",
                    "Value": "false"
                },
                {
                    "Key": "EXTERNAL",
                    "Value": "TRUE"
                },
                {
                    "Key": "table_spec_internal_v_0_1_1",
                    "Value": "[ ]"
                },
                {
                    "Key": "uuid",
                    "Value": "b9e945c2-2312-424e-a03f-2c3eeb71f095"
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
                    "Key": "lakehouse.storage.type",
                    "Value": "lakefs"
                }
            ],
            "PermValues": []
        },
        "Columns": [
            {
                "BizParams": [],
                "Description": "",
                "IsPartition": false,
                "Name": "name",
                "Params": null,
                "Position": 0,
                "Type": "string"
            },
            {
                "BizParams": [],
                "Description": "",
                "IsPartition": false,
                "Name": "age",
                "Params": null,
                "Position": 1,
                "Type": "int"
            },
            {
                "BizParams": [],
                "Description": "",
                "IsPartition": false,
                "Name": "id",
                "Params": null,
                "Position": 2,
                "Type": "int"
            }
        ],
        "DataUpdateTime": "2020-09-22T00:00:00+00:00",
        "DbName": "api_test",
        "LastAccessTime": "2020-09-22T00:00:00+00:00",
        "LifeTime": 0,
        "Name": "testName",
        "PartitionKeys": [],
        "Partitions": null,
        "RecordCount": 0,
        "RequestId": "46021e35-056c-4460-9a37-e74b25f5b81b",
        "Retention": 0,
        "SchemaName": "",
        "Sds": {
            "BucketCols": null,
            "Cols": null,
            "Compressed": false,
            "InputFormat": "org.apache.hadoop.mapred.FileInputFormat",
            "Location": "lakefs://10000034ec8fbe9c69533aa6685ed55676c8967a6e926f96e96e8f8294028d81060f6b3b@dlcfbe4-100018379117-1639652301-100017307912-1304028854/1305424723/warehouse/api_test/test",
            "NumBuckets": 0,
            "OutputFormat": "org.apache.hadoop.mapred.FileOutputFormat",
            "Params": [],
            "SerdeLib": "org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe",
            "SerdeName": "",
            "SerdeParams": null,
            "SortCols": null,
            "SortColumns": null,
            "StoredAsSubDirectories": false
        },
        "StorageSize": 0,
        "StructUpdateTime": "2020-09-22T00:00:00+00:00",
        "Type": "EXTERNAL_TABLE",
        "ViewExpandedText": "",
        "ViewOriginalText": ""
    }
}
```

