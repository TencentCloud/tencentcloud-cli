**Example 1: GenHiveTableDDLSql**

生成建hive表的sql

Input: 

```
tccli wedata GenHiveTableDDLSql --cli-unfold-argument  \
    --Id abc \
    --ProjectId abc \
    --MsType abc \
    --DatasourceId abc \
    --SourceDatabase abc \
    --TableName abc \
    --SinkDatabase abc \
    --SinkType abc \
    --SchemaName abc \
    --SourceFieldInfoList.0.FieldName abc \
    --SourceFieldInfoList.0.FieldType abc \
    --SourceFieldInfoList.0.Alias abc \
    --Partitions.0.Transform abc \
    --Partitions.0.Name abc \
    --Partitions.0.TransformArgs abc \
    --Properties.0.Key abc \
    --Properties.0.Value abc \
    --TableMode 0 \
    --TableVersion abc \
    --UpsertFlag True \
    --TableComment abc \
    --AddDataFiles 0 \
    --AddEqualityDeletes 0 \
    --AddPositionDeletes 0 \
    --AddDeleteFiles 0 \
    --TargetDatasourceId abc
```

Output: 
```
{
    "Response": {
        "DDLSql": "abc",
        "Data": "abc",
        "RequestId": "abc"
    }
}
```

