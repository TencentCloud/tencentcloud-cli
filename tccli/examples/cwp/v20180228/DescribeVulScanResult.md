**Example 1: 获取漏洞检测结果**

获取漏洞检测结果

Input: 

```
tccli cwp DescribeVulScanResult --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "ImpactedHostNum": 1,
        "BasicVersionNum": 1,
        "ProVersionNum": 1,
        "RequestId": "xx",
        "HostNum": 1,
        "VulNum": 1
    }
}
```

