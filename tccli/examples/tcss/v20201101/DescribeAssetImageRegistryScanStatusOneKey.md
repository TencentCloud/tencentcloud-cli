**Example 1: 正常请求**

正常请求

Input: 

```
tccli tcss DescribeAssetImageRegistryScanStatusOneKey --cli-unfold-argument  \
    --TaskID 13
```

Output: 
```
{
    "Response": {
        "ImageScanCnt": 0,
        "ImageStatus": [],
        "ImageTotal": 1525,
        "RequestId": "a8298892-31c6-4a39-84e2-ce998b5822fd",
        "RiskCount": 0,
        "ScanRemainTime": 0,
        "Schedule": 0,
        "Status": "SCANNING",
        "SuccessCount": 0
    }
}
```

**Example 2: 镜像仓库查询一键镜像扫描状态**

镜像仓库查询一键镜像扫描状态

Input: 

```
tccli tcss DescribeAssetImageRegistryScanStatusOneKey --cli-unfold-argument  \
    --All True \
    --TaskID 2257
```

Output: 
```
{
    "Response": {
        "ImageScanCnt": 0,
        "ImageStatus": [],
        "ImageTotal": 1,
        "RequestId": "2d6532f3-28b8-4a99-863b-e178b3c5c416",
        "RiskCount": 1,
        "ScanRemainTime": 0,
        "Schedule": 100,
        "Status": "SCAN_TIMEOUT",
        "SuccessCount": 0
    }
}
```

