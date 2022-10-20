**Example 1: 查询漏洞风险统计概览**



Input: 

```
tccli tcss DescribeVulSummary --cli-unfold-argument  \
    --Filters.0.Name CategoryType \
    --Filters.0.Values ALL
```

Output: 
```
{
    "Response": {
        "SeriousVulCount": 0,
        "VulTotalCount": 0,
        "RequestId": "xx",
        "SeriousVulNewestImageCount": 0,
        "SuggestVulCount": 0,
        "PocExpLevelVulCount": 0,
        "RemoteExpLevelVulCount": 0
    }
}
```

