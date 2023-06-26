**Example 1: 分页查询表数据质量详情**

分页查询表数据质量详情

Input: 

```
tccli wedata DescribeTableQualityDetails --cli-unfold-argument  \
    --PageSize 0 \
    --ProjectId 0 \
    --StatisticsDate 0 \
    --DatasourceId  \
    --OrderFields.0.Direction DESC \
    --OrderFields.0.Name TableScore \
    --PageNumber 0 \
    --Filters.0.Values TableName \
    --Filters.0.Name test
```

Output: 
```
{
    "Response": {
        "RequestId": "f2a131b8-0de7-4cb8-a354-9bbfc5d3a028",
        "Data": {
            "TotalCount": 4,
            "Items": [
                {
                    "DatabaseId": "",
                    "DatabaseName": "",
                    "TableId": "",
                    "TableName": "",
                    "OwnerUserId": 1234,
                    "OwnerUserName": "",
                    "DatabaseScore": 0.0,
                    "TableScore": 0.0,
                    "LastPeriodRatio": 0.0
                }
            ]
        }
    }
}
```

