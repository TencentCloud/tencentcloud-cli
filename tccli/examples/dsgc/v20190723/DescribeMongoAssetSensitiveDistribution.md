**Example 1: 查询mongo的敏感资产分布**

查询mongo的敏感资产分布

Input: 

```
tccli dsgc DescribeMongoAssetSensitiveDistribution --cli-unfold-argument  \
    --DspaId abc \
    --ComplianceId 0 \
    --AssetList.0.DataSourceType abc \
    --AssetList.0.DataSourceInfo.0.DataSourceId abc \
    --AssetList.0.DataSourceInfo.0.BindList abc
```

Output: 
```
{
    "Response": {
        "MongoAsset": {
            "DbNums": 0,
            "SensitiveDbNums": 0,
            "ColNums": 0,
            "SensitiveColNums": 0,
            "FieldNums": 0,
            "SensitiveFieldNums": 0
        },
        "TopAsset": [
            {
                "LevelName": "abc",
                "TopStat": [
                    {
                        "DataSourceId": "abc",
                        "SubData": "abc",
                        "SensitiveCnt": 0
                    }
                ]
            }
        ],
        "MongoDetail": [
            {
                "DataSourceId": "abc",
                "DdName": "abc",
                "DataType": "abc",
                "ColNums": 0,
                "SensitiveColNums": 0,
                "FieldNums": 0,
                "SensitiveFieldNums": 0,
                "DistributionData": [
                    {
                        "Key": "abc",
                        "Value": 0
                    }
                ]
            }
        ],
        "RequestId": "abc"
    }
}
```

