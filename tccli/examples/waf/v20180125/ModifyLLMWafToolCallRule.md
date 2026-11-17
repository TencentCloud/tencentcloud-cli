**Example 1: 批量修改防护规则**



Input: 

```
tccli waf ModifyLLMWafToolCallRule --cli-unfold-argument  \
    --ServiceId 9000002874 \
    --RuleIds gtc-baseline-001 \
    --RuleAction deny \
    --Status 1 \
    --InstanceId waf_2l15d14809yfq9sf
```

Output: 
```
{
    "Response": {
        "RequestId": "be8d36b9-ba0a-440f-af14-d079ad2fad3f"
    }
}
```

