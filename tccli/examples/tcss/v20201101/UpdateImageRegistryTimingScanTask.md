**Example 1: 镜像仓库更新定时任务**



Input: 

```
tccli tcss UpdateImageRegistryTimingScanTask --cli-unfold-argument  \
    --All True \
    --ScanType xx \
    --ScanTime xx \
    --ScanPeriod 1 \
    --Enable True \
    --Images.0.Force xx \
    --Images.0.ImageTag xx \
    --Images.0.InstanceId xx \
    --Images.0.RegistryType xx \
    --Images.0.Namespace xx \
    --Images.0.ImageRepoAddress xx \
    --Images.0.ImageName xx \
    --Images.0.ImageDigest xx \
    --Images.0.InstanceName xx
```

Output: 
```
{
    "Response": {
        "RequestId": "7dc14a3b-9238-40b7-aa68-425db89964fa"
    }
}
```

