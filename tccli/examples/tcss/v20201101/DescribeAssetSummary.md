**Example 1: 查询账户容器、镜像等统计信息**

查询账户容器、镜像等统计信息

Input: 

```
tccli tcss DescribeAssetSummary --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AppCnt": 926,
        "ContainerCnt": 1453849,
        "ContainerPause": 239,
        "ContainerRunning": 1275740,
        "ContainerStop": 175512,
        "CreateTime": "2021-06-04 17:24:40",
        "DbCnt": 41,
        "HostCnt": 57,
        "HostOnline": 42,
        "HostUnInstallCnt": 2,
        "ImageCnt": 6859,
        "ImageHasRiskInfoCnt": 33,
        "ImageHasVirusCnt": 196,
        "ImageHasVulsCnt": 1833,
        "ImageUnsafeCnt": 1833,
        "ImageUntrustCnt": 6246,
        "LatestImageScanTime": "2024-10-30 02:02:24",
        "ListenPortCnt": 1390,
        "ProcessCnt": 4398,
        "RecommendedFixImageCnt": 12,
        "RequestId": "c409c2f3-eaa0-4732-8f2b-e585c2515f3e",
        "ScannedImageCnt": 733,
        "SuperNodeCnt": 30,
        "SuperNodeRunningCnt": 30,
        "TodayNewImageCnt": 0,
        "TodayUnsafeImageCnt": 0,
        "UnScannedImageCnt": 12,
        "WebServiceCnt": 35
    }
}
```

