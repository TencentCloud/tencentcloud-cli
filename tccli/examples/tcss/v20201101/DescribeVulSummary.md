**Example 1: 查询漏洞风险统计概览**

查询漏洞风险统计概览

Input: 

```
tccli tcss DescribeVulSummary --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "VulTotalCount": 0,
        "SeriousVulCount": 0,
        "SuggestVulCount": 0,
        "PocExpLevelVulCount": 0,
        "RemoteExpLevelVulCount": 0,
        "SeriousVulNewestImageCount": 0,
        "SystemVulnerabilityFocusCount": 0,
        "WebVulnerabilityFocusCount": 0,
        "SeriousVulnerabilityLocalImageCount": 0,
        "SeriousVulnerabilityRegistryImageCount": 0,
        "EmergencyVulnerabilityCount": 0,
        "RequestId": "abc"
    }
}
```

