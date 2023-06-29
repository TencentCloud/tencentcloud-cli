**Example 1: 创建漏洞扫描任务**



Input: 

```
tccli tcss CreateVulScanTask --cli-unfold-argument  \
    --LocalImageScanType ALL \
    --RegistryImageScanType ALL
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "LocalTaskID": 0,
        "RegistryTaskID": 0
    }
}
```

