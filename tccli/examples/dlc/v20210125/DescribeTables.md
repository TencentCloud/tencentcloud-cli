**Example 1: 示例1**

查询数据表列表。

Input: 

```
tccli dlc DescribeTables --cli-unfold-argument  \
    --Limit 1 \
    --Offset 0 \
    --DatabaseName testdb \
    --DatasourceConnectionName DataLakeCatalog
```

Output: 
```
{
    "Response": {
        "RequestId": "8d02ec1a-1562-4780-98a2-15822f4cb517",
        "TableList": [
            {
                "TableBaseInfo": {
                    "DatasourceConnectionName": "",
                    "DatabaseName": "testdb",
                    "TableName": "table1",
                    "UserAlias": "testUser",
                    "UserSubUin": "100019878767"
                },
                "Columns": [],
                "Partitions": [],
                "Properties": [
                    {
                        "Key": "EXTERNAL",
                        "Value": "TRUE"
                    },
                    {
                        "Key": "transient_lastDdlTime",
                        "Value": "1630495521302"
                    },
                    {
                        "Key": "skip.header.line.count",
                        "Value": "1"
                    }
                ],
                "Location": "",
                "CreateTime": "1630495521000",
                "ModifiedTime": "1630495521000",
                "InputFormat": "",
                "StorageSize": 1024,
                "RecordCount": 10
            }
        ],
        "TotalCount": 2
    }
}
```

