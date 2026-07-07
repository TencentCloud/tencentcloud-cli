**Example 1: 仅修改意图路由名称**



Input: 

```
tccli clb ModifyIntentRouterAttribute --cli-unfold-argument  \
    --ModelRouterId cmr-abc12345 \
    --IntentRouterId ir-abc12345 \
    --RouteName IntentRouter/*****
```

Output: 
```
{
    "Response": {
        "RequestId": "dde9fece-1d15-4494-ae62-1632cc6b9f6f"
    }
}
```

**Example 2: 修改意图路由属性（同时修改名称和分层）**



Input: 

```
tccli clb ModifyIntentRouterAttribute --cli-unfold-argument  \
    --ModelRouterId cmr-abc12345 \
    --IntentRouterId ir-abc12345 \
    --RouteName IntentRouter/new-route-name \
    --Tiers.0.TierName SIMPLE \
    --Tiers.0.Models gpt-4o-mini \
    --Tiers.1.TierName MEDIUM \
    --Tiers.1.Models gpt-4o \
    --Tiers.2.TierName COMPLEX \
    --Tiers.2.Models claude-3-5-sonnet \
    --Tiers.3.TierName REASONING \
    --Tiers.3.Models o1-preview
```

Output: 
```
{
    "Response": {
        "RequestId": "dde9fece-1d15-4494-ae62-1632cc6b9f6f"
    }
}
```

