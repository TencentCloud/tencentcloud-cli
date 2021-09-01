**Example 1: 添加CC防护的访问频率控制规则**

想转发规则下的所有URI填加一致的频率控制规则，则只需要设置Uri=/即可

Input: 

```
tccli dayu CreateCCFrequencyRules --cli-unfold-argument  \
    --Business bgpip \
    --Id bgpip-000000xe \
    --RuleId rule-00000001 \
    --Uri / \
    --Mode include \
    --Period 60 \
    --ReqNumber 30 \
    --Act alg \
    --ExeDuration 120
```

Output: 
```
{
    "Response": {
        "CCFrequencyRuleId": "ccRule-000003h7",
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

