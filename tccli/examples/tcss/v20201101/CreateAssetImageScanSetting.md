**Example 1: 添加容器安全镜像扫描设置**

添加容器安全镜像扫描设置

Input: 

```
tccli tcss CreateAssetImageScanSetting --cli-unfold-argument  \
    --Enable True \
    --ScanTime 2020-12-28 15:53:26 \
    --ScanPeriod 3600 \
    --ScanVirus True \
    --ScanRisk True \
    --ScanVul True \
    --All True
```

Output: 
```
{
    "Response": {
        "RequestId": "af170769-a009-4c51-879a-8fe182ace76e"
    }
}
```

