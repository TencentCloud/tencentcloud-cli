**Example 1: 获取view名称列表**

获取view名称列表

Input: 

```
tccli wedata ListViewNames --cli-unfold-argument  \
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
                    "Name": "order_partition_view",
                    "Namespace": [
                        "DataLakeCatalog",
                        "default"
                    ]
                }
            ],
            "NextPageToken": "eyJvZmZzZXQiOjF9"
        },
        "RequestId": "9144f716-a16f-4c52-99bc-073581ccae06"
    }
}
```

