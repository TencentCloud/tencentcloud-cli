**Example 1: 查询数据库列表**

查询数据库列表

Input: 

```
tccli wedata ListDatabase --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 10 \
    --CatalogName 0 \
    --DatasourceId 8586 \
    --Keyword orcl
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "CatalogName": null,
                    "Description": "",
                    "Guid": "M2zrTn-RTcGos0IYH7tXnQ",
                    "Location": "",
                    "Name": "orcl",
                    "StorageSize": 0
                }
            ],
            "PageCount": 0,
            "PageNumber": 1,
            "PageSize": 1,
            "TotalCount": 1
        },
        "RequestId": "8559f6a1-98b5-452f-bc62-2ac51e61ca2a"
    }
}
```

**Example 2: OpenAPI-查询数据库**

OpenAPI-查询数据库

Input: 

```
tccli wedata ListDatabase --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 2 \
    --Keyword db
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "CatalogName": null,
                    "Description": "",
                    "Guid": "LKQYhWDPj0Yg2HcBzCkp_A",
                    "Location": "",
                    "Name": "test_db_table",
                    "StorageSize": null
                },
                {
                    "CatalogName": null,
                    "Description": "",
                    "Guid": "XkYUIom6t8A3TDA75uxzxA",
                    "Location": "",
                    "Name": "test_db_table",
                    "StorageSize": null
                }
            ],
            "PageCount": 0,
            "PageNumber": 1,
            "PageSize": 935,
            "TotalCount": 1870
        },
        "RequestId": "4f1276d6-a0af-4267-8ce6-fd61c08a5ba9"
    }
}
```

