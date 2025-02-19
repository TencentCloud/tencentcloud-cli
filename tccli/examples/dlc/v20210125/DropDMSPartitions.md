**Example 1: DMS元数据删除分区**



Input: 

```
tccli dlc DropDMSPartitions --cli-unfold-argument  \
    --DatabaseName database-xxxx \
    --SchemaName Schema1 \
    --TableName Table1 \
    --Name Name1 \
    --Values 1 2 \
    --DeleteData False \
    --DatasourceConnectionName DataLakeCatalog
```

Output: 
```
{
    "Response": {
        "RequestId": "12345-67890-12345-67890",
        "Status": true
    }
}
```

