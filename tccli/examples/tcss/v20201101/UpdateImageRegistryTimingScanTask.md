**Example 1: 定时扫描-扫描全部已授权的最新版本镜像**

扫描全部已授权的最新版本镜像，扫描类型：漏洞

Input: 

```
tccli tcss UpdateImageRegistryTimingScanTask --cli-unfold-argument  \
    --ScanPeriod 1 \
    --ScanType CVE \
    --Images.0.ImageDigest abc \
    --Images.0.RegistryType abc \
    --Images.0.ImageRepoAddress abc \
    --Images.0.InstanceId abc \
    --Images.0.InstanceName abc \
    --Images.0.Namespace abc \
    --Images.0.ImageName abc \
    --Images.0.ImageTag abc \
    --Images.0.Force abc \
    --All True \
    --Latest True \
    --Enable True \
    --ScanTime 04:00:00 \
    --Id 1
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

