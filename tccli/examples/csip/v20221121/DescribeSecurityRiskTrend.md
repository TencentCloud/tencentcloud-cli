**Example 1: 获取近30天安全风险趋势**



Input: 

```
tccli csip DescribeSecurityRiskTrend --cli-unfold-argument  \
    --MemberId mem-**********************29
```

Output: 
```
{
    "Response": {
        "TrendData": [],
        "RiskItems": [],
        "RequestId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    }
}
```

