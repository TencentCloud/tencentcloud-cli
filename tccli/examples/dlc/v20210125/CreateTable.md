**Example 1: 建表**



Input: 

```
tccli dlc CreateTable --cli-unfold-argument  \
    --TableInfo.TableBaseInfo.DatabaseName testhyw \
    --TableInfo.TableBaseInfo.TableName Table1 \
    --TableInfo.TableBaseInfo.DatasourceConnectionName DataLakeCatalog \
    --TableInfo.Columns.0.Name user_id \
    --TableInfo.Columns.0.Type int \
    --TableInfo.Columns.1.Name birthday \
    --TableInfo.Columns.1.Type int \
    --TableInfo.Columns.2.Name gender \
    --TableInfo.Columns.2.Type int \
    --TableInfo.Partitions.0.Comment part \
    --TableInfo.Partitions.0.Name gender \
    --TableInfo.Partitions.0.Type string \
    --TableInfo.Location cosn://ricky-1301xxx708/test1/ \
    --TableInfo.DataFormat.CSV.Format CSV \
    --TableInfo.DataFormat.CSV.CodeCompress None \
    --TableInfo.DataFormat.CSV.HeadLines 1 \
    --TableInfo.DataFormat.CSV.CSVSerde.Quote " \
    --TableInfo.DataFormat.CSV.CSVSerde.Separator , \
    --TableInfo.DataFormat.AVRO.Format  \
    --TableInfo.DataFormat.Json.Format  \
    --TableInfo.DataFormat.Parquet.Format  \
    --TableInfo.DataFormat.TextFile.Regex  \
    --TableInfo.DataFormat.TextFile.Format  \
    --TableInfo.DataFormat.ORC.Format 
```

Output: 
```
{
    "Response": {
        "Execution": {
            "SQL": "CREATE EXTERNAL TABLE IF NOT EXISTS `DataLakeCatalog`.`testhyw`.`Table1` (`user_id` int,`birthday` int,`gender` int) PARTITIONED BY (`gender` string)  ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde' WITH SERDEPROPERTIES ('separatorChar'=',','quoteChar'='\"') STORED AS TEXTFILE LOCATION 'cosn://rickyhu-1301312708/test1/'  TBLPROPERTIES ('skip.header.line.count'='1')"
        },
        "RequestId": "b076c1df-26f0-45b7-84f1-fa4eeca7c83f"
    }
}
```

