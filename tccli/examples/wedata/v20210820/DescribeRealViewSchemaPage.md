**Example 1: DescribeRealViewSchemaPage**



Input: 

```
tccli wedata DescribeRealViewSchemaPage --cli-unfold-argument  \
    --ProjectId 2347806860396163072 \
    --PageNumber 1 \
    --PageSize 300 \
    --DatabaseName di_dev \
    --DatasourceId 65408 \
    --DataSourceType SQLSERVER \
    --Keyword  \
    --Env development \
    --Model STANDARD \
    --DevDatasourceId 65407
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "SchemaName": "abc",
                "OriginDatabaseName": "abc"
            }
        ],
        "PageNumber": 1,
        "PageSize": 1,
        "TotalCount": 1,
        "TotalPage": 1,
        "RequestId": "abc"
    }
}
```

