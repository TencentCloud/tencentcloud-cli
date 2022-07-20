**Example 1: 示例1**



Input: 

```
tccli dlc DescribeTable --cli-unfold-argument  \
    --DatabaseName testdb \
    --TableName table1
```

Output: 
```
{
    "Response": {
        "RequestId": "a8317085-a8a7-46ea-b7db-ca7b72c2a6bf",
        "Table": {
            "TableBaseInfo": {
                "DatasourceConnectionName": "DataLakeCatalog",
                "DatabaseName": "testdb",
                "TableName": "table1",
                "TableComment": "测试表",
                "Type": "table",
                "TableFormat": "iceberg",
                "UserAlias": "testUser",
                "UserSubUin": "100019878767"
            },
            "Columns": [
                {
                    "Name": "user_id",
                    "Type": "int",
                    "Comment": ""
                },
                {
                    "Name": "birthday",
                    "Type": "int",
                    "Comment": ""
                }
            ],
            "Partitions": [
                {
                    "Name": "gender",
                    "Type": "string",
                    "Comment": ""
                }
            ],
            "Properties": [
                {
                    "Key": "skip.header.line.count",
                    "Value": "1"
                },
                {
                    "Key": "EXTERNAL",
                    "Value": "TRUE"
                },
                {
                    "Key": "transient_lastDdlTime",
                    "Value": "1630495521302"
                }
            ],
            "Location": "cosn://ricky-1301xxx708/test1",
            "CreateTime": "1630495521000",
            "ModifiedTime": "1630495521000",
            "InputFormat": "org.apache.hadoop.mapred.TextInputFormat",
            "StorageSize": 1024,
            "RecordCount": 10
        }
    }
}
```

