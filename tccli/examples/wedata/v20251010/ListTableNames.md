**Example 1: 获取表名称列表**

获取表名称列表

Input: 

```
tccli wedata ListTableNames --cli-unfold-argument  \
    --CatalogName DataLakeCatalog \
    --SchemaName default \
    --MaxResults 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "Name": "order_managed_table",
                    "Namespace": [
                        "DataLakeCatalog",
                        "default"
                    ]
                }
            ],
            "NextPageToken": "eyJvZmZzZXQiOjF9"
        },
        "RequestId": "9854afad-1afe-4f20-91f0-46bf3c3c01c2"
    }
}
```

