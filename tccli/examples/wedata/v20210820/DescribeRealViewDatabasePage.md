**Example 1: DescribeRealViewDatabasePage**



Input: 

```
tccli wedata DescribeRealViewDatabasePage --cli-unfold-argument  \
    --DatasourceId 0 \
    --ProjectId a1b1c \
    --Asc True \
    --ConnectionType a1b1c \
    --Keyword a1b1c \
    --PageNumber 0 \
    --PageSize 0 \
    --ResourceGroupId a1bc1 \
    --ResourceType 0 \
    --Sort a1b1c
```

Output: 
```
{
    "Response": {
        "Data": {
            "PageNumber": 1,
            "PageSize": 2,
            "Rows": [
                {
                    "DataSourceId": 8575,
                    "DataSourceName": "di_doris",
                    "DataSourceType": "DORIS",
                    "DatabaseName": "cockpit"
                },
                {
                    "DataSourceId": 8575,
                    "DataSourceName": "di_doris",
                    "DataSourceType": "DORIS",
                    "DatabaseName": "db_01"
                }
            ],
            "TotalCount": 816,
            "TotalPageNumber": 408
        },
        "RequestId": "99a63938-9900-4fac-ab37-3d7f14e95007"
    }
}
```

