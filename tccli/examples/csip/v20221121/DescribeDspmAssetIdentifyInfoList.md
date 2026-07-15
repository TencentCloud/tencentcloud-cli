**Example 1: 查询dspm资产数据识别信息列表**



Input: 

```
tccli csip DescribeDspmAssetIdentifyInfoList --cli-unfold-argument  \
    --MemberId mem-12ed1w12 \
    --ComplianceId 9050
```

Output: 
```
{
    "Response": {
        "DataSet": [
            {
                "AssetId": "cdb-3gxg132h",
                "AssetName": "cdb108345385",
                "AssetType": "cdb",
                "CategoryIds": [
                    355
                ],
                "CategoryNames": [
                    "个人敏感信息"
                ],
                "DetectedDbCount": 1,
                "DetectedTableCount": 1,
                "DetectedTime": "2026-06-02T10:57:47+08:00",
                "LevelId": 8,
                "LevelName": "敏感",
                "LevelScore": 10,
                "RuleIds": [
                    5800
                ],
                "RuleNames": [
                    "姓名"
                ]
            }
        ],
        "TotalCount": 1,
        "RequestId": "982933d7-0e72-4d54-9218-daee52a5545e"
    }
}
```

