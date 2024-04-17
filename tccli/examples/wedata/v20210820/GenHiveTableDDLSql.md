**Example 1: GenHiveTableDDLSql**

生成建hive表的sql

Input: 

```
tccli wedata GenHiveTableDDLSql --cli-unfold-argument  \
    --Id  \
    --ProjectId 1486446569620893696 \
    --MsType MYSQL \
    --DatasourceId 915669 \
    --SourceDatabase source_database_name \
    --TableName test_table_name \
    --SinkDatabase sink_database_name \
    --SinkType HIVE \
    --SchemaName test_schema_name \
    --SourceFieldInfoList.0.FieldName name \
    --SourceFieldInfoList.0.FieldType string \
    --SourceFieldInfoList.0.Alias name \
    --Partitions.0.Transform identity \
    --Partitions.0.Name id \
    --Partitions.0.TransformArgs  \
    --Properties.0.Key format-version \
    --Properties.0.Value 2 \
    --TableMode 0 \
    --TableVersion abc \
    --UpsertFlag True \
    --TableComment 表注释 \
    --AddDataFiles 0 \
    --AddEqualityDeletes 0 \
    --AddPositionDeletes 0 \
    --AddDeleteFiles 0 \
    --TargetDatasourceId 915792
```

Output: 
```
{
    "Response": {
        "DDLSql": "CREATE TABLE IF NOT EXISTS `test_hive`.`test_table`(`id` bigint comment '主键id',`name` string comment '名称',`len` decimal(5,2),`a1` bigint)row format delimited fields terminated by '\\t' STORED AS PARQUET;",
        "Data": "CREATE TABLE IF NOT EXISTS `test_hive`.`test_table`(`id` bigint comment '主键id',`name` string comment '名称',`len` decimal(5,2),`a1` bigint)row format delimited fields terminated by '\\t' STORED AS PARQUET;",
        "RequestId": "53042adf-3bf5-4d52-aa48-9b91ef2ccaa7"
    }
}
```

