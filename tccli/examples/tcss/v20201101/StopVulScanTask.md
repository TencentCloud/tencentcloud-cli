**Example 1: 停止漏洞扫描任务**



Input: 

```
tccli tcss StopVulScanTask --cli-unfold-argument  \
    --LocalTaskID 1 \
    --RegistryTaskID 1
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

