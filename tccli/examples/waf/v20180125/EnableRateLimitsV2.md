**Example 1: 批量更改自研版限流规则开关**



Input: 

```
tccli waf EnableRateLimitsV2 --cli-unfold-argument  \
    --Domain www.test.com \
    --EnableItems.0.LimitRuleId 400000023 \
    --EnableItems.0.Status 0
```

Output: 
```
{
    "Response": {
        "BaseInfo": {
            "Code": 0,
            "Info": "success"
        },
        "RequestId": "104cf2f9-c733-4a18-8905-372553b6ed80"
    }
}
```

