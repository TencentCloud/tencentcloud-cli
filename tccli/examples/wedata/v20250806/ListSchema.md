**Example 1: 查询Schema列表**

查询Schema列表

Input: 

```
tccli wedata ListSchema --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 10 \
    --CatalogName 0 \
    --DatasourceId 8499 \
    --DatabaseName orcl \
    --Keyword dev
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "DatabaseName": "orcl",
                    "Guid": "RpMuByxDK0C22iZeDOBMsA",
                    "Name": "WEDATA_DEV"
                }
            ],
            "PageCount": 0,
            "PageNumber": 1,
            "PageSize": 1,
            "TotalCount": 1
        },
        "RequestId": "283e76af-5333-4fe8-a968-b0370092e0cf"
    }
}
```

**Example 2: OpenAPI-查询数据库Schema**

OpenAPI-查询数据库Schema

Input: 

```
tccli wedata ListSchema --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 2 \
    --Keyword tab
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "DatabaseName": "my_database",
                    "Guid": "oJRdeGawTgyfMhtn8yvxHA",
                    "Name": "my_database"
                },
                {
                    "DatabaseName": "table_datatbases",
                    "Guid": "NJovXubQQXmb6cao__HYdA",
                    "Name": "table_datatbases"
                }
            ],
            "PageCount": 0,
            "PageNumber": 1,
            "PageSize": 2,
            "TotalCount": 4
        },
        "RequestId": "c6781fb3-5516-4a9b-ba06-2181481cd5ea"
    }
}
```

