**Example 1: Demo1**



Input: 

```
tccli wedata DeleteOnlineTable --cli-unfold-argument  \
    --WorkspaceId 1 \
    --TableNameInfo.CatalogName Catalog_1 \
    --TableNameInfo.SchemaName Schema_1 \
    --TableNameInfo.TableName Table_1 \
    --ResourceGroupId nps-sd218y9
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": false
        },
        "RequestId": "20340814-bd36-4e34-b6b8-b9311864cdc6"
    }
}
```

