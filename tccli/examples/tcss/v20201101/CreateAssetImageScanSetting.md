**Example 1: 添加容器安全镜像扫描设置**

添加容器安全镜像扫描设置

Input: 

```
tccli tcss CreateAssetImageScanSetting --cli-unfold-argument  \
    --Enable True \
    --ScanTime 00:00 \
    --ScanPeriod 1 \
    --ScanVirus True \
    --ScanRisk True \
    --ScanVul True \
    --ScanEndTime 02:00
```

Output: 
```
{
    "Response": {
        "RequestId": "e3526ac5-6a37-46c4-8f65-c722973f4f65"
    }
}
```

