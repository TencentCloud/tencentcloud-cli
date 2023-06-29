**Example 1: 查询各类型漏洞各威胁等级统计数**



Input: 

```
tccli tcss DescribeVulLevelSummary --cli-unfold-argument  \
    --CategoryType SYSTEM
```

Output: 
```
{
    "Response": {
        "MediumLevelVulCount": 0,
        "CriticalLevelVulCount": 0,
        "HighLevelVulCount": 0,
        "LowLevelVulCount": 0,
        "RequestId": "xx"
    }
}
```

