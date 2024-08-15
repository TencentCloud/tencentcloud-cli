**Example 1: DLC元数据复制表**



Input: 

```
tccli dlc CopyDLCTable --cli-unfold-argument  \
    --SourceData.0.SourceDatabaseName db1 \
    --SourceData.0.SourceTableNameList table1 \
    --Catalog catalog \
    --DestinationDatabaseName db2 \
    --DestinationTableName table2 \
    --DataEngineName data_engine_1 \
    --ResourceGroupName ResourceGroupName1 \
    --IsCreateTable True
```

Output: 
```
{
    "Response": {
        "TaskId": "123-abc",
        "RequestId": "123-abc"
    }
}
```

