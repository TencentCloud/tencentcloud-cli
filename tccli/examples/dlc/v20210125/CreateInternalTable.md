**Example 1: 创建托管存储内表**



Input: 

```
tccli dlc CreateInternalTable --cli-unfold-argument  \
    --Columns.0.Comment xx \
    --Columns.0.Default xx \
    --Columns.0.Type xx \
    --Columns.0.Name xx \
    --Columns.0.NotNull True \
    --TableBaseInfo.TableName xx \
    --TableBaseInfo.DatasourceConnectionName xx \
    --TableBaseInfo.DatabaseName xx \
    --TableBaseInfo.TableComment xx \
    --Partitions.0.Comment xx \
    --Partitions.0.PartitionDot 0 \
    --Partitions.0.Name xx \
    --Partitions.0.PartitionFormat xx \
    --Partitions.0.Type xx \
    --Partitions.0.PartitionType xx \
    --Partitions.0.Transform xx
```

Output: 
```
{
    "Response": {
        "Execution": "<create sql>",
        "RequestId": "RequestId"
    }
}
```

