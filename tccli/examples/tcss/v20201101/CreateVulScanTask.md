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
        "LocalTaskID": 36002,
        "RegistryTaskID": 0,
        "RequestId": "5d02bef4-9f93-4d9d-90a9-47d7be4c8fc0"
    }
}
```

