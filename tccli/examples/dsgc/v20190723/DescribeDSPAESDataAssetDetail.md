**Example 1: 查询es概览页列表**

查询es概览页列表

Input: 

```
tccli dsgc DescribeDSPAESDataAssetDetail --cli-unfold-argument  \
    --DspaId dspa-abcd1234 \
    --ComplianceId 1 \
    --Offset 0 \
    --Limit 10 \
    --Filters.0.Name DbName \
    --Filters.0.Values dsgc-es
```

Output: 
```
{
    "Response": {
        "TotalCount": 20,
        "Details": [
            {
                "DataSourceId": "es-",
                "DataSourceName": "dsgc-es",
                "DataSourceType": "es",
                "ResourceRegion": "ap-guangzhou",
                "IndexName": "dsgc-log",
                "FieldName": "name",
                "CategoryId": 1,
                "CategoryArr": [
                    "个人基本信息"
                ],
                "LevelRiskName": "高",
                "LevelRiskScore": 10,
                "TrustedScore": 1
            }
        ],
        "RequestId": "test-006"
    }
}
```

