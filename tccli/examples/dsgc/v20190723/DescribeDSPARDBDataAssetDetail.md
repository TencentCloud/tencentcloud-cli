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
        "Details": [
            {
                "DataSourceId": "abc",
                "DbType": "abc",
                "DbName": "abc",
                "TableName": "abc",
                "FieldName": "abc",
                "RuleName": "abc",
                "CategoryName": "abc",
                "LevelRiskName": "abc",
                "LevelRiskScore": 0,
                "TrustedScore": "abc",
                "ResourceRegion": "abc",
                "FieldResultId": "abc",
                "RuleId": 0,
                "LevelId": 0,
                "CategoryId": 0,
                "DataSourceName": "abc",
                "SafeGuard": {
                    "Encrypt": "abc",
                    "Desensitization": "abc"
                },
                "CategoryFullPath": "abc",
                "IdentifyType": 0,
                "CheckStatus": 0,
                "IsSensitiveData": 0
            }
        ],
        "TotalCount": 0,
        "RequestId": "abc"
    }
}
```

