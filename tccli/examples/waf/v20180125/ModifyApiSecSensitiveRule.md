**Example 1: 修改api安全敏感检测规则**



Input: 

```
tccli waf ModifyApiSecSensitiveRule --cli-unfold-argument  \
    --Domain hzh.qcloud.com \
    --RuleName ddp1 \
    --Status 1 \
    --CustomRule.Position get \
    --CustomRule.MatchKey key1 \
    --CustomRule.MatchCond pent \
    --CustomRule.MatchValue waf \
    --CustomRule.Level get \
    --RuleNameList ddptest
```

Output: 
```
{
    "Response": {
        "RequestId": "dfadb1fd-6008-4aa4-b7cf-6584f6cbdfb3"
    }
}
```

