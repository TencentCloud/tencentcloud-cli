**Example 1: 匹配修改dlp规则**



Input: 

```
tccli waf ModifyLLMWafDLPRule --cli-unfold-argument  \
    --ServiceId 9000002874 \
    --RuleIds gdl-002 \
    --RuleAction log \
    --Status 1 \
    --InstanceId waf_2l15d14809yfq9sf \
    --Direction 1
```

Output: 
```
{
    "Response": {
        "RequestId": "c0746c96-7c29-477d-8fa8-d268232f8210"
    }
}
```

