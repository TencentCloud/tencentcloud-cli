**Example 1: 开启或关闭CC防护的访问频率控制规则**



Input: 

```
tccli dayu ModifyCCFrequencyRulesStatus --cli-unfold-argument  \
    --Business bgpip \
    --Id bgpip-00000001 \
    --RuleId rule-000000xe \
    --Method off
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "Success": {
            "Code": "Success",
            "Message": "Success"
        }
    }
}
```

