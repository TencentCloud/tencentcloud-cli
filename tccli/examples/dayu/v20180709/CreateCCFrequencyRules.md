**Example 1: Adding access frequency control rule for CC protection**

This example shows you how to add an access frequency control rule for CC protection. To add a unified frequency control rule for all URIs under a forwarding rule, simply set `Uri` to `/`.

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

