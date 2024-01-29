**Example 1: 查询示例**



Input: 

```
tccli waf AddAttackWhiteRule --cli-unfold-argument  \
    --Status 1 \
    --Rules.0.MatchField URL \
    --Rules.0.MatchContent /url \
    --Rules.0.MatchMethod eq \
    --Domain www.testwaf.com \
    --SignatureIds 90501998 90501999 \
    --RuleId 1
```

Output: 
```
{
    "Response": {
        "RuleId": 109102367,
        "RequestId": "76a16020-6e13-4028-823b-b20fb33ecf44"
    }
}
```

