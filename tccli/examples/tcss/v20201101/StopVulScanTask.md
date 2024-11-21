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
        "RequestId": "8a64a4f9-864c-49c6-adcb-21b483de477a"
    }
}
```

