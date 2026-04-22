**Example 1: 更新批量精准白名单规则**



Input: 

```
tccli waf ModifyBatchCustomWhiteRuleStatus --cli-unfold-argument  \
    --Status 0 \
    --Ids 11101 11102
```

Output: 
```
{
    "Response": {
        "RequestId": "c937ce96-cf53-4df8-b288-07c6e092072d"
    }
}
```

