**Example 1: 查询容器资产信息**

查询容器资产信息

Input: 

```
tccli tcss DescribeContainerAssetSummary --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "ContainerTotalCnt": 1,
        "ContainerRunningCnt": 1,
        "ContainerPauseCnt": 1,
        "ContainerStopped": 1,
        "ImageCnt": 1,
        "HostCnt": 1,
        "HostRunningCnt": 1,
        "HostOfflineCnt": 1,
        "ImageRegistryCnt": 1,
        "ImageTotalCnt": 1,
        "HostUnInstallCnt": 1,
        "HostSuperNodeCnt": 1,
        "RequestId": "abc"
    }
}
```

