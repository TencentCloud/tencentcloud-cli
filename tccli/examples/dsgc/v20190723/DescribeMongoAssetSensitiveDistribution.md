**Example 1: 查询mongo的敏感资产分布**

查询mongo的敏感资产分布

Input: 

```
tccli dsgc DescribeMongoAssetSensitiveDistribution --cli-unfold-argument  \
    --DspaId dspa-a12fvc2d \
    --ComplianceId 0 \
    --AssetList.0.DataSourceType mongo \
    --AssetList.0.DataSourceInfo.0.DataSourceId cmgo-c1vsibl3 \
    --AssetList.0.DataSourceInfo.0.BindList table1
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
                "LevelName": "分级名称",
                "TopStat": [
                    {
                        "DataSourceId": "cmgo-c1vsibl3",
                        "SubData": "table1",
                        "SensitiveCnt": 0
                    }
                ]
            }
        ],
        "MongoDetail": [
            {
                "DataSourceId": "cmgo-c1vsibl3",
                "DdName": "table1",
                "DataType": "mongo",
                "ColNums": 0,
                "SensitiveColNums": 0,
                "FieldNums": 0,
                "SensitiveFieldNums": 0,
                "DistributionData": [
                    {
                        "Key": "key1",
                        "Value": 12
                    }
                ]
            }
        ],
        "RequestId": "91c7a73v-e540-4780-8b8e-74e0b65b4f1a"
    }
}
```

