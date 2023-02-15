**Example 1: GenHiveTableDDLSql**

生成建hive表的sql

Input: 

```
tccli wedata GenHiveTableDDLSql --cli-unfold-argument  \
    --TableVersion xx \
    --SourceDatabase xx \
    --ProjectId xx \
    --SourceFieldInfoList.0.Alias xx \
    --SourceFieldInfoList.0.FieldName xx \
    --SourceFieldInfoList.0.FieldType xx \
    --TableName xx \
    --UpsertFlag True \
    --SinkDatabase xx \
    --Properties.0.Value xx \
    --Properties.0.Key xx \
    --SinkType xx \
    --DatasourceId xx \
    --SchemaName xx \
    --TableMode 0 \
    --MsType xx \
    --Id xx \
    --TableComment xx \
    --AddDataFiles 1000 \
    --AddEqualityDeletes 1000 \
    --AddPositionDeletes 1000 \
    --AddDeleteFiles 1000 \
    --Partitions.0.Transform xx \
    --Partitions.0.TransformArgs xx \
    --Partitions.0.Name xx
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

