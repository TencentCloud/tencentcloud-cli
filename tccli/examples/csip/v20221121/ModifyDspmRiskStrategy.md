**Example 1: 修改Dspm风险策略**



Input: 

```
tccli csip ModifyDspmRiskStrategy --cli-unfold-argument  \
    --StrategyType ExposingPublicNetworkAccess \
    --IsEnabled 0
```

Output: 
```
{
    "Response": {
        "RequestId": "cf839eee-b651-4ff3-9b49-173f9f55733f"
    }
}
```

