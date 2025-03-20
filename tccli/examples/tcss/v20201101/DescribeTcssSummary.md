**Example 1: 查询容器安全概览信息**



Input: 

```
tccli tcss DescribeTcssSummary --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RiskLocalImageCnt": 21,
        "RiskRepositoryImageCnt": 12,
        "RuntimeUnhandleEventCnt": 51,
        "RiskBaseLineCnt": 151,
        "ScannedImageCnt": 41,
        "RiskVulCnt": 16,
        "RiskContainerCnt": 81,
        "ImageCnt": 12,
        "ContainerCnt": 71,
        "UnScannedVulCnt": 81,
        "UnScannedBaseLineCnt": 98,
        "RiskClusterCnt": 2,
        "ClusterCnt": 60,
        "UnScannedImageCnt": 20,
        "LocalImageCnt": 14,
        "RepositoryImageCnt": 12,
        "UnScannedClusterCnt": 21,
        "ScanImageStatus": true,
        "ScanClusterStatus": true,
        "ScanBaseLineStatus": true,
        "ScanVulStatus": true,
        "VulRiskImageCnt": 10,
        "RequestId": "29b37d86-f63d-43d1-b21a-640e82965198"
    }
}
```

