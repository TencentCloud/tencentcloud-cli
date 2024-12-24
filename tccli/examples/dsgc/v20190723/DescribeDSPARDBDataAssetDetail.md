**Example 1: 获取RDB关系数据库分类分级资产详情**



Input: 

```
tccli dsgc DescribeDSPARDBDataAssetDetail --cli-unfold-argument  \
    --DspaId dspa-7asd43mh \
    --ComplianceId 1
```

Output: 
```
{
    "Response": {
        "Details": [
            {
                "CategoryName": "个人基本信息",
                "DataSourceId": "postgres-kddpr59c",
                "DataSourceName": "订单数据库",
                "DbType": "postgres",
                "LevelRiskName": "中",
                "LevelRiskScore": 5,
                "TableName": "BackupTest002",
                "FieldName": "Backup_tinyPhone_2",
                "FieldResultId": "1",
                "RuleName": "手机",
                "SchemaName": "test_schema",
                "DbName": "ACLAutoTest002",
                "SafeGuard": {
                    "Encrypt": "UNSET",
                    "Desensitization": "UNSET"
                },
                "RuleId": 8,
                "LevelId": 2,
                "CategoryId": 103,
                "CategoryFullPath": "[\"个人基本信息\"]",
                "TrustedScore": "0.1",
                "ResourceRegion": "ap-shanghai",
                "IdentifyType": 0,
                "CheckStatus": 0
            }
        ],
        "TotalCount": 1,
        "RequestId": "826f0635-b168-52a7-8db9-45b1d46d2c8a"
    }
}
```

