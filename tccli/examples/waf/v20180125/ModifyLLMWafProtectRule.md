**Example 1: 批量修改防护规则**



Input: 

```
tccli waf ModifyLLMWafProtectRule --cli-unfold-argument  \
    --ServiceId 9000002874 \
    --RuleIds grl-safety-prompt-001 \
    --RuleAction deny \
    --Status 1 \
    --InstanceId waf_2l15d14809yfq9sf \
    --Direction 1
```

Output: 
```
{
    "Response": {
        "RequestId": "05690bf3-09bf-43e7-9a92-6b59074c6f3b"
    }
}
```

