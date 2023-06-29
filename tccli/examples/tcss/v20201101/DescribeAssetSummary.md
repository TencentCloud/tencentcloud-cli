**Example 1: 查询账户容器、镜像等统计信息**

查询账户容器、镜像等统计信息

Input: 

```
tccli tcss DescribeAssetSummary --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AppCnt": 1,
        "ContainerCnt": 1,
        "ContainerPause": 1,
        "ContainerRunning": 1,
        "ContainerStop": 1,
        "CreateTime": "abc",
        "DbCnt": 1,
        "ImageCnt": 1,
        "HostOnline": 1,
        "HostCnt": 1,
        "ImageHasRiskInfoCnt": 1,
        "ImageHasVirusCnt": 1,
        "ImageHasVulsCnt": 1,
        "ImageUntrustCnt": 1,
        "ListenPortCnt": 1,
        "ProcessCnt": 1,
        "WebServiceCnt": 1,
        "LatestImageScanTime": "abc",
        "ImageUnsafeCnt": 1,
        "HostUnInstallCnt": 1,
        "SuperNodeCnt": 1,
        "SuperNodeRunningCnt": 1,
        "RequestId": "abc"
    }
}
```

