**Example 1: DescribeTableInfo**

查询表信息

Input: 

```
tccli tccatalog DescribeTableInfo --cli-unfold-argument  \
    --CatalogName justtestdlc \
    --SchemaName dlc \
    --TableName products
```

Output: 
```
{
    "Response": {
        "RequestId": "0259f561-e457-4980-8d4d-07a96c3bed4e",
        "Table": {
            "Audit": {
                "CreatedTime": "1970-01-01 08:00:44",
                "Creator": "root",
                "LastModifiedTime": "",
                "LastModifier": ""
            },
            "Columns": [
                {
                    "Comment": "",
                    "Type": "string",
                    "Name": "moment_id"
                },
                {
                    "Comment": "",
                    "Type": "string",
                    "Name": "user_id"
                },
                {
                    "Comment": "",
                    "Type": "string",
                    "Name": "status"
                },
                {
                    "Comment": "",
                    "Type": "string",
                    "Name": "source_type"
                },
                {
                    "Comment": "",
                    "Type": "string",
                    "Name": "source_id"
                },
                {
                    "Comment": "",
                    "Type": "string",
                    "Name": "media_type"
                },
                {
                    "Comment": "",
                    "Type": "date",
                    "Name": "date_time"
                },
                {
                    "Comment": "",
                    "Type": "long",
                    "Name": "time_created"
                }
            ],
            "Comment": "",
            "Name": "target_table",
            "Properties": [
                {
                    "Key": "current-schema",
                    "Value": "{\"type\":\"struct\",\"schema-id\":0,\"fields\":[{\"id\":1,\"name\":\"moment_id\",\"required\":false,\"type\":\"string\"},{\"id\":2,\"name\":\"user_id\",\"required\":false,\"type\":\"string\"},{\"id\":3,\"name\":\"status\",\"required\":false,\"type\":\"string\"},{\"id\":4,\"name\":\"source_type\",\"required\":false,\"type\":\"string\"},{\"id\":5,\"name\":\"source_id\",\"required\":false,\"type\":\"string\"},{\"id\":6,\"name\":\"media_type\",\"required\":false,\"type\":\"string\"},{\"id\":7,\"name\":\"date_time\",\"required\":false,\"type\":\"date\"},{\"id\":8,\"name\":\"time_created\",\"required\":false,\"type\":\"long\"}]}"
                },
                {
                    "Key": "output-format",
                    "Value": "org.apache.hadoop.mapred.FileOutputFormat"
                },
                {
                    "Key": "dlc_sub_uin",
                    "Value": "100010537383"
                },
                {
                    "Key": "totalSize",
                    "Value": "0"
                },
                {
                    "Key": "metadata_location",
                    "Value": "lakefs://pwd/1305424723/warehouse/test_schema_001/target_table/metadata/00001-f81d5261-f599-4193-8f11-5e999f2c3c1f.metadata.json"
                },
                {
                    "Key": "location",
                    "Value": "lakefs://pwd/1305424723/warehouse/test_schema_001/target_table"
                },
                {
                    "Key": "table_type",
                    "Value": "ICEBERG"
                },
                {
                    "Key": "numRows",
                    "Value": "0"
                },
                {
                    "Key": "uuid",
                    "Value": "f9ef7137-8f3b-44d4-a20e-62ef8f6ebbf9"
                },
                {
                    "Key": "current-snapshot-summary",
                    "Value": "{\"spark.app.id\":\"spark-4c44172086c946ff86c4bc4ac87f28d9\",\"changed-partition-count\":\"0\",\"total-records\":\"0\",\"total-files-size\":\"0\",\"total-data-files\":\"0\",\"total-delete-files\":\"0\",\"total-position-deletes\":\"0\",\"total-equality-deletes\":\"0\"}"
                },
                {
                    "Key": "serde-lib",
                    "Value": "org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe"
                },
                {
                    "Key": "previous_metadata_location",
                    "Value": "lakefs://pwd/1305424723/warehouse/test_schema_001/target_table/metadata/00000-cde808b6-d1d5-4f98-9133-d5f0cebcff5e.metadata.json"
                },
                {
                    "Key": "input-format",
                    "Value": "org.apache.hadoop.mapred.FileInputFormat"
                },
                {
                    "Key": "numFiles",
                    "Value": "0"
                },
                {
                    "Key": "current-snapshot-timestamp-ms",
                    "Value": "1679800616683"
                },
                {
                    "Key": "snapshot-count",
                    "Value": "1"
                },
                {
                    "Key": "table-type",
                    "Value": "EXTERNAL_TABLE"
                },
                {
                    "Key": "current-snapshot-id",
                    "Value": "7137012799479785936"
                },
                {
                    "Key": "transient_lastDdlTime",
                    "Value": "1679800604105"
                },
                {
                    "Key": "lakehouse.storage.type",
                    "Value": "lakefs"
                },
                {
                    "Key": "owner",
                    "Value": "zYBEmJFg"
                }
            ]
        }
    }
}
```

