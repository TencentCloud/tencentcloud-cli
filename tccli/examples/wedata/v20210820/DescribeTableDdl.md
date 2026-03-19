**Example 1: 查询表的DDL**



Input: 

```
tccli wedata DescribeTableDdl --cli-unfold-argument  \
    --TableId guid_of_table_***
```

Output: 
```
{
    "Response": {
        "RequestId": "req_id_***",
        "Ddl": "CREATE TABLE `database_name`.`table_name` (\n  `col1` string COMMENT '字段描述',\n  `col2` bigint COMMENT '字段描述'\n)\nPARTITIONED BY (`pt_day` string)\nROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.orc.OrcSerde'\nSTORED AS ORC\nLOCATION 'hdfs://HDFS***/warehouse/...'\nTBLPROPERTIES (...)"
    }
}
```

