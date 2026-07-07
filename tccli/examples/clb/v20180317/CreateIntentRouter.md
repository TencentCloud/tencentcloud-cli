**Example 1: 创建意图路由**



Input: 

```
tccli clb CreateIntentRouter --cli-unfold-argument  \
    --ModelRouterId cmr-giljntwo \
    --RouteName IntentRouter/ekc-test \
    --Tiers.0.TierName default \
    --Tiers.0.Models gpt-4o-mini
```

Output: 
```
{
    "Response": {
        "IntentRouterId": "ir-pb139vho",
        "RequestId": "f2a262c3-b45c-4d8a-b1c3-ded110203ca3"
    }
}
```

