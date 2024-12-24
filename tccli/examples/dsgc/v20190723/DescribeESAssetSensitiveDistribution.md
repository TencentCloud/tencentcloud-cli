**Example 1: 查询es的敏感资产分布**

查询es的敏感资产分布

Input: 

```
tccli dsgc DescribeESAssetSensitiveDistribution --cli-unfold-argument  \
    --DspaId dspa-abcd1234 \
    --ComplianceId 1 \
    --AssetList.0.DataSourceType es \
    --AssetList.0.DataSourceInfo.0.DataSourceId es-23svw0g \
    --AssetList.0.DataSourceInfo.0.BindList db04
```

Output: 
```
{
    "Response": {
        "ESAsset": {
            "IndexNums": 8,
            "SensitiveIndexNums": 3,
            "FieldNums": 20,
            "SensitiveFieldNums": 12
        },
        "TopAsset": [
            {
                "LevelName": "高",
                "TopStat": [
                    {
                        "DataSourceId": "es-3svgfsf23",
                        "SubData": "db04",
                        "SensitiveCnt": 20
                    }
                ]
            }
        ],
        "ESDetail": [
            {
                "DataSourceId": "es-23svw0g",
                "IndexName": "db04",
                "DataType": "es",
                "FieldNums": 10,
                "SensitiveFieldNums": 3,
                "DistributionData": [
                    {
                        "Key": "个人信息",
                        "Value": 2
                    }
                ]
            }
        ],
        "RequestId": "fsdgsd-1234sd"
    }
}
```

