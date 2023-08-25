**Example 1: xx**

查询es概览页列表

Input: 

```
tccli dsgc DescribeDSPAESDataAssetDetail --cli-unfold-argument  \
    --DspaId abc \
    --ComplianceId 0 \
    --Offset 0 \
    --Limit 0 \
    --Filters.0.Name abc \
    --Filters.0.Values abc
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "Details": [
            {
                "DataSourceId": "abc",
                "DataSourceName": "abc",
                "DataSourceType": "abc",
                "ResourceRegion": "abc",
                "IndexName": "abc",
                "FieldName": "abc",
                "CategoryId": 0,
                "CategoryArr": [
                    "abc"
                ],
                "LevelRiskName": "abc",
                "LevelRiskScore": 0,
                "TrustedScore": 0
            }
        ],
        "RequestId": "abc"
    }
}
```

