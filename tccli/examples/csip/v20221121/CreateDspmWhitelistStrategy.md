**Example 1: 创建Dspm白名单策略**



Input: 

```
tccli csip CreateDspmWhitelistStrategy --cli-unfold-argument  \
    --StrategyType ExposingPublicNetworkAccess \
    --Rule 
```

Output: 
```
{
    "Response": {
        "WhitelistStrategyId": "d13d396a-d798-4229-899f-023da9230532",
        "RequestId": "cf839eee-b651-4ff3-9b49-173f9f55733f"
    }
}
```

