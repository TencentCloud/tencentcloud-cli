**Example 1: 获取schema列表**

获取schema列表

Input: 

```
tccli wedata ListSchemas --cli-unfold-argument  \
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
                    "Audit": {
                        "CreatedAt": "0",
                        "Creator": "",
                        "LastModifiedAt": "0",
                        "LastModifier": ""
                    },
                    "Comment": "Default database for catalog mico_catalog_table_1027",
                    "Name": "default",
                    "Properties": [
                        {
                            "Key": "location",
                            "Value": "cosn://dlcfd38-700001601851-1751253237-700001779129-251301051/1300298608/warehouse/1/mico_catalog_table_1027"
                        }
                    ]
                }
            ],
            "NextPageToken": "eyJvZmZzZXQiOjF9"
        },
        "RequestId": "5b912e37-680f-47f2-bd2f-f0b5bd25701b"
    }
}
```

