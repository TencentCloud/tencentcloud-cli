**Example 1: 查询容器资产信息**



Input: 

```
tccli tcss DescribeContainerAssetSummary --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "HostRunningCnt": 1,
        "ContainerPauseCnt": 1,
        "ContainerRunningCnt": 1,
        "ImageRegistryCnt": 1,
        "ContainerStopped": 1,
        "ImageTotalCnt": 1,
        "ImageCnt": 1,
        "HostCnt": 1,
        "RequestId": "xx",
        "HostOfflineCnt": 1,
        "ContainerTotalCnt": 1
    }
}
```

