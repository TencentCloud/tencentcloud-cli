**Example 1: 创建漏洞扫描（一键扫描）**



Input: 

```
tccli csip CreateVulScanManual --cli-unfold-argument  \
    --MemberId mem-tencent-6f5795752f66e429 \
    --Timeout 3600 \
    --VulCategory LINUX \
    --Level LOW \
    --Method VersionComparePOC \
    --AssetRange 0
```

Output: 
```
{
    "Response": {
        "TaskId": 142,
        "RequestId": "2bc81c28-ac02-4624-a565-73c1a11bbb3a"
    }
}
```

