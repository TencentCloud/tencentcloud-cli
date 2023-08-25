**Example 1: 示例**

示例描述

Input: 

```
tccli dsgc DescribeCOSAssetSensitiveDistribution --cli-unfold-argument  \
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
        "CosAsset": {
            "BucketNums": 0,
            "SensitiveBucketNums": 0,
            "FileNums": 0,
            "SensitiveFileNums": 0
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
        "CosDetail": [
            {
                "Bucket": "abc",
                "DataType": "abc",
                "FileNums": 0,
                "SensitiveFileNums": 0,
                "DistributionData": [
                    {
                        "Key": "abc",
                        "Value": 0
                    }
                ],
                "MatchedNum": 0
            }
        ],
        "RequestId": "abc"
    }
}
```

