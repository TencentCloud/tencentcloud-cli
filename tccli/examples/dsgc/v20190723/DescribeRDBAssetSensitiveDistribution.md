**Example 1: 数据资产报告-查询关系型数据库的敏感资产报告**

查询关系型数据库的敏感资产报告

Input: 

```
tccli dsgc DescribeRDBAssetSensitiveDistribution --cli-unfold-argument  \
    --DspaId dspa-a1b2c3 \
    --ComplianceId 1 \
    --AssetList.0.DataSourceType cdb \
    --AssetList.0.DataSourceInfo.0.DataSourceId cdb-a1b2c3 \
    --AssetList.0.DataSourceInfo.0.BindList asset
```

Output: 
```
{
    "Response": {
        "RDBAsset": {
            "DbNums": 2,
            "SensitiveDbNums": 1,
            "TableNums": 5,
            "SensitiveTableNums": 2,
            "FieldNums": 7,
            "SensitiveFieldNums": 4
        },
        "TopAsset": [
            {
                "LevelName": "高风险",
                "TopStat": [
                    {
                        "DataSourceId": "cdb",
                        "SubData": "high",
                        "SensitiveCnt": 0
                    }
                ]
            }
        ],
        "RDBDetail": [
            {
                "DataSourceId": "cdb",
                "DdName": "asset",
                "DataType": "cdb",
                "TableNums": 0,
                "SensitiveTableNums": 0,
                "FieldNums": 0,
                "SensitiveFieldNums": 0,
                "DistributionData": [
                    {
                        "Key": "high",
                        "Value": 0
                    }
                ]
            }
        ],
        "RequestId": "9f266ea1-30b1-4941-b513-417660be5e64"
    }
}
```

