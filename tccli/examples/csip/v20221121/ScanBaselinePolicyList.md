**Example 1: 扫描策略**

扫描策略

Input: 

```
tccli csip ScanBaselinePolicyList --cli-unfold-argument  \
    --PolicyType SELF \
    --PolicyIDList 2 \
    --MemberId mem-************95752f66e429
```

Output: 
```
{
    "Response": {
        "RequestId": "f00175a3-7a31-4872-8617-b6ae46285dc3"
    }
}
```

