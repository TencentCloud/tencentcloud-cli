**Example 1: drop table**

删除表

Input: 

```
tccli tccatalog DropTable --cli-unfold-argument  \
    --CatalogName justtestdlc \
    --SchemaName dlc \
    --TableName products
```

Output: 
```
{
    "Response": {
        "RequestId": "b8sd7dd7-ekd4-4e5e-993e-e5db64fa21c1",
        "Dropped": true
    }
}
```

