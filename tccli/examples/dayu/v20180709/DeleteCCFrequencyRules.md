**Example 1: Deleting access frequency control rule for CC protection**



Input: 

```
tccli dayu DeleteCCFrequencyRules --cli-unfold-argument  \
    --Business bgpip \
    --CCFrequencyRuleId ccRule-000000xe
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

