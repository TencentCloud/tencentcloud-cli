**Example 1: 示例**

示例描述

Input: 

```
tccli dsgc DescribeRDBAssetSensitiveDistribution --cli-unfold-argument  \
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
        "RDBAsset": {
            "DbNums": 0,
            "SensitiveDbNums": 0,
            "TableNums": 0,
            "SensitiveTableNums": 0,
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
        "RDBDetail": [
            {
                "DataSourceId": "abc",
                "DdName": "abc",
                "DataType": "abc",
                "TableNums": 0,
                "SensitiveTableNums": 0,
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

