**Example 1: 获取表schema信息**



Input: 

```
tccli wedata DescribeTableSchemaInfo --cli-unfold-argument  \
    --MsType HIVE \
    --Name 字符串 \
    --DatabaseName 字符串 \
    --DatasourceId 23432 \
    --ConnectionType rpc
```

Output: 
```
{
    "Response": {
        "SchemaInfoList": [
            {
                "ColumnKey": "ColumnKey",
                "Description": "Description",
                "Name": "Name",
                "Type": "HIVE"
            }
        ],
        "RequestId": "b91acd1a-1ca9-4d94-9647-e032924ac6bc"
    }
}
```

