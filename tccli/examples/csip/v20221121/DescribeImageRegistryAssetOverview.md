**Example 1: 查询镜像仓库资产总览**



Input: 

```
tccli csip DescribeImageRegistryAssetOverview --cli-unfold-argument  \
    --MemberId mem-12e1se11
```

Output: 
```
{
    "Response": {
        "ComponentCnt": 4805,
        "ImageCnt": 319,
        "ImageScannedCnt": 189,
        "RemainingQuota": 1010,
        "SensitiveCnt": 118,
        "TimedScanTaskConfigCnt": 5,
        "TotalQuota": 1010,
        "TrialQuota": 0,
        "UsedQuota": 0,
        "VirusCnt": 496,
        "VulCnt": 419,
        "RequestId": "aa4beda5-11ef-4295-a4c9-2713255b7e96"
    }
}
```

