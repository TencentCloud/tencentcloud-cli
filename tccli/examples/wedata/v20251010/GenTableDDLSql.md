**Example 1: 生成表DDL Sql**



Input: 

```
tccli wedata GenTableDDLSql --cli-unfold-argument  \
    --WorkspaceId test-project-001 \
    --SinkDatabase test_dlc_catalog \
    --MsType MYSQL \
    --ConnectionId dc03eaf1-7f9b-4128-8c18-68ec95187d08 \
    --SourceDatabase test_source_db \
    --TableName user_info \
    --SinkType TCLAKE \
    --SourceFieldInfoList.0.FieldName id \
    --SourceFieldInfoList.0.FieldType int \
    --SourceFieldInfoList.0.Alias id \
    --SourceFieldInfoList.0.Comment primary key
```

Output: 
```
{
    "Response": {
        "Data": {
            "DDLSql": "CREATE TABLE `test_dlc_catalog`.``.`user_info` (\n\t`id` INT\n)\n;"
        },
        "RequestId": "60a42024-8d95-4c89-b021-99fe9206282e"
    }
}
```

