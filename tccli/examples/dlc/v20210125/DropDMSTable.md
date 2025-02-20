**Example 1: DMS元数据删除表**



Input: 

```
tccli dlc DropDMSTable --cli-unfold-argument  \
    --DatasourceConnectionName DataLakeCatalog \
    --DbName database1 \
    --Name table1 \
    --DeleteData True
```

Output: 
```
{
    "Response": {
        "RequestId": "xxx-xxx-xxx"
    }
}
```

