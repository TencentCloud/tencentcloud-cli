**Example 1: 查询容器安全概览信息**



Input: 

```
tccli tcss DescribeTcssSummary --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RiskLocalImageCnt": 1,
        "RiskRepositoryImageCnt": 1,
        "RuntimeUnhandleEventCnt": 1,
        "RiskBaseLineCnt": 1,
        "ScannedImageCnt": 1,
        "RiskVulCnt": 1,
        "RiskContainerCnt": 1,
        "ImageCnt": 1,
        "ContainerCnt": 1,
        "UnScannedVulCnt": 1,
        "UnScannedBaseLineCnt": 1,
        "RiskClusterCnt": 1,
        "ClusterCnt": 1,
        "UnScannedImageCnt": 1,
        "LocalImageCnt": 1,
        "RepositoryImageCnt": 1,
        "UnScannedClusterCnt": 1,
        "ScanImageStatus": true,
        "ScanClusterStatus": true,
        "ScanBaseLineStatus": true,
        "ScanVulStatus": true,
        "VulRiskImageCnt": 10,
        "RequestId": "29b37d86-f63d-43d1-b21a-640e82965198"
    }
}
```

