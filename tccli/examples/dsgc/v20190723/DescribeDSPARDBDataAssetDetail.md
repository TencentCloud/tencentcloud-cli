**Example 1: 获取RDB关系数据库分类分级资产详情**



Input: 

```
tccli dsgc DescribeDSPARDBDataAssetDetail --cli-unfold-argument  \
    --DspaId dspa-001 \
    --ComplianceId 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Details": [
            {
                "CategoryName": "个人基本信息",
                "DataSourceId": "datasource-xxxx",
                "DbType": "MySQL",
                "LevelRiskName": "中",
                "LevelRiskScore": 2,
                "TableName": "beijing_01",
                "FieldName": "address",
                "RuleName": "住址",
                "FieldResultId": 123,
                "DbName": "db-1"
            }
        ],
        "RequestId": "xx"
    }
}
```

