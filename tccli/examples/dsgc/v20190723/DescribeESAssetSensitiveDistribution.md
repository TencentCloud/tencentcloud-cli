**Example 1: 查询es的敏感资产分布**

查询es的敏感资产分布

Input: 

```
tccli dsgc DescribeESAssetSensitiveDistribution --cli-unfold-argument  \
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
        "ESAsset": {
            "IndexNums": 0,
            "SensitiveIndexNums": 0,
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
        "ESDetail": [
            {
                "DataSourceId": "abc",
                "IndexName": "abc",
                "DataType": "abc",
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

