**Example 1: 建表**



Input: 

```
tccli dlc CreateTable --cli-unfold-argument  \
    --TableInfo.Columns.0.Comment xx \
    --TableInfo.Columns.0.Type xx \
    --TableInfo.Columns.0.Name xx \
    --TableInfo.DataFormat.CSV.HeadLines 0 \
    --TableInfo.DataFormat.CSV.CodeCompress xx \
    --TableInfo.DataFormat.CSV.Format xx \
    --TableInfo.DataFormat.CSV.CSVSerde.Quote xx \
    --TableInfo.DataFormat.CSV.CSVSerde.Separator xx \
    --TableInfo.DataFormat.CSV.CSVSerde.Escape xx \
    --TableInfo.DataFormat.AVRO.Format xx \
    --TableInfo.DataFormat.Json.Format xx \
    --TableInfo.DataFormat.Parquet.Format xx \
    --TableInfo.DataFormat.TextFile.Regex xx \
    --TableInfo.DataFormat.TextFile.Format xx \
    --TableInfo.DataFormat.ORC.Format xx \
    --TableInfo.Location xx \
    --TableInfo.TableBaseInfo.TableName xx \
    --TableInfo.TableBaseInfo.DatabaseName xx \
    --TableInfo.Partitions.0.Comment xx \
    --TableInfo.Partitions.0.Type xx \
    --TableInfo.Partitions.0.Name xx
```

Output: 
```
{
    "Response": {
        "Execution": {
            "SQL": "xx"
        },
        "RequestId": "xx"
    }
}
```

