**Example 1: 定时扫描-扫描全部已授权的最新版本镜像**

扫描全部已授权的最新版本镜像，扫描类型：漏洞

Input: 

```
tccli tcss UpdateImageRegistryTimingScanTask --cli-unfold-argument  \
    --Enable True \
    --ScanPeriod 1 \
    --ScanTime 18:10 \
    --ScanEndTime 20:00 \
    --ScanScope 2 \
    --ContainerRunning False \
    --Namespace tke-images \
    --RegistryType ccr \
    --Latest True \
    --ScanType CVE VIRUS RISK
```

Output: 
```
{
    "Response": {
        "RequestId": "5f2acb2d-2775-4ef4-8230-03df2762b1d1"
    }
}
```

