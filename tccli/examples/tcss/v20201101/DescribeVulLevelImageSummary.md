**Example 1: 查询应急漏洞各威胁等级统计镜像数**



Input: 

```
tccli tcss DescribeVulLevelImageSummary --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "LowLevelVulLocalImagePercent": 0.0,
        "HighLevelVulLocalImagePercent": 0.0,
        "LocalNewestImageCount": 0,
        "LowLevelVulRegistryImagePercent": 0.0,
        "MediumLevelVulRegistryImagePercent": 0.0,
        "HighLevelVulRegistryImagePercent": 0.0,
        "MediumLevelVulLocalImagePercent": 0.0,
        "RequestId": "8a64a4f9-864c-49c6-adcb-21b483de477a",
        "CriticalLevelVulLocalImagePercent": 0.0,
        "CriticalLevelVulRegistryImagePercent": 0.0,
        "RegistryNewestImageCount": 0
    }
}
```

