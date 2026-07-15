**Example 1: 查询语义路由Tier信息**



Input: 

```
tccli clb DescribeIntentRouterTiers --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TierSet": [
            {
                "Description": "默认兜底 Tier，当语义路由无法将请求匹配到其他Tier 时使用.",
                "DisplayName": "默认",
                "TierId": "default"
            }
        ],
        "TotalCount": 11,
        "RequestId": "e4181a98-3310-40bc-b805-09a2733712df"
    }
}
```

