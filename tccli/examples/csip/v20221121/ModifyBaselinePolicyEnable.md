**Example 1: 更改基线策略开关**

更改基线策略开关

Input: 

```
tccli csip ModifyBaselinePolicyEnable --cli-unfold-argument  \
    --PolicyIDList 1 \
    --PolicyType SELF \
    --Enable 0 \
    --MemberId mem-************95752f66e429
```

Output: 
```
{
    "Response": {
        "RequestId": "83f968b3-a8a7-4356-8312-21d9d7b98e1a"
    }
}
```

