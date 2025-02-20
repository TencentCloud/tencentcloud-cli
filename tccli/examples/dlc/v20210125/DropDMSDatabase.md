**Example 1: DMS元数据删除库**



Input: 

```
tccli dlc DropDMSDatabase --cli-unfold-argument  \
    --DatasourceConnectionName DataLakeCatalog \
    --Name Name1 \
    --DeleteData False \
    --Cascade False
```

Output: 
```
{
    "Response": {
        "RequestId": "1234567890"
    }
}
```

