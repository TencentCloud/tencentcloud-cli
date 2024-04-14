**Example 1: 分页查询表数据质量详情**

分页查询表数据质量详情

Input: 

```
tccli wedata DescribeTableQualityDetails --cli-unfold-argument  \
    --PageSize 1 \
    --ProjectId 153161111111111111 \
    --StatisticsDate 1679414400 \
    --DatasourceId dsadsa-dsadihjks \
    --OrderFields.0.Direction DESC \
    --OrderFields.0.Name TableScore \
    --PageNumber 0 \
    --Filters.0.Values TableName \
    --Filters.0.Name dq_table1
```

Output: 
```
{
    "Response": {
        "RequestId": "f2a131b8-0dd3a028",
        "Data": {
            "TotalCount": 4,
            "Items": [
                {
                    "DatabaseId": "dsadasd-dsad",
                    "DatabaseName": "dq_db1",
                    "TableId": "dsjklj-jkjk",
                    "TableName": "dq_table1",
                    "OwnerUserId": 100333290099,
                    "OwnerUserName": "zhangsna",
                    "DatabaseScore": 0.8,
                    "TableScore": 12.0,
                    "LastPeriodRatio": 0.18
                }
            ]
        }
    }
}
```

