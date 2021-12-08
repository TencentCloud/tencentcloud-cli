**Example 1: 镜像仓库更新定时任务**



Input: 

```
tccli tcss UpdateImageRegistryTimingScanTask --cli-unfold-argument  \
    --All True \
    --Enable True \
    --ScanPeriod 1 \
    --ScanTime 19:35:20 \
    --ScanType RISK VIRUS CVE
```

Output: 
```
{
    "Response": {
        "RequestId": "7dc14a3b-9238-40b7-aa68-425db89964fa"
    }
}
```

