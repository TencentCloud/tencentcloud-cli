**Example 1: 查询cos资产分布详情**

查询cos资产分布详情

Input: 

```
tccli dsgc DescribeCOSAssetSensitiveDistribution --cli-unfold-argument  \
    --DspaId dspa-abcd1234 \
    --ComplianceId 1 \
    --AssetList.0.DataSourceType 2 \
    --AssetList.0.DataSourceInfo.0.DataSourceId cdb-tsf1ewdfr \
    --AssetList.0.DataSourceInfo.0.BindList predb01
```

Output: 
```
{
    "Response": {
        "CosAsset": {
            "BucketNums": 3,
            "SensitiveBucketNums": 1,
            "FileNums": 20,
            "SensitiveFileNums": 6
        },
        "TopAsset": [
            {
                "LevelName": "中",
                "TopStat": [
                    {
                        "DataSourceId": "cdb-tsf1ewdfr",
                        "SubData": "数据",
                        "SensitiveCnt": 1
                    }
                ]
            }
        ],
        "CosDetail": [
            {
                "Bucket": "cos-atgwr0234",
                "DataType": "2",
                "FileNums": 16,
                "SensitiveFileNums": 6,
                "DistributionData": [
                    {
                        "Key": "103",
                        "Value": 5
                    }
                ],
                "MatchedNum": 3
            }
        ],
        "RequestId": "sfwtgw-gsdf-23rsfs"
    }
}
```

