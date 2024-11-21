**Example 1: 查询漏洞风险统计概览**

查询漏洞风险统计概览

Input: 

```
tccli tcss DescribeVulSummary --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "EmergencyVulnerabilityCount": 53,
        "PocExpLevelVulCount": 761,
        "RemoteExpLevelVulCount": 29,
        "RequestId": "4cfc5e95-49f3-4c71-8048-0db454ed49b7",
        "SeriousVulCount": 2924,
        "SeriousVulNewestImageCount": 296,
        "SeriousVulnerabilityLocalImageCount": 169,
        "SeriousVulnerabilityRegistryImageCount": 127,
        "SuggestVulCount": 2013,
        "SystemVulnerabilityFocusCount": 1536,
        "VulTotalCount": 5513,
        "WebVulnerabilityFocusCount": 477
    }
}
```

