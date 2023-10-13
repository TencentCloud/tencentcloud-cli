**Example 1: 查询示例**



Input: 

```
tccli waf AddAttackWhiteRule --cli-unfold-argument  \
    --Status 1 \
    --Rules.0.MatchField xx \
    --Rules.0.MatchContent xx \
    --Rules.0.MatchMethod xx \
    --Domain xx \
    --SignatureId xx \
    --RuleId 1
```

Output: 
```
{
    "Response": {
        "RuleId": 1,
        "RequestId": "xx"
    }
}
```

