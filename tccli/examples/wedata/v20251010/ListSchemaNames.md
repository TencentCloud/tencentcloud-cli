**Example 1: 获取schema名称列表**

获取schema名称列表

Input: 

```
tccli wedata ListSchemaNames --cli-unfold-argument  \
    --CatalogName mico_catalog_table_1027 \
    --MaxResults 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "Name": "default",
                    "Namespace": [
                        "mico_catalog_table_1027"
                    ]
                }
            ],
            "NextPageToken": "eyJvZmZzZXQiOjF9"
        },
        "RequestId": "7bd7de24-b051-4971-be3b-45f76381082f"
    }
}
```

