**Example 1: 修改CC防护的访问频率控制规则**



Input: 

```
tccli dayu ModifyCCFrequencyRules --cli-unfold-argument  \
    --Business bgpip \
    --CCFrequencyRuleId ccRule-000003h7 \
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
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "Success": {
            "Code": "Success",
            "Message": "Success"
        }
    }
}
```

