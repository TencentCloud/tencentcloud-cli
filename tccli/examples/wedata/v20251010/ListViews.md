**Example 1: 获取view列表**

获取view列表

Input: 

```
tccli wedata ListViews --cli-unfold-argument  \
    --CatalogName DataLakeCatalog \
    --SchemaName luffyshi_dlc \
    --MaxResults 10
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [],
            "NextPageToken": ""
        },
        "RequestId": "98fbd89b-96c5-4f79-a093-10b3d80e07e3"
    }
}
```

