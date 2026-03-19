**Example 1: 获取漏洞防御策略和事件统计**

获取漏洞防御策略和事件统计

Input: 

```
tccli cwp DescribeVulDefenceOverviewCount --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "db961ab0-a278-46e0-9771-4718e95b8389",
        "StrategyCount": 2,
        "StrategyOpenCount": 0,
        "SupportDefenceVulCount": 150
    }
}
```

