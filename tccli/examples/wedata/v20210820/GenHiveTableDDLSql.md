**Example 1: GenHiveTableDDLSql**

生成建hive表的sql

Input: 

```
tccli wedata GenHiveTableDDLSql --cli-unfold-argument  \
    --SourceDatabase xx \
    --ProjectId xx \
    --TableName xx \
    --SinkDatabase xx \
    --DatasourceId xx \
    --MsType xx \
    --Id xx \
    --SinkType xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "DDLSql": "xx"
    }
}
```

