**Example 1: DescribePolicyStatus**



Input: 

```
tccli waf DescribePolicyStatus --cli-unfold-argument  \
    --Domain test.com \
    --Edition saas-waf
```

Output: 
```
{
    "Response": {
        "RequestId": "b7984267-1b60-4979-accb-8f1ca497f827",
        "InstanceId": "aaa",
        "Status": 0
    }
}
```

