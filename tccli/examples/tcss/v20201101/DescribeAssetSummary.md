**Example 1: 查询账户容器、镜像等统计信息**



Input: 

```
tccli tcss DescribeAssetSummary --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AppCnt": 14,
        "ContainerCnt": 223,
        "ContainerPause": 1,
        "ContainerRunning": 56,
        "ContainerStop": 166,
        "CreateTime": "2020-11-02T12:55:02.043Z",
        "DbCnt": 2,
        "HostCnt": 122,
        "HostOnline": 119,
        "ImageCnt": 339,
        "ImageHasRiskInfoCnt": 145,
        "ImageHasVirusCnt": 22,
        "ImageHasVulsCnt": 325,
        "ImageUnsafeCnt": 326,
        "ImageUntrustCnt": 4,
        "LatestImageScanTime": "2021-01-29T06:10:17.043Z",
        "ListenPortCnt": 58,
        "ProcessCnt": 87,
        "RequestId": "c2ac8fcc-f9af-4aa6-97fc-26c855bf9a6b",
        "WebServiceCnt": 7,
        "HostUnInstallCnt": 1
    }
}
```

