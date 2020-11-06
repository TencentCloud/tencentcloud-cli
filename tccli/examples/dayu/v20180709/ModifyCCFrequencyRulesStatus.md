**Example 1: Enabling or disabling access frequency control rule for CC protection**



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

